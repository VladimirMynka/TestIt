# KEYWORDS: api, диалоги, сообщения, fastapi, плагины
"""[ANCHOR:PROJECT:TGBOT:CORE:APP:API:DIALOGS]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:APP:API:DIALOGS">
Роутер `/api/v1/dialogs` реализует первичный поток обработки сообщений.
Полноценная логика диалогов и БД появится в задачах D-003 и далее; текущая
версия фокусируется на интеграции с менеджером плагинов.
<HARMONY:END name="PROJECT:TGBOT:CORE:APP:API:DIALOGS">
"""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, status

from ..dependencies import get_plugin_manager, get_trace
from ..schemas.v1alpha import (
    DialogMessageCreateV1,
    DialogMessageResponseV1,
    DialogResetRequestV1,
    DialogSnapshotResponseV1,
    DialogSummaryV1,
    InvocationStatus,
)
from ..services.plugin_manager import PluginManager
from ..telemetry.tracing import TraceContext

router = APIRouter(prefix="/api/v1/dialogs", tags=["dialogs"])


@router.post(
    "/{dialog_id}/messages",
    response_model=DialogMessageResponseV1,
    summary="Создать сообщение в диалоге",
)
async def post_message(
    dialog_id: UUID,
    payload: DialogMessageCreateV1,
    manager: PluginManager = Depends(get_plugin_manager),
    trace: TraceContext = Depends(get_trace),
) -> DialogMessageResponseV1:
    """Принимает сообщение пользователя и маршрутизирует его в плагины."""

    if dialog_id != payload.dialog_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "dialog_id не совпадает")
    response = await manager.route_dialog_message(payload, trace=trace)
    return response


@router.post(
    "/{dialog_id}/reset",
    response_model=DialogMessageResponseV1,
    summary="Сбросить состояние диалога",
)
async def reset_dialog(
    dialog_id: UUID,
    payload: DialogResetRequestV1,
) -> DialogMessageResponseV1:
    """Временная заглушка сброса диалога до реализации БД."""

    if dialog_id != payload.dialog_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "dialog_id не совпадает")
    return DialogMessageResponseV1(
        dialog_id=dialog_id,
        trace_id=payload.trace_id or uuid4(),
        status=InvocationStatus.ACCEPTED,
        plugin_responses=[],
    )


@router.get(
    "/{dialog_id}",
    summary="Получить состояние диалога",
)
async def get_dialog(dialog_id: UUID) -> DialogSnapshotResponseV1:
    """Возвращает заглушку статуса до реализации DialogService."""

    summary = DialogSummaryV1(
        id=dialog_id,
        user_id=uuid4(),
        status="pending",
        reset_version=0,
        created_at=datetime.now(tz=timezone.utc),
    )
    return DialogSnapshotResponseV1(dialog=summary, messages=[])


__all__ = ["router", "post_message", "reset_dialog", "get_dialog"]
