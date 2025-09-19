# KEYWORDS: схемы, v1alpha, ядро, pydantic, api
"""[ANCHOR:PROJECT:TGBOT:CORE:SCHEMAS:V1ALPHA]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:SCHEMAS:V1ALPHA">
Реализация Pydantic-схем `v1alpha`, описанных в контракте
`docs/CONTRACTS/core/SCHEMAS.md`. Источник истины — контракт; код служит
исполнительной формой и должен обновляться синхронно с документацией.
<HARMONY:END name="PROJECT:TGBOT:CORE:SCHEMAS:V1ALPHA">
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl, field_validator


class MessagePayloadType(str, Enum):
    """Типы сообщений диалога, согласованные с контрактом."""

    TEXT = "text"
    VOICE = "voice"
    IMAGE = "image"
    COMMAND = "command"


class PluginStatus(str, Enum):
    """Состояние плагина согласно контракту ядра."""

    ACTIVE = "active"
    DEGRADED = "degraded"
    DISABLED = "disabled"


class InvocationStatus(str, Enum):
    """Статусы вызова плагина для логирования и отклика."""

    ACCEPTED = "accepted"
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    TIMEOUT = "timeout"
    REJECTED = "rejected"


class PluginEventType(str, Enum):
    """События, публикуемые менеджером плагинов."""

    PLUGIN_REGISTERED = "plugin_registered"
    PLUGIN_HEARTBEAT = "plugin_heartbeat"
    PLUGIN_HEARTBEAT_MISSED = "plugin_heartbeat_missed"
    PLUGIN_INVOCATION_STARTED = "plugin_invocation_started"
    PLUGIN_INVOCATION_COMPLETED = "plugin_invocation_completed"
    PLUGIN_FAILED = "plugin_failed"
    PLUGIN_TIMEOUT = "plugin_timeout"


class MessageAttachmentV1(BaseModel):
    """Метаинформация о вложении сообщения."""

    id: UUID = Field(..., description="Уникальный идентификатор вложения")
    type: str = Field(..., description="Тип вложения (image/png, audio/ogg и т.д.)")
    url: HttpUrl = Field(..., description="URL для скачивания вложения")


class MessagePayloadV1(BaseModel):
    """Тело сообщения пользователя или бота."""

    type: MessagePayloadType = Field(..., description="Тип сообщения")
    text: str | None = Field(None, description="Текстовая часть для text/command")
    attachments: list[MessageAttachmentV1] = Field(
        default_factory=list,
        description="Список вложений (опционально)",
    )


class DialogMessageCreateV1(BaseModel):
    """Запрос создания сообщения в диалоге (`POST /dialogs/{id}/messages`)."""

    dialog_id: UUID
    user_id: UUID
    message_id: str | None = Field(
        default=None, description="Идемпотентный идентификатор сообщения клиента"
    )
    trace_id: UUID
    payload: MessagePayloadV1
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Дополнительные сведения (таймзона, канал, флаги UI)",
    )


class LLMUsageV1(BaseModel):
    """Статистика использования токенов LLM."""

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class PluginMessageV1(BaseModel):
    """Ответ плагина на сообщение диалога."""

    plugin_id: UUID
    content: str
    content_type: str = Field(default="text/plain")
    suggested_actions: list[dict[str, Any]] = Field(default_factory=list)


class DialogMessageResponseV1(BaseModel):
    """Ответ ядра на обработку сообщения диалога."""

    dialog_id: UUID
    trace_id: UUID
    plugin_responses: list[PluginMessageV1] = Field(default_factory=list)
    usage: LLMUsageV1 | None = None
    status: InvocationStatus = Field(
        default=InvocationStatus.ACCEPTED,
        description="Статус обработки сообщения",
    )

    @field_validator("status", mode="before")
    @classmethod
    def _map_status(cls, value: str | InvocationStatus) -> InvocationStatus:
        """Поддерживает устаревшее значение `accepted` из контракта."""

        if value == "accepted":
            return InvocationStatus.ACCEPTED
        return InvocationStatus(value) if isinstance(value, str) else value


class DialogResetRequestV1(BaseModel):
    """Запрос на сброс состояния диалога."""

    dialog_id: UUID
    user_id: UUID
    trace_id: UUID | None = None
    reason: str | None = Field(
        default=None, description="Причина сброса (user_requested, timeout и т.д.)"
    )


class DialogSummaryV1(BaseModel):
    """Краткое описание диалога для snapshot-ответа."""

    id: UUID
    user_id: UUID
    status: str
    reset_version: int = 0
    created_at: datetime


class HistoricalMessageV1(BaseModel):
    """Сообщение истории диалога для snapshot-ответа."""

    sender_type: str
    payload: MessagePayloadV1
    created_at: datetime


class DialogSnapshotResponseV1(BaseModel):
    """Ответ `GET /api/v1/dialogs/{id}` (исторические данные)."""

    dialog: DialogSummaryV1
    messages: list[HistoricalMessageV1] = Field(default_factory=list)


class PluginAuthSettingsV1(BaseModel):
    """Описание настроек авторизации плагина."""

    type: str = Field(..., description="Тип авторизации (bearer/basic/none)")
    config: dict[str, Any] = Field(default_factory=dict)


class PluginManifestV1(BaseModel):
    """Manifest плагина (см. `docs/CONTRACTS/plugins/MANIFEST.md`)."""

    name: str
    version: str
    intents: list[str] = Field(..., description="Интенты, которые обрабатывает плагин")
    activation_condition: dict[str, Any] | None = Field(
        default=None, description="Условия активации (regex, intent, custom)"
    )
    input_schema: dict[str, Any] | None = Field(
        default=None, description="JSON Schema входного запроса"
    )
    output_schema: dict[str, Any] | None = Field(
        default=None, description="JSON Schema ответа"
    )
    auth: PluginAuthSettingsV1 | None = None
    description: str | None = Field(None, description="Человекочитаемое описание")
    is_default: bool = Field(
        default=False, description="Флаг плагина по умолчанию (fallback)"
    )


class PluginRegistrationRequestV1(BaseModel):
    """Запрос на регистрацию плагина в ядре."""

    name: str
    version: str
    base_url: HttpUrl
    manifest: PluginManifestV1
    scopes: list[str] = Field(default_factory=list)
    capabilities: dict[str, Any] = Field(default_factory=dict)


class PluginRegistrationResponseV1(BaseModel):
    """Ответ ядра при регистрации плагина."""

    plugin_id: UUID
    token: str
    issued_at: datetime
    expires_at: datetime


class PluginHeartbeatRequestV1(BaseModel):
    """Запрос heartbeat от плагина для поддержания статуса."""

    plugin_id: UUID
    status: PluginStatus
    latency_ms: int
    queue_depth: int
    metrics: dict[str, Any] = Field(default_factory=dict)


class PluginCatalogItemV1(BaseModel):
    """Элемент каталога плагинов, возвращаемый ядром."""

    plugin_id: UUID
    name: str
    version: str
    status: PluginStatus
    last_heartbeat: datetime | None
    intents: list[str]


class PluginCatalogResponseV1(BaseModel):
    """Ответ API `/api/v1/plugins` со списком активных плагинов."""

    items: list[PluginCatalogItemV1]


class PluginInvocationRequestV1(BaseModel):
    """Данные вызова плагина, которые ядро отправляет внешнему сервису."""

    dialog_id: UUID
    user_id: UUID
    intent: str
    payload: dict[str, Any]
    trace_id: str


class PluginInvocationResultV1(BaseModel):
    """Результат вызова плагина, возвращаемый ядру."""

    status: InvocationStatus
    output: dict[str, Any] | None = None
    usage: LLMUsageV1 | None = None
    error: str | None = None


class PluginInvocationLogV1(BaseModel):
    """Служебная структура логирования вызовов плагинов."""

    plugin_id: UUID
    invocation_id: UUID
    dialog_id: UUID
    status: InvocationStatus
    started_at: datetime
    finished_at: datetime | None = None

    @field_validator("started_at", "finished_at", mode="before")
    @classmethod
    def _ensure_timezone(cls, value: datetime | None) -> datetime | None:
        """Приводит значения к UTC, если они наивные."""

        if value is None:
            return value
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)


__all__ = [
    "DialogMessageCreateV1",
    "DialogMessageResponseV1",
    "DialogResetRequestV1",
    "DialogSnapshotResponseV1",
    "DialogSummaryV1",
    "HistoricalMessageV1",
    "InvocationStatus",
    "LLMUsageV1",
    "MessagePayloadType",
    "MessagePayloadV1",
    "PluginAuthSettingsV1",
    "PluginCatalogItemV1",
    "PluginCatalogResponseV1",
    "PluginEventType",
    "PluginHeartbeatRequestV1",
    "PluginInvocationLogV1",
    "PluginInvocationRequestV1",
    "PluginInvocationResultV1",
    "PluginManifestV1",
    "PluginMessageV1",
    "PluginRegistrationRequestV1",
    "PluginRegistrationResponseV1",
    "PluginStatus",
]
