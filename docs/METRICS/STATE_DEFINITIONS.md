KEYWORDS: метрики, состояние, change-файлы, качество, агрегатор
[ANCHOR:PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS">
# Определения метрик состояния

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:OVERVIEW">
## Назначение
Документ определяет обязательные метрики состояния проекта. Источник истины — этот список; расчёты фиксируются в `docs/METRICS/logs/`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:OVERVIEW">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:TABLE">
## Справочник метрик
| Код | Название | Описание | Метод расчёта | Порог |
|-----|----------|----------|---------------|-------|
| M-DOC-COVERAGE | Покрытие документации | Доля ключевых артефактов, снабжённых Harmony-якорями | Кол-во артефактов с якорями / общее кол-во артефактов | ≥ 0.9 |
| M-ROADMAP-HEALTH | Актуальность Roadmap | Доля задач, обновлённых через подтверждённые change-файлы за последние две сессии | Актуальные задачи / общее число задач | ≥ 0.8 |
| M-METRICS-FRESHNESS | Свежесть метрик | Количество дней с момента последнего лога метрик | `now - last_log_days` | ≤ 1 |
| M-DOC-AGGREGATION-LAG | Задержка агрегации документов | Количество сессий между созданием change-файла и его агрегацией | Среднее значение по очереди | ≤ 3 |
| M-CORE-CONTRACT | Состояние контракта ядра | Доля выполненных требований контракта ядра | (выполнено / общее число требований) из чек-листа | ≥ 0.85 |
| M-PLUGIN-COVERAGE | Покрытие контрактов плагинов | Число плагинов с актуальными контрактами | активные плагины с версиями / общее число плагинов | =1 |
| M-LLM-AVAILABILITY | Доступность LLM | Процент успешных вызовов LLM за сутки | успешные / все вызовы | ≥ 0.97 |
| M-TEXT-REPLY-SATISFACTION | Удовлетворённость ответами | Средний рейтинг (по отзывам/эвристикам) для `text_reply` | (сумма оценок / число оценок) | ≥ 4.2 из 5 |
| M-RELEASE-HEALTH | Здоровье релиза | Количество успешных релизов подряд | счётчик `success` перед первым `fail` | ≥ 3 |
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:TABLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:NEXT">
## Следующие шаги
- Автоматизировать сбор метрик через GitHub Actions и Prometheus.
- Добавить метрики для SLA Telegram-бота (время ответа, ошибки API).
- Визуализировать тренды в `human-friendly/dashboards/`, включая график задержки агрегации (`M-DOC-AGGREGATION-LAG`).
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS">
