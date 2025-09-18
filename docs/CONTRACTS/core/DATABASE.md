KEYWORDS: контракт, база-данных, postgres, schema, redis
[ANCHOR:PROJECT:TGBOT:CONTRACT:CORE:DATABASE]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE">
# Контракт базы данных ядра (V1.1)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:CONTEXT">
## Контекст
Документ описывает обязательные таблицы PostgreSQL, ограничения и процессы миграций для подсистемы `core/`. Он дополняет контракты ядра (`CORE.md`), схем (`core/SCHEMAS.md`) и интеграцию с Redis (краткоживущие данные и очереди).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:TABLES">
## Таблицы и схемы
### `users`
- Поля: `id (UUID, PK)`, `telegram_id (BIGINT, unique)`, `role (ENUM[user,admin,service])`, `locale (TEXT)`, `created_at (TIMESTAMP, default now())`, `updated_at (TIMESTAMP)`.
- Ограничения: уникальность `telegram_id`, индекс по `role`.

### `dialogs`
- Поля: `id (UUID, PK)`, `user_id (UUID, FK users.id)`, `status (ENUM[active, archived])`, `reset_version (INT, default 0)`, `created_at`, `updated_at`, `last_message_at (TIMESTAMP)`.
- Ограничения: индекс `(user_id, status)`, `last_message_at` обновляется триггером при новых сообщениях.

### `messages`
- Поля: `id (UUID, PK)`, `dialog_id (UUID, FK dialogs.id)`, `sender_type (ENUM[user,core,plugin])`, `payload (JSONB)`, `llm_usage (JSONB)`, `message_id (TEXT, nullable)`, `trace_id (UUID)`, `created_at`.
- Ограничения: уникальность `(dialog_id, message_id)` при `message_id IS NOT NULL`.

### `plugins`
- Поля: `id (UUID, PK)`, `name (TEXT)`, `version (TEXT)`, `intents (JSONB)`, `status (ENUM[active,disabled,degraded,registering])`, `base_url (TEXT)`, `manifest_hash (TEXT)`, `last_heartbeat (TIMESTAMP)`, `heartbeat_interval_sec (INT)`, `supported_schema_versions (TEXT[])`, `scopes (TEXT[])`, `metadata (JSONB)`.
- Ограничения: уникальность `(name, version)`, индекс по `status`, CHECK `heartbeat_interval_sec > 0`.

### `plugin_calls`
- Поля: `id (UUID, PK)`, `plugin_id (UUID, FK plugins.id)`, `dialog_id (UUID, FK dialogs.id)`, `invocation_id (UUID)`, `request_payload (JSONB)`, `response_payload (JSONB)`, `latency_ms (INT)`, `status (ENUM[queued,in_progress,succeeded,failed,timeout,rejected])`, `error_code (TEXT)`, `trace_id (UUID)`, `started_at (TIMESTAMP)`, `finished_at (TIMESTAMP, nullable)`.
- Ограничения: уникальность `(plugin_id, invocation_id)`, индексы `(dialog_id, created_at)` и `(status, started_at)`.

### `plugin_events`
- Поля: `id (UUID, PK)`, `plugin_id (UUID, FK plugins.id)`, `event_type (TEXT)`, `severity (ENUM[info,warning,critical])`, `payload (JSONB)`, `dialog_id (UUID, FK dialogs.id, nullable)`, `occurred_at (TIMESTAMP)`, `created_at (TIMESTAMP)`.
- Ограничения: индекс `(plugin_id, occurred_at)`, CHECK `event_type` соответствует whitelisted перечню (см. `core/SCHEMAS.md`).

### `audit_logs`
- Поля: `id (UUID, PK)`, `source (ENUM[user,core,plugin,system])`, `action (TEXT)`, `details (JSONB)`, `trace_id (UUID)`, `severity (ENUM[info,warning,critical])`, `created_at`.
- Ограничения: индекс по `trace_id`, `created_at`.

### `migrations_info`
- Управляется Alembic, хранит `version_num (TEXT, PK)`, `applied_at (TIMESTAMP)`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:TABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:RELATIONS">
## Связи с Redis
- Redis `dialog:state:{dialog_id}` дублирует поля `last_message_at`, `last_plugin_id`, `pending_invocation_id`; при сбросе диалога данные очищаются.
- Redis Streams `plugin:events` и `plugin:invocations:{plugin_id}` синхронизируются с таблицами `plugin_events` и `plugin_calls`; воркер обязан подтверждать доставку в БД.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:RELATIONS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:MIGRATIONS">
## Процесс миграций
1. Каждая миграция описывается в Alembic и сопровождается SQL-дампом отката (`down_revision`).
2. Перед merge запускается `alembic upgrade head` и `alembic downgrade -1` в CI.
3. Версия миграции фиксируется в `docs/CHANGELOG.md` с пометкой `[DB]`.
4. Скрипты миграций должны быть идемпотентными и не нарушать работу активных плагинов; изменения, влияющие на manifest, согласуются с командами плагинов.
5. Добавление новых ENUM значений должно сопровождаться обновлением `core/app/schemas/v1alpha/enums.py`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:MIGRATIONS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:SECURITY">
## Безопасность данных
- Используем отдельные роли PostgreSQL: `app_readonly`, `app_writer`, `migration` (минимальные привилегии).
- Доступ к таблицам плагинов предоставляется только через API ядра; прямой доступ из плагинов запрещён.
- Все JSONB поля проверяются на размер (лимит 64 КБ) и типизированы через Pydantic (`core/SCHEMAS.md`).
- Логи аудита хранятся минимум 180 дней и защищены от удаления без административного доступа.
- При удалении плагина записи `plugin_calls`/`plugin_events` остаются для аудита (soft delete через поле `status`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:TESTING">
## Тестирование
- Юнит-тесты моделей: `pytest -q core/tests/db`.
- Проверка миграций: `alembic upgrade head && alembic downgrade base` в pipeline.
- Согласованность с Redis: `scripts/check_stream_replication.py` (запланировано) сверяет записи Streams и таблиц.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:TESTING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:CHANGE-MANAGEMENT">
## Управление изменениями
- Ответственный: Владельцы БД и архитекторы.
- Нарушения совместимости фиксируются в `docs/COMPATIBILITY.md` (матрица версий) и `docs/CHANGELOG.md` (`[DB]`).
- Любая новая таблица требует согласования с безопасностью и обновления `docs/TRIGGERS.md`, если появляются новые события.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE:CHANGE-MANAGEMENT">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:DATABASE">
