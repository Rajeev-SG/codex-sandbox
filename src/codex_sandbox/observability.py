"""Observability helpers for the sandbox app."""
from __future__ import annotations

from dataclasses import dataclass
import json
import logging
import os
from typing import Any
import importlib.util

from codex_sandbox.feature_flags import is_feature_enabled


REDACT_KEYS = {"authorization", "token", "password", "api_key", "secret"}


class RedactingFilter(logging.Filter):
    """Redact sensitive fields from structured log payloads."""

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: D401
        if isinstance(record.msg, dict):
            record.msg = _redact_payload(record.msg)
        return True


def _redact_payload(payload: dict[str, Any]) -> dict[str, Any]:
    redacted: dict[str, Any] = {}
    for key, value in payload.items():
        if key.lower() in REDACT_KEYS:
            redacted[key] = "[redacted]"
        elif isinstance(value, dict):
            redacted[key] = _redact_payload(value)
        else:
            redacted[key] = value
    return redacted


class JsonFormatter(logging.Formatter):
    """Serialize log records as JSON for structured logging."""

    def format(self, record: logging.LogRecord) -> str:
        base = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            base["exception"] = self.formatException(record.exc_info)
        return json.dumps(base, default=str)


@dataclass(frozen=True)
class ObservabilityConfig:
    service_name: str
    environment: str
    enable_console_logs: bool = True
    sentry_dsn: str | None = None
    posthog_api_key: str | None = None
    posthog_host: str | None = None


@dataclass(frozen=True)
class MetricsHandles:
    request_counter: Any | None
    request_latency: Any | None


@dataclass(frozen=True)
class ObservabilityHandles:
    metrics: MetricsHandles


def configure_observability(config: ObservabilityConfig) -> ObservabilityHandles:
    """Configure logging, metrics, tracing, and error tracking."""
    _configure_logging(config)
    metrics = _configure_metrics(config)
    _configure_tracing(config)
    _configure_error_tracking(config)
    _configure_product_analytics(config)
    return ObservabilityHandles(metrics=metrics)


def _configure_logging(config: ObservabilityConfig) -> None:
    root = logging.getLogger()
    root.setLevel(os.getenv("LOG_LEVEL", "INFO"))
    handler = logging.StreamHandler()
    if is_feature_enabled("structured_logging"):
        handler.setFormatter(JsonFormatter())
        handler.addFilter(RedactingFilter())
    root.handlers = [handler] if config.enable_console_logs else []


def _configure_metrics(config: ObservabilityConfig) -> MetricsHandles:
    if not is_feature_enabled("metrics"):
        return MetricsHandles(request_counter=None, request_latency=None)

    if importlib.util.find_spec("prometheus_client") is None:
        return MetricsHandles(request_counter=None, request_latency=None)

    from prometheus_client import Counter, Histogram

    return MetricsHandles(
        request_counter=Counter(
            "codex_requests_total",
            "Total requests handled",
            ["service", "environment"],
        ),
        request_latency=Histogram(
            "codex_request_latency_seconds",
            "Latency for handled requests",
            ["service", "environment"],
        ),
    )


def _configure_tracing(config: ObservabilityConfig) -> None:
    if not is_feature_enabled("tracing"):
        return
    if importlib.util.find_spec("opentelemetry.sdk") is None:
        return

    from opentelemetry import trace
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.sdk.trace.export import ConsoleSpanExporter

    resource = Resource.create({"service.name": config.service_name})
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(provider)


def _configure_error_tracking(config: ObservabilityConfig) -> None:
    if not is_feature_enabled("error_tracking"):
        return
    if not config.sentry_dsn:
        return
    if importlib.util.find_spec("sentry_sdk") is None:
        return

    import sentry_sdk

    sentry_sdk.init(
        dsn=config.sentry_dsn,
        environment=config.environment,
        traces_sample_rate=0.1,
    )


def _configure_product_analytics(config: ObservabilityConfig) -> None:
    if not is_feature_enabled("product_analytics"):
        return
    if not config.posthog_api_key:
        return
    if importlib.util.find_spec("posthog") is None:
        return

    import posthog

    posthog.project_api_key = config.posthog_api_key
    if config.posthog_host:
        posthog.host = config.posthog_host
    posthog.debug = os.getenv("POSTHOG_DEBUG", "").lower() in {"1", "true", "yes"}
