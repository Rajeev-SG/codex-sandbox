# Level
Level 1

# Applications
1. . - Minimal sandbox repository intended for experimenting with OpenAI Codex Cloud workflows (delegation, PRs) while AFK.

# Criteria

**Style & Validation**
- Linter configured (lint_config): 1/1 - Ruff, pylint, radon, deptry, and vulture configured via Makefile/pyproject.
- Type checker (type_check): 1/1 - mypy strict configuration in pyproject.
- Formatter (formatter): 1/1 - black configured and ruff auto-fix enabled via pre-commit.
- Pre-commit hooks (pre_commit_hooks): 1/1 - pre-commit config includes merge conflict/large file/security checks.
- Strict typing enabled (strict_typing): 1/1 - mypy strict=true.
- Naming consistency (naming_consistency): 1/1 - Ruff naming rules enabled (N) in pyproject.
- Cyclomatic complexity (cyclomatic_complexity): 1/1 - radon cc configured in Makefile.
- Large file detection (large_file_detection): 1/1 - pre-commit check-added-large-files hook configured.
- Dead code detection (dead_code_detection): 1/1 - vulture configured in Makefile.
- Duplicate code detection (duplicate_code_detection): 1/1 - pylint R0801 enabled in Makefile.
- Code modularization (code_modularization): 1/1 - src package layout with separate modules and tests.
- Tech debt tracking (tech_debt_tracking): 1/1 - check_todos script enforced during lint.
- N+1 detection (n_plus_one_detection): null/1 - Skipped: no DB/ORM app present.
- Heavy dependency detection (heavy_dependency_detection): null/1 - Skipped: no bundled app/deps to analyze.
- Unused dependencies detection (unused_dependencies_detection): 1/1 - deptry configured.
- Version drift detection (version_drift_detection): 1/1 - Dependabot configuration present.
- Code quality metrics tracked (code_quality_metrics): null/1 - Skipped: no external quality dashboard configured.

**Build System**
- Build command documented (build_cmd_doc): 1/1 - README documents Makefile setup and verification commands.
- Dependencies pinned (deps_pinned): 1/1 - requirements files pin dependency versions.
- Single command setup (single_command_setup): 1/1 - make setup.
- Monorepo tooling (monorepo_tooling): null/1 - Skipped: not a monorepo.
- Release automation (release_automation): 1/1 - release-please workflow configured.
- Release notes automation (release_notes_automation): 1/1 - release-please config present.
- Build performance tracking (build_performance_tracking): null/1 - Skipped: no CI/build telemetry integration.
- Deployment frequency (deployment_frequency): null/1 - Skipped: no deploy workflows/releases present.
- Progressive rollout (progressive_rollout): null/1 - Skipped: not an infra/deploy repo.
- Rollback automation (rollback_automation): null/1 - Skipped: not an infra/deploy repo.
- Feature flag infrastructure (feature_flag_infrastructure): 1/1 - feature flag registry and docs present.
- Dead feature flag detection (dead_feature_flag_detection): 0/1 - No automated cleanup detection (docs/registry checks only).

**Testing**
- Unit tests present (unit_tests_exist): 1/1 - pytest tests under tests/.
- Integration tests present (integration_tests_exist): 1/1 - integration tests under tests/integration.
- Tests runnable locally (unit_tests_runnable): 1/1 - make test/coverage targets available.
- Test performance tracking (test_performance_tracking): 1/1 - pytest durations enabled in make coverage.
- Flaky test detection (flaky_test_detection): null/1 - Skipped: no flaky tooling configured.
- Test coverage thresholds (test_coverage_thresholds): 1/1 - coverage fail_under=85 configured.
- Test naming conventions (test_naming_conventions): 1/1 - pytest config enforces test_*.py.
- Test isolation (test_isolation): 1/1 - pytest-xdist parallel execution enabled.
- API schema docs (api_schema_docs): null/1 - Skipped: no API app present.
- Database schema (database_schema): null/1 - Skipped: no database app present.
- Health checks (health_checks): null/1 - Skipped: no deployed service/runtime.
- Circuit breakers (circuit_breakers): null/1 - Skipped: no external calls/app code.
- DAST scanning (dast_scanning): null/1 - Skipped: no web service/CI pipeline.

