#!/usr/bin/env python3
# KEYWORDS: метрики, автоматизация, snapshot, когнитивная-нагрузка, журнал
# [ANCHOR:PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT]
# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT:MODULE">
"""Утилита для формирования полуавтоматического снимка метрик состояния.

Инструмент собирает объективные показатели (покрытие документации,
свежесть логов, задержку агрегации) и генерирует заготовку для субъективных
метрик когнитивной нагрузки, которые должен заполнить LLM-агент.

Скрипт не заменяет ручного ввода субъективных значений, но экономит время
на поиске численных данных и формирует JSON-заготовку для `docs/METRICS/logs/`.
"""
# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT:MODULE">

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


@dataclass
class MetricsSnapshot:
    """Хранит агрегированные данные для записи метрик."""

    session_id: str
    timestamp: dt.datetime
    metrics: Dict[str, Optional[float]]
    subjective_template: Dict[str, str]
    notes: str

    def to_json(self) -> str:
        """Сериализует снапшот в JSON-строку с ISO-датой."""

        payload = {
            "session_id": self.session_id,
            "timestamp": self.timestamp.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "metrics": self.metrics,
            "subjective": self.subjective_template,
            "notes": self.notes,
        }
        return json.dumps(payload, ensure_ascii=False)


# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT:IO">
def discover_markdown_files(base_paths: Iterable[Path]) -> List[Path]:
    """Возвращает список Markdown-файлов по заданным директориям."""

    files: List[Path] = []
    for base in base_paths:
        if not base.exists():
            continue
        files.extend(sorted(base.rglob("*.md")))
    return files


def calculate_anchor_coverage(files: List[Path]) -> Optional[float]:
    """Рассчитывает долю документов, содержащих Harmony-якоря."""

    if not files:
        return None
    with_anchor = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        if "[ANCHOR:" in text:
            with_anchor += 1
    return round(with_anchor / len(files), 3)


def compute_metrics_freshness(log_dir: Path, now: dt.datetime) -> Optional[float]:
    """Возвращает время в днях с момента последней записи логов метрик."""

    if not log_dir.exists():
        return None
    log_files = sorted(log_dir.glob("*.jsonl"))
    if not log_files:
        return None
    latest = max(log_files, key=lambda p: p.stat().st_mtime)
    latest_mtime = dt.datetime.fromtimestamp(latest.stat().st_mtime, tz=dt.timezone.utc)
    delta = now - latest_mtime
    return round(delta.total_seconds() / 86400, 3)


def compute_aggregation_lag(changes_dir: Path, latest_session: Optional[str]) -> Optional[float]:
    """Оценивает среднюю задержку агрегации по change-файлам human-friendly."""

    if not changes_dir.exists():
        return None
    change_files = sorted(changes_dir.glob("summary-changes-S*.md"))
    if not change_files:
        return 0.0
    session_numbers: List[int] = []
    for path in change_files:
        match = re.search(r"S(\d+)", path.stem)
        if match:
            session_numbers.append(int(match.group(1)))
    if not session_numbers:
        return None
    latest_number = int(latest_session[1:]) if latest_session else max(session_numbers)
    total_gap = sum(max(latest_number - number, 0) for number in session_numbers)
    return round(total_gap / len(session_numbers), 2)


def infer_latest_aggregated_session(summary_path: Path) -> Optional[str]:
    """Извлекает идентификатор последней агрегированной сессии из SUMMARY."""

    if not summary_path.exists():
        return None
    text = summary_path.read_text(encoding="utf-8")
    match = re.search(r"Последняя подтверждённая агрегация: \*\*(S\d+)\*\*", text)
    if match:
        return match.group(1)
    return None


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT:IO">

# <HARMONY:BEGIN name="PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT:CLI">
def build_snapshot(root: Path, session_id: str, notes: str) -> MetricsSnapshot:
    """Формирует снапшот метрик на основе состояния репозитория."""

    now = dt.datetime.now(tz=dt.timezone.utc)
    docs_dir = root / "docs"
    human_dir = root / "human-friendly"
    markdown_files = discover_markdown_files([docs_dir, human_dir])
    doc_coverage = calculate_anchor_coverage(markdown_files)

    logs_dir = docs_dir / "METRICS" / "logs"
    metrics_freshness = compute_metrics_freshness(logs_dir, now)

    summary_path = human_dir / "SUMMARY.md"
    latest_session = infer_latest_aggregated_session(summary_path)
    changes_dir = human_dir / "changes"
    aggregation_lag = compute_aggregation_lag(changes_dir, latest_session)

    metrics: Dict[str, Optional[float]] = {
        "M-DOC-COVERAGE": doc_coverage,
        "M-ROADMAP-HEALTH": None,
        "M-METRICS-FRESHNESS": metrics_freshness,
        "M-DOC-AGGREGATION-LAG": aggregation_lag,
        "M-CORE-CONTRACT": None,
        "M-PLUGIN-COVERAGE": None,
        "M-LLM-AVAILABILITY": None,
        "M-TEXT-REPLY-SATISFACTION": None,
        "M-RELEASE-HEALTH": None,
    }

    subjective_template = {
        "M-CONTEXT-LOAD": (
            "0:<50% лимита, без свёрток; 1:50-75%, ≤1 свёртка; 2:75-90%, единичная коррекция; "
            "3:>90% или ≥2 свёртки, но без потерь; 4:очистка после каждого шага и перенос ≥1 фрагмента; "
            "5:контекст разваливается, нужна перезагрузка."
        ),
        "M-NAVIGATION-CLARITY": (
            "0:>5 безрезультатных поисков подряд; 1:3-5 неудачных переходов; 2:1-2 цепочки с помехами; "
            "3:нахожу со второй попытки, ≤3 лишних шагов; 4:≤2 лишних перехода; 5:всё находится сразу."
        ),
        "M-NOISE-RATIO": (
            "0:<10% нерелевантных чтений; 1:10-25%; 2:25-40%; 3:40-60%; 4:60-80%; 5:>80%, прогресс стоит."
        ),
    }

    return MetricsSnapshot(
        session_id=session_id,
        timestamp=now,
        metrics=metrics,
        subjective_template=subjective_template,
        notes=notes,
    )


def parse_args() -> argparse.Namespace:
    """Разбирает аргументы командной строки."""

    parser = argparse.ArgumentParser(
        description=(
            "Собирает объективные метрики и формирует заготовку JSON для журнала состояния. "
            "Субъективные показатели (когнитивная нагрузка) необходимо заполнить вручную."
        )
    )
    parser.add_argument("--session-id", required=True, help="Идентификатор сессии (например, S007).")
    parser.add_argument("--notes", default="", help="Свободные заметки (добавляются в поле notes).")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Корень репозитория (по умолчанию вычисляется автоматически).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Путь до файла для сохранения результата. Если не указан, вывод в stdout.",
    )
    return parser.parse_args()


def main() -> None:
    """Точка входа CLI."""

    args = parse_args()
    snapshot = build_snapshot(args.root, args.session_id, args.notes)
    content = snapshot.to_json()
    if args.output:
        args.output.write_text(content + "\n", encoding="utf-8")
    else:
        print(content)


# <HARMONY:END name="PROJECT:TGBOT:SCRIPTS:METRICS:SNAPSHOT:CLI">
if __name__ == "__main__":
    main()
