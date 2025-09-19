KEYWORDS: протокол, разработчик, сессия, change-файлы, контроль
[ANCHOR:PROJECT:TGBOT:PROTOCOL:DEV-SESSION]
<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION">
# Протокол сессии разработчика (P1.2)

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:HEADER">
## Шапка
- Роль: Разработчик / Архитектор документации
- Связанные протоколы: `human-friendly/AGGREGATION_PROTOCOL.md`
- Обязательные метрики: `M-DOC-AGGREGATION-LAG`, `M-ROADMAP-HEALTH`, `M-METRICS-FRESHNESS`
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:HEADER">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:INPUTS">
## Входные данные
- Назначенная задача из `docs/ROADMAP.md` и её change-файл (если уже в очереди).
- Соответствующие контракты (ядро, плагины, LLM, БД).
- Последний лог метрик `docs/METRICS/logs/*.jsonl`.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:STEPS">
## Шаги
1. **Планирование** — изучить Roadmap, очередь change-файлов и уточнить контракты; зафиксировать план изменений.
2. **Подготовка** — выполнить `scripts/bootstrap/setup_env.sh`, активировать `.venv`, убедиться в наличии шаблонов change-файлов.
3. **Реализация** — вносить изменения в код и документы, создавая change-файлы (`{ARTIFACT_NAME}-changes-{SESSION_ID}`) для Summary, Roadmap, Issues и других агрегирующих артефактов.
4. **Тестирование** — выполнить `pytest -q`, `ruff check .`, `mypy .`, `bandit -r core plugins`, `safety check --full-report`, `detect-secrets scan` (при наличии кода).
5. **Документация** — обновить метрики, добавить change-файлы в очереди `human-friendly/SUMMARY.md`, `docs/ROADMAP.md` и указать статус (`🟡 pending`).
6. **PR** — сформировать описание по шаблону, приложить ссылки на change-файлы и снимок метрик.
7. **Ретроспектива** — выявленные вопросы фиксировать в `docs/QUESTIONS.md`; при необходимости создать change-файл Issues для эскалации.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:OUTPUTS">
## Выходные данные
- Обновлённые change-файлы (Summary/Roadmap/Issues) с отмеченным статусом ожидания агрегации.
- Логи метрик (`docs/METRICS/logs/`).
- PR с чек-листом проверок и ссылками на change-файлы.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:CHECKPOINTS">
## Контрольные точки
- Все изменения сопровождаются ссылкой на контракт и change-файл.
- Рабочее дерево чистое перед завершением сессии.
- Roadmap и Summary обновлены через очереди агрегации, без прямых правок индекса.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:CHECKPOINTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ESCALATION">
## Эскалации
- Несоответствие контракту → инициировать `TR-001` (см. `docs/TRIGGERS.md`).
- Просрочка change-файла более трёх сессий → уведомить агрегатора и создать Issue.
- Невозможность воспроизвести окружение → добавить вопрос в `docs/QUESTIONS.md` и задачу в Roadmap.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION">
