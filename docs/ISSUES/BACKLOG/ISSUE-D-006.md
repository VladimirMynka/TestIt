KEYWORDS: issue, developer, плагин, генератор, scaffolding
[ANCHOR:PROJECT:TGBOT:ISSUE:D-006]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006">
# Issue D-006 — Реализовать плагин генерации плагинов (MVP)

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/plugins/PLUGIN_GENERATOR.md`, `docs/CONTRACTS/plugins/MANIFEST.md`, `docs/CONTRACTS/LLM_CLIENT.md`
- Протоколы: `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:GOAL">
## Цель
Создать минимальную версию сервиса `plugins/plugin_generator` с эндпоинтами `/health`, `/manifest`, `/invoke`, который генерирует zip-архив со scaffold на основе шаблона (без автоматического деплоя). Интегрировать `AsyncOpenAIClient` для генерации кода и записывать инструкции по ручному развертыванию.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:DELIVERABLES">
## Ожидаемые артефакты
- Код плагина, шаблоны scaffold в `plugins/plugin_generator/templates`.
- Тесты на корректность схемы manifest и генерации структуры.
- Документация по использованию в `plugins/plugin_generator/README.md`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-003`, `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-004`
- Разблокирует: `ISSUE-T-002`, `ISSUE-D-008`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-006:NOTES">
## Примечания
MVP ограничивается генерацией архива и инструкциями. Интеграцию автодеплоя нужно вынести в будущие задачи.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-006">
