KEYWORDS: telegram-bot, плагины, llm, fastapi, документация
[ANCHOR:PROJECT:TGBOT:README]
<HARMONY:BEGIN name="PROJECT:TGBOT:README">
# Платформа Telegram-бота с плагинами

<HARMONY:BEGIN name="PROJECT:TGBOT:README:MISSION">
## Миссия репозитория
Мы строим промышленную платформу Telegram-бота, где ядро FastAPI, LLM-классификатор и динамические плагины обеспечивают расширяемую функциональность. Репозиторий служит единственным источником правды: требования фиксируются в контрактах `docs/CONTRACTS/`, процессы — в `docs/PROTOCOLS/`, текущее состояние — в `docs/ROADMAP.md` и `human-friendly/SUMMARY.md`.
<HARMONY:END name="PROJECT:TGBOT:README:MISSION">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:COMPONENTS">
## Ключевые компоненты
- **Ядро (`core/`)** — FastAPI-приложение, управляющее диалогами, LLM-классификатором и пулом плагинов.
- **Библиотека LLM (`libs/llm_client/`)** — единый API-клиент для вызова моделей и генерации кода.
- **Плагины (`plugins/`)** — REST-сервисы с манифестами, активируемые по интентам пользователя.
- **Telegram-блот (`bots/telegram/`)** — адаптер между Telegram API и ядром.
- **Инфраструктура (`docker/`, `.github/workflows/`)** — docker-compose, GitHub Actions, политики безопасности.
Каждый модуль описан в архитектурном документе `docs/ARCHITECTURE.md` и связан с контрактами.
<HARMONY:END name="PROJECT:TGBOT:README:COMPONENTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:FEATURES">
## Основные сценарии
1. Пользователь отправляет сообщение в Telegram → бот пересылает его в ядро.
2. Классификатор LLM выбирает подходящий плагин или дефолтный `text_reply`.
3. Плагин вызывается через HTTP, обрабатывает запрос и возвращает ответ.
4. Ядро логирует событие в PostgreSQL, обновляет метрики и отправляет ответ пользователю.
5. Пользователь может сбросить контекст диалога командой «обновить диалог».
<HARMONY:END name="PROJECT:TGBOT:README:FEATURES">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:STRUCTURE">
## Структура репозитория
- `core/` — ядро и тесты.
- `plugins/` — стандартные и пользовательские плагины.
- `libs/` — общие библиотеки.
- `bots/` — адаптеры для клиентских платформ.
- `docs/` — архитектура, контракты, протоколы, метрики, безопасность.
- `human-friendly/` — оперативные сводки.
- `scripts/`, `experiments/`, `docker/` — вспомогательные артефакты.
<HARMONY:END name="PROJECT:TGBOT:README:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:GETTING-STARTED">
## Как начать
1. Прочитайте `docs/ROADMAP.md` и актуальные контракты подсистем.
2. Запустите `scripts/bootstrap/setup_env.sh` для создания виртуального окружения и установки зависимостей из `requirements.txt` (используется `python>=3.11`).
3. Скопируйте `.env.example` в `.env` и заполните ключи (`OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `REDIS_URL`, `POSTGRES_DSN`, `LLM_MODEL`).
4. Следуйте протоколу `docs/PROTOCOLS/DEV_SESSION.md` для планирования работы и запуска проверок (`pytest`, `ruff`, `mypy`, `bandit`, `safety`, `detect-secrets`).
5. Запустите локальный API: `uvicorn core.app.main:create_app --reload` (использует реализованный каркас FastAPI).
6. Для новых плагинов используйте контракт `docs/CONTRACTS/plugins/MANIFEST.md`.
7. Перед PR убедитесь, что метрики обновлены и описаны в `docs/METRICS/logs/`.
<HARMONY:END name="PROJECT:TGBOT:README:GETTING-STARTED">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:ENV">
## Управление зависимостями
- `pyproject.toml` — основной источник конфигурации (`tool.poetry`, `ruff`, `mypy`, `pytest`).
- `requirements.in` → `requirements.txt` — процесс закрепления версий; обновляйте через `poetry export --with dev --format requirements.txt --output requirements.txt`.
- Скрипт `scripts/bootstrap/setup_env.sh` автоматически обновляет виртуальное окружение и шаблон `.env`.
Источник истины — `docs/CONTRACTS/CORE.md` и протокол `docs/PROTOCOLS/DEV_SESSION.md`.
<HARMONY:END name="PROJECT:TGBOT:README:ENV">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:REFERENCE">
## Быстрые ссылки
- Архитектура: `docs/ARCHITECTURE.md`
- Контракты ядра и БД: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/DATABASE.md`
- Протоколы: `docs/PROTOCOLS/`
- Политика безопасности: `docs/SECURITY.md`
<HARMONY:END name="PROJECT:TGBOT:README:REFERENCE">

<HARMONY:BEGIN name="PROJECT:TGBOT:README:SOURCE-OF-TRUTH">
## Источник истины
При несоответствии информации приоритет имеют контракты и протоколы. Любое изменение реализации требует обновления соответствующего документа.
<HARMONY:END name="PROJECT:TGBOT:README:SOURCE-OF-TRUTH">

<HARMONY:END name="PROJECT:TGBOT:README">
