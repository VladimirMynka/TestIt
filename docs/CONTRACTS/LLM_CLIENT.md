KEYWORDS: контракт, llm, api-клиент, генерация, классификация
[ANCHOR:PROJECT:TGBOT:CONTRACT:LLM-CLIENT]
<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT">
# Контракт библиотеки LLM-клиента (V1.0)

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:CONTEXT">
## Контекст
`libs/llm_client` предоставляет унифицированный доступ к моделям LLM для задач классификации интентов и генерации текстов/кода. Клиент используется ядром и плагинами и должен работать одинаково во всех окружениях. Источник истины — этот контракт и архитектура (`docs/ARCHITECTURE.md`).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:API">
## Публичный интерфейс
- `LLMClient.invoke(prompt: Prompt, *, model: str, temperature: float) -> LLMResponse`
- `LLMClient.classify(input: ClassificationRequest) -> ClassificationResult`
- `LLMClient.generate_code(spec: CodeGenerationSpec) -> GeneratedProject`
- `LLMClient.health() -> HealthStatus`

Все методы асинхронные (`async`) и поддерживают таймаут и ретраи с экспоненциальной задержкой. Схемы `Prompt`, `ClassificationRequest`, `CodeGenerationSpec` версионируются в `libs/llm_client/schemas/v{n}`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:API">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:FUNCTIONAL">
## Функциональные требования
1. Поддержка минимум двух провайдеров: OpenAI API и локальный mock.
2. Возможность ограничивать использование токенов по подсистемам (ядро, плагины) через конфигурацию.
3. Логирование запросов и ответов с усечёнными данными (обрезка до 2 КБ).
4. Поддержка кеширования ответов на уровне клиента (опционально, фича-флаг).
5. Для генерации кода клиент должен возвращать структуру файлов и инструкции по развертыванию.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:FUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:NONFUNCTIONAL">
## Нефункциональные требования
- **Доступность:** ≥ 99% успешных запросов в течение 10-минутного окна.
- **Latency:** p95 для классификации ≤ 400 мс при использовании локального кэша.
- **Конфигурируемость:** параметры клиентов задаются через `.yaml` файл и переменные окружения.
- **Наблюдаемость:** метрики `llm_requests_total`, `llm_tokens_total`, `llm_errors_total` публикуются через интеграцию с ядром.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:NONFUNCTIONAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:SECURITY">
## Безопасность
- Секреты API провайдеров никогда не пишутся в логи, маскирование обязательно.
- Все исходящие запросы используют HTTPS и валидацию сертификатов.
- Конфигурация хранится в Secret Storage (например, HashiCorp Vault) с ротацией ключей каждые 90 дней.
- Ведение журнала доступа к токенам (кто использовал, когда, сколько токенов).
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:COMPATIBILITY">
## Совместимость
- Все публичные методы должны сохранять обратную совместимость на минорных релизах.
- Добавление новых провайдеров не должно требовать изменений в ядре или плагинах.
- Формат ошибок (`LLMError`) стабилен: `code`, `message`, `provider`, `retryable`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:COMPATIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:TESTING">
## Тестирование
- Юнит-тесты провайдеров: `pytest -q libs/llm_client/tests/providers`.
- Контрактные тесты: моковый сервер, проверяющий форматы запросов/ответов.
- Интеграционные тесты с ядром и плагином `text_reply`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:TESTING">

<HARMONY:BEGIN name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:CHANGE-MANAGEMENT">
## Управление изменениями
- Ответственные: владельцы библиотеки LLM.
- Все изменения сопровождаются обновлением версии (`V1.x`).
- При изменении схем требуется уведомить плагины через Roadmap и обновить `docs/COMPATIBILITY.md`.
<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT:CHANGE-MANAGEMENT">

<HARMONY:END name="PROJECT:TGBOT:CONTRACT:LLM-CLIENT">
