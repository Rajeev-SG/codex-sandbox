"""Feature flag utilities with environment-based toggles."""
from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class FeatureFlag:
    name: str
    description: str
    env_var: str


REGISTERED_FLAGS: tuple[FeatureFlag, ...] = (
    FeatureFlag(
        name="structured_logging",
        description="Emit JSON structured logs for observability.",
        env_var="CODEX_FEATURE_STRUCTURED_LOGGING",
    ),
    FeatureFlag(
        name="metrics",
        description="Expose Prometheus-compatible metrics.",
        env_var="CODEX_FEATURE_METRICS",
    ),
    FeatureFlag(
        name="tracing",
        description="Enable OpenTelemetry tracing instrumentation.",
        env_var="CODEX_FEATURE_TRACING",
    ),
    FeatureFlag(
        name="error_tracking",
        description="Enable Sentry error tracking.",
        env_var="CODEX_FEATURE_ERROR_TRACKING",
    ),
    FeatureFlag(
        name="product_analytics",
        description="Enable PostHog product analytics.",
        env_var="CODEX_FEATURE_PRODUCT_ANALYTICS",
    ),
)


def is_feature_enabled(flag_name: str) -> bool:
    """Return True when a feature flag env var is set to a truthy value."""
    flag = next((item for item in REGISTERED_FLAGS if item.name == flag_name), None)
    if flag is None:
        raise ValueError(f"Unknown feature flag: {flag_name}")
    value = os.getenv(flag.env_var, "").strip().lower()
    return value in {"1", "true", "yes", "on"}
