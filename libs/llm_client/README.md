KEYWORDS: библиотека, llm, api-клиент, контракты, документация
[ANCHOR:PROJECT:TGBOT:LIBS:LLM-CLIENT:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README">
# Универсальный LLM-клиент

<HARMONY:BEGIN name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:ROLE">
## Назначение
Библиотека обеспечивает единый интерфейс обращения к LLM для ядра и плагинов. Она инкапсулирует аутентификацию, ретраи, трейсинг и лимиты. Источник истины — контракт `docs/CONTRACTS/LLM_CLIENT.md`.
<HARMONY:END name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:FEATURES">
## Ключевые возможности
- Абстракция над поставщиками (OpenAI, локальные модели).
- Система политик (токен-лимиты, задержки, кеширование).
- Логирование и наблюдаемость для метрик SLA.
- Клиент для синхронного и асинхронного вызова.
<HARMONY:END name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:FEATURES">

<HARMONY:BEGIN name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:STRUCTURE">
## Структура
- `client.py` — основной интерфейс.
- `providers/` — адаптеры LLM.
- `schemas/` — определения запросов и ответов.
- `tests/` — контрактные тесты интеграций.
<HARMONY:END name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:NEXT">
## Следующие шаги
- Зафиксировать список поддерживаемых провайдеров.
- Определить формат конфигурации и secret storage.
- Подготовить мок-реализацию для тестов.
<HARMONY:END name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README:NEXT">

<HARMONY:END name="PROJECT:TGBOT:LIBS:LLM-CLIENT:README">
