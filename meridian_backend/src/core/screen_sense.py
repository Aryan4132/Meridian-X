"""
meridian_backend/src/core/screen_sense.py — PL-03 Production Backend Module
Real-Time Screen & Active Window Sense
"""

import os
import sys
import time
import asyncio
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("meridian_screen_sense")

_VISION_CACHE: Dict[str, Dict[str, Any]] = {}
_CACHE_TTL_SECONDS = 300


def get_active_window_metadata() -> Dict[str, Any]:
    """
    Cross-platform active window tracker returning metadata:
    { "title": str, "process": str, "pid": int, "path": str, "timestamp": float }
    """
    res = {
        "title": "Unknown Window",
        "process": "unknown",
        "pid": 0,
        "path": "",
        "timestamp": time.time()
    }
    
    # Windows
    if sys.platform == "win32":
        try:
            import ctypes
            user32 = ctypes.windll.user32
            hwnd = user32.GetForegroundWindow()
            if hwnd:
                length = user32.GetWindowTextLengthW(hwnd)
                buf = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buf, length + 1)
                res["title"] = buf.value or "Desktop/Unknown"

                pid = ctypes.c_ulong()
                user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                res["pid"] = pid.value
                if pid.value > 0:
                    try:
                        import psutil
                        proc = psutil.Process(pid.value)
                        res["process"] = proc.name()
                        res["path"] = proc.exe()
                    except Exception:
                        pass
                return res
        except Exception as exc:
            logger.debug("[ScreenSense] Windows active window capture error: %s", exc)

    # macOS
    elif sys.platform == "darwin":
        try:
            import subprocess
            cmd = 'tell application "System Events" to get name of first process whose frontmost is true'
            proc_name = subprocess.check_output(["osascript", "-e", cmd]).decode("utf-8").strip()
            title_cmd = 'tell application "System Events" to get name of front window of (first process whose frontmost is true)'
            win_title = subprocess.check_output(["osascript", "-e", title_cmd]).decode("utf-8").strip()
            res["process"] = proc_name or "darwin_app"
            res["title"] = win_title or proc_name
            return res
        except Exception as exc:
            logger.debug("[ScreenSense] macOS active window error: %s", exc)

    # Linux
    elif sys.platform.startswith("linux"):
        try:
            import subprocess
            win_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8").strip()
            win_name = subprocess.check_output(["xdotool", "getwindowname", win_id]).decode("utf-8").strip()
            res["title"] = win_name
            res["process"] = "linux_app"
            return res
        except Exception as exc:
            logger.debug("[ScreenSense] Linux active window error: %s", exc)

    return res


class ScreenSenseTracker:
    """Tracks active window transitions and handles visual LLM screen sense caching."""

    def __init__(self, cache_ttl: int = _CACHE_TTL_SECONDS):
        self.cache_ttl = cache_ttl
        self.last_window_key = ""

    def get_window_key(self, meta: Dict[str, Any]) -> str:
        return f"{meta.get('process', '')}:{meta.get('title', '')}"

    async def get_screen_sense(self, force_refresh: bool = False) -> Dict[str, Any]:
        """
        Fetches active window metadata and performs multimodal vision scan
        if window switched or cache expired.
        """
        from src.core.vision import analyze_screen_multimodal

        meta = get_active_window_metadata()
        key = self.get_window_key(meta)
        now = time.time()

        cached = _VISION_CACHE.get(key)
        if not force_refresh and cached and (now - cached.get("timestamp", 0) < self.cache_ttl):
            return {
                "active_window": meta,
                "vision": cached.get("vision"),
                "cached": True
            }

        vision_res = await analyze_screen_multimodal()
        _VISION_CACHE[key] = {
            "timestamp": now,
            "vision": vision_res
        }
        self.last_window_key = key

        return {
            "active_window": meta,
            "vision": vision_res,
            "cached": False
        }


_global_tracker = ScreenSenseTracker()


async def get_active_window_sense(force_refresh: bool = False) -> Dict[str, Any]:
    """Helper to get current active window & screen sense."""
    return await _global_tracker.get_screen_sense(force_refresh=force_refresh)
