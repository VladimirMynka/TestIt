KEYWORDS: телеграм, бот, адаптер, webhook, документация
[ANCHOR:PROJECT:TGBOT:BOTS:TELEGRAM:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:BOTS:TELEGRAM:README">
# Telegram-бот

<HARMONY:BEGIN name="PROJECT:TGBOT:BOTS:TELEGRAM:README:ROLE">
## Назначение
Telegram-подсистема обеспечивает связь пользователя с ядром через webhook или long polling. Источник истины — предстоящий контракт бота (будет добавлен после спецификации API ядра).
<HARMONY:END name="PROJECT:TGBOT:BOTS:TELEGRAM:README:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:BOTS:TELEGRAM:README:FEATURES">
## Основные функции
- Авторизация и хранение токена бота.
- Проброс сообщений в ядро и получение ответов.
- Реализация команды «/reset» для обнуления контекста.
- Обработка ошибок и уведомления администратору.
<HARMONY:END name="PROJECT:TGBOT:BOTS:TELEGRAM:README:FEATURES">

<HARMONY:BEGIN name="PROJECT:TGBOT:BOTS:TELEGRAM:README:STRUCTURE">
## Структура (план)
- `app/main.py` — точка входа.
- `app/handlers/` — обработчики апдейтов.
- `app/services/` — интеграция с ядром.
- `tests/` — контрактные тесты API бота.
<HARMONY:END name="PROJECT:TGBOT:BOTS:TELEGRAM:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:BOTS:TELEGRAM:README:NEXT">
## Следующие шаги
- Зафиксировать контракт ядро ↔ бот.
- Определить требования к развертыванию (docker-compose).
- Подготовить протокол инцидентов на стороне бота.
<HARMONY:END name="PROJECT:TGBOT:BOTS:TELEGRAM:README:NEXT">

<HARMONY:END name="PROJECT:TGBOT:BOTS:TELEGRAM:README">
