KEYWORDS: протокол, разработчик, сессия, change-файлы, контроль
[ANCHOR:PROJECT:TGBOT:PROTOCOL:DEV-SESSION]
<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION">
# Протокол сессии разработчика (P1.2)

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:HEADER">
## Шапка
- Роль: Разработчик / Архитектор документации
- Связанные протоколы: `human-friendly/AGGREGATION_PROTOCOL.md`
- Обязательные метрики: `M-DOC-AGGREGATION-LAG`, `M-ROADMAP-HEALTH`, `M-METRICS-FRESHNESS`, `M-CONTEXT-LOAD`,
  `M-NAVIGATION-CLARITY`, `M-NOISE-RATIO`
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ROLES">
## Ролевые ограничения
- Исполнитель — всегда LLM-агент, отвечающий за изменение кода и подготовку change-файлов. Исполнитель **не** агрегирует
  собственные изменения и не редактирует напрямую индексы (`docs/ROADMAP.md`, `human-friendly/SUMMARY.md`).
- Агрегатор (также LLM-агент) действует по `human-friendly/AGGREGATION_PROTOCOL.md`, переносит подтверждённые изменения и
  фиксирует статусы. Он обнаруживает change-файлы по их расположению в каталогах, поэтому исполнитель отмечает статус `🟡 pending`
  внутри файла и ожидает отдельной сессии агрегатора.
- Человек-менеджер проекта не редактирует репозиторий напрямую: он взаимодействует через запросы к LLM-агентам и читает
  только human-friendly отчёты.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ROLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:INPUTS">
## Входные данные
- Назначенная задача из `docs/ROADMAP.md` и её change-файл (если уже создан).
- Соответствующие контракты (ядро, плагины, LLM, БД).
- Последний лог метрик `docs/METRICS/logs/*.jsonl`.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:STEPS">
## Шаги
1. **Планирование** — изучить Roadmap, существующие change-файлы в каталогах `human-friendly/changes/`, `docs/ROADMAP/changes/`,
   `docs/ISSUES/changes/` и уточнить контракты; зафиксировать план изменений.
2. **Подготовка** — выполнить `scripts/bootstrap/setup_env.sh`, активировать `.venv`, убедиться в наличии шаблонов change-файлов.
3. **Реализация** — вносить изменения в код и документы, создавая change-файлы (`{ARTIFACT_NAME}-changes-{SESSION_ID}`) для Summary, Roadmap, Issues и других агрегирующих артефактов.
4. **Тестирование** — выполнить `pytest -q`, `ruff check .`, `mypy .`, `bandit -r core plugins`, `safety check --full-report`, `detect-secrets scan` (при наличии кода).
5. **Документация** — обновить метрики (субъективные и объективные), создать или дополнить change-файлы в соответствующих
   каталогах и указать статус (`🟡 pending`) внутри каждого файла.
6. **PR** — сформировать описание по шаблону, приложить ссылки на change-файлы и снимок метрик.
7. **Ретроспектива** — выявленные вопросы фиксировать в `docs/QUESTIONS.md`; при необходимости создать change-файл Issues для эскалации.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:METRICS">
## Работа с метриками
- Перед завершением сессии выполнить `python scripts/metrics/snapshot.py --session-id SXXX --notes "<краткая заметка>"` для
  получения шаблона записи. Значения субъективных метрик (`M-CONTEXT-LOAD`, `M-NAVIGATION-CLARITY`, `M-NOISE-RATIO`) агент
  проставляет вручную, опираясь на свою когнитивную нагрузку в текущей сессии.
- При значениях `M-CONTEXT-LOAD ≥ 4` или `M-NOISE-RATIO ≥ 4` исполнитель обязан зафиксировать причину перегрузки в разделе
  `notes` и подготовить change-файл с предложением по разгрузке (например, рефакторинг документации или создание нового
  инструмента навигации).
- Если `M-NAVIGATION-CLARITY ≤ 2`, необходимо предложить улучшения структуры в соответствующем change-файле или создать задачу
  в `docs/ISSUES/BACKLOG/`.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:METRICS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:OUTPUTS">
## Выходные данные
- Обновлённые change-файлы (Summary/Roadmap/Issues) с отмеченным внутри файла статусом ожидания агрегации.
- Логи метрик (`docs/METRICS/logs/`).
- PR с чек-листом проверок и ссылками на change-файлы.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:CHECKPOINTS">
## Контрольные точки
- Все изменения сопровождаются ссылкой на контракт и change-файл.
- Рабочее дерево чистое перед завершением сессии.
- Roadmap и Summary не редактировались напрямую; все изменения оформлены через change-файлы.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:CHECKPOINTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ESCALATION">
## Эскалации
- Несоответствие контракту → инициировать `TR-001` (см. `docs/TRIGGERS.md`).
- Просрочка change-файла более трёх сессий → уведомить агрегатора и создать Issue.
- Невозможность воспроизвести окружение → добавить вопрос в `docs/QUESTIONS.md` и задачу в Roadmap.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION">
