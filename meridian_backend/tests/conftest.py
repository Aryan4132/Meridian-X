"""Shared pytest fixtures for Meridian-X backend tests.

FIX: previously every test file hand-rolled sys.path insertion and data-dir
env setup in setUpClass without restoring state, causing cross-test leakage
and execution-order dependence. This conftest centralizes that once per run.
"""
import os
import sys
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
