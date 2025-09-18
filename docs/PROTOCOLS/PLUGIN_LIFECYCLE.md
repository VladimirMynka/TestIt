KEYWORDS: протокол, плагин, lifecycle, регистрация, контроль
[ANCHOR:PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE]
<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE">
# Протокол жизненного цикла плагина (P1.0)

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:INPUTS">
## Входные данные
- Manifest плагина (`docs/CONTRACTS/plugins/MANIFEST.md`).
- Контракт конкретного плагина (`docs/CONTRACTS/plugins/*.md`).
- Доступ к API ядра `/api/v1/plugins/register`.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:STEPS">
## Этапы
1. **Подготовка** — проверить соответствие manifest контракту, обновить changelog плагина.
2. **Регистрация** — вызвать `/plugins/register`, получить токен и scopes.
3. **Валидация** — прогнать `pytest`, `bandit`, `safety`, `detect-secrets`, `jsonschema`.
4. **Интеграция** — развернуть плагин в docker-compose, убедиться в успешном `/health` и `/manifest`.
5. **Мониторинг** — настроить алерты на latency, error_rate, heartbeat.
6. **Депрекация** — при нарушении контракта отправить `/events` с состоянием `disabled`, обновить Roadmap, удалить токен.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:OUTPUTS">
## Выходные данные
- Активный плагин с токеном и статусом `active`.
- Обновлённые документы (`README` плагина, контракты, changelog).
- Метрики плагина в `human-friendly/SUMMARY.md` при вводе.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:CHECKPOINTS">
## Контрольные точки
- Manifest и схемы опубликованы и доступны.
- Тесты и линтеры зелёные.
- Плагин появляется в `/api/v1/plugins` и проходит `/health` ≤ 200 мс.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:CHECKPOINTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:ESCALATION">
## Эскалации
- Провал health-check → инициировать `TR-004` (добавим в триггеры).
- Несоответствие схем → обновить контракты и Roadmap до merge.
- Нарушение SLA → эскалировать в безопасность и архитектуру.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:PLUGIN-LIFECYCLE">
