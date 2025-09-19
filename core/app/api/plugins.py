# KEYWORDS: api, плагины, регистрация, heartbeat, каталог
"""[ANCHOR:PROJECT:TGBOT:CORE:APP:API:PLUGINS]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:APP:API:PLUGINS">
Роутер `/api/v1/plugins` реализует публичные методы ядра для управления
плагинами: регистрация, heartbeat, каталог и отладочный вызов. Источник
истины — `docs/CONTRACTS/CORE.md` и manifest-политики.
<HARMONY:END name="PROJECT:TGBOT:CORE:APP:API:PLUGINS">
"""

from __future__ import annotations

import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from ..dependencies import get_plugin_manager, get_trace
from ..schemas.v1alpha import (
    PluginCatalogResponseV1,
    PluginHeartbeatRequestV1,
    PluginInvocationRequestV1,
    PluginInvocationResultV1,
    PluginRegistrationRequestV1,
    PluginRegistrationResponseV1,
)
from ..services.plugin_manager import PluginManager
from ..telemetry.tracing import TraceContext

router = APIRouter(prefix="/api/v1/plugins", tags=["plugins"])
_logger = logging.getLogger(__name__)


@router.post(
    "/register",
    response_model=PluginRegistrationResponseV1,
    status_code=status.HTTP_201_CREATED,
    summary="Регистрация плагина",
)
async def register_plugin(
    payload: PluginRegistrationRequestV1,
    manager: PluginManager = Depends(get_plugin_manager),
    trace: TraceContext = Depends(get_trace),
) -> PluginRegistrationResponseV1:
    """Регистрирует плагин и выдаёт токен доступа."""

    response = await manager.register(payload)
    _logger.info(
        "plugin_registration_accepted",
        extra={"trace_id": trace.trace_id, "plugin_id": str(response.plugin_id)},
    )
    return response


@router.get(
    "",
    response_model=PluginCatalogResponseV1,
    summary="Каталог зарегистрированных плагинов",
)
async def list_plugins(
    manager: PluginManager = Depends(get_plugin_manager),
) -> PluginCatalogResponseV1:
    """Возвращает список плагинов и их текущее состояние."""

    return await manager.list_catalog()


@router.post(
    "/{plugin_id}/heartbeat",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Обновление статуса плагина",
)
async def heartbeat(
    plugin_id: UUID,
    payload: PluginHeartbeatRequestV1,
    manager: PluginManager = Depends(get_plugin_manager),
) -> dict[str, str]:
    """Обновляет статус и метрики плагина."""

    if plugin_id != payload.plugin_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "plugin_id не совпадает с телом")
    try:
        await manager.heartbeat(payload)
    except KeyError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
    return {"status": "accepted"}


@router.post(
    "/{plugin_id}/invoke",
    response_model=PluginInvocationResultV1,
    summary="Отладочный вызов плагина через ядро",
)
async def invoke_plugin(
    plugin_id: UUID,
    payload: PluginInvocationRequestV1,
    manager: PluginManager = Depends(get_plugin_manager),
    trace: TraceContext = Depends(get_trace),
) -> PluginInvocationResultV1:
    """Позволяет отладочно вызвать плагин, используя токен ядра."""

    try:
        plugin = await manager.get_plugin(plugin_id)
    except KeyError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(exc)) from exc
    invocation = payload.model_copy(update={"trace_id": trace.trace_id})
    return await manager.invoke_plugin(plugin, invocation, trace=trace)


__all__ = [
    "router",
    "register_plugin",
    "list_plugins",
    "heartbeat",
    "invoke_plugin",
]
