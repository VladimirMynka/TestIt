KEYWORDS: контракт, плагин, manifest, события, heartbeat
[ANCHOR:PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST">
# Контракт manifest плагина (V1.1)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:CONTEXT">
## Контекст
Все плагины являются REST-сервисами, которые предоставляют manifest через `GET /manifest`, регистрируются в ядре (`/api/v1/plugins/register`) и публикуют события. Контракт описывает обязательные поля, версии и требования к взаимодействию с ядром. Источник истины — данный документ, `docs/CONTRACTS/CORE.md` и `docs/CONTRACTS/core/SCHEMAS.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:FORMAT">
## Формат manifest
```json
{
  "name": "text_reply",
  "version": "1.0.0",
  "description": "Ответ пользователю",
  "intents": [
    {
      "tag": "reply.default",
      "activation_condition": {
        "type": "classifier",
        "value": "reply.default",
        "threshold": 0.35
      },
      "priority": 100
    }
  ],
  "input_schema": "https://repo/schemas/text_reply/input/v1.json",
  "output_schema": "https://repo/schemas/text_reply/output/v1.json",
  "auth": {
    "type": "bearer",
    "scopes": ["dialogs:read", "dialogs:write"]
  },
  "capabilities": {
    "streaming": false,
    "max_tokens": 1024,
    "supports_retry": true
  },
  "llm": {
    "provider": "openai",
    "model": "gpt-4o-mini",
    "temperature": 0.7
  },
  "telemetry": {
    "events_supported": [
      "plugin_invocation_started",
      "plugin_invocation_completed",
      "plugin_failed"
    ],
    "heartbeat_interval_seconds": 60
  },
  "metadata": {
    "changelog_url": "https://repo/CHANGELOG.md",
    "owner": "plugins-team"
  }
}
```
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:FORMAT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:REQUIREMENTS">
## Требования
1. Manifest доступен по `GET /manifest` и кэшируется на стороне ядра 30 секунд; изменение `manifest_hash` требует вызова `/register`.
2. Поле `intents` содержит минимум один тег и описание условия активации (classifier, regex, custom) с `priority` (0–1000).
3. `input_schema` и `output_schema` указывают на версионируемые JSON Schema; несовместимые изменения повышают `MAJOR`.
4. Каждое описание указывает необходимые scopes; ядро выдаёт токен только при совпадении запрошенных scopes с политикой безопасности.
5. Плагин обязан публиковать heartbeat каждые `telemetry.heartbeat_interval_seconds` секунд через `/api/v1/plugins/{id}/heartbeat`.
6. При ошибках/таймаутах плагин отправляет событие `plugin_failed`/`plugin_timeout` с деталями (`PluginEventV1`).
7. Плагин должен поддерживать идемпотентность по `invocation_id`, полученному от ядра.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:REQUIREMENTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:ENDPOINTS">
## Эндпоинты плагина
- `GET /health` → `{ "status": "ok", "version": "1.0.0" }` (должен отражать состояние зависимостей).
- `GET /manifest` → JSON по контракту выше.
- `POST /invoke` → тело запроса и ответа соответствуют указанным схемам; поддерживает заголовки `X-Trace-Id`, `X-Invocation-Id`, `X-Schema-Version`.
- Дополнительно рекомендуется `POST /events` для пользовательских уведомлений (ссылается на `PluginEventV1`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:ENDPOINTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:SECURITY">
## Безопасность
- Все вызовы `/invoke` требуют Bearer-токен с выданными ядром scopes; токен хранится в защищённом хранилище.
- Плагин обязан проверять `trace_id` и возвращать его в ответе.
- Логи исключают персональные данные, токены и промпты; детальная информация передаётся через защищённые каналы (например, `/events`).
- При компрометации токена плагин обязан вызвать `/register` для перевыпуска и уведомить ядро событием `plugin_failed` severity `critical`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:EVENTS">
## События плагина
| Событие | Обязательность | Схема | Описание |
|---------|----------------|-------|----------|
| `plugin_invocation_started` | Обязательное | `PluginEventV1` | Плагин принял задачу к обработке |
| `plugin_invocation_completed` | Обязательное | `PluginEventV1` | Плагин успешно завершил обработку |
| `plugin_failed` | Обязательное | `PluginEventV1` | Ошибка исполнения (с указанием `error_code`) |
| `plugin_timeout` | Условное | `PluginEventV1` | Внутренний таймаут плагина |
| `plugin_custom_*` | Опционально | `PluginEventV1` | Пользовательские события с согласованными типами |

События отправляются на `/api/v1/plugins/{id}/events` не позднее 5 секунд после наступления и дублируются в логах плагина.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:EVENTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:COMPATIBILITY">
## Совместимость
- Плагины поддерживают минимум две версии схем (текущую и предыдущую) и объявляют их в manifest (`supported_schema_versions`).
- Ядро хранит `manifest_hash`; при изменении hash плагин обязан сообщить о несовместимости через `PluginEventV1` (`event_type=plugin_failed`, `severity=warning`).
- Manifest версии `1.x` совместим с ядром API `v1`; при переходе ядра на `v2` предоставляется grace-период и адаптер.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:COMPATIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:TESTING">
## Тестирование
- Контрактные тесты manifest: `pytest -q plugins/<name>/tests/test_manifest.py` (валидатор JSON Schema и полей).
- Интеграционный тест регистрации: `scripts/smoke/verify_plugin_registration.py` — проверяет `/register`, heartbeat и события.
- Линтер схем: `jsonschema --instance sample.json schema.json` и `schemathesis run` для `/invoke`.
- Проверка heartbeat: `scripts/check_plugin_heartbeat.py` — имитирует паузу и ожидает событие `plugin_heartbeat_missed`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:TESTING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:CHANGE-MANAGEMENT">
## Управление изменениями
- Ответственные: владельцы плагинов и менеджер платформы.
- Несовместимые изменения фиксируются в `docs/COMPATIBILITY.md` и `docs/CHANGELOG.md` (секция `[PLUGINS]`).
- Перед публикацией новой версии manifest требуется уведомить владельцев ядра и тестовую команду минимум за 5 рабочих дней.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST:CHANGE-MANAGEMENT">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:MANIFEST">
