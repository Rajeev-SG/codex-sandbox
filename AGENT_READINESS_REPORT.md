# Level
Level 1

# Applications
1. . - Minimal sandbox repository intended for experimenting with OpenAI Codex Cloud workflows (delegation, PRs) while AFK.

# Criteria

**Style & Validation**
- Linter configured (lint_config): 0/1 - No linter config present.
- Type checker (type_check): 0/1 - No type-check config present.
- Formatter (formatter): 0/1 - No formatter config present.
- Pre-commit hooks (pre_commit_hooks): 0/1 - No pre-commit hook tooling found.
- Strict typing enabled (strict_typing): null/1 - Skipped: no typed language/tooling to evaluate.
- Naming consistency (naming_consistency): 0/1 - No enforced naming conventions found.
- Cyclomatic complexity (cyclomatic_complexity): 0/1 - No complexity analysis tooling found.
- Large file detection (large_file_detection): 0/1 - No hooks/CI/LFS rules for large files found.
- Dead code detection (dead_code_detection): 0/1 - No unused/dead code tooling found.
- Duplicate code detection (duplicate_code_detection): 0/1 - No duplication detection tooling found.
- Code modularization (code_modularization): null/1 - Skipped: no meaningful module structure/tooling in minimal repo.
- Tech debt tracking (tech_debt_tracking): 0/1 - No tech-debt tracking automation found.
- N+1 detection (n_plus_one_detection): null/1 - Skipped: no DB/ORM app present.
- Heavy dependency detection (heavy_dependency_detection): null/1 - Skipped: no bundled app/deps to analyze.
- Unused dependencies detection (unused_dependencies_detection): 0/1 - No unused-deps tooling and no dependency manifests.
- Version drift detection (version_drift_detection): null/1 - Skipped: not a monorepo.
- Code quality metrics tracked (code_quality_metrics): null/1 - Skipped: no CI/quality platform evidence.

**Build System**
- Build command documented (build_cmd_doc): 0/1 - README does not document build commands; no build system detected.
- Dependencies pinned (deps_pinned): 0/1 - No lockfiles or pinned dependency manifests found.
- Single command setup (single_command_setup): 0/1 - No single setup/run command sequence documented.
- Monorepo tooling (monorepo_tooling): null/1 - Skipped: not a monorepo.
- Release automation (release_automation): 0/1 - No release/deploy automation found.
- Release notes automation (release_notes_automation): 0/1 - No changelog/release-notes automation found.
- Build performance tracking (build_performance_tracking): null/1 - Skipped: no CI/build runs to analyze.
- Deployment frequency (deployment_frequency): null/1 - Skipped: no deploy workflows/releases present.
- Progressive rollout (progressive_rollout): null/1 - Skipped: not an infra/deploy repo.
- Rollback automation (rollback_automation): null/1 - Skipped: not an infra/deploy repo.
- Feature flag infrastructure (feature_flag_infrastructure): 0/1 - No feature flag system configured.
- Dead feature flag detection (dead_feature_flag_detection): null/1 - Skipped: prerequisite feature_flag_infrastructure not present.

**Testing**
- Unit tests present (unit_tests_exist): 0/1 - No tests found.
- Integration tests present (integration_tests_exist): 0/1 - No integration/E2E test setup found.
- Tests runnable locally (unit_tests_runnable): 0/1 - No test runner/scripts found.
- Test performance tracking (test_performance_tracking): 0/1 - No timing/analytics for tests.
- Flaky test detection (flaky_test_detection): null/1 - Skipped: no CI/test history or flaky tooling.
- Test coverage thresholds (test_coverage_thresholds): 0/1 - No coverage tooling/thresholds configured.
- Test naming conventions (test_naming_conventions): 0/1 - No test framework config or tests present.
- Test isolation (test_isolation): 0/1 - No isolation/parallel config; no tests.
- API schema docs (api_schema_docs): null/1 - Skipped: no API app present.
- Database schema (database_schema): null/1 - Skipped: no database app present.
- Health checks (health_checks): null/1 - Skipped: no deployed service/runtime.
- Circuit breakers (circuit_breakers): null/1 - Skipped: no external calls/app code.
- DAST scanning (dast_scanning): null/1 - Skipped: no web service/CI pipeline.

