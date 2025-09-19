# KEYWORDS: менеджер, плагины, fastapi, httpx, трассировка
"""[ANCHOR:PROJECT:TGBOT:CORE:SERVICES:PLUGIN-MANAGER]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:SERVICES:PLUGIN-MANAGER">
Сервис управления плагинами реализует требования `docs/CONTRACTS/CORE.md`
и `docs/CONTRACTS/plugins/MANIFEST.md`: регистрация, heartbeat, каталог и
вызов плагинов через HTTP. Источник истины — указанные контракты.
<HARMONY:END name="PROJECT:TGBOT:CORE:SERVICES:PLUGIN-MANAGER">
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Iterable
from uuid import UUID, uuid4

import httpx

from ..schemas.v1alpha import (
    DialogMessageCreateV1,
    DialogMessageResponseV1,
    InvocationStatus,
    PluginCatalogItemV1,
    PluginCatalogResponseV1,
    PluginHeartbeatRequestV1,
    PluginInvocationRequestV1,
    PluginInvocationResultV1,
    PluginManifestV1,
    PluginMessageV1,
    PluginRegistrationRequestV1,
    PluginRegistrationResponseV1,
    PluginStatus,
)
from ..telemetry.tracing import TraceContext, get_trace_context

_LOGGER = logging.getLogger(__name__)
_TOKEN_TTL = timedelta(hours=1)


@dataclass(slots=True)
class PluginRecord:
    """Служебная запись зарегистрированного плагина."""

    plugin_id: UUID
    token: str
    registration: PluginRegistrationRequestV1
    status: PluginStatus = PluginStatus.ACTIVE
    last_heartbeat: datetime | None = None

    def as_catalog_item(self) -> PluginCatalogItemV1:
        """Формирует элемент каталога для публичного API."""

        return PluginCatalogItemV1(
            plugin_id=self.plugin_id,
            name=self.registration.name,
            version=self.registration.version,
            status=self.status,
            last_heartbeat=self.last_heartbeat,
            intents=list(self.registration.manifest.intents),
        )


class PluginManager:
    """Высокоуровневый сервис управления жизненным циклом плагинов."""

    def __init__(self, http_client: httpx.AsyncClient) -> None:
        self._http_client = http_client
        self._registry: dict[UUID, PluginRecord] = {}
        self._lock = asyncio.Lock()

    async def register(
        self, registration: PluginRegistrationRequestV1
    ) -> PluginRegistrationResponseV1:
        """Регистрирует плагин и выдаёт токен доступа."""

        trace = get_trace_context()
        async with self._lock:
            plugin_id = uuid4()
            token = uuid4().hex
            record = PluginRecord(
                plugin_id=plugin_id,
                token=token,
                registration=registration,
                status=PluginStatus.ACTIVE,
                last_heartbeat=datetime.now(tz=timezone.utc),
            )
            self._registry[plugin_id] = record
        issued_at = datetime.now(tz=timezone.utc)
        expires_at = issued_at + _TOKEN_TTL
        _LOGGER.info(
            "plugin_registered",
            extra={
                "trace_id": trace.trace_id,
                "plugin_id": str(plugin_id),
                "name": registration.name,
                "version": registration.version,
            },
        )
        return PluginRegistrationResponseV1(
            plugin_id=plugin_id,
            token=token,
            issued_at=issued_at,
            expires_at=expires_at,
        )

    async def heartbeat(self, heartbeat: PluginHeartbeatRequestV1) -> None:
        """Обновляет состояние плагина на основании heartbeat-сообщения."""

        async with self._lock:
            record = self._registry.get(heartbeat.plugin_id)
            if record is None:
                raise KeyError(f"Плагин {heartbeat.plugin_id} не зарегистрирован")
            record.status = heartbeat.status
            record.last_heartbeat = datetime.now(tz=timezone.utc)
        _LOGGER.debug(
            "plugin_heartbeat",
            extra={
                "plugin_id": str(heartbeat.plugin_id),
                "status": heartbeat.status.value,
                "latency_ms": heartbeat.latency_ms,
                "queue_depth": heartbeat.queue_depth,
            },
        )

    async def list_catalog(self) -> PluginCatalogResponseV1:
        """Возвращает список зарегистрированных плагинов."""

        async with self._lock:
            items = [record.as_catalog_item() for record in self._registry.values()]
        return PluginCatalogResponseV1(items=items)

    async def get_plugin(self, plugin_id: UUID) -> PluginRecord:
        """Возвращает зарегистрированный плагин или выбрасывает исключение."""

        async with self._lock:
            record = self._registry.get(plugin_id)
        if record is None:
            raise KeyError(f"Плагин {plugin_id} не зарегистрирован")
        return record

    async def route_dialog_message(
        self,
        message: DialogMessageCreateV1,
        *,
        trace: TraceContext | None = None,
    ) -> DialogMessageResponseV1:
        """Выбирает плагин и инициирует его вызов для сообщения диалога."""

        trace = trace or get_trace_context()
        plugin = await self._select_plugin_for_message(message)
        if plugin is None:
            _LOGGER.warning(
                "plugin_not_found",
                extra={"trace_id": trace.trace_id, "dialog_id": str(message.dialog_id)},
            )
            return DialogMessageResponseV1(
                dialog_id=message.dialog_id,
                trace_id=message.trace_id,
                plugin_responses=[],
                status=InvocationStatus.REJECTED,
            )
        invocation = PluginInvocationRequestV1(
            dialog_id=message.dialog_id,
            user_id=message.user_id,
            intent=self._determine_intent(plugin.registration.manifest),
            payload={
                "text": message.payload.text,
                "metadata": message.metadata,
                "attachments": [
                    attachment.model_dump() for attachment in message.payload.attachments
                ],
            },
            trace_id=trace.trace_id,
        )
        result = await self.invoke_plugin(plugin, invocation, trace=trace)
        response = DialogMessageResponseV1(
            dialog_id=message.dialog_id,
            trace_id=message.trace_id,
            status=result.status,
            plugin_responses=[
                PluginMessageV1(
                    plugin_id=plugin.plugin_id,
                    content=result.output.get("text", "") if result.output else "",
                    content_type=result.output.get("content_type", "text/plain")
                    if result.output
                    else "text/plain",
                    suggested_actions=result.output.get("suggested_actions", [])
                    if result.output
                    else [],
                )
            ]
            if result.output
            else [],
            usage=result.usage,
        )
        return response

    async def invoke_plugin(
        self,
        plugin: PluginRecord,
        invocation: PluginInvocationRequestV1,
        *,
        trace: TraceContext | None = None,
    ) -> PluginInvocationResultV1:
        """Выполняет HTTP-вызов плагина с учётом таймаутов и трассировки."""

        trace = trace or get_trace_context()
        url = str(invocation.payload.get("endpoint") or "")
        if not url:
            base_url = str(plugin.registration.base_url).rstrip("/")
            url = f"{base_url}/invoke"
        headers = {
            "Authorization": f"Bearer {plugin.token}",
            "X-Trace-Id": trace.trace_id,
        }
        payload = invocation.model_dump()
        _LOGGER.debug(
            "plugin_invocation_started",
            extra={
                "trace_id": trace.trace_id,
                "plugin_id": str(plugin.plugin_id),
                "intent": invocation.intent,
            },
        )
        try:
            response = await self._http_client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            result = PluginInvocationResultV1.model_validate(
                {
                    "status": data.get("status", InvocationStatus.SUCCEEDED.value),
                    "output": data.get("output"),
                    "usage": data.get("usage"),
                    "error": data.get("error"),
                }
            )
            _LOGGER.info(
                "plugin_invocation_completed",
                extra={
                    "trace_id": trace.trace_id,
                    "plugin_id": str(plugin.plugin_id),
                    "status": result.status.value,
                },
            )
            return result
        except httpx.HTTPError as exc:  # pragma: no cover - сетевые ошибки
            _LOGGER.exception(
                "plugin_failed",
                extra={
                    "trace_id": trace.trace_id,
                    "plugin_id": str(plugin.plugin_id),
                    "error": str(exc),
                },
            )
            return PluginInvocationResultV1(
                status=InvocationStatus.FAILED,
                output=None,
                usage=None,
                error=str(exc),
            )

    async def _select_plugin_for_message(
        self, message: DialogMessageCreateV1
    ) -> PluginRecord | None:
        """Находит подходящий плагин по интентам или возвращает fallback."""

        async with self._lock:
            records: Iterable[PluginRecord] = list(self._registry.values())
        if not records:
            return None
        # На данном этапе отсутствует классификатор; выбираем default-плагин.
        for record in records:
            if record.registration.manifest.is_default:
                return record
        return next(iter(records), None)

    @staticmethod
    def _determine_intent(manifest: PluginManifestV1) -> str:
        """Выбирает ключевой интент плагина для маршрутизации."""

        return manifest.intents[0] if manifest.intents else "default"


__all__ = ["PluginManager", "PluginRecord"]
