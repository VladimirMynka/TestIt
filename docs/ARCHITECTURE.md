KEYWORDS: архитектура, telegram-bot, плагины, fastapi, redis
[ANCHOR:PROJECT:TGBOT:DOCS:ARCHITECTURE]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE">
# Архитектура системы

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:OVERVIEW">
## Обзор
Платформа состоит из ядра FastAPI, Redis-кеша, набора автономных плагинов, библиотеки LLM-клиента и адаптеров клиентских ботов. Все взаимодействия фиксируются в PostgreSQL и дублируются в Redis Streams для оперативной обработки. Источник истины по требованиям — контракты в `docs/CONTRACTS/`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:OVERVIEW">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:COMPONENTS">
## Карта компонентов
| Подсистема | Технологии | Ответственность | Контракты |
|------------|------------|-----------------|-----------|
| Ядро (`core/`) | FastAPI, SQLAlchemy, Alembic, Redis | Управление диалогами, маршрутизация интентов, API для ботов и плагинов, очереди событий | `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/DATABASE.md`, `docs/CONTRACTS/core/SCHEMAS.md` |
| LLM-клиент (`libs/llm_client/`) | httpx, Pydantic | Абстракция над OpenAI и локальным mock, политика токенов, генерация кода | `docs/CONTRACTS/LLM_CLIENT.md` |
| Плагины (`plugins/`) | FastAPI (Python) + REST | Реализация интентов, manifest, heartbeat, события | `docs/CONTRACTS/plugins/MANIFEST.md`, `docs/CONTRACTS/plugins/*.md` |
| Telegram-бот (`bots/telegram/`) | aiogram 3.x, Redis | Long polling адаптер, нормализация сообщений, команда «обновить диалог» | `docs/CONTRACTS/bots/TELEGRAM.md` |
| Инфраструктура | Docker, docker-compose, GitHub Actions | Оркестрация сервисов, CI/CD, безопасность | `docs/PROTOCOLS/RELEASE_PIPELINE.md`, `docs/SECURITY.md` |
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:COMPONENTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:DATA-FLOW">
## Поток данных пользовательского запроса
1. Пользователь → Telegram API → бот (`bots/telegram/`) на `aiogram` (long polling, решение S004).
2. Бот формирует `DialogMessageCreateV1`, добавляет `trace_id`, кеширует контекст в Redis и вызывает `POST /api/v1/dialogs/{dialog_id}/messages` ядра.
3. Ядро записывает сообщение в таблицы `dialogs`/`messages`, обновляет Redis (`dialog:state`) и вызывает LLM-классификатор (`libs/llm_client`, провайдер OpenAI по умолчанию).
4. Классификатор возвращает интент и вероятность. Менеджер плагинов выбирает manifest с наивысшим приоритетом и публикует событие `plugin_invocation_started` (Redis Stream + `plugin_calls`).
5. Ядро вызывает `POST /invoke` выбранного плагина, передавая идентификатор диалога, историю и контекст. Ответ валидируется по `PluginManifestV1`.
6. Плагин возвращает структурированный ответ. Ядро логирует событие `plugin_invocation_completed`/`plugin_failed`, обновляет метрики, Redis и отправляет ответ пользователю.
7. Все шаги фиксируются в `audit_logs` и `plugin_events`; критические события инициируют триггеры (`docs/TRIGGERS.md`).
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:DATA-FLOW">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:PLUGIN-LIFECYCLE">
## Жизненный цикл плагина
1. **Регистрация** — плагин публикует manifest и вызывает `/core/api/v1/plugins/register`, получает токен и heartbeat-интервал.
2. **Активация** — менеджер плагинов периодически опрашивает `/manifest`, обновляет `manifest_hash` и Redis-каталог.
3. **Маршрутизация** — при поступлении сообщения менеджер учитывает приоритеты, условия активации и состояние плагина (`active`, `degraded`, `disabled`).
4. **Вызов** — ядро делает HTTP-запрос `POST /invoke`; статусы фиксируются в `plugin_calls` и Redis Stream `plugin:invocations`.
5. **Мониторинг** — плагин шлёт heartbeat и события; при `plugin_failed` severity `critical` триггер `TR-008` отключает плагин.
6. **Депрекация** — при нарушении контракта плагин переводится в `disabled`, инициируется протокол `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md` и обновляется Roadmap.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:PLUGIN-LIFECYCLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:DATABASE">
## Модель данных PostgreSQL
| Таблица | Назначение | Основные поля |
|---------|------------|---------------|
| `users` | Пользователи Telegram и администраторы | `id`, `telegram_id`, `role`, `locale`, `created_at`, `updated_at` |
| `dialogs` | Диалоги пользователей | `id`, `user_id`, `status`, `reset_version`, `last_message_at` |
| `messages` | Сообщения диалога | `id`, `dialog_id`, `sender_type`, `payload`, `llm_usage`, `trace_id`, `created_at` |
| `plugins` | Зарегистрированные плагины | `id`, `name`, `version`, `status`, `manifest_hash`, `heartbeat_interval_sec`, `supported_schema_versions` |
| `plugin_calls` | История вызовов плагинов | `id`, `plugin_id`, `dialog_id`, `invocation_id`, `status`, `latency_ms`, `error_code`, `started_at`, `finished_at` |
| `plugin_events` | События плагинов | `id`, `plugin_id`, `event_type`, `severity`, `payload`, `occurred_at` |
| `audit_logs` | Аудит событий | `id`, `source`, `action`, `severity`, `trace_id`, `details`, `created_at` |
| `migrations_info` | Служебная таблица Alembic | `version_num`, `applied_at` |
Полная спецификация — в `docs/CONTRACTS/core/DATABASE.md`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:DATABASE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:SECURITY">
## Безопасность и наблюдаемость
- Все межсервисные вызовы проходят через HTTPS (в dev допускается HTTP с ограниченной сетью docker-compose).
- Аутентификация ботов и плагинов — токены с тегированными scopes; токены выдаёт ядро.
- Redis используется для rate limiting и хранения краткоживущих данных; при деградации включается режим резервного хранения (триггер `TR-009`).
- Метрики публикуются ядром, ботом и плагинами в `/metrics` (Prometheus), включая latency, error rate, usage токенов, размер очередей Redis.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:DEPLOYMENT">
## Развёртывание и окружения
| Окружение | Назначение | Особенности |
|-----------|------------|-------------|
| `dev` | Локальная разработка | docker-compose (ядро, Redis, PostgreSQL, плагины), debug-логи, mock LLM |
| `staging` | Предпродакшн | Подключение к OpenAI, прогон интеграционных тестов, нагрузочные тесты, алерты Redis |
| `prod` | Боевая среда | Автоскейлинг плагинов, централизованный логинг, изолированная сеть, мониторинг heartbeat |
Процесс релиза описан в `docs/PROTOCOLS/RELEASE_PIPELINE.md`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:DEPLOYMENT">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ARCHITECTURE:NEXT">
## Следующие шаги
- Сформировать диаграммы последовательностей для сценариев «создать новый плагин» и «обновить диалог» с учётом Redis Streams.
- Подготовить архитектурные решения по масштабированию менеджера плагинов (очереди, шардирование Redis).
- Зафиксировать требования к наблюдаемости (логирование, трассировка, алерты) в отдельном контракте для мониторинга (`docs/CONTRACTS/core/TELEMETRY.md`, запланировано).
<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCS:ARCHITECTURE">
