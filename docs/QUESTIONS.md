KEYWORDS: questions, вопросы, уточнения, архитектура, roadmap
[ANCHOR:PROJECT:TGBOT:DOCS:QUESTIONS]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:QUESTIONS">
# Журнал вопросов

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:QUESTIONS:GUIDE">
## Правило фиксации
Все вопросы, требующие решения на уровне продукта или стейкхолдеров, фиксируются здесь и дублируются в человеко-ориентированной сводке (`human-friendly/SUMMARY.md`). Источник истины — данный журнал.
<HARMONY:END name="PROJECT:TGBOT:DOCS:QUESTIONS:GUIDE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:QUESTIONS:STATUS">
## Текущий статус
| ID | Вопрос | Ответственный | Срок | Статус |
|----|--------|----------------|------|--------|
| — | — | — | — | Все вопросы текущей сессии закрыты |
<HARMONY:END name="PROJECT:TGBOT:DOCS:QUESTIONS:STATUS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:QUESTIONS:RESOLVED">
## Закрытые вопросы
| ID | Вопрос | Ответ | Сессия |
|----|--------|--------|--------|
| Q002 | Требуется ли поддержка как webhook, так и polling для Telegram на первом этапе? | Используем только long polling (webhook в бэклоге). | S004 |
| Q003 | Какой провайдер LLM использовать по умолчанию (OpenAI, локальный)? | Основной провайдер — OpenAI, локальный mock остаётся резервом. | S004 |
| Q004 | Нужен ли Redis для кеширования диалогов в MVP или достаточно PostgreSQL? | Redis обязателен для кеша и очередей (`config V1`). | S004 |
<HARMONY:END name="PROJECT:TGBOT:DOCS:QUESTIONS:RESOLVED">

<HARMONY:END name="PROJECT:TGBOT:DOCS:QUESTIONS">
