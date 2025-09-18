KEYWORDS: контракт, схемы, api, ядро, pydantic
[ANCHOR:PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS">
# Контракт схем API ядра (v1alpha)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:CONTEXT">
## Контекст
Документ описывает версии DTO и событий, используемых ядром (`core/`) для общения с ботами, плагинами и внутренними сервисами. Схемы реализуются в пакете `core/app/schemas/v1alpha` (Pydantic). Источник истины — этот контракт и `docs/CONTRACTS/CORE.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:VERSIONING">
## Версионирование
- Путь импорта: `from core.app.schemas.v1alpha import ...`.
- Для несовместимых изменений создаётся папка `v1beta`, `v2alpha` и обновляется Roadmap.
- Заголовок `X-Schema-Version` (значение `v1alpha`) обязателен в API для валидации клиентов.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:VERSIONING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:DIALOGS">
## Схемы диалогов
### `DialogMessageCreateV1`
| Поле | Тип | Описание |
|------|-----|----------|
| `dialog_id` | UUID | Идентификатор диалога (создаётся ботом или ядром) |
| `user_id` | UUID | Ссылка на пользователя из БД |
| `message_id` | str \| None | Идемпотентный идентификатор сообщения клиента |
| `trace_id` | UUID | Корреляция логов |
| `payload` | `MessagePayloadV1` | Тело сообщения (см. ниже) |
| `metadata` | dict | Временная зона, язык, источник |

`MessagePayloadV1`:
- `type`: enum [`text`, `voice`, `image`, `command`]
- `text`: str (для `type=text|command`)
- `attachments`: список объектов `{id: UUID, type: str, url: str}`

### `DialogMessageResponseV1`
| Поле | Тип | Описание |
|------|-----|----------|
| `dialog_id` | UUID | Целевой диалог |
| `trace_id` | UUID | Наследуется от запроса |
| `plugin_responses` | список `PluginMessageV1` | Ответы плагинов |
| `usage` | `LLMUsageV1` \| None | Информация о токенах |
| `status` | enum [`accepted`, `queued`, `failed`] | Статус обработки |

`PluginMessageV1` включает поля `plugin_id`, `content`, `content_type`, `suggested_actions`.

### `DialogResetRequestV1`
- `dialog_id`: UUID
- `user_id`: UUID
- `reason`: str (например, `user_requested`)

### `DialogSnapshotResponseV1`
- `dialog`: объект `DialogSummaryV1` (`id`, `user_id`, `status`, `reset_version`, `created_at`)
- `messages`: список `HistoricalMessageV1` (содержит `sender_type`, `payload`, `created_at`)

### `UserUpsertV1`
- `telegram_id`: int
- `display_name`: str
- `locale`: str (`ru`, `en`, ...)
- `metadata`: dict (источник, версия клиента)
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:DIALOGS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:PLUGINS">
## Схемы плагинов
### `PluginRegistrationRequestV1`
| Поле | Тип | Описание |
|------|-----|----------|
| `name` | str | Имя плагина |
| `version` | str | Семантическая версия |
| `base_url` | AnyHttpUrl | Точка доступа |
| `manifest` | `PluginManifestV1` | Полный manifest |
| `scopes` | список str | Запрашиваемые scopes |
| `capabilities` | dict | Доп. опции (streaming, throttling) |

### `PluginRegistrationResponseV1`
- `plugin_id`: UUID
- `token`: str (Bearer)
- `issued_at`: datetime
- `expires_at`: datetime

### `PluginHeartbeatRequestV1`
- `plugin_id`: UUID
- `status`: enum [`active`, `degraded`, `disabled`]
- `latency_ms`: int
- `queue_depth`: int
- `metrics`: dict (например, `{ "requests_total": 120 }`)

### `PluginEventV1`
| Поле | Тип | Описание |
|------|-----|----------|
| `event_id` | UUID |
| `plugin_id` | UUID |
| `dialog_id` | UUID \| None |
| `event_type` | enum [`plugin_registered`, `plugin_heartbeat`, `plugin_invocation_started`, `plugin_invocation_completed`, `plugin_failed`, `plugin_timeout`, `plugin_heartbeat_missed`]
| `severity` | enum [`info`, `warning`, `critical`]
| `payload` | dict |
| `occurred_at` | datetime |

### `PluginInvocationLogV1`
- `plugin_id`: UUID
- `invocation_id`: UUID
- `dialog_id`: UUID
- `request_payload`: dict
- `response_payload`: dict \| None
- `status`: enum [`queued`, `in_progress`, `succeeded`, `failed`, `timeout`, `rejected`]
- `error_code`: str \| None
- `started_at`: datetime
- `finished_at`: datetime \| None
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:PLUGINS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:MAPPINGS">
## Соответствие эндпоинтов и схем
| Эндпоинт | Запрос | Ответ | События |
|----------|--------|-------|---------|
| `POST /api/v1/dialogs/{dialog_id}/messages` | `DialogMessageCreateV1` | `DialogMessageResponseV1` | `plugin_invocation_started`, `plugin_invocation_completed`, `plugin_failed`, `plugin_timeout` |
| `POST /api/v1/dialogs/{dialog_id}/reset` | `DialogResetRequestV1` | `DialogMessageResponseV1` | `dialog_reset` |
| `GET /api/v1/dialogs/{dialog_id}` | — | `DialogSnapshotResponseV1` | — |
| `POST /api/v1/users` | `UserUpsertV1` | `UserUpsertResponseV1` (`status`, `user_id`) | `user_created` |
| `POST /api/v1/plugins/register` | `PluginRegistrationRequestV1` | `PluginRegistrationResponseV1` | `plugin_registered` |
| `POST /api/v1/plugins/{plugin_id}/heartbeat` | `PluginHeartbeatRequestV1` | `HeartbeatAckV1` (`status`) | `plugin_heartbeat` |
| `POST /api/v1/plugins/{plugin_id}/events` | `PluginEventV1` | `EventAckV1` | (как в поле `event_type`) |
| `GET /api/v1/plugins` | — | `PluginCatalogResponseV1` (список manifest) | — |

`PluginCatalogResponseV1` содержит `items: list[PluginManifestSummaryV1]` с полями `plugin_id`, `name`, `version`, `intents`, `status`, `last_heartbeat`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:MAPPINGS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:REDIS">
## Redis структуры
- `dialog:state:{dialog_id}` → хранит короткоживущий контекст (TTL 10 минут) с полями `last_plugin_id`, `pending_invocation_id`.
- `plugin:events` (Redis Stream) → события `PluginEventV1` для асинхронной обработки и алертинга.
- `plugin:invocations:{plugin_id}` (Stream) → статусные обновления `PluginInvocationLogV1`.
Эти структуры синхронизируются с таблицами PostgreSQL (`dialogs`, `plugin_calls`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:REDIS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:VALIDATION">
## Валидаторы и соглашения
- Все datetime значения передаются в UTC ISO8601.
- Enum значения регистрируются в общем модуле `core/app/schemas/v1alpha/enums.py`.
- Для обратной совместимости новые поля объявляются с `Field(default=None)` и документируются в `CHANGELOG`.
- Любая схема должна иметь docstring на русском языке с ссылкой на этот контракт.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:VALIDATION">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:TESTING">
## Тестирование
- Генерация JSON Schema: `python -m core.app.schemas.generate --version v1alpha`.
- Контрактные тесты: `pytest -q core/tests/schemas/test_v1alpha.py` (создать).
- Сравнение с БД: `scripts/check_schema_db_alignment.py` сверяет enum и поля с `docs/CONTRACTS/core/DATABASE.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS:TESTING">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:CORE:SCHEMAS">
