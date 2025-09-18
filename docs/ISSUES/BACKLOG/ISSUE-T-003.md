KEYWORDS: issue, tester, telegram, e2e, asyncio
[ANCHOR:PROJECT:TGBOT:ISSUE:T-003]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003">
# Issue T-003 — Провести end-to-end тестирование Telegram-бота

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:ROLE">
## Роль
- [ ] Architect
- [ ] Developer
- [x] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/bots/TELEGRAM.md`, `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/SCHEMAS.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:GOAL">
## Цель
Настроить end-to-end тест, поднимающий docker-compose окружение и эмулирующий сообщения Telegram через aiogram тестовый клиент. Проверить обработку команды «обновить диалог», маршрутизацию на плагин текстового ответа и логирование в БД.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:DELIVERABLES">
## Ожидаемые артефакты
- Тестовый сценарий в `bots/telegram/tests/test_e2e.py`.
- Скрипт `scripts/tests/run_e2e.sh`.
- Отчёт о прохождении в CI (workflow `ci.yml`).
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-001`, `ISSUE-A-002`, `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-003`, `ISSUE-D-005`, `ISSUE-D-006`, `ISSUE-D-007`, `ISSUE-D-008`, `ISSUE-D-009`, `ISSUE-T-002`
- Разблокирует: —
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:T-003:NOTES">
## Примечания
Тесты должны повторно использовать общие схемы из `core.app.schemas` и конфигурацию Docker из `docker-compose.yml`, чтобы избежать дрейфа.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:T-003">
