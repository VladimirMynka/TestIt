KEYWORDS: issue, developer, github actions, ci, линтинг
[ANCHOR:PROJECT:TGBOT:ISSUE:D-009]
<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009">
# Issue D-009 — Настроить GitHub Actions для линтинга, тестов и безопасности

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:ROLE">
## Роль
- [ ] Architect
- [x] Developer
- [ ] Tester
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:ROLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:CONTEXT">
## Контекст
- Связанные Roadmap элементы: `[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP:NEXT-STEPS]`
- Контракты: `docs/SECURITY.md`
- Протоколы: `docs/PROTOCOLS/RELEASE_PIPELINE.md`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:CONTEXT">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:GOAL">
## Цель
Создать workflows: `ci.yml` (lint + tests), `security.yml` (bandit, safety, detect-secrets), `deploy.yml` (заглушка). Настроить кеширование зависимостей, матрицу Python 3.11/3.12, публикацию артефактов отчётов.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:GOAL">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:DELIVERABLES">
## Ожидаемые артефакты
- Workflow файлы в `.github/workflows/`.
- Обновлённый `docs/SECURITY.md` и `docs/CHANGELOG.md` (ссылки на pipelines).
- Документация в `docs/PROTOCOLS/RELEASE_PIPELINE.md` с шагами CI.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:DELIVERABLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:DEPENDENCIES">
## Зависимости
- Блокирующие: `ISSUE-D-001`
- Разблокирует: `ISSUE-T-001`, `ISSUE-T-002`, `ISSUE-T-003`
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:DEPENDENCIES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:CHECKS">
## Проверки
- [ ] Контракты обновлены
- [ ] Протоколы обновлены
- [ ] Метрики обновлены
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ISSUE:D-009:NOTES">
## Примечания
Workflow должны выполняться для всех pull request и main-ветки. Источник истины по шагам — протокол релизного конвейера.
<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009:NOTES">

<HARMONY:END name="PROJECT:TGBOT:ISSUE:D-009">
