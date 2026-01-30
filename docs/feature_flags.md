# Feature Flags

The sandbox uses environment-based feature flags. Enable a flag by setting the
corresponding environment variable to `true`, `1`, `yes`, or `on`.

| Flag | Env var | Description |
| --- | --- | --- |
| structured_logging | CODEX_FEATURE_STRUCTURED_LOGGING | Emit JSON structured logs. |
| metrics | CODEX_FEATURE_METRICS | Enable Prometheus metrics. |
| tracing | CODEX_FEATURE_TRACING | Enable OpenTelemetry tracing. |
| error_tracking | CODEX_FEATURE_ERROR_TRACKING | Enable Sentry error tracking. |
| product_analytics | CODEX_FEATURE_PRODUCT_ANALYTICS | Enable PostHog analytics. |
