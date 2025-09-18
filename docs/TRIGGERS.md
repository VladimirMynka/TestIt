KEYWORDS: триггеры, события, эскалация, качество, контроль
[ANCHOR:PROJECT:TGBOT:DOCS:TRIGGERS]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:TRIGGERS">
# Триггеры и реакции

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:TRIGGERS:OVERVIEW">
## Обзор
Триггеры фиксируют условия, требующие действий (эскалация, обновление документации, запуск протоколов). Источник истины — этот документ, `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/plugins/MANIFEST.md` и связанные протоколы.
<HARMONY:END name="PROJECT:TGBOT:DOCS:TRIGGERS:OVERVIEW">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:TRIGGERS:TABLE">
## Таблица триггеров
| ID | Условие | Действие | Протокол |
|----|---------|----------|----------|
| TR-001 | Несогласованная правка контракта | Остановить merge, запустить протокол ревью | `docs/PROTOCOLS/DEV_SESSION.md` |
| TR-002 | Провал безопасности (bandit/safety/detect-secrets) | Создать инцидент, уведомить безопасность | `docs/SECURITY.md`, `docs/PROTOCOLS/RELEASE_PIPELINE.md` |
| TR-003 | Несоответствие метрик порогам (`M-DOC-COVERAGE`, `M-ROADMAP-HEALTH`) | Обновить Roadmap, инициировать ретроспективу | `docs/METRICS/STATE_DEFINITIONS.md` |
| TR-004 | Плагин не проходит `/health` или heartbeat > 2 мин | Перевести плагин в `disabled`, выполнить `PLUGIN_LIFECYCLE` | `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md` |
| TR-005 | Доступность LLM < 97% (`M-LLM-AVAILABILITY`) | Переключиться на резервного провайдера, уведомить архитекторов | `docs/CONTRACTS/LLM_CLIENT.md` |
| TR-006 | Ошибка релизного smoke-теста | Выполнить откат, зарегистрировать инцидент | `docs/PROTOCOLS/RELEASE_PIPELINE.md` |
| TR-007 | Пользователь запросил новую функцию (intent неизвестен) | Активировать плагин генерации, обновить Roadmap | `docs/CONTRACTS/plugins/PLUGIN_GENERATOR.md` |
| TR-008 | Получено событие `plugin_failed` severity `critical` | Заблокировать плагин, уведомить владельца, создать инцидент | `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md` |
| TR-009 | Redis недоступен > 30 секунд или задержка Streams > 5 секунд | Перевести ядро в режим `degraded`, включить прямую запись в PostgreSQL, уведомить DevOps | `docs/CONTRACTS/CORE.md`, `docs/SECURITY.md` |
| TR-010 | Количество сообщений в `plugin:invocations` > 1000 | Масштабировать воркеры, проверить плагин, обновить метрики | `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md` |
<HARMONY:END name="PROJECT:TGBOT:DOCS:TRIGGERS:TABLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:TRIGGERS:NEXT">
## Следующие шаги
- Добавить автоматическое уведомление в Telegram-канал при срабатывании `TR-004`, `TR-008` и `TR-009`.
- Связать триггеры с GitHub Actions (оповещение о провале CI и деградации Redis).
- Определить триггеры SLA Telegram API и включить их в следующий релиз контракта бота.
<HARMONY:END name="PROJECT:TGBOT:DOCS:TRIGGERS:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCS:TRIGGERS">
