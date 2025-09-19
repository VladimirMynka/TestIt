KEYWORDS: roadmap, индекс, агрегатор, задачи, статусы
[ANCHOR:PROJECT:TGBOT:DOCS:ROADMAP]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP">
# Индекс Roadmap

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:STRUCTURE">
## Структура
- `docs/ROADMAP/changes/` — change-файлы по сессиям (`roadmap-changes-SXXX.md`).
- `docs/ROADMAP/templates/roadmap-change-template.md` — обязательный шаблон для авторов.
- Этот индекс содержит только подтверждённые статусы задач и список очереди для агрегации.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:STRUCTURE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:STATUS">
## Подтверждённый статус (агрегация S006 от 2025-09-19)
| Идентификатор | Описание | Статус | Источник |
|---------------|----------|--------|----------|
| `ROADMAP:S001` | Сформировать документный каркас репозитория | ✅ Выполнено | `docs/ROADMAP/changes/roadmap-changes-S003.md` |
| `ROADMAP:S002` | Уточнить архитектурные решения ядра и подсистем | ✅ Выполнено | `docs/ROADMAP/changes/roadmap-changes-S003.md` |
| `ROADMAP:S003` | Сформировать план MVP и каталог Issues | ✅ Выполнено | `docs/ROADMAP/changes/roadmap-changes-S003.md` |
| `ROADMAP:A-001…A-003` | Завершить архитектурные Issues и manifest | ✅ Выполнено | `docs/ROADMAP/changes/roadmap-changes-S004.md` |
| `ROADMAP:D-001` | Подготовить базовую Python-конфигурацию | ✅ Выполнено | `docs/ROADMAP/changes/roadmap-changes-S005.md` |
| `ROADMAP:D-002` | Реализовать каркас FastAPI ядра | ✅ Выполнено | `docs/ROADMAP/changes/roadmap-changes-S006.md` |
| `ROADMAP:D-003` | Реализовать модели БД и миграции | 🗓 Запланировано | `docs/ISSUES/BACKLOG/ISSUE-D-003.md` |
| `ROADMAP:D-004` | Реализовать асинхронный LLM-клиент | 🗓 Запланировано | `docs/ISSUES/BACKLOG/ISSUE-D-004.md` |
| `ROADMAP:D-005…D-007` | Стандартные плагины и Telegram-адаптер | 🗓 Запланировано | `docs/ISSUES/BACKLOG/ISSUE-D-005.md` и далее |
| `ROADMAP:D-008` | Настроить docker-compose и Dockerfile | 🗓 Запланировано | `docs/ISSUES/BACKLOG/ISSUE-D-008.md` |
| `ROADMAP:D-009` | Настроить GitHub Actions | 🗓 Запланировано | `docs/ISSUES/BACKLOG/ISSUE-D-009.md` |
| `ROADMAP:T-001…T-003` | Подготовить тестовый контур | 🗓 Запланировано | `docs/ISSUES/BACKLOG/ISSUE-T-001.md` |
| `ROADMAP:MONITORING` | Формализовать контракт мониторинга | ❓ Требует уточнения | `docs/ROADMAP/changes/roadmap-changes-S004.md` |
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:STATUS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:QUEUE">
## Очередь change-файлов
| Change-файл | Автор | Статус |
|-------------|-------|--------|
| *(пусто)* | — | — |
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:QUEUE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:HISTORY">
## История агрегаций
| Сессия | Change-файл | Основные сдвиги |
|--------|-------------|-----------------|
| S006 | `docs/ROADMAP/changes/roadmap-changes-S006.md` | Закрыт `ROADMAP:D-002` (FastAPI каркас). |
| S005 | `docs/ROADMAP/changes/roadmap-changes-S005.md` | Закрыт `ROADMAP:D-001`, активирована подготовка к D-002. |
| S004 | `docs/ROADMAP/changes/roadmap-changes-S004.md` | Завершены архитектурные Issues, активирована D-001. |
| S003 | `docs/ROADMAP/changes/roadmap-changes-S003.md` | Создан каркас документации, архитектура и план MVP. |
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:HISTORY">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:ROADMAP:GUIDE">
## Инструкции авторам
- Перед созданием change-файла уточните статус связанного Issue.
- Не вносите прямых правок в этот индекс; изменения проходят через агрегатор.
- После агрегации обновите `docs/METRICS/STATE_DEFINITIONS.md`, если появились новые метрики.
<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP:GUIDE">

<HARMONY:END name="PROJECT:TGBOT:DOCS:ROADMAP">