**Documentation**
- AGENTS.md exists (agents_md): 1/1 - AGENTS.md present at repo root.
- README exists (readme): 1/1 - README.md present with purpose and workflow.
- Automated doc generation (automated_doc_generation): 1/1 - MkDocs config + make docs target.
- Skills configured (skills): 1/1 - skills/ directory present.
- Documentation freshness (documentation_freshness): 1/1 - README updated within last 180 days.
- Service flow documented (service_flow_documented): 1/1 - docs/architecture.md present.
- AGENTS.md validation (agents_md_validation): 1/1 - validate_agents_md.py enforced in lint.
- Runbooks documented (runbooks_documented): 1/1 - docs/runbooks.md present.
- Deployment observability (deployment_observability): 1/1 - docs/observability.md present.

**Dev Environment**
- Devcontainer configured (devcontainer): 1/1 - .devcontainer/devcontainer.json present.
- Env template (env_template): 1/1 - .env.example present.
- Local services setup (local_services_setup): null/1 - Skipped: no external services indicated.
- Devcontainer runnable (devcontainer_runnable): null/1 - Skipped: devcontainer CLI not validated.

**Debugging & Observability**
- Structured logging (structured_logging): 1/1 - structured logging with redaction helpers.
- Distributed tracing (distributed_tracing): 1/1 - OpenTelemetry hooks available.
- Metrics collection (metrics_collection): 1/1 - Prometheus metrics hooks available.
- Error tracking contextualized (error_tracking_contextualized): 1/1 - Sentry hook configuration present.
- Alerting configured (alerting_configured): 0/1 - Requires configuring alerting in Sentry/PostHog.
- Profiling instrumentation (profiling_instrumentation): null/1 - Skipped: no profiling setup.
- Log scrubbing (log_scrubbing): 1/1 - redacting log filter included.
- Product analytics instrumentation (product_analytics_instrumentation): 1/1 - PostHog hooks available.
- Error to insight pipeline (error_to_insight_pipeline): 1/1 - docs describe Sentry → GitHub issue integration.

**Security**
- VCS CLI tools available (vcs_cli_tools): 1/1 - gh is installed and can query repo APIs.
- Automated PR review generation (automated_pr_review): 1/1 - reviewdog workflow and CodeRabbit config present.
- Agentic development detected (agentic_development): 1/1 - AGENTS.md and skills documentation present.
- Branch protection (branch_protection): 0/1 - Requires enabling branch protection in repo settings.
- Secret scanning configured (secret_scanning): 0/1 - Requires confirming secret scanning/push protection in repo settings.
- CODEOWNERS exists (codeowners): 1/1 - CODEOWNERS file present.
- Automated security review generation (automated_security_review): 1/1 - CodeQL workflow configured.
- Dependency update automation (dependency_update_automation): 1/1 - Dependabot configuration present.
- Gitignore comprehensive (gitignore_comprehensive): 1/1 - .gitignore present.
- Privacy compliance (privacy_compliance): null/1 - Skipped: no end-user data surface identified.
- Secrets management (secrets_management): 1/1 - docs/secrets.md present.
- Issue templates (issue_templates): 1/1 - .github/ISSUE_TEMPLATE present.
- Issue labeling system (issue_labeling_system): 1/1 - labels workflow/config present.
- Backlog health (backlog_health): null/1 - Skipped: no open issues to evaluate.
- PR templates (pr_templates): 1/1 - PR template present.
- PII handling (pii_handling): null/1 - Skipped: no PII-processing app identified.

# Action Items
- Enable branch protection rules for `main` with required status checks.
- Confirm secret scanning and push protection are enabled in GitHub security settings.
- Configure alerting rules in Sentry/PostHog if you enable those integrations.
