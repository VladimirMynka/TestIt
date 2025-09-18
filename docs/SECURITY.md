KEYWORDS: безопасность, политика, токены, плагины, ci/cd
[ANCHOR:PROJECT:TGBOT:DOCS:SECURITY]
<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:SECURITY">
# Политика безопасности

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:SECURITY:PRINCIPLES">
## Базовые принципы
1. **Secret Management:** секреты хранятся в Vault/GitHub Secrets, загрузка через переменные окружения. Жёсткий запрет на секреты в репозитории; проверки `detect-secrets` обязательны.
2. **Secure Coding:** следуем OWASP ASVS, проверяем ввод/вывод плагинов по JSON Schema, используем Pydantic для валидации.
3. **Audit Trail:** все действия (пользователь, плагин, система) записываются в `audit_logs` (контракт БД) с `trace_id`.
4. **Zero Trust:** плагины получают только необходимые scopes, все запросы проходят через TLS и проверку токенов.
<HARMONY:END name="PROJECT:TGBOT:DOCS:SECURITY:PRINCIPLES">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:SECURITY:AREAS">
## Зоны контроля
- **Ядро (`core/`):** управление токенами, rate limiting, защита от повторных сообщений.
- **Плагины:** проверка токенов, фильтрация данных, контроль heartbeat.
- **LLM-клиент:** маскирование промптов и ответов, контроль квот.
- **CI/CD:** подпись Docker-образов, проверка зависимостей, запрещение привилегированных контейнеров.
<HARMONY:END name="PROJECT:TGBOT:DOCS:SECURITY:AREAS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:SECURITY:CHECKS">
## Обязательные проверки
| Этап | Инструмент | Команда | Частота |
|------|------------|---------|---------|
| CI | `bandit` | `bandit -r core plugins` | каждый PR |
| CI | `safety` | `safety check --full-report` | каждый PR |
| CI | `detect-secrets` | `detect-secrets scan` | каждый PR |
| Release | Docker image scan | `trivy image` (добавить в workflow) | перед релизом |
| Runtime | Health & heartbeat | `/api/v1/plugins/{id}/heartbeat` | каждые 60 секунд |
<HARMONY:END name="PROJECT:TGBOT:DOCS:SECURITY:CHECKS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:SECURITY:INCIDENTS">
## Реакция на инциденты
1. Зафиксировать событие в журнале `docs/PROTOCOLS/runtime/INCIDENT_TEMPLATE.md` (создать при первом инциденте).
2. Активировать соответствующий триггер (`TR-002`, `TR-004`, `TR-006`).
3. Провести пост-мортем, обновить контракты и Roadmap.
4. При утечке токенов — немедленно перевыпустить через ядро и уведомить владельцев плагинов.
<HARMONY:END name="PROJECT:TGBOT:DOCS:SECURITY:INCIDENTS">

<HARMONY:BEGIN name="PROJECT:TGBOT:DOCS:SECURITY:NEXT">
## Следующие шаги
- Настроить GitHub Actions для `trivy` и подписания образов (Cosign).
- Определить политику ротации токенов плагинов (например, каждые 30 дней).
- Добавить security-линтер для Prometheus-эндпоинтов (проверка метаданных).
<HARMONY:END name="PROJECT:TGBOT:DOCS:SECURITY:NEXT">

<HARMONY:END name="PROJECT:TGBOT:DOCS:SECURITY">
