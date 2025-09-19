KEYWORDS: issue, developer, pyproject, зависимости, асинхронность
[ANCHOR:PROJECT:TGBOT:ISSUE:D-001]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001">
# Issue D-001 — Подготовить базовую Python-конфигурацию репозитория

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/CONTRACTS/CORE.md`, `docs/CONTRACTS/core/SCHEMAS.md`, `docs/CONTRACTS/LLM_CLIENT.md`, `docs/CONTRACTS/bots/TELEGRAM.md`
- Протоколы: `docs/PROTOCOLS/DEV_SESSION.md`, `docs/PROTOCOLS/RELEASE_PIPELINE.md`
- Инфраструктура: Redis (`config V1`) и OpenAI SDK должны быть отражены в зависимостях и `.env` шаблоне
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:GOAL">
## Цель
Создать `pyproject.toml`, `requirements.in`, `requirements.txt`, настроить общие зависимости (`fastapi`, `sqlalchemy[asyncio]`, `alembic`, `uvicorn[standard]`, `aiogram`, `openai`, `httpx`, `redis`, `pydantic`, `pytest`, `pytest-asyncio`, `ruff`, `mypy`). Настроить базовые конфигурации для `ruff`, `mypy`, `pytest`, добавить `core/__init__.py` и аналогичные заглушки.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:DELIVERABLES">
## Ожидаемые артефакты
- Конфигурационные файлы зависимостей и линтеров с фиксацией версий.
- Обновлённый `README.md` с инструкцией по установке зависимостей и переменных окружения (OpenAI, Redis, PostgreSQL).
- Скрипт `scripts/bootstrap/setup_env.sh` (минимальный) для установки зависимостей и генерации `.env` шаблона.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-A-002`
- Разблокирует: `ISSUE-D-002`, `ISSUE-D-003`, `ISSUE-D-004`, `ISSUE-D-007`, `ISSUE-D-008`, `ISSUE-D-009`, `ISSUE-T-001`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:CHECKS">
## Проверки
- [x] Контракты обновлены
- [x] Протоколы обновлены
- [x] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:OUTCOME">
## Итог
- Добавлены `pyproject.toml`, `requirements.in`, `requirements.txt` с закреплёнными версиями и конфигурациями `ruff`, `mypy`, `pytest`, `bandit`.
- Создан скрипт `scripts/bootstrap/setup_env.sh`, формирующий виртуальное окружение и шаблон `.env.example` с ключевыми переменными.
- Обновлены README, Roadmap, Summary, каталог Issues и Changelog; синхронизированы проверки и протоколы (`DEV_SESSION`).
- Зафиксированы метрики сессии `S005` и перенесена задача в каталог `CLOSED`.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:OUTCOME">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-001:NOTES">
## Примечания
Все версии зависимостей зафиксированы в `requirements.txt`; обновление выполняется через `poetry export --with dev`. Источник истины — `docs/CHANGELOG.md`. Окружение рассчитано на `python>=3.11` и включает асинхронный Redis-клиент.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-001">
