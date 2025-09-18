KEYWORDS: плагины, архитектура, manifest, интенты, документация
[ANCHOR:PROJECT:TGBOT:PLUGINS:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:README">
# Плагины

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:README:ROLE">
## Роль подсистемы
Плагины реализуют расширения функциональности бота через автономные REST-сервисы. Каждый плагин следует контракту `docs/CONTRACTS/plugins/MANIFEST.md` и взаимодействует с ядром через универсальный API. Источник истины — контракты плагинов.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:README:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:README:STANDARD-SET">
## Стандартный набор
- `text_reply` — отвечает пользователю с использованием LLM.
- `plugin_generator` — создаёт новый каркас плагина по запросу пользователя и регистрирует его в ядре.
Оба плагина написаны на Python (FastAPI) и используют библиотеку `libs/llm_client`.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:README:STANDARD-SET">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:README:DELIVERY">
## Требования к плагинам
1. Поддержка эндпоинтов `/health`, `/manifest`, `/invoke`.
2. Версионирование `MAJOR.MINOR.PATCH` в manifest.
3. Регистрация в ядре через API `/core/plugins/register`.
4. Набор тестов, подтверждающих совместимость с контрактом.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:README:DELIVERY">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:README:LINKS">
## Связанные документы
- Контракт manifest: `docs/CONTRACTS/plugins/MANIFEST.md`.
- Контракт плагина ответа: `docs/CONTRACTS/plugins/TEXT_REPLY.md`.
- Контракт генератора плагинов: `docs/CONTRACTS/plugins/PLUGIN_GENERATOR.md`.
- Протокол жизненного цикла плагина: `docs/PROTOCOLS/PLUGIN_LIFECYCLE.md`.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:README:LINKS">

<HARMONY:END name="PROJECT:TGBOT:PLUGINS:README">
