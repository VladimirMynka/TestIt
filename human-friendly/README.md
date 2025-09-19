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
- `SUMMARY.md` используется как навигационный индекс; задачи на агрегацию определяются по наличию файлов в каталоге `changes/`.
- Протокол агрегации (`AGGREGATION_PROTOCOL.md`) обязателен к исполнению и ссылается на метрики свежести.
- Все действия выполняются LLM-агентами: исполнители подготавливают change-файлы, агрегатор (отдельный LLM) переносит данные, а
  человек-менеджер читает только утверждённые сессионные сводки и формулирует запросы через задачи.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:README:RESPONSIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:README:ROLES">
## Роли и доступ
- **LLM-исполнители** — создают change-файлы в `changes/` и отмечают статус `🟡 pending`.
- **LLM-агрегатор** — следует `AGGREGATION_PROTOCOL.md`, использует `scripts/reporting/change_cards.py` для обзора файлов в каталоге
  `changes/` и обновляет `SUMMARY.md`/`sessions/`.
- **Менеджер проекта (человек)** — не редактирует файлы; просматривает `SUMMARY.md` и сессионные отчёты, передаёт новые запросы
  через постановку задач агентам.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:README:ROLES">

<HARMONY:END name="PROJECT:TGBOT:HUMAN:README">
