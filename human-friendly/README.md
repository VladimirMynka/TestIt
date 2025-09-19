KEYWORDS: human-friendly, summary, агрегатор, сессии, документация
[ANCHOR:PROJECT:TGBOT:HUMAN:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:README">
# Каталог human-friendly

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:README:STRUCTURE">
## Структура
- `SUMMARY.md` — агрегирующий индекс, фиксирующий статус последней агрегации и ссылки на сессионные отчёты.
- `sessions/SXXX/summary.md` — утверждённые отчёты конкретных сессий (источник истины для людей).
- `changes/summary-changes-SXXX.md` — черновые дополнения независимых агентов, ожидающие агрегации.
- `templates/summary-changes-template.md` — обязательная форма для change-файлов.
- `AGGREGATION_PROTOCOL.md` — регламент действий агрегатора, сверяющего change-файлы и обновляющего индекс.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:README:FLOW">
## Поток работы
1. Каждый автор создаёт файл `changes/summary-changes-SXXX.md` с заполненным шаблоном.
2. Агрегатор по расписанию (минимум раз в три сессии) просматривает накопленные change-файлы, консолидацию фиксирует в `sessions/`.
3. После агрегации change-файлы помечаются как обработанные (перемещаются в архив или удаляются с указанием ссылки в протоколе).
4. Любые прямые правки `SUMMARY.md` и файлов в `sessions/` допускаются только агрегатором по протоколу.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:README:FLOW">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:README:RESPONSIBILITY">
## Ответственность
- Источник истины для содержимого — файлы `sessions/SXXX/summary.md`.
- `SUMMARY.md` используется как навигационный индекс и список задач на агрегацию.
- Протокол агрегации (`AGGREGATION_PROTOCOL.md`) обязателен к исполнению и ссылается на метрики свежести.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:README:RESPONSIBILITY">

<HARMONY:END name="PROJECT:TGBOT:HUMAN:README">
