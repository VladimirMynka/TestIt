KEYWORDS: roadmap, template, change-file, задачи, агрегатор
[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE">
# Шаблон change-файла Roadmap

> Change-файл хранит предложения по обновлению Roadmap. Агрегатор переносит подтверждённые пункты в индекс `docs/ROADMAP.md`.

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:HEADER">
## Метаданные
- Сессия: `SXXX`
- Автор: `<агент>`
- Роль автора: `LLM-исполнитель`
- Дата: `<YYYY-MM-DD>`
- Связанные Issues: `<ISSUE-*>`
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:UPDATES">
## Предлагаемые изменения
| Элемент | Текущее состояние | Предлагаемое состояние | Обоснование |
|---------|-------------------|------------------------|-------------|
| `<Roadmap ID>` | `<status>` | `<status>` | `<link>` |
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:UPDATES">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:CHECKS">
## Проверки
- [ ] Контракты/Issues обновлены.
- [ ] Метрики актуализированы (`M-ROADMAP-HEALTH`).
- [ ] Связанные change-файлы (Summary/Issues) созданы.
- [ ] Подтвердил, что агрегатор (LLM) перенесёт изменения в индекс; прямых правок `docs/ROADMAP.md` не вносилось.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:NOTES">
## Примечания
- Добавьте ссылки на PR/коммиты и протоколы.
- Укажите, если требуется решение агрегатора или архитектурного совета.
- Напомните, что человек-менеджер читает только агрегированную версию и ставит задачи через агентов.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE:NOTES">

<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:TEMPLATE:CHANGE">
