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
- `bootstrap/` — инициализация окружения (`setup_env.sh` создаёт `.venv` и `.env.example`).
- `metrics/` — автоматизация объективных метрик (`metrics/snapshot.py`).
- `navigation/` — инструменты обзора документации (`navigation/context_radar.py`).
- `reporting/` — сборщики обзорных карточек (`reporting/change_cards.py`).
- `migrations/` — вспомогательные скрипты для alembic.
- `smoke/` — скрипты проверки доступности сервисов.
- `ci/` — служебные скрипты для GitHub Actions.
<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README:PLAN">

<HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:README:TOOLS">
## Новые инструменты автоматизации
- `python scripts/metrics/snapshot.py --session-id SXXX` — формирует JSON-шаблон записи метрик, заполняя объективные поля и
  добавляя подсказки для субъективных метрик когнитивной нагрузки.
- `python scripts/navigation/context_radar.py --format markdown` — строит обзор актуальности ключевых каталогов и подсвечивает
  потенциально устаревшие файлы (порог изменяется флагом `--stale-days`).
- `python scripts/reporting/change_cards.py --format json` — создаёт карточки по change-файлам в каталогах, ожидающих агрегации,
  с пометкой, что авторы — LLM-исполнители.
<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README:TOOLS">

<HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:README:NEXT">
## Следующие шаги
- Добавить генератор контрактов для новых плагинов.
- Подготовить запуск локального стенда через `make`.
- Задокументировать требования к окружению.
- Включить проверки запуска новых скриптов в CI (smoke-проверка метрик и карточек).
<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README:NEXT">

<HARMONY:END name="PROJECT:TGBOT:SCRIPTS:README">
