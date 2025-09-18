KEYWORDS: issue, developer, плагин, text-reply, async
[ANCHOR:PROJECT:TGBOT:ISSUE:D-005]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005">
# Issue D-005 — Реализовать плагин текстового ответа

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/plugins/TEXT_REPLY.md`, `docs/CONTRACTS/plugins/MANIFEST.md`, `docs/CONTRACTS/LLM_CLIENT.md`
- Протоколы: `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:GOAL">
## Цель
Реализовать сервис `plugins/text_reply` (FastAPI или Starlette) с эндпоинтами `/health`, `/manifest`, `/invoke`, интегрировать `AsyncOpenAIClient`, поддержать локализацию, ретраи и логирование в формате контракта. Обеспечить dockerfile и запуск через uvicorn.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:DELIVERABLES">
## Ожидаемые артефакты
- Код плагина, тесты и manifest.
- Скрипт развертывания в `docker/` и `docker-compose` сервис.
- Документация `plugins/text_reply/README.md` с примерами запросов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-003`, `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-004`
- Разблокирует: `ISSUE-T-002`, `ISSUE-D-008`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-005:NOTES">
## Примечания
Плагин должен поддерживать асинхронную обработку запросов и совместимость с будущим мониторингом `/metrics`. Источник истины — контракты плагина.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-005">
