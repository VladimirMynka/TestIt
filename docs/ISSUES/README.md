KEYWORDS: issues, каталог, статусы, change-файлы, агрегатор
[ANCHOR:PROJECT:TGBOT:ISSUES:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:README">
# Каталог Issues

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:README:STRUCTURE">
## Структура
- `BACKLOG/` — задачи, ожидающие разблокировки или планирования.
- `IN_PROGRESS/` — активные задачи (меняется только через change-файлы статуса).
- `CLOSED/` — завершённые задачи.
- `REJECTED/` — отклонённые задачи (создать при первом переносе).
- `templates/status-change-template.md` — форма для пакетного обновления статуса.
<HARMONY:END name="PROJECT:TGBOT:ISSUES:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:README:PROCESS">
## Поток обновления статусов
1. Исполнитель создаёт файл `docs/ISSUES/changes/{ISSUE_ID}-changes-SXXX.md` по шаблону.
2. Change-файл фиксируется в сопроводительном PR и остаётся в каталоге `docs/ISSUES/changes/` до обработки агрегатором (индексы не требуют дополнительных записей).
3. Агрегатор переносит Issue в нужную директорию, обновляет связанные документы и проставляет отметку в change-файле.
4. Прямые перемещения файлов без change-файла запрещены (кроме аварийного восстановления по протоколу).
<HARMONY:END name="PROJECT:TGBOT:ISSUES:README:PROCESS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:README:LINKS">
## Связанные документы
- Roadmap: `docs/ROADMAP.md`
- Протокол агрегации: `human-friendly/AGGREGATION_PROTOCOL.md`
- Протокол сессии: `docs/PROTOCOLS/DEV_SESSION.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUES:README:LINKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:README:RESPONSIBILITY">
## Ответственность
- Источник истины по статусу задачи — её расположение в каталоге после агрегации.
- Change-файлы хранятся до подтверждения; после обработки агрегатор обязан указать результат и удалить/архивировать файл.
<HARMONY:END name="PROJECT:TGBOT:ISSUES:README:RESPONSIBILITY">

<HARMONY:END name="PROJECT:TGBOT:ISSUES:README">
