KEYWORDS: протоколы, процессы, документация, агрегация, контроль
[ANCHOR:PROJECT:TGBOT:DOCS:PROTOCOLS:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:README">
# Каталог протоколов

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:PURPOSE">
## Назначение
Протоколы описывают пошаговые процедуры разработки, релизов и эксплуатации. Источник истины — соответствующий протокол.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:PURPOSE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:STRUCTURE">
## Структура каталога
- `DEV_SESSION.md` — проведение сессии разработчика (включает работу с change-файлами).
- `RELEASE_PIPELINE.md` — CI/CD релизы.
- `PLUGIN_LIFECYCLE.md` — подключение и сопровождение плагинов.
- `human-friendly/AGGREGATION_PROTOCOL.md` — агрегирование Summary и связанных change-файлов.
- `runtime/` — шаблоны инцидентов и оперативных процедур (запланировано).
- `templates/` — общие шаблоны протоколов.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:PROCESS">
## Правила обновления
1. Любое изменение процесса фиксируется в протоколе и `docs/CHANGELOG.md` с пометкой `[PROTOCOL]`.
2. Протоколы нумеруются `PMAJOR.MINOR` и синхронизируются с Roadmap и change-файлами.
3. Несоответствия между протоколами и контрактами устраняются в пользу контрактов.
4. Все ссылки на агрегирующие документы должны вести на соответствующие change-файлы или индексы.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:PROCESS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:LINKS">
## Связанные документы
- Контракты: `docs/CONTRACTS/`
- Триггеры: `docs/TRIGGERS.md`
- Метрики: `docs/METRICS/STATE_DEFINITIONS.md`
- Индексы change-файлов: `human-friendly/SUMMARY.md`, `docs/ROADMAP.md`
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:README:LINKS">

<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:README">
