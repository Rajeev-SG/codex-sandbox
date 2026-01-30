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

## References

- Codex docs overview: https://platform.openai.com/docs/codex/overview
- Codex Cloud environments: https://developers.openai.com/codex/cloud/environments
- GitHub integration (tagging `@codex`): https://developers.openai.com/codex/integrations/github
