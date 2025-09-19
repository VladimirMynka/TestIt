# KEYWORDS: fastapi, ядро, приложение, инициализация, плагины
"""[ANCHOR:PROJECT:TGBOT:CORE:APP:MAIN]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:APP:MAIN">
Создаёт и настраивает FastAPI-приложение ядра: middleware трассировки,
роутеры, сервисы и зависимости. Источник истины — контракты ядра и схемы
`v1alpha`.
<HARMONY:END name="PROJECT:TGBOT:CORE:APP:MAIN">
"""

from __future__ import annotations

import logging
from typing import Any

import httpx
from fastapi import FastAPI

from .api import dialogs, health, plugins
from .services.plugin_manager import PluginManager
from .telemetry.tracing import TraceMiddleware

_LOGGER = logging.getLogger(__name__)


def create_app(**settings: Any) -> FastAPI:
    """Фабрика FastAPI-приложения ядра."""

    app = FastAPI(
        title="TestIt Core",
        version=settings.get("version", "0.1.0"),
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    app.add_middleware(TraceMiddleware)

    @app.on_event("startup")
    async def _startup() -> None:
        timeout = httpx.Timeout(10.0, read=30.0, connect=5.0)
        app.state.http_client = httpx.AsyncClient(timeout=timeout)
        app.state.plugin_manager = PluginManager(app.state.http_client)
        _LOGGER.info("core_app_started", extra={"timeout": timeout.read})

    @app.on_event("shutdown")
    async def _shutdown() -> None:
        http_client: httpx.AsyncClient | None = getattr(app.state, "http_client", None)
        if http_client:
            await http_client.aclose()
        _LOGGER.info("core_app_shutdown")

    app.include_router(health.router)
    app.include_router(dialogs.router)
    app.include_router(plugins.router)

    return app


__all__ = ["create_app"]
