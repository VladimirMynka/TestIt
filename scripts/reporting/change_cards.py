#!/usr/bin/env python3
# KEYWORDS: change-файлы, обзор, карточки, агрегатор, автоматизация
# [ANCHOR:PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS]
# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:MODULE">
"""Генерирует обзорные карточки для change-файлов в каталогах, ожидающих агрегации.

Инструмент помогает агрегатору и исполнителям увидеть, какие change-файлы
ожидают обработки, из каких сессий они поступили и какое основное содержание
они несут. Все карточки помечаются как созданные LLM-агентами.
"""
# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:MODULE">

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


@dataclass
class ChangeCard:
    """Отображение change-файла для агрегатора."""

    scope: str
    path: Path
    session: Optional[str]
    headline: Optional[str]
    status_hint: Optional[str]

    def to_dict(self) -> Dict[str, Optional[str]]:
        """Возвращает карточку в виде словаря."""

        return {
            "scope": self.scope,
            "path": str(self.path),
            "session": self.session,
            "headline": self.headline,
            "status_hint": self.status_hint,
            "role": "LLM-исполнитель",
        }


# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:PARSERS">
CHANGE_DIRECTORIES: Tuple[Tuple[str, str], ...] = (
    ("human-friendly", "human-friendly/changes"),
    ("roadmap", "docs/ROADMAP/changes"),
    ("issues", "docs/ISSUES/changes"),
)

SESSION_RE = re.compile(r"S(\d{3,})")
STATUS_RE = re.compile(r"([✅⚠️🚫🟡][^\n]*)")


def iter_change_files(root: Path) -> Iterable[Tuple[str, Path]]:
    """Итерирует change-файлы во всех поддерживаемых каталогах."""

    for scope, relative in CHANGE_DIRECTORIES:
        directory = root / relative
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            yield scope, path


def extract_session(text: str) -> Optional[str]:
    """Выделяет идентификатор сессии из текста."""

    match = SESSION_RE.search(text)
    if match:
        return f"S{match.group(1)}"
    return None


def extract_status_hint(text: str) -> Optional[str]:
    """Возвращает первую найденную строку со статусной отметкой."""

    match = STATUS_RE.search(text)
    if match:
        return match.group(1).strip()
    return None


def extract_headline(text: str) -> Optional[str]:
    """Получает первую содержательную строку списка."""

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("-") and "[" not in stripped:
            return stripped.lstrip("- ")
    return None


def build_card(scope: str, path: Path) -> ChangeCard:
    """Собирает карточку по одному файлу."""

    text = path.read_text(encoding="utf-8")
    session = extract_session(text)
    status = extract_status_hint(text)
    headline = extract_headline(text)
    return ChangeCard(scope=scope, path=path, session=session, headline=headline, status_hint=status)


def collect_cards(root: Path) -> List[ChangeCard]:
    """Собирает карточки по всем каталогам."""

    cards: List[ChangeCard] = []
    for scope, path in iter_change_files(root):
        cards.append(build_card(scope, path))
    return cards


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:PARSERS">

# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:OUTPUT">
def render_markdown(cards: List[ChangeCard], limit: Optional[int]) -> str:
    """Возвращает Markdown-таблицу по карточкам."""

    rows = []
    header = "| Очередь | Сессия | Путь | Кратко | Статус |\n"
    header += "|---------|--------|------|--------|--------|\n"
    iterable = cards[:limit] if limit else cards
    for card in iterable:
        rows.append(
            f"| {card.scope} | {card.session or '—'} | `{card.path}` | {card.headline or '—'} | "
            f"{card.status_hint or 'ожидает агрегации'} |"
        )
    return header + "\n".join(rows)


def render_json(cards: List[ChangeCard], limit: Optional[int]) -> str:
    """Формирует JSON."""

    iterable = cards[:limit] if limit else cards
    payload = [card.to_dict() for card in iterable]
    return json.dumps(payload, ensure_ascii=False, indent=2)


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:OUTPUT">

# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:CLI">
def parse_args() -> argparse.Namespace:
    """Разбирает аргументы."""

    parser = argparse.ArgumentParser(
        description="Создаёт обзорную таблицу change-файлов для агрегатора (все файлы создаются LLM-агентами)."
    )
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Формат вывода.")
    parser.add_argument("--limit", type=int, default=None, help="Ограничение числа карточек в выводе.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Корень репозитория (по умолчанию определяется автоматически).",
    )
    return parser.parse_args()


def main() -> None:
    """Главная функция."""

    args = parse_args()
    cards = collect_cards(args.root)
    if args.format == "markdown":
        output = render_markdown(cards, args.limit)
    else:
        output = render_json(cards, args.limit)
    print(output)


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:REPORTING:CHANGE-CARDS:CLI">
if __name__ == "__main__":
    main()
