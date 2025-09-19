KEYWORDS: summary, человек, агрегатор, сессии, планирование
[ANCHOR:PROJECT:TGBOT:HUMAN:SUMMARY]
<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:SUMMARY">
# Индекс человеко-ориентированных отчётов

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:SUMMARY:AGGREGATION-STATUS">
## Статус агрегации
- Последняя подтверждённая агрегация: **S006** (2025-09-19T12:30:00Z).
- Ответственный агрегатор: назначается в `docs/PROTOCOLS/DEV_SESSION.md`.
- Источник истины по содержанию — файлы в `sessions/`.
- Читатель human-friendly слоя — менеджер проекта (человек), он не вносит прямых правок и взаимодействует только через запросы к
  LLM-агентам.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:SUMMARY:AGGREGATION-STATUS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:SUMMARY:SESSION-INDEX">
## Навигация по сессиям
| Сессия | Статус | Ссылка |
|--------|--------|--------|
| S006 | подтверждено | `sessions/S006/summary.md` |
| S005 | подтверждено | `sessions/S005/summary.md` |
| S004 | подтверждено | `sessions/S004/summary.md` |
<HARMONY:END name="PROJECT:TGBOT:HUMAN:SUMMARY:SESSION-INDEX">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:SUMMARY:PENDING">
## Ожидающие change-файлы
Все необработанные change-файлы находятся в каталоге `changes/`. Для обзора используйте
`python scripts/reporting/change_cards.py` или просмотрите каталог напрямую — дополнительная регистрация в индексе не требуется.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:SUMMARY:PENDING">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:SUMMARY:PROTOCOL">
## Связанные протоколы и метрики
- Протокол агрегации: `human-friendly/AGGREGATION_PROTOCOL.md`.
- Метрика свежести документации: `M-DOC-AGGREGATION-LAG` (см. `docs/METRICS/STATE_DEFINITIONS.md`).
- При обработке change-файлов фиксируйте ссылки на PR/коммиты в журнале протокола.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:SUMMARY:PROTOCOL">

<HARMONY:END name="PROJECT:TGBOT:HUMAN:SUMMARY">
