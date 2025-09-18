KEYWORDS: issue, developer, llm, openai, асинхронный клиент
[ANCHOR:PROJECT:TGBOT:ISSUE:D-004]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004">
# Issue D-004 — Реализовать асинхронный LLM-клиент на базе OpenAI

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/LLM_CLIENT.md`, `docs/CONTRACTS/plugins/TEXT_REPLY.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:GOAL">
## Цель
Создать пакет `libs/llm_client` с асинхронным клиентом OpenAI (`AsyncOpenAIClient`) поверх официальной библиотеки, реализовать методы `invoke`, `stream`, `embedding`. Настроить конфигурацию через `pydantic`-модель и внедрить ретраи/таймауты.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:DELIVERABLES">
## Ожидаемые артефакты
- Реализация клиента и интерфейса для зависимых модулей.
- Юнит-тесты с моками OpenAI API (`pytest-asyncio`).
- Документация по конфигурации (`libs/llm_client/README.md`).
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-D-001`
- Разблокирует: `ISSUE-D-005`, `ISSUE-D-006`, `ISSUE-T-002`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-004:NOTES">
## Примечания
Использовать новую версию OpenAI SDK с асинхронными методами. Все ключи хранятся в переменных окружения и не попадают в код.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-004">
