KEYWORDS: issue, architect, core, схемы, api
[ANCHOR:PROJECT:TGBOT:ISSUE:A-002]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002">
# Issue A-002 — Спроектировать асинхронные схемы API ядра и каркас модулей

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:ROLE">
## Роль
- [x] Architect
- [ ] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/DATABASE.md`, `docs/CONTRACTS/core/SCHEMAS.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`, `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`
- Кеш: Redis как слой быстрой выборки токенов и состояний (ответ на Q004)
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:GOAL">
## Цель
Зафиксировать в `core/README.md` и контракте `docs/CONTRACTS/core/SCHEMAS.md` структуру пакетов `core/app`, интерфейсы сервисов, Pydantic-модели запросов и ответов для всех эндпоинтов ядра, события менеджера плагинов и очередь обработки диалогов. Обеспечить единое описание для разработчиков и тестировщиков.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:DELIVERABLES">
## Ожидаемые артефакты
- Новый контракт `docs/CONTRACTS/core/SCHEMAS.md` с версиями Pydantic-моделей (`v1alpha`).
- Обновлённый `core/README.md` с деревом модулей, событиями и точками расширения.
- Таблица соответствия эндпоинтов → схемы → события плагинов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:DEPENDENCIES">
## Зависимости
- Блокирующие: —
- Разблокирует: `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-003`, `ISSUE-T-001`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:CHECKS">
## Проверки
- [x] Контракты обновлены
- [x] Протоколы обновлены
- [x] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:OUTCOME">
## Итог
- Сформирован контракт `docs/CONTRACTS/core/SCHEMAS.md` (`v1alpha`) с определениями DTO, событиями и таблицей соответствия API ↔ схемы ↔ события.
- `core/README.md` расширен картой модулей, описанием сервисов, очередей и Redis-кеша для сессий.
- Roadmap, Summary и Plan отражают перенос зависимых задач в `IN_PROGRESS`/`BACKLOG` и зафиксированные схемы.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:OUTCOME">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-002:NOTES">
## Примечания
Источник истины по схемам API ядра — `docs/CONTRACTS/core/SCHEMAS.md`. Все реализации должны импортировать типы из общего пакета `core/app/schemas/v1alpha`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-002">
