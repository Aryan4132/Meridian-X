"""
Webcam & Mic Access Guard (SEC-40)
Heuristic scan of running processes for camera/microphone-indicative names.

NOTE: per-handle hardware locks (which process holds the camera device open)
require OS driver queries unavailable to portable Python — this tool reports a
real process-name heuristic plus an honest capability caveat, never a
fabricated "0 processes" verdict.
"""

import time
from typing import Dict, Any, List

_FLAG_KEYWORDS = (
    "camera", "webcam", "obs", "zoom", "teams", "meet", "skype",
    "discord", "mic", "microphone", "audio", "voice", "recorder",
    "stream", "capture",
)


def audit_camera_mic_access() -> str:
    """
    Scan running processes for camera/microphone-indicative names and report.
    """
    total = 0
    suspects: List[str] = []
    scan_error = ""
    try:
        import psutil
        for proc in psutil.process_iter(["pid", "name", "exe", "cmdline"]):
            total += 1
            try:
                info = proc.info
                blob = " ".join([
                    str(info.get("name") or ""),
                    str(info.get("exe") or ""),
                    " ".join(info.get("cmdline") or []),
                ]).lower()
            except Exception:
                continue
            if any(k in blob for k in _FLAG_KEYWORDS):
                suspects.append(f"PID {info.get('pid')}: {info.get('name') or '?'}")
    except ImportError:
        scan_error = "psutil not installed — process scan unavailable."
    except Exception as e:
        scan_error = f"Process scan failed: {e}"

    lines = [
        "Cam & Mic Access Guard Status:",
        f"- Processes Scanned: {total} at {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Media-Indicative Processes: {len(suspects)}",
    ]
    lines.extend(f"  * {s}" for s in suspects[:15])
    if scan_error:
        lines.append(f"- Scan Note: {scan_error}")
    lines.append(
        "- Capability Note: heuristic process-name scan only — per-handle "
        "hardware locks need OS driver queries. Treat hits as review leads, "
        "not proof of active recording."
    )
    return "\n".join(lines)
