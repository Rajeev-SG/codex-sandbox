"""Ensure registered feature flags are documented."""
from __future__ import annotations

import pathlib

from codex_sandbox.feature_flags import REGISTERED_FLAGS


ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_FILE = ROOT / "docs" / "feature_flags.md"
ENV_FILE = ROOT / ".env.example"


def main() -> int:
    if not DOCS_FILE.exists():
        raise SystemExit("docs/feature_flags.md is missing")
    content = DOCS_FILE.read_text(encoding="utf-8")
    env_content = ENV_FILE.read_text(encoding="utf-8") if ENV_FILE.exists() else ""
    missing_docs = [flag.name for flag in REGISTERED_FLAGS if flag.name not in content]
    missing_env = [
        flag.env_var for flag in REGISTERED_FLAGS if flag.env_var not in env_content
    ]
    if missing_docs:
        raise SystemExit(f"Feature flags missing from docs: {', '.join(missing_docs)}")
    if missing_env:
        raise SystemExit(
            \"Feature flag env vars missing from .env.example: \"\n            + \", \".join(missing_env)\n+        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
