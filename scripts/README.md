KEYWORDS: scripts, утилиты, миграции, сборка, документация
[ANCHOR:PROJECT:TGBOT:SCRIPTS:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:README">
# Сценарии и утилиты

<HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:README:ROLE">
## Назначение
Директория содержит вспомогательные скрипты для разработчиков и CI: генераторы каркасов, миграции, smoke-тесты. Источник истины — соответствующие протоколы и контракты.
<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:README:PLAN">
## План содержимого
- `bootstrap/` — инициализация окружения.
- `migrations/` — вспомогательные скрипты для alembic.
- `smoke/` — скрипты проверки доступности сервисов.
- `ci/` — служебные скрипты для GitHub Actions.
<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README:PLAN">

<HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:README:NEXT">
## Следующие шаги
- Добавить генератор контрактов для новых плагинов.
- Подготовить запуск локального стенда через `make`.
- Задокументировать требования к окружению.
<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README:NEXT">

<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README">
