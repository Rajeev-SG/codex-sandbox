"""Validate that AGENTS.md exists with required sections."""
from __future__ import annotations

import pathlib


REQUIRED_HEADINGS = {"## Setup", "## Testing"}
ROOT = pathlib.Path(__file__).resolve().parents[1]


def main() -> int:
    agents = ROOT / "AGENTS.md"
    if not agents.exists():
        raise SystemExit("AGENTS.md is missing.")
    content = agents.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in content]
    if missing:
        raise SystemExit(f"AGENTS.md missing sections: {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
