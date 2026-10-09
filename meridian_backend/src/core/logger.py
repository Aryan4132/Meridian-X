"""
meridian_backend/src/core/logger.py
Centralized structured logger for Meridian-X backend.
Provides consistent formatting, level management, and optional JSON output.
"""

import os
import sys
import json
import logging
from typing import Optional, Dict, Any

_LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class JSONFormatter(logging.Formatter):
    """JSON log formatter for production observability."""
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        if hasattr(record, "extra") and isinstance(record.extra, dict):
            payload.update(record.extra)
        return json.dumps(payload, ensure_ascii=False)


def get_logger(name: str = "meridian") -> logging.Logger:
    """
    Returns a configured logger instance with standard Meridian formatting.
    Ensures handlers are attached idempotently.
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if already configured
    if logger.handlers:
        return logger

    log_level_str = os.environ.get("MERIDIAN_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, log_level_str, logging.INFO)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    if os.environ.get("MERIDIAN_LOG_JSON", "0") in ("1", "true", "True"):
        handler.setFormatter(JSONFormatter(datefmt=_DATE_FORMAT))
    else:
        handler.setFormatter(logging.Formatter(_LOG_FORMAT, datefmt=_DATE_FORMAT))

    logger.addHandler(handler)
    logger.propagate = False
    return logger


def log_event(logger: logging.Logger, event_name: str, payload: Optional[Dict[str, Any]] = None, level: int = logging.INFO) -> None:
    """Helper to log structured events cleanly."""
    data = payload or {}
    logger.log(level, f"EVENT [{event_name}]: {json.dumps(data, ensure_ascii=False)}")


# Default global logger
logger = get_logger("meridian")
