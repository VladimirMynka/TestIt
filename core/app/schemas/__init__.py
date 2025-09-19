# KEYWORDS: схемы, ядро, pydantic, версии, v1alpha
"""[ANCHOR:PROJECT:TGBOT:CORE:SCHEMAS]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:SCHEMAS">
Пакет `core.app.schemas` хранит Pydantic-модели, соответствующие контракту
`docs/CONTRACTS/core/SCHEMAS.md`. Текущая активная версия — `v1alpha`.
<HARMONY:END name="PROJECT:TGBOT:CORE:SCHEMAS">
"""

from . import v1alpha

__all__ = ["v1alpha"]
