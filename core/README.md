KEYWORDS: core, fastapi, менеджер-плагинов, архитектура, redis
[ANCHOR:PROJECT:TGBOT:CORE:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README">
# Ядро системы

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:MISSION">
## Назначение
Ядро объединяет FastAPI-приложение, менеджер плагинов, LLM-классификатор и интеграцию с базами данных/PostgreSQL и Redis. Оно обеспечивает единый интерфейс для ботов, пользователей и подключаемых плагинов. Источник истины — контракты `docs/CONTRACTS/CORE.md` и `docs/CONTRACTS/core/SCHEMAS.md`.
<HARMONY:END name="PROJECT:TGBOT:CORE:README:MISSION">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:STRUCTURE">
## Структура директорий
```
core/
├─ app/
│  ├─ api/
│  │  ├─ dialogs.py            # эндпоинты диалогов (messages/reset/history)
│  │  ├─ plugins.py            # регистрация, heartbeat, каталог
│  │  ├─ users.py              # upsert пользователей
│  │  └─ telemetry.py          # /metrics и health
│  ├─ services/
│  │  ├─ dialog_service.py     # работа с PostgreSQL и Redis
│  │  ├─ plugin_manager.py     # каталог плагинов, маршрутизация, очереди
│  │  ├─ classifier.py         # обёртка над `libs/llm_client`
│  │  └─ llm_router.py         # политика выбора моделей OpenAI/локальных
│  ├─ db/
│  │  ├─ models.py             # SQLAlchemy модели (см. контракт БД)
│  │  ├─ repository.py         # CRUD-операции
│  │  └─ session.py            # фабрика сессий и управление транзакциями
│  ├─ schemas/
│  │  ├─ v1alpha/              # Pydantic-модели (см. `SCHEMAS.md`)
│  │  └─ __init__.py
│  ├─ telemetry/
│  │  ├─ metrics.py            # Prometheus-контроли, экспорт lat/p95
│  │  └─ logging.py            # структурированные JSON-логи
│  ├─ classifiers/
│  │  ├─ prompts/              # текстовые промпты маршрутизации
│  │  └─ router.py             # стратегия распределения intents
│  ├─ queues/
│  │  ├─ redis_events.py       # обработка Redis Streams (plugin events)
│  │  └─ tasks.py              # фоновые задания обработки очередей
│  └─ main.py                  # точка входа FastAPI и инициализация зависимостей
├─ tests/
│  ├─ api/                     # контрактные тесты HTTP-эндпоинтов
│  ├─ services/                # юнит-тесты сервисного слоя
│  └─ schemas/                 # проверки `v1alpha`
└─ README.md                   # текущий файл
```
<HARMONY:END name="PROJECT:TGBOT:CORE:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:SERVICES">
## Основные сервисы
| Сервис | Ответственность | Зависящие контракты |
|--------|-----------------|----------------------|
| `DialogService` | CRUD диалогов, кеш Redis `dialog:state:*`, идемпотентность сообщений | `core/DATABASE.md`, `core/SCHEMAS.md` |
| `PluginManager` | Регистрация, heartbeat, выбор плагинов, публикация событий в Redis | `CORE.md`, `plugins/MANIFEST.md`, `core/SCHEMAS.md` |
| `LLMRouter` | Выбор провайдера (по умолчанию OpenAI) и контроль квот | `LLM_CLIENT.md`, `CORE.md` |
| `TelemetryService` | Экспорт `/metrics`, запись `plugin_calls` | `CORE.md`, `TRIGGERS.md` |
| `RedisQueueConsumer` | Мониторинг `plugin:events` и синхронизация с PostgreSQL | `core/SCHEMAS.md`, `core/DATABASE.md` |
<HARMONY:END name="PROJECT:TGBOT:CORE:README:SERVICES">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:FLOW">
## Поток обработки сообщения
1. API `POST /api/v1/dialogs/{dialog_id}/messages` принимает `DialogMessageCreateV1` и валидирует заголовок `X-Schema-Version`.
2. `DialogService` записывает сообщение в PostgreSQL, кеширует состояние в Redis (`dialog:state:{dialog_id}`) и вызывает `PluginManager`.
3. `PluginManager` использует классификатор (`LLMRouter`) для выбора плагина; публикует событие `plugin_invocation_started` в Redis Stream и таблицу `plugin_calls`.
4. Вызов плагина осуществляется через `httpx.AsyncClient` с таймаутами и ретраями. Ответ валидируется по схемам manifest.
5. По завершении публикуются события `plugin_invocation_completed`/`plugin_failed` и обновляется Redis/БД.
6. Сформированный `DialogMessageResponseV1` возвращается ботам, telemetry обновляет метрики (`core_metrics`).
<HARMONY:END name="PROJECT:TGBOT:CORE:README:FLOW">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:DEPENDENCIES">
## Ключевые зависимости
- `fastapi`, `uvicorn` — HTTP API и сервер.
- `sqlalchemy`, `alembic` — база данных PostgreSQL.
- `redis-py` — кэш состояний и очереди событий.
- `httpx` — асинхронный HTTP-клиент для плагинов и LLM.
- `pydantic` — Pydantic-схемы (`v1alpha`).
<HARMONY:END name="PROJECT:TGBOT:CORE:README:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:LINKS">
## Связанные документы
- Контракт ядра: `docs/CONTRACTS/CORE.md`.
- Контракт схем: `docs/CONTRACTS/core/SCHEMAS.md`.
- Контракт БД: `docs/CONTRACTS/core/DATABASE.md`.
- Архитектура: `docs/ARCHITECTURE.md`.
- Политика безопасности: `docs/SECURITY.md`.
<HARMONY:END name="PROJECT:TGBOT:CORE:README:LINKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:EXTENSIBILITY">
## Точки расширения
- `PluginManager.register_adapter()` — адаптеры для разных версий manifest.
- `DialogService.middleware` — хуки для аудита и rate limiting.
- `LLMRouter.add_provider()` — добавление альтернативных провайдеров (например, локальная модель).
- `queues/tasks.py` — запуск фоновых задач (ретраи вызовов, TTL очистка Redis).
<HARMONY:END name="PROJECT:TGBOT:CORE:README:EXTENSIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CORE:README:SOURCE-OF-TRUTH">
## Источник истины
При несоответствии реализации и документации приоритет имеют контракты в `docs/CONTRACTS/`. Любая новая схема должна добавляться одновременно в `core/app/schemas/v*` и `docs/CONTRACTS/core/SCHEMAS.md`.
<HARMONY:END name="PROJECT:TGBOT:CORE:README:SOURCE-OF-TRUTH">

<HARMONY:END name="PROJECT:TGBOT:CORE:README">
