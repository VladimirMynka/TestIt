# KEYWORDS: core, fastapi, приложение, плагины, инициализация
"""[ANCHOR:PROJECT:TGBOT:CORE:APP]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:APP">
Пакет `core.app` содержит точку входа FastAPI и прикладные модули (роутеры,
зависимости, сервисы), реализующие контракт ядра (`docs/CONTRACTS/CORE.md`).
<HARMONY:END name="PROJECT:TGBOT:CORE:APP">
"""

__all__ = [
    "create_app",
]

from .main import create_app
