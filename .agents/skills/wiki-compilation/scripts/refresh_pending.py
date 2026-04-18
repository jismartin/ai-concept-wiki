#!/usr/bin/env python3
"""Refresh wiki/_pending.md from compilable files in raw/.

Behavior:
- Ensures wiki/_pending.md exists.
- Preserves entries already listed under ## Processed.
- Rebuilds ## Pending from compilable files currently present in raw/ that are not processed.
- Skips raw/originals/ because original long-form sources should be digested first.
- Includes raw/digests/ and legacy files directly under raw/.
- Keeps dates already recorded for processed files.
- Sorts file paths alphabetically for deterministic output.

Expected repository layout:
- raw/
- wiki/_pending.md

Usage:
    python refresh_pending.py
    python refresh_pending.py /path/to/repo
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

PENDING_HEADER = "## Pending"
PROCESSED_HEADER = "## Processed"
PROCESSED_LINE_RE = re.compile(r"^-\s+(?P<path>.+?)\s*[-—]\s*(?P<date>\d{4}-\d{2}-\d{2})\s*$")
BULLET_LINE_RE = re.compile(r"^-\s+(?P<path>.+?)\s*$")
IGNORED_NAMES = {".DS_Store", "Thumbs.db", "_source_registry.md"}


@dataclass
class PendingState:
    pending: list[str]
    processed: dict[str, str]


def normalize_relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def iter_raw_files(raw_dir: Path, root: Path) -> Iterable[str]:
    for path in sorted(raw_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.name in IGNORED_NAMES:
            continue
        rel_parts = path.relative_to(raw_dir).parts
        if rel_parts and rel_parts[0] == "originals":
            continue
        yield normalize_relpath(path, root)


def parse_pending_file(path: Path) -> PendingState:
    if not path.exists():
        return PendingState(pending=[], processed={})

    current_section: str | None = None
    pending: list[str] = []
    processed: dict[str, str] = {}

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line == PENDING_HEADER:
            current_section = "pending"
            continue
        if line == PROCESSED_HEADER:
            current_section = "processed"
            continue

        if current_section == "pending":
            match = BULLET_LINE_RE.match(line)
            if match:
                pending.append(match.group("path").strip())
        elif current_section == "processed":
            match = PROCESSED_LINE_RE.match(line)
            if match:
                processed[match.group("path").strip()] = match.group("date")
                continue
            match = BULLET_LINE_RE.match(line)
            if match:
                processed[match.group("path").strip()] = "unknown-date"

    return PendingState(pending=pending, processed=processed)


def build_pending_state(root: Path) -> PendingState:
    raw_dir = root / "raw"
    pending_file = root / "wiki" / "_pending.md"

    existing = parse_pending_file(pending_file)

    if not raw_dir.exists() or not raw_dir.is_dir():
        raise FileNotFoundError(f"Missing raw directory: {raw_dir}")

    raw_files = list(iter_raw_files(raw_dir, root))
    processed_paths = set(existing.processed.keys())
    pending = [p for p in raw_files if p not in processed_paths]

    return PendingState(pending=pending, processed=existing.processed)


def render_pending_md(state: PendingState) -> str:
    lines: list[str] = ["# Pending wiki processing", "", PENDING_HEADER]

    if state.pending:
        for relpath in state.pending:
            lines.append(f"- {relpath}")
    else:
        lines.append("<!-- empty -->")

    lines.extend(["", PROCESSED_HEADER])

    if state.processed:
        for relpath in sorted(state.processed):
            date = state.processed[relpath]
            if date == "unknown-date":
                lines.append(f"- {relpath}")
            else:
                lines.append(f"- {relpath} — {date}")
    else:
        lines.append("<!-- empty -->")

    lines.append("")
    return "\n".join(lines)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    pending_file = root / "wiki" / "_pending.md"

    try:
        state = build_pending_state(root)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    ensure_parent(pending_file)
    pending_file.write_text(render_pending_md(state), encoding="utf-8")

    print(f"Updated: {pending_file}")
    print(f"Pending: {len(state.pending)}")
    print(f"Processed: {len(state.processed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
