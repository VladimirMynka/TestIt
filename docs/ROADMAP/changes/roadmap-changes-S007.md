KEYWORDS: roadmap, change-файл, S007, автоматизация, метрики
[ANCHOR:PROJECT:TGBOT:ROADMAP:CHANGES:S007]
<HARMONY:BEGIN name="PROJECT:TGBOT:ROADMAP:CHANGES:S007">
# Change-файл Roadmap (S007)

<HARMONY:BEGIN name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:HEADER">
## Метаданные
- Сессия: `S007`
- Автор: `AC (Agent-Coder)`
- Роль автора: `LLM-исполнитель`
- Дата: `2025-09-19`
- Связанные Issues: `планируется ISSUE-OPS-001` (создать после агрегации)
<HARMONY:END name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:UPDATES">
## Предлагаемые изменения
| Элемент | Текущее состояние | Предлагаемое состояние | Обоснование |
|---------|-------------------|------------------------|-------------|
| `ROADMAP:OPS-OBS` | отсутствует в индексе | 🆕 Предложено (Backlog) | Закрепить задачу по автоматизации метрик и интеграции скриптов `metrics/snapshot.py`, `navigation/context_radar.py`, `reporting/change_cards.py` в CI/оперативные регламенты, чтобы агенты быстрее фиксировали когнитивную нагрузку и состояние документации. |
| Процесс регистрации change-файлов | Требовал ручного списка в индексах | ✅ Исправлено: фиксация только по каталогу | Исключаем ручные очереди, чтобы избежать git-конфликтов; агрегаторы находят pending-файлы по их расположению и отметкам внутри файлов. |
<HARMONY:END name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:UPDATES">

<HARMONY:BEGIN name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:CHECKS">
## Проверки
- [ ] Контракты/Issues обновлены.
- [x] Метрики актуализированы (`M-ROADMAP-HEALTH` оценка отложена до агрегации; текущие метрики зафиксированы в логе).
- [x] Связанные change-файлы (Summary/Issues) созданы.
- [x] Подтвердил, что агрегатор (LLM) перенесёт изменения в индекс; прямых правок `docs/ROADMAP.md` не вносилось.
<HARMONY:END name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:NOTES">
## Примечания
- После агрегации потребуется оформить Issue `ISSUE-OPS-001` в `docs/ISSUES/BACKLOG/` с детальной постановкой и чек-листом.
- Менеджер проекта узнает о задаче через human-friendly блок; прямые правки он не делает.
- Агрегатор должен указать коммит при подтверждении (формат примечания: `aggregated in <commit>`).
<HARMONY:END name="PROJECT:TGBOT:ROADMAP:CHANGES:S007:NOTES">

🟡 pending — ожидает обработки агрегатором Roadmap.

<HARMONY:END name="PROJECT:TGBOT:ROADMAP:CHANGES:S007">
