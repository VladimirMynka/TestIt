KEYWORDS: issue, developer, docker, compose, инфраструктура
[ANCHOR:PROJECT:TGBOT:ISSUE:D-008]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008">
# Issue D-008 — Настроить docker-compose для ядра, плагинов и БД

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/plugins/TEXT_REPLY.md`, `docs/CONTRACTS/plugins/PLUGIN_GENERATOR.md`
- Протоколы: `docs/PROTOCOLS/RELEASE_PIPELINE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:GOAL">
## Цель
Подготовить `docker-compose.yml` с сервисами: `core`, `postgres`, `telegram-bot`, `text-reply`, `plugin-generator`, `migrations`. Создать Dockerfile для каждого сервиса, сконфигурировать сети, переменные окружения и volume для БД. Обеспечить скрипт запуска и smoke-тест.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:DELIVERABLES">
## Ожидаемые артефакты
- Файл `docker-compose.yml` и Dockerfile в `docker/`.
- Скрипт `scripts/run/docker_up.sh` для локального запуска.
- Обновлённый `docker/README.md` с инструкцией и требованиями.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-D-001`, `ISSUE-D-002`, `ISSUE-D-003`, `ISSUE-D-005`, `ISSUE-D-006`, `ISSUE-D-007`
- Разблокирует: `ISSUE-T-002`, `ISSUE-T-003`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-008:NOTES">
## Примечания
Сервисы должны использовать единый `.env` файл с параметрами и совместимый healthcheck. Источник истины по портам — контракт ядра и Telegram-бота.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-008">
