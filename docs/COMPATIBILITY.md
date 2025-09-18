KEYWORDS: совместимость, версии, api, плагины, миграции
[ANCHOR:PROJECT:TGBOT:DOCS:COMPATIBILITY]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:COMPATIBILITY">
# Политика совместимости

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:COMPATIBILITY:POLICY">
## Общие положения
- Семантическое версионирование (`MAJOR.MINOR.PATCH`) для ядра, плагинов и библиотек.
- Несовместимые изменения допускаются только при повышении `MAJOR` и объявлении периода поддержки ≥ 2 минорных релиза.
- Источник истины — записи в `docs/CHANGELOG.md` и актуальные контракты.
<HARMONY:END name="PROJECT:TGBOT:DOCS:COMPATIBILITY:POLICY">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:COMPATIBILITY:MATRIX">
## Матрица совместимости
| Компонент | Текущая версия | Совместимые версии | Заметки |
|-----------|----------------|--------------------|---------|
| Ядро API | `v1` (`CORE.md` V1.1) | Плагины manifest `1.x`, Telegram-бот `v1` | Redis обязателен, fallback в PostgreSQL описан в `CORE.md` |
| База данных | `schema V1.1` | Ядро `v1`, плагины `>=1.0` | `plugin_calls.status` расширен до 6 состояний |
| Схемы API | `v1alpha` | Боты и плагины `>=1.0` | Версия передаётся в заголовке `X-Schema-Version` |
| LLM-клиент | `V1.x` | Ядро `>=1.0`, плагины `>=1.0` | Основной провайдер — OpenAI, fallback — mock |
| Плагин text_reply | `1.0.0` | Ядро API `v1`, manifest `1.x` | Требует LLM-клиент `V1.x` |
| Плагин plugin_generator | `1.0.0` | Ядро API `v1`, manifest `1.x` | Требует LLM-клиент `V1.x` |
| Telegram-бот | `v1.0` | Ядро API `v1`, схемы `v1alpha` | Режим long polling, webhook в бэклоге |
| Redis слой | `config V1` | Ядро `v1`, бот `v1`, плагины `1.x` | TTL 10 мин, Streams обязательны для событий |
<HARMONY:END name="PROJECT:TGBOT:DOCS:COMPATIBILITY:MATRIX">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:COMPATIBILITY:PROCESS">
## Процесс управления
1. Оценить влияние изменений и задокументировать в контракте.
2. Обновить Changelog и матрицу совместимости.
3. Указать сроки депрекации и план миграций (минимум 2 недели для плагинов).
4. Сообщить владельцам плагинов о грядущих изменениях через Roadmap и отдельные уведомления.
<HARMONY:END name="PROJECT:TGBOT:DOCS:COMPATIBILITY:PROCESS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:COMPATIBILITY:NEXT">
## Ближайшие задачи
- Зафиксировать контракт мониторинга/телеметрии и добавить в матрицу.
- Автоматизировать проверку manifest на совместимость в CI.
- Подготовить гайд по миграциям плагинов между версиями ядра.
<HARMONY:END name="PROJECT:TGBOT:DOCS:COMPATIBILITY:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCS:COMPATIBILITY">
