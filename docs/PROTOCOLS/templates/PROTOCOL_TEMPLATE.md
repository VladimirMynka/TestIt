KEYWORDS: protocol-template, процедуры, change-файлы, шаги, контроль
[ANCHOR:PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC">
# Шаблон протокола

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:HEADER">
## Шапка
- Название: `<процесс>`
- Версия: `P1.0`
- Роль исполнителя: `<роль>`
- Связанные контракты: `<ссылки>`
- Связанные change-файлы: `<ARTIFACT-changes-SXXX>`
- Метрики контроля: `<идентификаторы>`
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:INPUTS">
## Входные данные
Перечислите необходимые артефакты, конфигурации, change-файлы и окружения.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:STEPS">
## Шаги выполнения
1. `<шаг>`
2. `<шаг>`
После каждого шага фиксируйте ожидаемый результат, ссылку на change-файл и метрику.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:OUTPUTS">
## Результат
Опишите критерии завершения, состояние change-файлов (✅/⚠️/🚫) и контрольные точки для аудита.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:ESCALATION">
## Эскалация
Приведите правила реакции на отклонения, каналы коммуникации и шаги при зависших change-файлах.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:ESCALATION">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:LOGGING">
## Логирование
Укажите форму протокола (markdown/jira) и обязательные поля журнала, включая ссылки на change-файлы и коммиты.
<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC:LOGGING">

<HARMONY:END name="PROJECT:TGBOT:DOCS:PROTOCOLS:TEMPLATE:GENERIC">
