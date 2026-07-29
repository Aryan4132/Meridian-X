import pytest
import os
from database import get_auditor_model, get_model_source, get_brain_model
from src.core.loop import route_model_by_complexity

def test_get_model_source_default():
    # Verify get_model_source fallback to env var
    os.environ["MERIDIAN_MODEL_SOURCE"] = "cloud"
    try:
        assert get_model_source() == "cloud"
    finally:
        os.environ.pop("MERIDIAN_MODEL_SOURCE", None)

def test_get_auditor_model_fallback(monkeypatch):
    # Verify get_auditor_model falls back to brain model when auditor profile & env are not set
    monkeypatch.setattr("database.get_user_profile", lambda k: None)
    os.environ.pop("MERIDIAN_AUDITOR_MODEL", None)
    os.environ["MERIDIAN_MODEL"] = "test-brain-model"
    try:
        assert get_auditor_model() == "test-brain-model"
    finally:
        os.environ.pop("MERIDIAN_MODEL", None)

def test_route_model_by_complexity_cloud():
    # Verify cloud mode always returns active brain model
    res = route_model_by_complexity("refactor full application pipeline", "claude-3-5-sonnet", model_source="cloud")
    assert res == "claude-3-5-sonnet"
