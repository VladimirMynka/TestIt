KEYWORDS: issue, tester, core, contract tests, pytest
[ANCHOR:PROJECT:TGBOT:ISSUE:T-001]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001">
# Issue T-001 — Подготовить контрактные тесты API ядра

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:ROLE">
## Роль
- [ ] Architect
- [ ] Developer
- [x] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/SCHEMAS.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:GOAL">
## Цель
Создать набор pytest-тестов (async) в `core/tests/test_api_contract.py`, проверяющих соответствие эндпоинтов схемам (`pydantic` модели), корректность кодов ответов и логики «обновить диалог».
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:DELIVERABLES">
## Ожидаемые артефакты
- Тестовые данные и фабрики для диалогов.
- Отчёт о покрытии (минимум 70% для API) в CI.
- Документация по запуску тестов в `core/README.md`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-002`, `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-003`, `ISSUE-D-009`
- Разблокирует: `ISSUE-T-002`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-001:NOTES">
## Примечания
Тесты должны импортировать общие Pydantic-схемы из пакета `core.app.schemas`, чтобы исключить расхождения интерфейсов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-001">
