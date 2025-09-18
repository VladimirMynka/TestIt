KEYWORDS: contributing, процессы, harmony, документация, стиль
[ANCHOR:PROJECT:TGBOT:DOCS:CONTRIBUTING]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING">
# Руководство по внесению изменений

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:PRINCIPLES">
## Основные принципы
1. Все документы и комментарии пишутся на русском языке.
2. Источник истины — соответствующие контракты и протоколы (`docs/CONTRACTS`, `docs/PROTOCOLS`).
3. Каждый файл начинается со строки `KEYWORDS:` и содержит внешние якоря `[ANCHOR:...]` и внутренние блоки `<HARMONY:BEGIN/END ...>`.
4. Минимальная глубина вложенности Harmony-якорей — три уровня (проект → подсистема → раздел/артефакт).
5. Любое изменение реализации сопровождается обновлением метрик и Roadmap.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:PRINCIPLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:CONTRIBUTING:FLOW">
## Поток работы сессии
1. Изучить Roadmap и открытые контракты.
2. Сформировать план и зафиксировать его в протоколе задачи.
3. Реализовать изменения, синхронно обновляя документы и тесты.
4. Запустить обязательные проверки (pytest, ruff, mypy, bandit, safety, detect-secrets) после появления кода.
5. Обновить метрики (`docs/METRICS/logs/*.jsonl`), Roadmap, Summary и связанные триггеры.
6. Сформировать PR по шаблону `.github/PULL_REQUEST_TEMPLATE.md`, приложить снимок метрик.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:FLOW">

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
- Перед merge рабочее дерево должно быть чистым.
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
Для любых вопросов приоритет имеют контракты в `docs/CONTRACTS` и протоколы в `docs/PROTOCOLS`. Изменение логики без обновления контракта запрещено.
<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING:SOURCE-OF-TRUTH">

<HARMONY:END name="PROJECT:TGBOT:DOCS:CONTRIBUTING">
