KEYWORDS: template, summary, change-file, агрегатор, human-friendly
[ANCHOR:PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES]
<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES">
# Шаблон change-файла сводки

> Источник истины после агрегации — `sessions/SXXX/summary.md`. Этот файл служит для независимых дополнений и удаляется (или архивируется) агрегатором после обработки.

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:HEADER">
## Метаданные
- Сессия: `SXXX`
- Автор: `<ФИО или агент>`
- Роль автора: `LLM-исполнитель (создатель change-файла)`
- Дата: `<YYYY-MM-DD>`
- Связанные change-файлы: `<ссылки, если есть>`
<HARMONY:END name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:CONTENT">
## Предлагаемые дополнения
### Ключевые результаты
- `<пункт>`

### Что дальше
- `<пункт>`

### Вопросы
- `<вопрос или "нет">`

### Метрики (если обновляются)
- `<код метрики>: <значение> (обоснование>`
<HARMONY:END name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:CONTENT">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:CHECKS">
## Проверки автора
- [ ] Согласовал изменения с соответствующими контрактами/протоколами.
- [ ] Добавил метрики в `docs/METRICS/logs/` (если требуется).
- [ ] Обновил Roadmap change-файл при необходимости.
- [ ] Подтвердил, что агрегатор (LLM) обработает файл отдельно; прямые правки `SUMMARY.md` не выполнялись.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:NOTES">
## Примечания
- Добавьте ссылку на PR или коммит.
- Укажите, какие разделы требуют решения агрегатора.
- Помните, что человек-менеджер читает только агрегированные отчёты; все правки проходят через LLM-агентов.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES:NOTES">

<HARMONY:END name="PROJECT:TGBOT:HUMAN:TEMPLATE:SUMMARY-CHANGES">
