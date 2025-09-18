KEYWORDS: протокол, релиз, ci/cd, docker, деплой
[ANCHOR:PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE]
<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE">
# Протокол релизного пайплайна (P1.0)

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:INPUTS">
## Входные данные
- Одобренный PR с зелёными проверками.
- Обновлённые контракты и `docs/CHANGELOG.md`.
- Версия релиза (`MAJOR.MINOR.PATCH`).
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:CI">
## Этап CI
1. Запуск GitHub Actions `ci.yml`: `ruff check .`, `pytest -q`, `mypy .`, `bandit`, `safety`, `detect-secrets`.
2. Сборка Docker-образов: `core`, `text-reply`, `plugin-generator`, `telegram-bot`.
3. Публикация образов в registry (ghcr.io) с тегом `candidate`.
4. Прогон интеграционных тестов в docker-compose (`scripts/smoke/full_stack.sh`).
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:CI">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:CD">
## Этап CD
1. Создать git-тег `vMAJOR.MINOR.PATCH` после успешного CI.
2. Запустить workflow `deploy.yml`, который:
   - Применяет миграции `alembic upgrade head`.
   - Разворачивает сервисы через `docker stack deploy` или Kubernetes (определить в Roadmap).
   - Выполняет smoke-тесты доступности `/health` и `/metrics`.
3. Уведомляет команду в Telegram-канале об успешном деплое.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:CD">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:ROLLBACK">
## Откат
- Выполнить `docker stack rollback` (или helm rollback) до предыдущей версии.
- Запустить `alembic downgrade -1` при необходимости.
- Зафиксировать инцидент в `docs/PROTOCOLS/runtime/INCIDENT_TEMPLATE.md`.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:ROLLBACK">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:OUTPUTS">
## Выходные данные
- Обновлённый `docs/CHANGELOG.md` с версией.
- Успешно задеплоенный стек в целевом окружении.
- Метрики релиза в `human-friendly/SUMMARY.md` (latency, ошибки).
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:ESCALATION">
## Эскалации
- Провал любого шага CI → блокируем релиз, инициируем `TR-002`.
- Ошибка smoke-тестов → откат и регистрация инцидента.
- Несоответствие метрик SLA → эскалация в архитектурный комитет.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:RELEASE-PIPELINE">
