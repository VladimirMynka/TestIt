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
| Код | Тип | Назначение | Метод расчёта / источник | Порог |
|-----|-----|------------|---------------------------|-------|
| M-DOC-COVERAGE | Непрерывная | Доля ключевых артефактов, снабжённых Harmony-якорями | Скрипт `python scripts/metrics/snapshot.py --session-id <ID>` (поле `M-DOC-COVERAGE`) | ≥ 0.9 |
| M-ROADMAP-HEALTH | Непрерывная | Доля задач, обновлённых через подтверждённые change-файлы за последние две сессии | Ручной расчёт (см. формулу ниже) | ≥ 0.8 |
| M-METRICS-FRESHNESS | Непрерывная | Количество дней с момента последнего лога метрик | Скрипт `python scripts/metrics/snapshot.py --session-id <ID>` (поле `M-METRICS-FRESHNESS`) | ≤ 1 |
| M-DOC-AGGREGATION-LAG | Непрерывная | Количество сессий между созданием change-файла и его агрегацией | Скрипт `python scripts/metrics/snapshot.py --session-id <ID>` (поле `M-DOC-AGGREGATION-LAG`) | ≤ 3 |
| M-CORE-CONTRACT | Непрерывная | Доля выполненных требований контракта ядра | Ручной расчёт (см. формулу ниже) | ≥ 0.85 |
| M-PLUGIN-COVERAGE | Непрерывная | Доля активных плагинов с актуальными контрактами | Ручной расчёт (см. формулу ниже) | =1 |
| M-LLM-AVAILABILITY | Непрерывная | Процент успешных вызовов LLM за сутки | Ручной расчёт по журналу обращений (см. формулу ниже) | ≥ 0.97 |
| M-TEXT-REPLY-SATISFACTION | Непрерывная | Средний рейтинг (по отзывам/эвристикам) для `text_reply` | Ручной расчёт (см. формулу ниже) | ≥ 4.2 из 5 |
| M-RELEASE-HEALTH | Дискретная | Количество успешных релизов подряд | Ручной учёт по журналу релизов (см. критерии ниже) | ≥ 3 |
| M-CONTEXT-LOAD | Дискретная | Субъективная оценка вместимости контекста LLM | Заполняется агентом по таблице критериев | ≤ 2 |
| M-NAVIGATION-CLARITY | Дискретная | Субъективная оценка лёгкости навигации | Заполняется агентом по таблице критериев | ≥ 3 |
| M-NOISE-RATIO | Дискретная | Субъективная оценка доли нерелевантных чтений | Заполняется агентом по таблице критериев | ≤ 2 |
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:TABLE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:FORMULAS">
## Формулы непрерывных метрик
- **M-ROADMAP-HEALTH:** `актуальные_задачи / общее_число_задач`, где актуальной считается задача с подтверждённым change-файлом
  за последние две сессии.
- **M-CORE-CONTRACT:** `выполнено_пунктов / общее_число_пунктов` в чек-листе контракта ядра; каждый пункт проверяется ручным
  ревью исполнителя.
- **M-PLUGIN-COVERAGE:** `активные_плагины_с_актуальными_контрактами / общее_число_активных_плагинов`, актуальность проверяется
  по дате последней ревизии контракта против версии плагина.
