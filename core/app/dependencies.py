# KEYWORDS: зависимости, ядро, fastapi, плагины, llm
"""[ANCHOR:PROJECT:TGBOT:CORE:APP:DEPENDENCIES]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:APP:DEPENDENCIES">
Модуль предоставляет зависимости FastAPI для ядра: менеджер плагинов,
LLM-клиент и фабрика сессий БД. Источник истины — `docs/CONTRACTS/CORE.md`
и `docs/CONTRACTS/core/SCHEMAS.md`.
<HARMONY:END name="PROJECT:TGBOT:CORE:APP:DEPENDENCIES">
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable
from contextlib import AbstractAsyncContextManager
from typing import Protocol

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from .services.plugin_manager import PluginManager
from .telemetry.tracing import TraceContext, get_trace_context


class LLMClientProtocol(Protocol):
    """Протокол клиента LLM для взаимодействия с классификатором."""

    async def generate_reply(self, *, prompt: str, trace: TraceContext) -> str:
        """Генерирует ответ на основе промпта и контекста трассировки."""


SessionFactory = Callable[[], AbstractAsyncContextManager[AsyncSession]]


def get_trace(_: Request) -> TraceContext:
    """Возвращает активный `TraceContext` и регистрирует его в зависимостях."""

    return get_trace_context()


def get_plugin_manager(request: Request) -> PluginManager:
    """Получает менеджер плагинов из состояния приложения FastAPI."""

    try:
        return request.app.state.plugin_manager
    except AttributeError as exc:  # pragma: no cover - защитный код
        raise RuntimeError(
            "Менеджер плагинов не инициализирован (см. core.app.main.create_app)."
        ) from exc


async def get_llm_client(request: Request) -> LLMClientProtocol:
    """Возвращает зарегистрированный LLM-клиент или сообщает о нехватке."""

    client = getattr(request.app.state, "llm_client", None)
    if client is None:
        raise RuntimeError(
            "LLM-клиент не настроен. Выполните задачу D-004 или обновите bootstrap."
        )
    return client


async def get_db_session(
    request: Request,
    _: TraceContext = Depends(get_trace),
) -> AsyncIterator[AsyncSession]:
    """Поставляет асинхронную сессию БД через DI (используется SQLAlchemy)."""

    session_factory: SessionFactory | None = getattr(
        request.app.state, "db_session_factory", None
    )
    if session_factory is None:
        raise RuntimeError(
            "Фабрика сессий БД не настроена. См. ISSUE-D-003 и конфиг PostgreSQL."
        )
    async with session_factory() as session:
        yield session


__all__ = [
    "LLMClientProtocol",
    "SessionFactory",
    "get_plugin_manager",
    "get_llm_client",
    "get_db_session",
    "get_trace",
]
