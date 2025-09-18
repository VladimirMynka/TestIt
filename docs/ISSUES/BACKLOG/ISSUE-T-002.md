KEYWORDS: issue, tester, плагины, интеграция, контрактные тесты
[ANCHOR:PROJECT:TGBOT:ISSUE:T-002]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002">
# Issue T-002 — Написать интеграционные тесты ядра и плагинов

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:ROLE">
## Роль
- [ ] Architect
- [ ] Developer
- [x] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/plugins/MANIFEST.md`, `docs/CONTRACTS/plugins/TEXT_REPLY.md`, `docs/CONTRACTS/plugins/PLUGIN_GENERATOR.md`
- Протоколы: `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:GOAL">
## Цель
Реализовать тесты, запускающие ядро и плагины в тестовом окружении (pytest + docker-compose или testcontainers), проверяющие регистрацию плагинов, маршрутизацию по интентам и обработку ошибок.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:DELIVERABLES">
## Ожидаемые артефакты
- Набор интеграционных тестов в `core/tests/integration/test_plugins.py`.
- Скрипт запуска `scripts/tests/run_integration.sh`.
- Отчёт о результатах в CI (использование сервисов docker-compose).
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-003`, `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-003`, `ISSUE-D-004`, `ISSUE-D-005`, `ISSUE-D-006`, `ISSUE-D-008`, `ISSUE-D-009`, `ISSUE-T-001`
- Разблокирует: `ISSUE-T-003`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-002:NOTES">
## Примечания
Тесты должны использовать те же manifest-схемы, что и плагины, и проверять idempotent-поведение регистрации.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-002">
