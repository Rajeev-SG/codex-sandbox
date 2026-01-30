from codex_sandbox.observability import ObservabilityConfig, configure_observability


def test_configure_observability_smoke() -> None:
    config = ObservabilityConfig(service_name="codex", environment="test")
    handles = configure_observability(config)
    assert handles.metrics.request_counter is None
