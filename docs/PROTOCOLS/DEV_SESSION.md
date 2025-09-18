KEYWORDS: протокол, разработчик, сессия, документация, контроль
[ANCHOR:PROJECT:TGBOT:PROTOCOL:DEV-SESSION]
<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION">
# Протокол сессии разработчика (P1.1)

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:INPUTS">
## Входные данные
- Назначенная задача из `docs/ROADMAP.md`.
- Соответствующие контракты (ядро, плагины, LLM, БД).
- Последний лог метрик `docs/METRICS/logs/*.jsonl`.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:INPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:STEPS">
## Шаги
1. **Планирование** — изучить Roadmap, уточнить контракты, зафиксировать план изменений.
2. **Подготовка** — создать ветку (если используется), настроить окружение по `scripts/bootstrap` (когда появится).
3. **Реализация** — вносить изменения в код и документы, поддерживая синхронизацию с контрактами.
4. **Тестирование** — выполнить `pytest -q`, `ruff check .`, `mypy .`, `bandit -r core plugins`, `safety check --full-report`, `detect-secrets scan` (при наличии кода).
5. **Документация** — обновить Roadmap, Summary, метрики, соответствующие контракты/протоколы.
6. **Вопросы высшего уровня** — все нерешённые продуктовые вопросы фиксировать в `docs/QUESTIONS.md` и дублировать в `human-friendly/SUMMARY.md`.
7. **PR** — сформировать описание по шаблону `.github/PULL_REQUEST_TEMPLATE.md`, приложить метрики.
8. **Ретроспектива** — при обнаружении проблем зафиксировать триггеры и вопросы (`docs/QUESTIONS.md`).
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:STEPS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:OUTPUTS">
## Выходные данные
- Обновлённые документы и код.
- Логи метрик (`docs/METRICS/logs/`).
- PR с чек-листом проверок.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:OUTPUTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:CHECKPOINTS">
## Контрольные точки
- Все изменения сопровождаются ссылкой на контракт.
- Рабочее дерево чистое перед завершением сессии.
- Roadmap и Summary обновлены не более чем на одну сессию назад.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:CHECKPOINTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ESCALATION">
## Эскалации
- Несоответствие контракту → инициировать `TR-001` (см. `docs/TRIGGERS.md`).
- Провал проверки безопасности → `TR-002`.
- Невозможность воспроизвести окружение → добавить вопрос в `docs/QUESTIONS.md` и задачу в Roadmap.
<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION:ESCALATION">

<HARMONY:END name="PROJECT:TGBOT:PROTOCOL:DEV-SESSION">
