# KEYWORDS: api, health, ядро, fastapi, наблюдаемость
"""[ANCHOR:PROJECT:TGBOT:CORE:APP:API:HEALTH]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:APP:API:HEALTH">
Эндпоинты технического состояния ядра (`/health`, `/metrics`). Они служат
минимальной реализацией требований наблюдаемости до внедрения полноценного
Prometheus-экспортера.
<HARMONY:END name="PROJECT:TGBOT:CORE:APP:API:HEALTH">
"""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, Response

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", summary="Проверка доступности ядра")
async def healthcheck() -> dict[str, str]:
    """Возвращает статус сервиса и отметку времени."""

    return {
        "status": "ok",
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
    }


@router.get("/metrics", summary="Черновой экспорт метрик")
async def metrics() -> Response:
    """Возвращает заготовку в формате Prometheus (будет расширена)."""

    body = "# TYPE core_uptime_seconds counter\ncore_uptime_seconds 0"
    return Response(content=body, media_type="text/plain; version=0.0.4")


__all__ = ["router", "healthcheck", "metrics"]
