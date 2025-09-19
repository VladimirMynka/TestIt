#!/usr/bin/env python3
# KEYWORDS: навигация, контекст, документация, обзор, автоматизация
# [ANCHOR:PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR]
# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:MODULE">
"""Строит карту актуальных документов и подсвечивает потенциально устаревшие зоны.

Скрипт помогает LLM-агенту быстро понять, какие каталоги документации обновлялись
давно, и где стоит ожидать повышенную когнитивную нагрузку при поиске данных.
"""
# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:MODULE">

from __future__ import annotations

import argparse
import datetime as dt
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List


@dataclass
class SectionInfo:
    """Информация по логическому разделу документации."""

    name: str
    root: Path
    file_count: int
    anchor_ratio: float
    latest_update: dt.datetime
    stale_paths: List[str]

    def to_dict(self) -> Dict[str, object]:
        """Возвращает данные раздела в виде словаря."""

        return {
            "name": self.name,
            "path": str(self.root),
            "file_count": self.file_count,
            "anchor_ratio": round(self.anchor_ratio, 3),
            "latest_update": self.latest_update.isoformat().replace("+00:00", "Z"),
            "stale_files": self.stale_paths,
        }


# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:COLLECTORS">
def iter_markdown(path: Path) -> Iterable[Path]:
    """Возвращает Markdown-файлы раздела."""

    if not path.exists():
        return []
    return sorted(path.rglob("*.md"))


def compute_anchor_ratio(files: List[Path]) -> float:
    """Рассчитывает долю файлов с `[ANCHOR:`."""

    if not files:
        return 0.0
    hits = sum(1 for file in files if "[ANCHOR:" in file.read_text(encoding="utf-8"))
    return hits / len(files)


def detect_stale_files(files: List[Path], now: dt.datetime, stale_delta: dt.timedelta, limit: int) -> List[str]:
    """Определяет файлы, которые не обновлялись дольше заданного порога."""

    stale: List[Path] = []
    for file in files:
        mtime = dt.datetime.fromtimestamp(file.stat().st_mtime, tz=dt.timezone.utc)
        if now - mtime >= stale_delta:
            stale.append(file)
    stale_sorted = sorted(stale, key=lambda item: item.stat().st_mtime)[:limit]
    return [str(path) for path in stale_sorted]


def collect_section_info(name: str, root: Path, now: dt.datetime, stale_days: int, limit: int) -> SectionInfo:
    """Формирует агрегированную информацию по разделу."""

    files = list(iter_markdown(root))
    anchor_ratio = compute_anchor_ratio(files)
    if files:
        latest_mtime = max(f.stat().st_mtime for f in files)
        latest_update = dt.datetime.fromtimestamp(latest_mtime, tz=dt.timezone.utc)
    elif root.exists():
        latest_update = dt.datetime.fromtimestamp(root.stat().st_mtime, tz=dt.timezone.utc)
    else:
        latest_update = now
    stale_delta = dt.timedelta(days=stale_days)
    stale_paths = detect_stale_files(files, now, stale_delta, limit)
    return SectionInfo(
        name=name,
        root=root,
        file_count=len(files),
        anchor_ratio=anchor_ratio,
        latest_update=latest_update,
        stale_paths=stale_paths,
    )


def build_sections(root: Path, now: dt.datetime, stale_days: int, limit: int) -> List[SectionInfo]:
    """Собирает срез по основным каталогам документации."""

    mapping = {
        "Контракты": root / "docs" / "CONTRACTS",
        "Протоколы": root / "docs" / "PROTOCOLS",
        "Метрики": root / "docs" / "METRICS",
        "Roadmap": root / "docs" / "ROADMAP",
        "Human-friendly": root / "human-friendly",
    }
    sections: List[SectionInfo] = []
    for name, path in mapping.items():
        sections.append(collect_section_info(name, path, now, stale_days, limit))
    return sections


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:COLLECTORS">

# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:FORMATS">
def render_markdown(sections: List[SectionInfo]) -> str:
    """Создаёт Markdown-таблицу для отчёта."""

    header = "| Раздел | Файлы | Доля с якорями | Последнее обновление | Потенциально устаревшие |\n"
    header += "|--------|-------|----------------|-----------------------|-------------------------|\n"
    rows = []
    for section in sections:
        stale = "<br/>".join(section.stale_paths) if section.stale_paths else "—"
        rows.append(
            f"| {section.name} | {section.file_count} | {section.anchor_ratio:.2f} | "
            f"{section.latest_update.date()} | {stale} |"
        )
    return header + "\n".join(rows)


def render_json(sections: List[SectionInfo]) -> str:
    """Формирует JSON-представление."""

    payload = [section.to_dict() for section in sections]
    return json.dumps(payload, ensure_ascii=False, indent=2)


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:FORMATS">

# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:CLI">
def parse_args() -> argparse.Namespace:
    """Парсит аргументы CLI."""

    parser = argparse.ArgumentParser(
        description="Генерирует обзор документации с подсветкой потенциально устаревших файлов."
    )
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Формат вывода.")
    parser.add_argument("--stale-days", type=int, default=3, help="Порог устаревания файла в днях.")
    parser.add_argument("--limit", type=int, default=5, help="Максимальное число устаревших файлов в отчёте.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Корень репозитория (по умолчанию определяется автоматически).",
    )
    return parser.parse_args()


def main() -> None:
    """Точка входа сценария."""

    args = parse_args()
    now = dt.datetime.now(tz=dt.timezone.utc)
    sections = build_sections(args.root, now, args.stale_days, args.limit)
    if args.format == "markdown":
        output = render_markdown(sections)
    else:
        output = render_json(sections)
    print(output)


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:NAVIGATION:CONTEXT-RADAR:CLI">
if __name__ == "__main__":
    main()
