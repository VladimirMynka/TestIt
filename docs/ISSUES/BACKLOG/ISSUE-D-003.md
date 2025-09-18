KEYWORDS: issue, developer, база данных, alembic, sqlalchemy
[ANCHOR:PROJECT:TGBOT:ISSUE:D-003]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003">
# Issue D-003 — Реализовать модели БД и миграции Alembic

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/core/DATABASE.md`, `docs/CONTRACTS/CORE.md`
- Протоколы: `docs/PROTOCOLS/RELEASE_PIPELINE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:GOAL">
## Цель
Создать асинхронные модели SQLAlchemy для сущностей `users`, `dialogs`, `messages`, `plugins`, `plugin_calls`, `audit_logs`, `migrations_info`. Настроить Alembic со стартовой миграцией, seed-данными для стандартных плагинов и ensure `asyncpg` подключение.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:DELIVERABLES">
## Ожидаемые артефакты
- Пакет `core/app/db/models` с моделями и датаклассами для чтения.
- Alembic-конфигурация и начальная миграция.
- Документация в `docs/CONTRACTS/core/DATABASE.md` с ссылкой на миграцию.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-002`, `ISSUE-D-001`
- Разблокирует: `ISSUE-D-002`, `ISSUE-D-008`, `ISSUE-T-001`, `ISSUE-T-002`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-003:NOTES">
## Примечания
Миграции должны использовать версии с timestamp и хранить seed через Alembic data migration. Источник истины для схем данных — контракт `DATABASE.md`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-003">
