# KEYWORDS: tests, plugin-manager, async, httpx, fastapi
"""[ANCHOR:PROJECT:TGBOT:CORE:TESTS:SERVICES:PLUGIN-MANAGER]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:TESTS:SERVICES:PLUGIN-MANAGER">
Юнит-тесты менеджера плагинов. Проверяют регистрацию, каталог, heartbeat и
асинхронный вызов через HTTP-клиент. Источник истины — контракт ядра.
<HARMONY:END name="PROJECT:TGBOT:CORE:TESTS:SERVICES:PLUGIN-MANAGER">
"""

from __future__ import annotations

from uuid import uuid4

import httpx
import pytest

from core.app.schemas.v1alpha import (
    DialogMessageCreateV1,
    MessagePayloadV1,
    MessagePayloadType,
    PluginCatalogResponseV1,
    PluginHeartbeatRequestV1,
    PluginManifestV1,
    PluginRegistrationRequestV1,
    PluginStatus,
)
from core.app.services.plugin_manager import PluginManager
from core.app.telemetry.tracing import get_trace_context


@pytest.mark.asyncio
async def test_register_and_list_plugin() -> None:
    """Регистрация плагина заносит его в каталог."""

    async with httpx.AsyncClient() as client:
        manager = PluginManager(client)
        registration = PluginRegistrationRequestV1(
            name="text_reply",
            version="1.0.0",
            base_url="http://plugin.local",
            manifest=PluginManifestV1(
                name="text_reply",
                version="1.0.0",
                intents=["text_reply"],
                activation_condition=None,
                input_schema={},
                output_schema={},
                is_default=True,
            ),
        )
        response = await manager.register(registration)
        catalog = await manager.list_catalog()
        assert isinstance(catalog, PluginCatalogResponseV1)
        assert catalog.items[0].plugin_id == response.plugin_id
        assert catalog.items[0].status == PluginStatus.ACTIVE


@pytest.mark.asyncio
async def test_heartbeat_updates_status() -> None:
    """Heartbeat переводит плагин в нужный статус."""

    async with httpx.AsyncClient() as client:
        manager = PluginManager(client)
        registration = PluginRegistrationRequestV1(
            name="text_reply",
            version="1.0.0",
            base_url="http://plugin.local",
            manifest=PluginManifestV1(
                name="text_reply",
                version="1.0.0",
                intents=["text_reply"],
                activation_condition=None,
                input_schema={},
                output_schema={},
                is_default=True,
            ),
        )
        response = await manager.register(registration)
        heartbeat = PluginHeartbeatRequestV1(
            plugin_id=response.plugin_id,
            status=PluginStatus.DEGRADED,
            latency_ms=120,
            queue_depth=5,
            metrics={"requests_total": 10},
        )
        await manager.heartbeat(heartbeat)
        catalog = await manager.list_catalog()
        assert catalog.items[0].status == PluginStatus.DEGRADED


@pytest.mark.asyncio
async def test_route_dialog_message_invokes_plugin() -> None:
    """Маршрутизация сообщения вызывает зарегистрированный плагин."""

    trace = get_trace_context()

    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("Authorization", "").startswith("Bearer ")
        payload = request.json()
        assert payload["intent"] == "text_reply"
        body = {
            "status": "succeeded",
            "output": {"text": "Привет!", "content_type": "text/plain"},
        }
        return httpx.Response(200, json=body)

    transport = httpx.MockTransport(handler)
    async with httpx.AsyncClient(transport=transport) as client:
        manager = PluginManager(client)
        registration = PluginRegistrationRequestV1(
            name="text_reply",
            version="1.0.0",
            base_url="http://plugin.local",
            manifest=PluginManifestV1(
                name="text_reply",
                version="1.0.0",
                intents=["text_reply"],
                activation_condition=None,
                input_schema={},
                output_schema={},
                is_default=True,
            ),
        )
        await manager.register(registration)
        message = DialogMessageCreateV1(
            dialog_id=uuid4(),
            user_id=uuid4(),
            message_id="mid",
            trace_id=uuid4(),
            payload=MessagePayloadV1(type=MessagePayloadType.TEXT, text="Привет"),
            metadata={"locale": "ru"},
        )
        response = await manager.route_dialog_message(message, trace=trace)
        assert response.plugin_responses[0].content == "Привет!"
        assert response.status.value == "succeeded"
