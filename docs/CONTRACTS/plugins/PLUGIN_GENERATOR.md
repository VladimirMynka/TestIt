KEYWORDS: контракт, плагин, генератор, код, автогенерация
[ANCHOR:PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR">
# Контракт плагина генерации плагинов (V1.0)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:CONTEXT">
## Контекст
`plugins/plugin_generator` отвечает за создание нового плагина по запросу пользователя, если нужный функционал отсутствует. Он использует LLM для генерации кода и шаблонов и взаимодействует с ядром для регистрации результата.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:FUNCTIONAL">
## Функциональные требования
1. Плагин активируется, если классификатор возвращает тег `plugin.generate` или если intent неизвестен, но пользователь просит новую функцию.
2. `/invoke` принимает структуру `desired_capability`, `constraints`, `user_context`.
3. Ответ содержит `scaffold_archive` (base64), `manifest`, `testing_plan`, `migration_notes`.
4. Плагин автоматически вызывает API ядра `/plugins/register` в режиме черновика и возвращает идентификатор заявки.
5. При невозможности генерации плагин обязан вернуть причину и рекомендации.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:FUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:NONFUNCTIONAL">
## Нефункциональные требования
- Генерация должна занимать ≤ 60 секунд; при превышении — обновлять статус через `/events`.
- Все файлы шаблона проходят линтинг (`ruff`, `mypy`) и формирование `README` автоматически.
- Поддерживается кеширование частых шаблонов и повторное использование артефактов.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:NONFUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:SECURITY">
## Безопасность
- Валидация пользовательских требований: запрещены запросы на выполнение произвольного кода.
- Все генерируемые артефакты проходят проверку секретов (`detect-secrets`).
- Плагин не выполняет сгенерированный код; только создаёт архив.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:TESTING">
## Тестирование
- Юнит-тесты промптов генерации.
- Контрактный тест: проверка, что manifest соответствует `docs/CONTRACTS/plugins/MANIFEST.md`.
- Интеграционный тест: сценарий полного цикла генерации и регистрации плагина в docker-compose.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:TESTING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:COMPATIBILITY">
## Совместимость
- Поддерживает выпуск плагинов под manifest `1.x` и API ядра `v1`.
- Новые типы артефактов (например, GraphQL) требуют обновления версии контракта.
- Выходной архив должен быть совместим с `scripts/bootstrap/create_plugin.py` (когда появится).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR:COMPATIBILITY">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:PLUGINS:PLUGIN-GENERATOR">
