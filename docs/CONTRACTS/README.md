KEYWORDS: контракты, ядро, плагины, документация, управление
[ANCHOR:PROJECT:TGBOT:DOCS:CONTRACTS:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRACTS:README">
# Каталог контрактов

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRACTS:README:PURPOSE">
## Назначение
Контракты фиксируют требования к подсистемам (ядро, плагины, LLM-клиент, бот, база данных). Источник истины для реализации — конкретные контракты.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRACTS:README:PURPOSE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRACTS:README:STRUCTURE">
## Структура каталога
- `CORE.md` — API и сервисные требования ядра (`V1.1`).
- `core/DATABASE.md` — схема PostgreSQL и миграции (`V1.1`).
- `core/SCHEMAS.md` — Pydantic-схемы API (`v1alpha`).
- `LLM_CLIENT.md` — библиотека LLM.
- `bots/TELEGRAM.md` — контракт адаптера Telegram (long polling, `V1.0`).
- `plugins/` — manifest и специализированные плагины (`MANIFEST.md`, `TEXT_REPLY.md`, `PLUGIN_GENERATOR.md`).
- `templates/` — шаблоны для новых контрактов.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRACTS:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRACTS:README:PROCESS">
## Процесс работы
1. Перед изменениями изучить соответствующий контракт и Roadmap.
2. При обновлении реализации синхронно обновить контракт и `docs/CHANGELOG.md`.
3. Согласовать несовместимые изменения через `docs/COMPATIBILITY.md`.
4. Для новых подсистем создать контракт на основе шаблона.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRACTS:README:PROCESS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRACTS:README:VERSIONING">
## Версионирование
- Контракты используют схему `VMAJOR.MINOR` (например, `V1.1`).
- Обновления, влияющие на совместимость, увеличивают `MAJOR`.
- Минорные обновления фиксируются в таблице изменений и Roadmap.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRACTS:README:VERSIONING">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRACTS:README:LINKS">
## Быстрые ссылки
- Архитектура: `docs/ARCHITECTURE.md`
- Политика совместимости: `docs/COMPATIBILITY.md`
- Протокол ведения контрактов: `docs/PROTOCOLS/DEV_SESSION.md`
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRACTS:README:LINKS">

<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRACTS:README">
