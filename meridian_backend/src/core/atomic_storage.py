"""
atomic_storage.py — Crash-resilient atomic file read/write operations for Meridian-X.
Guarantees zero file corruption on abrupt system restarts, process kills, or power cuts.
"""

import os
import json
import tempfile
import logging
from typing import Any, Optional

logger = logging.getLogger("meridian.storage")


def atomic_write_json(filepath: str, data: Any, indent: int = 2) -> bool:
    """
    Atomically writes JSON-serializable data to target filepath.
    Writes to a temporary file in the same directory, flushes, syncs,
    and replaces the target file atomically.
    """
    dir_name = os.path.dirname(os.path.abspath(filepath))
    os.makedirs(dir_name, exist_ok=True)

    temp_path = None
    try:
        # Create temp file in same directory to ensure same filesystem for os.replace
        with tempfile.NamedTemporaryFile("w", dir=dir_name, delete=False, encoding="utf-8") as tf:
            temp_path = tf.name
            json.dump(data, tf, indent=indent, ensure_ascii=False)
            tf.flush()
            os.fsync(tf.fileno())

        # Atomically replace target file
        os.replace(temp_path, filepath)
        return True
    except Exception as e:
        logger.error(f"Failed atomic write to {filepath}: {e}", exc_info=True)
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass
        raise


def safe_load_json(filepath: str, default: Any = None) -> Any:
    """
    Safely reads JSON from target filepath.
    Returns `default` if file does not exist, is empty, or is corrupted.
    """
    if not os.path.exists(filepath):
        return default

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return default
            return json.loads(content)
    except Exception as e:
        logger.warning(f"Error reading JSON from {filepath}, using default: {e}")
        return default
