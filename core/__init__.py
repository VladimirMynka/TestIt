# KEYWORDS: core, пакет, fastapi, плагины, инфраструктура
"""[ANCHOR:PROJECT:TGBOT:CORE:PACKAGE]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:PACKAGE">
Пакет `core` агрегирует FastAPI-приложение, менеджер плагинов, работу с БД и Redis.
Источник истины — контракт `docs/CONTRACTS/CORE.md` и сопутствующие схемы.
<HARMONY:END name="PROJECT:TGBOT:CORE:PACKAGE">
"""

from .app import create_app

__all__ = ["create_app"]
