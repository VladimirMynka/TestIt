KEYWORDS: pull-request, шаблон, harmony, документация, процессы
[ANCHOR:PROJECT:TGBOT:GITHUB:PR-TEMPLATE]
<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE">
# Шаблон Pull Request

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:SUMMARY">
## Сводка
- _что изменено_ (ссылки на контракты/протоколы)
- _зачем_ (связь с Roadmap)
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:SUMMARY">

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:CHECKLIST">
## Чек-лист
- [ ] Контракты и протоколы обновлены
- [ ] Roadmap/метрики актуализированы
- [ ] Документы содержат Harmony-якоря
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:CHECKLIST">

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:DETAILS">
## Детали
- Контракты: `<перечень>`
- Протоколы: `<перечень>`
- Метрики: `<файл журнала>`
- Триггеры: `<изменения>`
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:DETAILS">

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:TESTS">
## Тесты
- pytest -q
- ruff check .
- mypy .
- bandit -r core plugins
- safety check --full-report
- detect-secrets scan
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:TESTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:SECURITY">
## Security & CI
- [ ] lint passed
- [ ] tests passed
- [ ] security checks (bandit/safety)
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:SECURITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:COMPATIBILITY">
## Совместимость
- Влияние на API/БД: `<описание>`
- Ссылка на `docs/COMPATIBILITY.md`: `<ссылка>`
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:COMPATIBILITY">

<HARMONY:BEGIN name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:METRICS">
## Снимок метрик
Вставьте JSON из `docs/METRICS/logs/`.
<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE:METRICS">

<HARMONY:END name="PROJECT:TGBOT:GITHUB:PR-TEMPLATE">
