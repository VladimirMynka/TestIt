KEYWORDS: контракт, telegram, бот, long-polling, aiogram
[ANCHOR:PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM">
# Контракт Telegram-бота (V1.0)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:CONTEXT">
## Контекст
Адаптер `bots/telegram/` обеспечивает обмен сообщениями между Telegram API и ядром (`core/`). Бот реализуется на `aiogram 3.x`, работает в режиме long polling и использует HTTP API ядра (`v1`). Источник истины по интерфейсам — данный контракт и `docs/CONTRACTS/core/SCHEMAS.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:RESPONSIBILITIES">
## Ответственность подсистемы
- Получать апдейты Telegram (сообщения, команды) и нормализовывать их в `DialogMessageCreateV1`.
- Поддерживать единственную пользовательскую команду `обновить диалог`, транслируемую в `DialogResetRequestV1`.
- Маркировать сообщения `trace_id` и `message_id`, проксируя их в ядро.
- Обрабатывать ответы ядра (`DialogMessageResponseV1`) и пересылать их пользователю.
- Логировать ошибки и телеметрию в соответствии с `docs/CONTRACTS/CORE.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:RESPONSIBILITIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:ARCH">
## Архитектура и режимы работы
1. **Long polling (обязательный)**
   - Используется `aiogram.Dispatcher.start_polling()` с интервалом 1–2 секунды.
   - Для каждого апдейта создаётся задача `handle_update`, выполняющая преобразование и вызов ядра.
2. **Webhook (будущий)**
   - Не активируется в MVP. Заготовка эндпоинта описывается в TODO, но не включается в запуск.
3. **Очередь исходящих сообщений**
   - Ответы ядра возвращаются напрямую через HTTP. При недоступности Telegram сохраняются в Redis (`telegram:outbox:{chat_id}`) для повторной доставки (TTL 15 минут).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:ARCH">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:INTERFACES">
## Интерфейсы и схемы
| Действие | Telegram | Схема ядра | Эндпоинт |
|----------|----------|------------|----------|
| Получение сообщения пользователя | `Message.text` | `DialogMessageCreateV1` | `POST /api/v1/dialogs/{dialog_id}/messages`
| Команда «обновить диалог» | `/reset` или кнопка | `DialogResetRequestV1` | `POST /api/v1/dialogs/{dialog_id}/reset`
| Получение истории | `/history` (админ) | `DialogSnapshotResponseV1` | `GET /api/v1/dialogs/{dialog_id}`
| Обработка ответа ядра | — | `DialogMessageResponseV1` | исходящий ответ (Telegram sendMessage)
| Регистрация пользователя | — | `UserUpsertV1` | `POST /api/v1/users` (при появлении) |

Все схемы определены в `docs/CONTRACTS/core/SCHEMAS.md` (`v1alpha`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:INTERFACES">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:FLOW">
## Поток обработки апдейта
1. `aiogram` получает апдейт `Update` и извлекает `chat_id`, `message_id`, `text`.
2. Генерируется `trace_id` (UUID4) и формируется `DialogMessageCreateV1`.
3. Выполняется `POST` в ядро. При успехе ответ (`DialogMessageResponseV1`) транслируется пользователю.
4. Если ответ содержит `plugin_messages`, бот выводит основной текст и (опционально) сервисные уведомления.
5. При команде `обновить диалог` бот вызывает `POST /reset` и подтверждает пользователю, очищая локальный кеш Redis (`telegram:context:{dialog_id}`).
6. Ошибки ядра (`status >= 500` или `core_error_code`) логируются и отправляются в `/api/v1/plugins/events` через сервис ядра (автоматически).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:FLOW">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:ERRORS">
## Обработка ошибок
- **Недоступность ядра:** повтор через 3, 9, 27 секунд. После 3 попыток сообщение отправляется в Redis для повторной доставки.
- **Недоступность Telegram API:** ошибка фиксируется, ответ ядра остаётся в Redis до восстановления (TTL 15 минут).
- **Неверный формат ответа ядра:** бот регистрирует событие `plugin_failed` через `/api/v1/plugins/events` и отправляет пользователю сообщение по умолчанию.
- **Команда вне контекста:** бот отвечает подсказкой и не вызывает ядро.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:ERRORS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:SECURITY">
## Безопасность
- Токен бота хранится в переменной окружения `TELEGRAM_BOT_TOKEN` и не логируется.
- Все исходящие вызовы к ядру подписываются заголовками `X-Bot-Token` и `X-Trace-Id`.
- Кнопки и команды проходят фильтрацию по списку разрешённых команд.
- Redis подключается по TLS (в продуктиве) и хранит только временные данные без персональных полей.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:OBS">
## Наблюдаемость и метрики
- `telegram_updates_total{status="processed|failed"}`
- `telegram_outbox_queue_size`
- `telegram_core_latency_seconds` (гистограмма)
- Логи формата JSON с полями `trace_id`, `chat_id`, `intent`, `plugin_id`.
Метрики публикуются через встроенный в бота `/metrics` (FastAPI) или проксируются в ядро.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:OBS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:COMPATIBILITY">
## Совместимость и миграции
- Версия API бота: `v1`. Изменения, требующие webhook, увеличивают минорную версию (`v1.1`).
- Совместим с ядром API `v1` и схемами `v1alpha`.
- При переходе на webhook необходимо обновить этот контракт, Roadmap и добавить миграцию инфраструктуры.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:COMPATIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:APPENDIX">
## Приложение A — Настройки
| Параметр | Значение по умолчанию | Описание |
|----------|-----------------------|----------|
| `POLL_INTERVAL_SECONDS` | `1.0` | Интервал между long polling запросами |
| `CORE_TIMEOUT_SECONDS` | `10` | Таймаут HTTP-запроса в ядро |
| `OUTBOX_RETRY_SECONDS` | `30` | Частота повторной доставки сообщений из Redis |
| `RESET_COMMANDS` | `{"/reset", "обновить диалог"}` | Список команд для сброса |
| `REDIS_URI` | `redis://redis:6379/0` | Подключение к кешу |
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM:APPENDIX">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:BOTS:TELEGRAM">
