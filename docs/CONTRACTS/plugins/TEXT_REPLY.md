KEYWORDS: контракт, плагин, text-reply, llm, ответы
[ANCHOR:PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY">
# Контракт плагина текстового ответа (V1.0)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:CONTEXT">
## Контекст
`plugins/text_reply` реализует базовый ответ пользователю и активируется, если не найден специализированный плагин. Контракт дополняет manifest (`docs/CONTRACTS/plugins/MANIFEST.md`) и определяет обязательное поведение при генерации ответа.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:FUNCTIONAL">
## Функциональные требования
1. При получении запроса `/invoke` плагин формирует ответ, используя `LLMClient.invoke` с моделью по умолчанию `gpt-4o-mini`.
2. Плагин обязан учитывать историю диалога, переданную в `context.messages` (не менее 5 последних сообщений).
3. Ответ должен содержать поля: `text`, `confidence`, `usage` (токены, стоимость).
4. Если LLM недоступен, плагин возвращает предопределённое сообщение об ошибке пользователю и инициирует событие `llm_unavailable` через `/events`.
5. Плагин поддерживает локализацию: определяет язык пользователя по полю `locale` и выбирает соответствующие промпты.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:FUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:NONFUNCTIONAL">
## Нефункциональные требования
- Время ответа плагина ≤ 2 000 мс при стабильном LLM.
- Ошибки LLM должны иметь механизм повторных попыток (до 2 ретраев).
- Логи плагина содержат `trace_id`, `dialog_id`, `llm_model`, `tokens_used`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:NONFUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:SECURITY">
## Безопасность
- Токен ядра хранится только в переменных окружения и не логируется.
- Промпты и ответы не должны содержать персональные данные сверх необходимых.
- Плагин обязан использовать `https` при обращении к LLM-провайдеру.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:TESTING">
## Тестирование
- Юнит-тесты промптов и форматирования: `pytest -q plugins/text_reply/tests`.
- Контрактный тест с ядром (мок): `scripts/smoke/verify_text_reply.sh`.
- Мониторинг качества: метрика `M-TEXT-REPLY-SATISFACTION` (см. `docs/METRICS/STATE_DEFINITIONS.md`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:TESTING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:COMPATIBILITY">
## Совместимость
- Поддерживает manifest версий `1.x`.
- Изменения промптов фиксируются в `CHANGELOG` плагина и не требуют изменения API.
- При добавлении новых выходных полей требуется увеличить минорную версию (`1.x`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY:COMPATIBILITY">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:TEXT-REPLY">
