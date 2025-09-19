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

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:ROLES">
## Ролевые допущения
- Агрегатор — LLM-агент, назначенный на отдельную сессию. Он не вносит исходные изменения в код, а только переносит согласованный
  контент из change-файлов в индекс и архив.
- Исполнители (также LLM-агенты) создают change-файлы и отмечают их статус `🟡 pending` внутри файла; после агрегации агрегатор
  проставляет отметку `✅` с ссылкой на коммит и при необходимости перемещает файл в архив.
- Человек-менеджер проекта читает итоговый блок `human-friendly/SUMMARY.md` и `sessions/SXXX/summary.md`, но не редактирует файлы
  напрямую. Все его запросы поступают через постановку задач LLM-агентам.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:ROLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:INPUTS">
## Входные данные
- Change-файлы `human-friendly/changes/summary-changes-SXXX.md`.
- Последние метрики `docs/METRICS/logs/*.jsonl`.
- Связанные change-файлы Roadmap/Issues (при наличии ссылок в change-файле).
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:STEPS">
## Шаги
1. **Сбор входных данных** — выполнить `python scripts/reporting/change_cards.py` (или просмотреть каталоги `changes/`) для
   получения списка активных change-файлов.
2. **Верификация** — сверить, что указанные изменения синхронны с контрактами/протоколами и что соответствующие метрики обновлены.
3. **Агрегация** — перенести утверждённые блоки в `sessions/SXXX/summary.md` или добавить новый сессионный файл при необходимости.
4. **Обновление индекса** — скорректировать `SUMMARY.md`: статус агрегации, таблицу сессий и при необходимости ссылки на новые
   сессионные отчёты.
5. **Журналирование** — в конце change-файла указать статус (например, `✅ aggregated in commit <hash>`) и переместить файл в архив или удалить.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:OUTPUTS">
## Результат
- Обновлённые `sessions/SXXX/summary.md` с фиксированными итогами.
- Индекс `SUMMARY.md` отражает последнюю дату агрегации и ссылки на актуальные сессионные отчёты (без ручного списка ожидающих файлов).
- Лог метрик дополнен записью об агрегации (при необходимости).
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:ESCALATION">
## Эскалация
- Если change-файлы противоречат контрактам — эскалировать по `docs/TRIGGERS.md` (TR-001).
- Если метрики не обновлены более одной сессии — инициировать задачу в Roadmap и уведомить ответственного за метрики.
<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:HUMAN:PROTOCOL:AGGREGATION">
