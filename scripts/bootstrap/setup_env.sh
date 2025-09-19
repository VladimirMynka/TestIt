#!/usr/bin/env bash
# KEYWORDS: bootstrap, окружение, зависимости, poetry, env
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
VENV_DIR="${VENV_DIR:-$ROOT_DIR/.venv}"
REQUIREMENTS_FILE="$ROOT_DIR/requirements.txt"
ENV_TEMPLATE="$ROOT_DIR/.env.example"

printf "[setup] Корневая директория: %s\n" "$ROOT_DIR"

if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
  printf "[setup] Создано виртуальное окружение: %s\n" "$VENV_DIR"
else
  printf "[setup] Используется существующее окружение: %s\n" "$VENV_DIR"
fi

# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip
python -m pip install -r "$REQUIREMENTS_FILE"

cat > "$ENV_TEMPLATE" <<'EOT'
# KEYWORDS: env, конфигурация, openai, redis, postgres
# Шаблон переменных окружения для локальной разработки.
# Источник истины — контракты и протоколы; значения заполните перед запуском.
OPENAI_API_KEY=changeme
TELEGRAM_BOT_TOKEN=changeme
REDIS_URL=redis://localhost:6379/0
POSTGRES_DSN=postgresql+asyncpg://bot:bot@localhost:5432/bot
LLM_MODEL=gpt-4o-mini
UVICORN_HOST=0.0.0.0
UVICORN_PORT=8000
EOT

printf "[setup] Обновлён шаблон переменных: %s\n" "$ENV_TEMPLATE"
printf "[setup] Завершено. Активируйте окружение командой: 'source %s/bin/activate'\n" "$VENV_DIR"
