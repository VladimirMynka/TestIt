KEYWORDS: контракт, ядро, fastapi, плагины, redis
[ANCHOR:PROJECT:TGBOT:CONTRACT:CORE]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE">
# Контракт ядра FastAPI (V1.1)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:CONTEXT">
## Контекст
Ядро обслуживает HTTP API для Telegram-бота и плагинов, управляет диалогами пользователей и взаимодействует с PostgreSQL и Redis. Контракт распространяется на подсистему `core/` и определяет требования к API, безопасности, данным и наблюдаемости. Источник истины для реализации — этот документ, `docs/CONTRACTS/core/SCHEMAS.md`, `docs/CONTRACTS/core/DATABASE.md` и `docs/CONTRACTS/LLM_CLIENT.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCOPE">
## Область действия
- Публичное REST API для клиентских ботов.
- Служебное REST API для плагинов и событий.
- Менеджер диалогов, LLM-классификатор и очередь вызовов плагинов.
- Интеграция с LLM-клиентом и Redis-кешем.
- Логирование, метрики и управление событиями.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCOPE">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:INTERFACES">
## Интерфейсы API
Все эндпоинты используют схемы `v1alpha` (см. `core/SCHEMAS.md`).

### Публичные эндпоинты (боты)
| Метод | Путь | Описание | Авторизация | Схемы |
|-------|------|----------|-------------|-------|
| `POST` | `/api/v1/dialogs/{dialog_id}/messages` | Добавить сообщение пользователя | Bot Token (`X-Bot-Token`) | `DialogMessageCreateV1` → `DialogMessageResponseV1` |
| `POST` | `/api/v1/dialogs/{dialog_id}/reset` | Обнулить контекст диалога | Bot Token | `DialogResetRequestV1` → `DialogMessageResponseV1` |
| `GET` | `/api/v1/dialogs/{dialog_id}` | Получить статус и историю | Bot Token + Scope `dialogs:read` | `DialogSnapshotResponseV1` |
| `POST` | `/api/v1/users` | Зарегистрировать/обновить пользователя | Bot Token + Scope `users:write` | `UserUpsertV1` → `UserUpsertResponseV1` |

### Служебные эндпоинты (плагины)
| Метод | Путь | Описание | Авторизация | Схемы |
|-------|------|----------|-------------|-------|
| `POST` | `/api/v1/plugins/register` | Регистрация плагина и получение токена | API Key (registry) | `PluginRegistrationRequestV1` → `PluginRegistrationResponseV1` |
| `GET` | `/api/v1/plugins` | Список активных плагинов и их manifest | Plugin Token + Scope `plugins:read` | `PluginCatalogResponseV1` |
| `POST` | `/api/v1/plugins/{plugin_id}/heartbeat` | Обновление статуса плагина | Plugin Token | `PluginHeartbeatRequestV1` → `HeartbeatAckV1` |
| `POST` | `/api/v1/plugins/{plugin_id}/events` | Публикация событий/логов | Plugin Token + Scope `telemetry:write` | `PluginEventV1` → `EventAckV1` |

### Внутренние интерфейсы
- `DialogService` ↔ PostgreSQL (`Session`, модели `dialogs`, `messages`, `plugin_calls`).
- `DialogService` ↔ Redis (`dialog:state:*`, `plugin:events`, `plugin:invocations:*`).
- `PluginManager` ↔ LLM-клиент (`libs/llm_client`) через адаптер `LLMRouter`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:INTERFACES">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:FUNCTIONAL">
## Функциональные требования
1. Ядро маршрутизирует входящие сообщения в плагины согласно классификатору и условиям активации; при отсутствии подходящего плагина вызывается `text_reply`.
2. Для каждого вызова плагина ядро логирует запрос, ответ, статус и время выполнения в `plugin_calls` и Redis Stream `plugin:invocations:*`.
3. Регистрация плагина выдаёт токен доступа, сохраняет manifest-хэш и публикует событие `plugin_registered`.
4. Heartbeat обновляет `last_heartbeat`, статус плагина, публикует `plugin_heartbeat`; при отсутствии heartbeat > 120 секунд создаётся `plugin_heartbeat_missed` и плагин переводится в `degraded`.
5. Команда «обновить диалог» сбрасывает историю сообщений (PostgreSQL) и очищает кеш Redis `dialog:state:{dialog_id}`.
6. Ядро предоставляет endpoint `/metrics` (Prometheus) с показателями latency, error_rate, token_usage, queue_depth.
7. Все события плагинов доступны через `/api/v1/plugins/events` и тиражируются в систему уведомлений (см. `docs/TRIGGERS.md`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:FUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:NONFUNCTIONAL">
## Нефункциональные требования
- **Производительность:** медиана ответа ядра ≤ 500 мс (без времени плагина), p95 ≤ 1 500 мс.
- **Масштабируемость:** поддержка горизонтального масштабирования через stateless-инстансы; состояние хранится в PostgreSQL и Redis.
- **Надёжность:** автоматическое восстановление зависших плагинов через health-check, ретраи вызовов и перевод в режим `degraded`.
- **Наблюдаемость:** корреляционные ID (trace_id) присутствуют во всех логах и заголовках HTTP; события записываются в Redis Streams и БД.
- **Кеширование:** Redis используется для краткоживущих состояний (TTL ≤ 10 минут) и очередей событий; при деградации Redis ядро переходит в режим `degraded` и записывает операции напрямую в PostgreSQL.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:NONFUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SECURITY">
## Требования безопасности
1. Все токены ботов и плагинов выдаются ядром и хранятся в PostgreSQL с хэшированием (`bcrypt`).
2. Доступ к API ограничивается scopes (например, `dialogs:write`, `plugins:manage`); scopes указываются в manifest и токене.
3. Ядро поддерживает rate limiting на уровне пользователя и плагина; параметры лимитов хранятся в Redis (`rate:bot:{id}`).
4. Все секреты загружаются из переменных окружения или секретов CI/CD (см. `docs/SECURITY.md`), логирование секретов запрещено.
5. Все запросы и ответы плагинов проходят валидацию по схемам Pydantic (`v1alpha`) с документированием ошибок через `LLMError`/`PluginError`.
6. События безопасности (`plugin_failed` severity `critical`) инициируют протокол `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md` и триггер `TR-004`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:EVENTS">
## События и очереди
| Событие | Источник | Назначение | Очередь |
|---------|----------|------------|---------|
| `plugin_registered` | `/plugins/register` | Добавить плагин в каталог, уведомить администраторов | Redis Stream `plugin:events` |
| `plugin_heartbeat` | `/plugins/{id}/heartbeat` | Обновить статус, метрики | Redis Stream `plugin:events` |
| `plugin_heartbeat_missed` | Watcher Redis | Триггер деградации плагина, уведомление | Redis Stream `plugin:events` |
| `plugin_invocation_started` | PluginManager | Зафиксировать запуск вызова | Redis Stream `plugin:invocations:{id}` |
| `plugin_invocation_completed` | PluginManager | Зафиксировать успешный ответ | Redis Stream `plugin:invocations:{id}` |
| `plugin_failed` | PluginManager | Зафиксировать ошибку выполнения | Redis Stream `plugin:invocations:{id}` |
| `plugin_timeout` | PluginManager | Отметить таймаут вызова | Redis Stream `plugin:invocations:{id}` |
| `dialog_reset` | DialogService | Логировать сброс диалога | Redis Stream `dialog:events` |

Каждое событие дублируется в таблицу `audit_logs` с `trace_id` и `severity`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:EVENTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:COMPATIBILITY">
## Совместимость и версии
- Версия API: `v1`. Изменения, нарушающие совместимость, требуют выпуска `v2` и периода поддержки ≥ 2 минорных релиза.
- Pydantic-схемы версионируются в `app/schemas/v{n}` и документируются в `core/SCHEMAS.md`.
- Менеджер плагинов поддерживает несколько версий manifest (через адаптеры) и предоставляет backward-совместимость.
- Любая миграция БД сопровождается скриптом отката и записью в `docs/COMPATIBILITY.md`.
- Добавление новых событий требует обновления `docs/TRIGGERS.md` и контракта manifest.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:COMPATIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:TESTING">
## Тестирование
- Контрактные тесты API: `pytest -q core/tests/api` с фикстурами плагинов и Redis-моком.
- Интеграционные тесты docker-compose: `scripts/smoke/core_with_plugins.sh` (в разработке).
- Нагрузочное тестирование: `k6` сценарий 100 RPS (задача в Roadmap).
- Безопасность: `bandit -r core`, `safety check --full-report`, `detect-secrets scan`.
- Мониторинг Redis: `scripts/redis_health_check.py` (создать) — проверка TTL и задержек.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:TESTING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:CHANGE-MANAGEMENT">
## Управление изменениями
- Ответственный: Архитектор проекта.
- Изменения фиксируются в `docs/CHANGELOG.md` с пометкой `[CORE]` и версией (`V1.x`).
- При изменении API требуется обновить соответствующие контракты плагинов, схем и уведомить разработчиков через Roadmap.
- Переход на новую схему сопровождается миграциями Pydantic (создание `v1beta`) и уведомлением тестовой команды.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:CHANGE-MANAGEMENT">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE">