**Documentation**
- AGENTS.md exists (agents_md): 0/1 - AGENTS.md not found at repo root.
- README exists (readme): 1/1 - README.md present with purpose and workflow.
- Automated doc generation (automated_doc_generation): 0/1 - No doc generation tooling/workflows found.
- Skills configured (skills): 0/1 - No skills directories found.
- Documentation freshness (documentation_freshness): 1/1 - README.md updated within last 180 days.
- Service flow documented (service_flow_documented): 0/1 - No architecture/service flow diagrams/docs found.
- AGENTS.md validation (agents_md_validation): 0/1 - AGENTS.md missing, so no validation automation.
- Runbooks documented (runbooks_documented): 0/1 - No runbooks or incident-playbook links found.
- Deployment observability (deployment_observability): 0/1 - No monitoring/deploy-impact references found.

**Dev Environment**
- Devcontainer configured (devcontainer): 0/1 - No .devcontainer/devcontainer.json found.
- Env template (env_template): 0/1 - No .env.example and no env var documentation.
- Local services setup (local_services_setup): null/1 - Skipped: no external services indicated.
- Devcontainer runnable (devcontainer_runnable): null/1 - Skipped: devcontainer missing and devcontainer CLI not installed.

**Debugging & Observability**
- Structured logging (structured_logging): 0/1 - No logging library/module present.
- Distributed tracing (distributed_tracing): 0/1 - No tracing/request-id evidence.
- Metrics collection (metrics_collection): 0/1 - No metrics/telemetry instrumentation found.
- Error tracking contextualized (error_tracking_contextualized): 0/1 - No Sentry/Bugsnag/Rollbar config found.
- Alerting configured (alerting_configured): 0/1 - No alerting/on-call tooling/config found.
- Profiling instrumentation (profiling_instrumentation): null/1 - Skipped: no runtime/APM/profiling setup.
- Log scrubbing (log_scrubbing): 0/1 - No log redaction/sanitization mechanisms found.
- Product analytics instrumentation (product_analytics_instrumentation): 0/1 - No analytics tooling found.
- Error to insight pipeline (error_to_insight_pipeline): 0/1 - No error-to-issue automation evidence.

**Security**
- VCS CLI tools available (vcs_cli_tools): 1/1 - gh is installed and can query repo APIs.
- Automated PR review generation (automated_pr_review): 0/1 - No PR review automation evidence; no PR history.
- Agentic development detected (agentic_development): 0/1 - No agent configs or agent co-authorship in git history.
- Branch protection (branch_protection): 0/1 - No rulesets; main branch protection reports “Branch not protected”.
- Secret scanning configured (secret_scanning): 1/1 - Secret scanning alerts endpoint is accessible (enabled); no alerts currently.
- CODEOWNERS exists (codeowners): 0/1 - No CODEOWNERS file found.
- Automated security review generation (automated_security_review): null/1 - Skipped: no analyses and API needs extra scopes; no other evidence.
- Dependency update automation (dependency_update_automation): 0/1 - No dependabot/renovate config found.
- Gitignore comprehensive (gitignore_comprehensive): 0/1 - No .gitignore found.
- Privacy compliance (privacy_compliance): null/1 - Skipped: no end-user data surface identified.
- Secrets management (secrets_management): 0/1 - No secrets management pattern evident.
- Issue templates (issue_templates): 0/1 - No .github/ISSUE_TEMPLATE found.
- Issue labeling system (issue_labeling_system): 0/1 - No labeling system evidence; no issues/labels present.
- Backlog health (backlog_health): null/1 - Skipped: no open issues to evaluate.
- PR templates (pr_templates): 0/1 - No PR template found.
- PII handling (pii_handling): null/1 - Skipped: no PII-processing app identified.

# Action Items
- Add `AGENTS.md` with exact setup/test commands you want Codex/agents to run.
- Add a basic `.gitignore` plus an `.env.example` if you expect env vars.
- Add a minimal CI workflow so Codex Cloud changes get automatic validation.

---
View the full report: https://app.factory.ai/analytics/readiness/https%253A%252F%252Fgithub.com%252Frajeev-sg%252Fcodex-sandbox

Note: I attempted to persist the report via `store_agent_readiness_report`, but the tool failed with `Fetch failed`, so the stored report may not be available yet.
