import os
import pytest

from codex_sandbox.feature_flags import REGISTERED_FLAGS, is_feature_enabled


def test_feature_flags_are_unique() -> None:
    names = [flag.name for flag in REGISTERED_FLAGS]
    assert len(names) == len(set(names))


def test_is_feature_enabled_reads_env(monkeypatch: pytest.MonkeyPatch) -> None:
    flag = REGISTERED_FLAGS[0]
    monkeypatch.setenv(flag.env_var, "true")
    assert is_feature_enabled(flag.name) is True

    monkeypatch.setenv(flag.env_var, "no")
    assert is_feature_enabled(flag.name) is False


def test_is_feature_enabled_unknown() -> None:
    with pytest.raises(ValueError):
        is_feature_enabled("does-not-exist")
