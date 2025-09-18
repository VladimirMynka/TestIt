KEYWORDS: roadmap, архитектура, планирование, плагины, ядро
[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP">
# Дорожная карта

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:LEGEND">
## Легенда состояний
- ✅ Выполнено
- 🚧 В работе
- 🗓 Запланировано
- ❓ Требует уточнения
Источник истины — контракты `docs/CONTRACTS/` и Issues `docs/ISSUES/`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:LEGEND">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:CURRENT">
## Состояние на текущую сессию (S004)
- ✅ Сформировать документный каркас репозитория (S001).
- ✅ Уточнить архитектурные решения ядра (`docs/ARCHITECTURE.md`).
- ✅ Подготовить контракт для ядра и БД (`docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/DATABASE.md`).
- ✅ Сформировать контракты стандартных плагинов и manifest.
- ✅ Обновить метрики, триггеры и политику безопасности под проект.
- ✅ Зафиксировать план MVP и структуру Issues (`docs/ISSUES/`).
- ✅ Специфицировать контракт Telegram-бота (`ISSUE-A-001`, `docs/CONTRACTS/bots/TELEGRAM.md`).
- ✅ Спроектировать асинхронные схемы API и каркас модулей (`ISSUE-A-002`, `docs/CONTRACTS/core/SCHEMAS.md`, `core/README.md`).
- ✅ Дополнить контракт регистрации плагинов и событий (`ISSUE-A-003`, обновлённые `CORE.md`, `MANIFEST.md`, `TRIGGERS.md`).
- 🚧 Подготовить базовую Python-конфигурацию (`ISSUE-D-001`, перенесено в `IN_PROGRESS`).
- 🗓 Реализовать каркас FastAPI ядра (`ISSUE-D-002`).
- 🗓 Реализовать модели БД и миграции (`ISSUE-D-003`).
- 🗓 Реализовать асинхронный LLM-клиент (`ISSUE-D-004`).
- 🗓 Реализовать стандартные плагины (`ISSUE-D-005`, `ISSUE-D-006`).
- 🗓 Реализовать адаптер Telegram (`ISSUE-D-007`).
- 🗓 Настроить docker-compose и Dockerfile (`ISSUE-D-008`).
- 🗓 Настроить GitHub Actions (`ISSUE-D-009`).
- 🗓 Подготовить тестовый контур (`ISSUE-T-001…T-003`).
- ❓ Формализовать контракт мониторинга (`docs/CONTRACTS/core/TELEMETRY.md`) — требуется план.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:CURRENT">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS">
## Следующие шаги (MVP)
1. Выполнить разработческую задачу D-001 (конфигурация Python/poetry, зависимость от схем) с учётом Redis и OpenAI ключей.
2. После D-001 перейти к D-002…D-004, используя схемы `v1alpha` и новые контракты.
3. Реализовать стандартные плагины и Telegram-адаптер (D-005…D-007), проверяя manifest и события.
4. Настроить окружение запуска и CI/CD (D-008, D-009) с Redis и OpenAI секретами.
5. Подготовить тестовый контур (T-001…T-003) с общими схемами и docker-compose.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:HISTORY">
## История изменений
| Сессия | Изменение |
|--------|-----------|
| S001 | Создан каркас документации и зафиксированы процессы сопровождения. |
| S002 | Описана целевая архитектура, подготовлены контракты ядра, БД, LLM и плагинов, добавлены протоколы CI/CD и жизненного цикла. |
| S003 | Сформирован план MVP, созданы Issues и граф зависимостей, обновлены Roadmap и протоколы под новые требования. |
| S004 | Закрыты архитектурные задачи A-001…A-003, добавлены контракты Telegram-бота и схем API, переработаны триггеры и совместимость. |
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:HISTORY">

<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP">
