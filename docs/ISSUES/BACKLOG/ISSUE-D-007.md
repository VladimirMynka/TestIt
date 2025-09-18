KEYWORDS: issue, developer, telegram, aiogram, адаптер
[ANCHOR:PROJECT:TGBOT:ISSUE:D-007]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007">
# Issue D-007 — Реализовать асинхронный адаптер Telegram на aiogram

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/bots/TELEGRAM.md` (после A-001)
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:GOAL">
## Цель
Создать модуль `bots/telegram/app` с aiogram-приложением, реализовать маршруты для сообщений и команды «обновить диалог», интегрировать конфигурацию webhook/polling, настроить проксирование запросов в ядро по контракту. Реализовать middleware для трассировки и авторизации.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:DELIVERABLES">
## Ожидаемые артефакты
- Код aiogram-приложения, конфигурация запуска, докер-образ.
- Тесты на парсинг сообщений и корректный вызов ядра (моки HTTP).
- Обновлённый `bots/telegram/README.md` с описанием запуска.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-001`, `ISSUE-D-001`, `ISSUE-D-002`
- Разблокирует: `ISSUE-D-008`, `ISSUE-T-003`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-007:NOTES">
## Примечания
Необходимо предусмотреть возможность переключения между webhook и polling в зависимости от окружения. Источник истины — контракт Telegram-бота.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-007">
