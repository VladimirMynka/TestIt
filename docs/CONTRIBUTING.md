KEYWORDS: contributing, процессы, harmony, документация, change-файлы
[ANCHOR:PROJECT:TGBOT:DOCS:CONTRIBUTING]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING">
# Руководство по внесению изменений

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:PRINCIPLES">
## Основные принципы
1. Все документы и комментарии пишутся на русском языке.
2. Источник истины — соответствующие контракты и протоколы (`docs/CONTRACTS`, `docs/PROTOCOLS`).
3. Каждый файл начинается со строки `KEYWORDS:` и содержит внешние якоря `[ANCHOR:...]` и внутренние блоки `<HARMONY:BEGIN/END ...>`.
4. Минимальная глубина вложенности Harmony-якорей — три уровня (проект → подсистема → раздел/артефакт).
5. Любое изменение реализации сопровождается обновлением метрик и Roadmap через change-файлы (`{ARTIFACT_NAME}-changes-{SESSION_ID}`).
6. Прямые правки агрегирующих файлов (Summary, Roadmap, каталоги Issues) запрещены без выполнения протокола агрегации.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:PRINCIPLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:FLOW">
## Поток работы сессии
1. Изучить Roadmap, открытые контракты и очередь change-файлов.
2. Сформировать план и зафиксировать его в протоколе задачи.
3. Реализовать изменения, параллельно создавая change-файлы для документов, которые редактируют несколько агентов.
4. Запустить обязательные проверки (`pytest -q`, `ruff check .`, `mypy .`, `bandit -r core plugins`, `safety check --full-report`, `detect-secrets scan`) после появления кода.
5. Обновить метрики (`docs/METRICS/logs/*.jsonl`), добавить change-файлы Roadmap/Summary/Issues и зарегистрировать их в очереди агрегации.
6. Сформировать PR по шаблону `.github/PULL_REQUEST_TEMPLATE.md`, приложить снимок метрик и ссылки на change-файлы.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:FLOW">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:BATCH-UPDATES">
## Пакетные изменения и агрегация
- Формат change-файла: `{каталог}/{имя}-changes-{SESSION_ID}.md` с обязательным шаблоном каталога `templates/`.
- Все change-файлы фиксируются в разделе очереди агрегирующего документа (`human-friendly/SUMMARY.md`, `docs/ROADMAP.md`).
- Агрегатор запускает протокол минимум раз в три сессии, переносит изменения и помечает обработанные файлы (✅/⚠️/🚫) в их конце.
- После агрегации change-файл удаляется или переносится в архив с ссылкой на коммит.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:BATCH-UPDATES">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:ARCHITECTURE-LINKS">
## Связь с архитектурой
- `core/` — реализует контракт `docs/CONTRACTS/CORE.md`.
- `plugins/` — каждый плагин следует manifest и собственному контракту.
- `libs/llm_client/` — общее ядро работы с LLM.
- `bots/telegram/` — адаптер Telegram (контракт в разработке).
- `docker/` и `.github/workflows/` — реализуют протокол релиза.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:ARCHITECTURE-LINKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:ANCHORS">
## Правила якорей Harmony
- Внешний якорь `[ANCHOR:...]` закрепляется в начале файла и перед ключевыми блоками.
- Внутренние блоки оформляются `<HARMONY:BEGIN name="...">`/`<HARMONY:END name="...">`.
- Имена якорей пишутся в верхнем регистре, разделяются двоеточием: `PROJECT:TGBOT:...`.
- Для ссылок на артефакты используем уровни `CONTRACT`, `PROTOCOL`, `METRIC`, `TRIGGER`.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:ANCHORS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:COMMITS">
## Коммиты и PR
- Коммиты — атомарные, в настоящем времени: «Добавить контракт ядра».
- PR включает заполненные разделы: изменения, проверки, метрики, совместимость.
- Перед merge рабочее дерево должно быть чистым, все change-файлы обработаны или оставлены в очереди с указанием статуса.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:COMMITS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:TOOLS">
## Инструменты и проверки
| Категория | Команда | Назначение |
|-----------|---------|------------|
| Тесты | `pytest -q` | Юнит и интеграционные тесты ядра и плагинов |
| Линтер | `ruff check .` | Статический анализ Python |
| Типы | `mypy .` | Статическая типизация |
| Безопасность | `bandit -r core plugins` | Поиск уязвимостей |
| Зависимости | `safety check --full-report` | Проверка зависимостей |
| Секреты | `detect-secrets scan` | Контроль утечек секретов |
| Форматирование | `ruff format .` | Автоформатирование |
| Контейнеры | `trivy image` | Сканирование Docker-образов (перед релизом) |
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:TOOLS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:SOURCE-OF-TRUTH">
## Источник истины
Для любых вопросов приоритет имеют контракты в `docs/CONTRACTS`, протоколы в `docs/PROTOCOLS` и утверждённые change-файлы, агрегированные в индексах (`human-friendly/SUMMARY.md`, `docs/ROADMAP.md`). Изменение логики без обновления контракта и соответствующего change-файла запрещено.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:SOURCE-OF-TRUTH">

<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING">
