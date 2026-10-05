import os
import json
import pytest
from src.core.atomic_storage import atomic_write_json, safe_load_json


def test_atomic_write_and_safe_load(tmp_path):
    target = str(tmp_path / "test_data.json")
    payload = {"status": "ok", "items": [1, 2, 3], "unicode": "こんにちは"}

    res = atomic_write_json(target, payload)
    assert res is True
    assert os.path.exists(target)

    loaded = safe_load_json(target)
    assert loaded == payload


def test_safe_load_nonexistent(tmp_path):
    target = str(tmp_path / "does_not_exist.json")
    res = safe_load_json(target, default={"default": True})
    assert res == {"default": True}


def test_safe_load_corrupted_file(tmp_path):
    target = str(tmp_path / "corrupt.json")
    with open(target, "w", encoding="utf-8") as f:
        f.write("{ invalid json ...")

    res = safe_load_json(target, default=[])
    assert res == []


def test_atomic_write_overwrites_existing(tmp_path):
    target = str(tmp_path / "replace.json")
    atomic_write_json(target, {"version": 1})
    assert safe_load_json(target)["version"] == 1

    atomic_write_json(target, {"version": 2})
    assert safe_load_json(target)["version"] == 2
