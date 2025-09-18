KEYWORDS: docker, контейнеры, инфраструктура, compose, документация
[ANCHOR:PROJECT:TGBOT:DOCKER:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCKER:README">
# Контейнеризация

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCKER:README:SCOPE">
## Область ответственности
Директория хранит Dockerfile и связанные конфигурации для ядра, плагинов, бота и вспомогательных сервисов (PostgreSQL, мониторинг). Источник истины — протокол деплоя `docs/PROTOCOLS/RELEASE_PIPELINE.md`.
<HARMONY:END name="PROJECT:TGBOT:DOCKER:README:SCOPE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCKER:README:PLAN">
## Планируемая структура
- `core.Dockerfile`
- `text-reply.Dockerfile`
- `plugin-generator.Dockerfile`
- `telegram-bot.Dockerfile`
- `postgres/` — init-скрипты и конфигурация.
<HARMONY:END name="PROJECT:TGBOT:DOCKER:README:PLAN">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCKER:README:NEXT">
## Следующие шаги
- Подготовить базовые Dockerfile с мультистейдж-сборкой.
- Сформировать `docker-compose.yml` с healthcheck и общими сетями.
- Настроить кэширование зависимостей и разделение build/run слоёв.
<HARMONY:END name="PROJECT:TGBOT:DOCKER:README:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCKER:README">
