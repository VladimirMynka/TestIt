KEYWORDS: issue, architect, плагины, события, контракт
[ANCHOR:PROJECT:TGBOT:ISSUE:A-003]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003">
# Issue A-003 — Уточнить контракт регистрации плагинов и событий ядра

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:ROLE">
## Роль
- [x] Architect
- [ ] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/SCHEMAS.md`, `docs/CONTRACTS/plugins/MANIFEST.md`
- Протоколы: `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`
- Очереди событий: Redis Streams для telemetry и heartbeat (заявлено в архитектуре)
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:GOAL">
## Цель
Расширить `docs/CONTRACTS/CORE.md` и `docs/CONTRACTS/plugins/MANIFEST.md` разделами про регистрацию, heartbeat и каталогизацию плагинов, добавить схему событий (`plugin_registered`, `plugin_invocation_started`, `plugin_invocation_completed`, `plugin_failed`, `plugin_heartbeat_missed`). Определить общие структуры очередей и REST-эндпоинтов `/plugins/register`, `/plugins/events`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:DELIVERABLES">
## Ожидаемые артефакты
- Дополнения к контрактам ядра, manifest и БД со схемами событий и статусами вызовов.
- Обновлённый `docs/TRIGGERS.md` с реакциями на нарушения heartbeat и событий плагинов.
- Консолидация статусов вызовов плагинов (`queued`, `in_progress`, `succeeded`, `failed`, `timeout`, `rejected`).
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-002`
- Разблокирует: `ISSUE-D-002`, `ISSUE-D-005`, `ISSUE-D-006`, `ISSUE-T-002`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:CHECKS">
## Проверки
- [x] Контракты обновлены
- [x] Протоколы обновлены
- [x] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:OUTCOME">
## Итог
- Контракты ядра и manifest дополнены процедурами регистрации, heartbeat и описанием событий/очередей Redis.
- `docs/CONTRACTS/core/DATABASE.md` обновлён расширенным списком статусов `plugin_calls` и связью с событиями.
- `docs/TRIGGERS.md` расширен автоматическими реакциями на просроченный heartbeat и неуспешные вызовы плагинов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:OUTCOME">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:A-003:NOTES">
## Примечания
Актуальные события и статусы отражены в `docs/CONTRACTS/core/SCHEMAS.md` и используются всеми компонентами. Любые новые события требуют синхронизации с Redis-очередями и триггерами.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:A-003">
