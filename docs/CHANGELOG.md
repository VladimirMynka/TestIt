KEYWORDS: changelog, версии, история, документация, change-файлы
[ANCHOR:PROJECT:TGBOT:DOCS:CHANGELOG]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG">
# Журнал изменений

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG:POLICY">
## Политика ведения
Мы следуем стандарту Keep a Changelog. Даты указываются в формате ISO8601. Источник истины — соответствующие контракты и протоколы.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG:POLICY">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG:UNRELEASED">
## [Unreleased]
### Добавлено
- Механизм пакетного дополнения документации: change-файлы `human-friendly/`, `docs/ROADMAP/`, `docs/ISSUES/` и соответствующие шаблоны.
- Протокол агрегации `human-friendly/AGGREGATION_PROTOCOL.md` и метрика `M-DOC-AGGREGATION-LAG` для контроля задержек.
- Сессионные сводки `human-friendly/sessions/S004…S006/summary.md`, восстановленные из истории репозитория.

### Изменено
- `human-friendly/SUMMARY.md` и `docs/ROADMAP.md` превращены в агрегирующие индексы с очередью change-файлов.
- `docs/CONTRIBUTING.md`, `docs/PROTOCOLS/DEV_SESSION.md`, `docs/PROTOCOLS/README.md`, `docs/PROTOCOLS/templates/PROTOCOL_TEMPLATE.md` обновлены под новый процесс агрегации.
- `docs/METRICS/STATE_DEFINITIONS.md` дополнён метрикой задержки агрегации и уточнением расчёта `M-ROADMAP-HEALTH`.

### Исправлено
- Восстановлена история Roadmap (change-файлы S003–S006) для снижения git-конфликтов.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG:UNRELEASED">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CHANGELOG:HISTORY">
## История релизов
*Пока нет опубликованных релизов.*
<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG:HISTORY">

<HARMONY:END name="PROJECT:TGBOT:DOCS:CHANGELOG">
