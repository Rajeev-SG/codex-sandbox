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

## AI code review setup (free-tier friendly)

This repo is set up to work well with GitHub-based AI reviewers while keeping unnecessary runs to a minimum:

- Keep PRs in **draft** while you’re still iterating.
- Mark PRs **Ready for review** only when the diff is in a reviewable state.

### CodeRabbit

- Install the CodeRabbit GitHub App for this repository.
- Repo configuration is in `.coderabbit.yaml`.
  - Auto review is enabled.
  - Draft PRs are skipped.

Docs:
https://docs.coderabbit.ai/configure-coderabbit/

### Devin Review

- Connect GitHub in Devin: https://docs.devin.ai/integrations/gh
- Devin Review docs: https://docs.devin.ai/work-with-devin/devin-review

Notes:

- Auto-review runs when a PR is opened (non-draft), when new commits are pushed, when a draft is marked ready, or when an enrolled user is added as reviewer/assignee.
- Configure which repos/users are auto-reviewed in `app.devin.ai` under **Settings > Review**.
- Devin reads repo instruction files like `AGENTS.md`.

### Sentry Seer AI Code Review

- Enable the Sentry GitHub integration and Seer settings, then enable AI Code Review.
- AI Code Review can also be invoked via PR comments using `@sentry review`.

Important:

- Sentry’s docs indicate enabling Seer/AI features may start paid usage (active contributor pricing). Confirm what’s included in your Sentry plan before enabling in a production org.
- If you use branch protection, consider keeping Sentry’s AI Code Review check **optional** (to avoid blocking merges during service issues/timeouts).

Docs:
https://docs.sentry.io/product/ai-in-sentry/ai-code-review/

## References

- Codex docs overview: https://platform.openai.com/docs/codex/overview
- Codex Cloud environments: https://developers.openai.com/codex/cloud/environments
- GitHub integration (tagging `@codex`): https://developers.openai.com/codex/integrations/github
