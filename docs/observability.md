# Observability

## Logging
- Enable structured logging by setting `CODEX_FEATURE_STRUCTURED_LOGGING=true`.
- Logs are emitted as JSON and redact common secrets.

## Metrics
- Enable metrics with `CODEX_FEATURE_METRICS=true`.
- `prometheus_client` exposes counters/histograms for requests.

## Tracing
- Enable tracing with `CODEX_FEATURE_TRACING=true`.
- OpenTelemetry uses a console exporter by default for development.

## Error tracking
- Enable Sentry with `CODEX_FEATURE_ERROR_TRACKING=true` and `SENTRY_DSN=...`.

## Product analytics
- Enable PostHog with `CODEX_FEATURE_PRODUCT_ANALYTICS=true` and `POSTHOG_API_KEY=...`.

## Alerting
Use Sentry or PostHog alerting rules (both have free tiers) to notify on
regressions once you configure the credentials.

## Error to insight pipeline
Connect Sentry to GitHub issues (Integrations → Issue Tracking) so new errors
can open or link to issues automatically.
