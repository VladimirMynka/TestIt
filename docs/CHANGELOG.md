KEYWORDS: changelog, версии, история, документация, обновления
[ANCHOR:PROJECT:TGBOT:DOCS:CHANGELOG]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG">
# Журнал изменений

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG:POLICY">
## Политика ведения
Мы следуем стандарту Keep a Changelog. Даты указываются в формате ISO8601. Источник истины — соответствующие контракты и протоколы.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG:POLICY">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG:UNRELEASED">
## [Unreleased]
### Добавлено
- Контракт Telegram-бота `docs/CONTRACTS/bots/TELEGRAM.md` (long polling, aiogram, Redis outbox).
- Контракт схем `docs/CONTRACTS/core/SCHEMAS.md` (`v1alpha`) и карта соответствия эндпоинтов ↔ событий.
- Обновлённые каталоги Issues (`docs/ISSUES/{BACKLOG,IN_PROGRESS,CLOSED,REJECTED}`) с фиксацией статусов.
- Новые триггеры `TR-008…TR-010` для событий плагинов и деградации Redis.

### Изменено
- `docs/CONTRACTS/CORE.md`, `core/DATABASE.md`, `plugins/MANIFEST.md` расширены регистрацией, heartbeat, Redis Streams и статусами вызовов.
- `docs/ARCHITECTURE.md`, `core/README.md`, `docs/COMPATIBILITY.md`, `docs/ROADMAP.md`, `human-friendly/SUMMARY.md` синхронизированы с решениями (OpenAI, long polling, Redis).
- Roadmap и Plan обновлены под новую структуру Issues и статусы задач.

### Исправлено
- Уточнены ссылки и версии контрактов в `docs/CONTRACTS/README.md` и `docs/TRIGGERS.md`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG:UNRELEASED">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG:HISTORY">
## История релизов
*Пока нет опубликованных релизов.*
<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG:HISTORY">

<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG">
