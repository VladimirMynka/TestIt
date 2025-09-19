KEYWORDS: протокол, сводка, агрегация, human-friendly, документация
[ANCHOR:PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION]
<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION">
# Протокол агрегации human-friendly

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:HEADER">
## Шапка
- Версия: `P1.0`
- Роль исполнителя: Агрегатор документации
- Связанные протоколы: `docs/PROTOCOLS/DEV_SESSION.md`
- Метрики контроля: `M-DOC-AGGREGATION-LAG`, `M-METRICS-FRESHNESS`
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:INPUTS">
## Входные данные
- Change-файлы `human-friendly/changes/summary-changes-SXXX.md`.
- Последние метрики `docs/METRICS/logs/*.jsonl`.
- Связанные change-файлы Roadmap/Issues (при наличии ссылок в change-файле).
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:STEPS">
## Шаги
1. **Сбор входных данных** — перечислить все change-файлы и зафиксировать их в журнале (раздел "Очередь" `SUMMARY.md`).
2. **Верификация** — сверить, что указанные изменения синхронны с контрактами/протоколами и что соответствующие метрики обновлены.
3. **Агрегация** — перенести утверждённые блоки в `sessions/SXXX/summary.md` или добавить новый сессионный файл при необходимости.
4. **Обновление индекса** — скорректировать `SUMMARY.md`: статус агрегации, таблицу сессий и очистить очередь обработанных файлов.
5. **Журналирование** — в конце change-файла указать статус (например, `✅ aggregated in commit <hash>`) и переместить файл в архив или удалить.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:OUTPUTS">
## Результат
- Обновлённые `sessions/SXXX/summary.md` с фиксированными итогами.
- Индекс `SUMMARY.md` отражает последнюю дату агрегации и пустую очередь либо ссылки на необработанные файлы.
- Лог метрик дополнен записью об агрегации (при необходимости).
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:ESCALATION">
## Эскалация
- Если change-файлы противоречат контрактам — эскалировать по `docs/TRIGGERS.md` (TR-001).
- Если метрики не обновлены более одной сессии — инициировать задачу в Roadmap и уведомить ответственного за метрики.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION">
