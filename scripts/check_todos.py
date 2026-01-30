"""Fail if TODO/FIXME comments lack an issue reference."""
from __future__ import annotations

import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"\b(TODO|FIXME)\b(?!\(#[0-9]+\))")


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*.py"):
        if "/.venv/" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        for idx, line in enumerate(text.splitlines(), start=1):
            if PATTERN.search(line):
                failures.append(f"{path}:{idx}:{line.strip()}")
    if failures:
        message = "\n".join(failures)
        raise SystemExit(f"TODO/FIXME entries need issue references:\n{message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
