KEYWORDS: плагин, text-reply, manifest, fastapi, документация
[ANCHOR:PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README">
# Плагин текстового ответа

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README:SCOPE">
## Область ответственности
Плагин предоставляет дефолтный текстовый ответ пользователю, опираясь на LLM и контекст диалога. Он активируется по умолчанию, если не найден специализированный плагин. Источник истины — контракт `docs/CONTRACTS/plugins/TEXT_REPLY.md`.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README:SCOPE">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README:ENDPOINTS">
## Эндпоинты
- `GET /health`
- `GET /manifest`
- `POST /invoke`
Схемы запросов и ответов описаны в контракте manifest.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README:ENDPOINTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README:TODO">
## Следующие шаги
- Реализовать FastAPI-приложение и тесты.
- Настроить интеграцию с `libs/llm_client` и логированием usage.
- Добавить dockerfile и CI-пайплайн.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README:TODO">

<HARMONY:END name="PROJECT:TGBOT:PLUGINS:TEXT-REPLY:README">
