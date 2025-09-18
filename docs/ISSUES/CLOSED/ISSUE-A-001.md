KEYWORDS: issue, architect, telegram, контракт, пуллинг
[ANCHOR:PROJECT:TGBOT:ISSUE:A-001]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001">
# Issue A-001 — Специфицировать контракт Telegram-бота

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:ROLE">
## Роль
- [x] Architect
- [ ] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/DATABASE.md`, `docs/CONTRACTS/core/SCHEMAS.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`
- Используемая SDK: `aiogram` (асинхронная Python-библиотека для Telegram)
- Режим доставки апдейтов: только long polling (webhook переносится на следующий этап)
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:GOAL">
## Цель
Подготовить документ `docs/CONTRACTS/bots/TELEGRAM.md`, описывающий асинхронные сценарии интеграции бота с ядром: обработку long polling апдейтов, сигнатуры callback-ов, преобразование сообщений в формат ядра и ограничение на функцию «обновить диалог». Контракт должен синхронизироваться с существующими схемами диалогов и журналированием.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:DELIVERABLES">
## Ожидаемые артефакты
- Новый контракт Telegram-бота с описанием API, очередей задач и политик ошибок.
- Обновлённый `docs/ARCHITECTURE.md` с ссылкой на контракт и фиксированным режимом long polling.
- Обновлённые человеко-ориентированные документы с решением по SDK и режиму запуска.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:DEPENDENCIES">
## Зависимости
- Блокирующие: —
- Разблокирует: `ISSUE-D-007`, `ISSUE-T-003`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:CHECKS">
## Проверки
- [x] Контракты обновлены
- [x] Протоколы обновлены
- [x] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:OUTCOME">
## Итог
- Добавлен контракт `docs/CONTRACTS/bots/TELEGRAM.md`, фиксирующий поток long polling, асинхронные обработчики и связь с API ядра.
- `docs/ARCHITECTURE.md`, `docs/ROADMAP.md` и `human-friendly/SUMMARY.md` обновлены ссылками на контракт и решением о long polling.
- В `docs/QUESTIONS.md` зафиксирован ответ: используем OpenAI, long polling и Redis для кеша диалогов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:OUTCOME">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-001:NOTES">
## Примечания
Источник истины по взаимодействию бота и ядра — контракт `docs/CONTRACTS/bots/TELEGRAM.md`. Все схемы сообщений должны ссылаться на `docs/CONTRACTS/core/SCHEMAS.md`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-001">
