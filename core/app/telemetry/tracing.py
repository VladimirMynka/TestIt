# KEYWORDS: трассировка, ядро, fastapi, middleware, наблюдаемость
"""[ANCHOR:PROJECT:TGBOT:CORE:TELEMETRY:TRACING]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:TELEMETRY:TRACING">
Модуль реализует минимальный контур трассировки запросов FastAPI для
соблюдения требований наблюдаемости (`docs/CONTRACTS/CORE.md`). Источник
истины для формата trace_id — контракт ядра и протоколы `DEV_SESSION`.
<HARMONY:END name="PROJECT:TGBOT:CORE:TELEMETRY:TRACING">
"""

from __future__ import annotations

import contextvars
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request

_TRACE_CONTEXT: contextvars.ContextVar["TraceContext"] = contextvars.ContextVar(
    "trace_context"
)


@dataclass(slots=True)
class TraceContext:
    """Контейнер состояния трассировки для текущего запроса."""

    trace_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    started_at: float = field(default_factory=time.perf_counter)
    attributes: dict[str, Any] = field(default_factory=dict)

    def as_headers(self) -> dict[str, str]:
        """Возвращает заголовки для проброса `trace_id` вниз по стеку."""

        return {"X-Trace-Id": self.trace_id}


def get_trace_context() -> TraceContext:
    """Возвращает активный контекст трассировки или создаёт новый."""

    try:
        return _TRACE_CONTEXT.get()
    except LookupError:
        context = TraceContext()
        _TRACE_CONTEXT.set(context)
        return context


class TraceMiddleware(BaseHTTPMiddleware):
    """Простейший middleware, фиксирующий `trace_id` и длительность запроса."""

    def __init__(self, app, *, header_name: str = "X-Trace-Id") -> None:
        super().__init__(app)
        self._header_name = header_name

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        context = TraceContext()
        token = _TRACE_CONTEXT.set(context)
        try:
            response = await call_next(request)
        finally:
            _TRACE_CONTEXT.reset(token)
        duration_ms = (time.perf_counter() - context.started_at) * 1000
        response.headers[self._header_name] = context.trace_id
        response.headers["X-Response-Time-ms"] = f"{duration_ms:.2f}"
        return response


def with_trace_context(func: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[Any]]:
    """Оборачивает корутины, гарантируя наличие контекста трассировки."""

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        get_trace_context()
        return await func(*args, **kwargs)

    return wrapper


__all__ = ["TraceContext", "TraceMiddleware", "get_trace_context", "with_trace_context"]
