
# --- CI AUTO-PATCH: Headless Display & Mode Isolation ---
import os
import sys

os.environ["TESTING"] = "true"
os.environ["PYTEST_CURRENT_TEST"] = "1"
from unittest.mock import MagicMock
import pytest

# 1. Prevent mouseinfo / pyautogui from crashing on headless Linux without X11 DISPLAY
if sys.platform.startswith("linux"):
    if "DISPLAY" not in os.environ:
        os.environ["DISPLAY"] = ":99"
    sys.modules.setdefault("mouseinfo", MagicMock())
    try:
        import pyautogui
    except Exception:
        sys.modules["pyautogui"] = MagicMock()

@pytest.fixture(autouse=True)
def _ci_isolate_event_loop_and_state():
    yield
    # Reset airgap / local_only_mode so test_day9 doesn't pollute subsequent tests
    try:
        from src.core.mode import set_local_only_mode
        set_local_only_mode(False)
    except Exception:
        pass

"""Shared pytest fixtures for Meridian-X backend tests.

FIX: previously every test file hand-rolled sys.path insertion and data-dir
env setup in setUpClass without restoring state, causing cross-test leakage
and execution-order dependence. This conftest centralizes that once per run.
"""
import os
import sys

os.environ["TESTING"] = "true"
os.environ["PYTEST_CURRENT_TEST"] = "1"
import tempfile

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# Isolate all test writes (SQLite DBs, vault, vector indexes) in a temp dir
# BEFORE any meridian module is imported — src.core.config reads this at
# import time to derive DB_DIR / VAULT_FILE.
if not os.environ.get("MERIDIAN_DATA_DIR"):
    _tmp_data_dir = os.path.join(tempfile.gettempdir(), "meridian-test-data")
    os.makedirs(_tmp_data_dir, exist_ok=True)
    os.environ["MERIDIAN_DATA_DIR"] = _tmp_data_dir

# Keep unit tests hermetic: never auto-launch heavyweight daemons during tests.
os.environ.setdefault("DISABLE_AUTH", "false")
