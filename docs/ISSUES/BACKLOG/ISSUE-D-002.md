KEYWORDS: issue, developer, fastapi, ядро, менеджер плагинов
[ANCHOR:PROJECT:TGBOT:ISSUE:D-002]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002">
# Issue D-002 — Реализовать каркас FastAPI ядра и менеджер плагинов

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/SCHEMAS.md` (после A-002), `docs/CONTRACTS/plugins/MANIFEST.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`, `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:GOAL">
## Цель
Создать асинхронное приложение FastAPI (`core/app/main.py`) с роутерами `dialogs`, `plugins`, `health`, реализовать менеджер плагинов (регистрация, список активных, вызов через HTTP-клиент), интегрировать логирование и трассировки. Обеспечить совместимость с схемами и событиями, определёнными в A-002 и A-003.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:DELIVERABLES">
## Ожидаемые артефакты
- Реализация `core/app/main.py`, `core/app/api/*`, `core/app/services/plugin_manager.py`.
- Конфигурация `core/app/dependencies.py` с DI для LLM клиента и БД.
- Юнит-тесты для менеджера плагинов (минимальные, async).
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-002`, `ISSUE-A-003`, `ISSUE-D-001`
- Разблокирует: `ISSUE-D-005`, `ISSUE-D-006`, `ISSUE-D-008`, `ISSUE-T-001`, `ISSUE-T-002`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-002:NOTES">
## Примечания
При реализации HTTP-клиента для плагинов использовать `httpx.AsyncClient` с таймаутами и ретраями. Источник истины — контракты ядра и плагинов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-002">
