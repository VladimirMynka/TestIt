KEYWORDS: плагин, генератор, код, fastapi, документация
[ANCHOR:PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README">
# Плагин генерации плагинов

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README:SCOPE">
## Область ответственности
Плагин анализирует запросы пользователя и создаёт новый плагин, если требуемый функционал отсутствует. Он генерирует код, схемы manifest, Dockerfile и регистрацию в ядре. Источник истины — контракт `docs/CONTRACTS/plugins/PLUGIN_GENERATOR.md`.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README:SCOPE">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README:PIPELINE">
## Основной пайплайн
1. Получить запрос и контекст диалога.
2. Вызвать LLM-генератор кода через `libs/llm_client` с подсказками.
3. Сформировать каркас плагина (файлы, manifest, тесты).
4. Вернуть результат и инструкции оператору ядра.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README:PIPELINE">

<HARMONY:BEGIN name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README:TODO">
## Следующие шаги
- Уточнить промпты генерации.
- Определить стратегию валидации сгенерированного кода.
- Настроить сохранение шаблонов в `scripts/`.
<HARMONY:END name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README:TODO">

<HARMONY:END name="PROJECT:TGBOT:PLUGINS:PLUGIN-GENERATOR:README">
