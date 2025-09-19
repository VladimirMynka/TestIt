KEYWORDS: issues, template, change-file, статусы, агрегатор
[ANCHOR:PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE">
# Шаблон change-файла статуса задачи

> Используйте файл при точечных изменениях статуса Issues, чтобы избежать конфликтов в общих каталогах. После агрегации файл переносится в архив или удаляется.

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:HEADER">
## Метаданные
- Сессия: `SXXX`
- Автор: `<агент>`
- Дата: `<YYYY-MM-DD>`
- Issue: `ISSUE-*-XXX`
<HARMONY:END name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:PROPOSED">
## Предлагаемое изменение
| Атрибут | Значение |
|---------|----------|
| Текущая директория | `<BACKLOG/IN_PROGRESS/CLOSED/REJECTED>` |
| Новая директория | `<BACKLOG/IN_PROGRESS/CLOSED/REJECTED>` |
| Обновлённые поля | `<разделы файла и краткое описание>` |
<HARMONY:END name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:PROPOSED">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:CHECKS">
## Проверки
- [ ] Согласовано с Roadmap change-файлом.
- [ ] Метрики и Summary обновлены.
- [ ] Ссылки в других документах остаются валидными.
<HARMONY:END name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:NOTES">
## Примечания
- Укажите ссылку на PR/коммит.
- Добавьте решение агрегатора (✅/⚠️/🚫) после обработки.
<HARMONY:END name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUES:TEMPLATE:STATUS-CHANGE">
