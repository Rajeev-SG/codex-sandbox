# codex-sandbox

Sandbox repo for experimenting with **OpenAI Codex Cloud** while I’m AFK.

- **Codex Cloud**: OpenAI’s hosted “coding agent” environment that can read/edit/run code and propose changes back to a GitHub repo (often via PRs), so work can continue in the background.
- **AFK**: “Away From Keyboard” (i.e., I’m not actively watching/responding).

## What this repo is for

- Minimal, disposable workspace to validate Codex Cloud setup and workflows (auth, repo access, environment setup, background runs, PR creation, etc.).
- Safe place to try prompts/automation patterns without risking real projects.

## How to use (typical workflow)

1. Connect this repository in Codex web.
2. Create an issue describing a small task (e.g., “add a hello-world script”, “set up linting”, “refactor X”).
3. Delegate the task to Codex Cloud (via Codex web or GitHub integration, depending on your setup).
4. Review the resulting PR/diff locally before merging.

## Notes / conventions

- Keep tasks small and reversible.
- Avoid putting secrets in this repo (API keys, tokens, `.env` files, etc.).
- If you add tooling, prefer lightweight scripts so environment setup stays fast.

## Agent readiness criteria (free tier features)

This repo now includes a lightweight, fully free toolchain to satisfy the
agent readiness criteria. Most checks are automated via `make` targets and CI,
but a few require manual configuration in GitHub settings.

### Local setup

```bash
make setup
```

### Quality gates (automated)

Run these locally or rely on CI:

```bash
make lint       # ruff, pylint (dup detection), deptry, vulture, docs checks
make typecheck  # mypy (strict)
make coverage   # pytest + coverage threshold + performance durations
make docs       # mkdocs build
```

### Pre-commit hooks

Install hooks after setup:

```bash
pre-commit install
```

### Observability scaffolding (optional services)

Enable features through `.env` (copy from `.env.example`):

- **Structured logging**: set `CODEX_FEATURE_STRUCTURED_LOGGING=true`.
- **Metrics**: set `CODEX_FEATURE_METRICS=true` and install `prometheus-client`.
- **Tracing**: set `CODEX_FEATURE_TRACING=true` and install OpenTelemetry SDK.
- **Error tracking**: set `CODEX_FEATURE_ERROR_TRACKING=true` and `SENTRY_DSN=...`.
- **Product analytics**: set `CODEX_FEATURE_PRODUCT_ANALYTICS=true` and
  `POSTHOG_API_KEY=...`.

If you want to enable Sentry or PostHog, create free-tier accounts and provision
API keys/DSNs in those services before setting the env vars above.

### Documentation and runbooks

Documentation builds are automated via MkDocs (`make docs`). The docs live under
`docs/` and include architecture, runbooks, observability guidance, secrets
management, and feature flag documentation.

### Manual GitHub configuration (one-time)

These items cannot be fully automated from within the repo but are free to
enable:

- **Branch protection rules**: protect `main` with required status checks
  (`CI`, `CodeQL`, `Reviewdog`).
- **Secret scanning & push protection**: ensure both are enabled in the repo
  security settings.
- **Label sync**: run the “Sync labels” workflow once to create labels.
- **Release automation**: ensure GitHub Actions is allowed to create PRs; the
  `Release Please` workflow manages release notes.
- **Dependabot**: enable Dependabot updates in the repo settings so the
  configuration can run.

### Skills

Sample skills live under `skills/`. Replace them with real Codex skills as
needed.

## References

- Codex docs overview: https://platform.openai.com/docs/codex/overview
- Codex Cloud environments: https://developers.openai.com/codex/cloud/environments
- GitHub integration (tagging `@codex`): https://developers.openai.com/codex/integrations/github
