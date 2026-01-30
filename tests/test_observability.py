from codex_sandbox.observability import _redact_payload


def test_redact_payload_scrubs_sensitive_keys() -> None:
    payload = {
        "Authorization": "secret-token",
        "nested": {"api_key": "abc", "value": 1},
        "safe": "ok",
    }
    redacted = _redact_payload(payload)
    assert redacted["Authorization"] == "[redacted]"
    assert redacted["nested"]["api_key"] == "[redacted]"
    assert redacted["safe"] == "ok"