- **M-LLM-AVAILABILITY:** `успешные_вызовы / общее_число_вызовов` за последние сутки согласно журналу телеметрии.
- **M-TEXT-REPLY-SATISFACTION:** `сумма_оценок / число_оценок`, где оценки берутся из пользовательских отзывов или эвристических
  проверок качества ответа.

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:FORMULAS:AUTOMATION">
### Метрики, рассчитываемые скриптом
- **M-DOC-COVERAGE**, **M-METRICS-FRESHNESS**, **M-DOC-AGGREGATION-LAG** вычисляются автоматически
  командой `python scripts/metrics/snapshot.py --session-id <ID>`; полученные значения переносятся в журнал без ручной корректировки.
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:FORMULAS:AUTOMATION">
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:FORMULAS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE">
## Критерии дискретных метрик

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-RELEASE-HEALTH">
### M-RELEASE-HEALTH — здоровье релиза
| Значение | Проверяемый критерий |
|----------|----------------------|
| 0 | Последний релиз завершился с ошибкой; счётчик обнуляется. |
| 1 | Один успешный релиз подряд без ошибок в журнале релизов. |
| 2 | Два успешных релиза подряд; ни одной ошибки между ними. |
| 3 | Три успешных релиза подряд; условие базовой нормы выполнено. |
| 4 | Четыре успешных релиза подряд, что формирует запас устойчивости. |
| 5 | Пять и более успешных релизов подряд; продолжаем считать значение равным 5 до появления сбоя. |
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-RELEASE-HEALTH">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-CONTEXT-LOAD">
### M-CONTEXT-LOAD — перегрузка контекстом
| Значение | Проверяемый критерий |
|----------|----------------------|
| 0 | Занятость контекста < 50% лимита токенов; не было попыток вынести информацию во внешние заметки. |
| 1 | Занятость контекста 50–75%; ≤ 1 вынужденное свёртывание или очистка контекста за сессию. |
| 2 | Занятость контекста 75–90%; приходится один раз перераспределять фокус, но ключевые детали сохраняются. |
| 3 | Занятость контекста > 90% или ≥ 2 свёртываний; требуется планирование чтений, но работа продолжается без потерь артефактов. |
| 4 | Контекст приходится очищать после каждого крупного шага; ≥ 1 важный фрагмент переносится в change-файл из-за нехватки места. |
| 5 | Выполнение задачи невозможно без перезапуска или делегирования; свыше 2 критичных фрагментов потеряно. |
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-CONTEXT-LOAD">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-NAVIGATION-CLARITY">
### M-NAVIGATION-CLARITY — ясность навигации
| Значение | Проверяемый критерий |
|----------|----------------------|
| 0 | > 5 последовательных безрезультатных попыток найти нужный артефакт; требуется внешняя подсказка. |
| 1 | 3–5 безрезультатных переходов подряд; нужный документ найден только после эскалации к Roadmap/индексам. |
| 2 | 1–2 неудачных поисковых цепочки; артефакты находятся, но с заминками. |
| 3 | Каждый нужный артефакт находится максимум со второй попытки; лишних шагов ≤ 3 за сессию. |
| 4 | Лишние переходы возникают эпизодически (≤ 2 за сессию); структура репозитория очевидна. |
| 5 | Все артефакты находятся с первой попытки; лишних переходов нет. |
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-NAVIGATION-CLARITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-NOISE-RATIO">
### M-NOISE-RATIO — доля нерелевантных чтений
| Значение | Проверяемый критерий |
|----------|----------------------|
| 0 | Нерелевантные материалы составляют < 10% просмотренного; не было возвращений к одной и той же папке без пользы. |
| 1 | 10–25% просмотренного оказалось нерелевантным; ≤ 1 повторное чтение без результата. |
| 2 | 25–40% чтений нерелевантны; ≤ 2 повторных обращений к бесполезным файлам. |
| 3 | 40–60% чтений нерелевантны; заметно влияние шума на темп работы. |
| 4 | 60–80% чтений нерелевантны; значительная часть времени уходит на фильтрацию шума. |
| 5 | > 80% просмотренного нерелевантно; прогресс невозможен без внешней помощи или смены стратегии поиска. |
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE:M-NOISE-RATIO">
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:DISCRETE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:SUBJECTIVE">
## Правила заполнения субъективных метрик
- Значения `M-CONTEXT-LOAD`, `M-NAVIGATION-CLARITY`, `M-NOISE-RATIO` фиксируются в каждом логе метрик и отражают субъективное
  ощущение LLM-агента. Оценка производится по шкале 0–5 с точностью до 0.5.
- При значениях `M-CONTEXT-LOAD ≥ 4` или `M-NOISE-RATIO ≥ 4` агент обязан задать вопрос в `docs/QUESTIONS.md` и отметить
  необходимость разгрузки контекста в change-файле соответствующего артефакта.
- Скрипт `python scripts/metrics/snapshot.py --session-id SXXX` заполняет объективные поля и оставляет подсказки для субъективных
  метрик; после запуска агент дописывает значения вручную перед добавлением записи в `docs/METRICS/logs/`.
- При необходимости можно дополнять заметки (`notes`) пояснением, что повлияло на субъективную оценку.
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:SUBJECTIVE">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:NEXT">
## Следующие шаги
- Интегрировать `scripts/metrics/snapshot.py` в CI, чтобы напоминать агентам о необходимости заполнения субъективных шкал.
- Добавить метрики для SLA Telegram-бота (время ответа, ошибки API).
- Визуализировать тренды в `human-friendly/dashboards/`, включая график задержки агрегации (`M-DOC-AGGREGATION-LAG`) и
  субъективных метрик когнитивной нагрузки.
<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCS:METRICS:STATE-DEFINITIONS">
