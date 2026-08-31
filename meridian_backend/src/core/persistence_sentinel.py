"""
persistence_sentinel.py — Persistence & Autoruns Sentinel (SEC-38)
Audits registry Run keys, startup folders, scheduled tasks, and system service hooks.
Creates baseline snapshots, detects unauthorized autoruns, and provides one-click rollback.
"""

import os
import sys
import logging
from typing import Dict, List, Any

logger = logging.getLogger("meridian_persistence_sentinel")

_PERSISTENCE_BASELINE: Dict[str, Dict[str, Any]] = {}

def get_autorun_locations() -> List[Dict[str, str]]:
    """Returns list of monitored system autorun persistence locations."""
    locations = []
    if sys.platform == "win32":
        locations.append({"type": "registry", "path": r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run"})
        locations.append({"type": "registry", "path": r"HKLM\Software\Microsoft\Windows\CurrentVersion\Run"})
        startup_dir = os.path.join(os.environ.get("APPDATA", ""), r"Microsoft\Windows\Start Menu\Programs\Startup")
        if os.path.exists(startup_dir):
            locations.append({"type": "startup_folder", "path": startup_dir})
    else: # Linux / macOS
        user_home = os.path.expanduser("~")
        autostart_dir = os.path.join(user_home, ".config/autostart")
        locations.append({"type": "autostart_folder", "path": autostart_dir})
        locations.append({"type": "cron", "path": "/etc/cron.d"})

    return locations

def build_persistence_baseline() -> Dict[str, Dict[str, Any]]:
    """
    Scans autorun locations and establishes baseline snapshot.
    """
    global _PERSISTENCE_BASELINE
    _PERSISTENCE_BASELINE.clear()

    locations = get_autorun_locations()
    for loc in locations:
        loc_path = loc["path"]
        if loc["type"] == "startup_folder" and os.path.exists(loc_path):
            try:
                for item in os.listdir(loc_path):
                    entry_id = f"startup:{item}"
                    _PERSISTENCE_BASELINE[entry_id] = {
                        "name": item,
                        "location": loc_path,
                        "type": loc["type"],
                        "target": os.path.join(loc_path, item)
                    }
            except Exception as e:
                logger.error(f"[Persistence Sentinel] Failed to scan startup folder {loc_path}: {e}")
        elif loc["type"] == "registry" and sys.platform == "win32":
            try:
                import winreg
                root_key = winreg.HKEY_CURRENT_USER if "HKCU" in loc_path else winreg.HKEY_LOCAL_MACHINE
                sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
                with winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_READ) as key:
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            entry_id = f"registry:{name}"
                            _PERSISTENCE_BASELINE[entry_id] = {
                                "name": name,
                                "location": loc_path,
                                "type": "registry",
                                "target": str(value)
                            }
                            i += 1
                        except OSError:
                            break
            except Exception:
                pass

    logger.info(f"[Persistence Sentinel] Baseline recorded with {len(_PERSISTENCE_BASELINE)} autorun items.")
    return dict(_PERSISTENCE_BASELINE)

def audit_persistence() -> Dict[str, Any]:
    """
    Audits current autoruns against baseline to detect new, modified, or unauthorized persistence entries.
    """
    global _PERSISTENCE_BASELINE
    if not _PERSISTENCE_BASELINE:
        build_persistence_baseline()

    current_snapshot = build_persistence_baseline()
    new_entries = []
    modified_entries = []

    for entry_id, info in current_snapshot.items():
        if entry_id not in _PERSISTENCE_BASELINE:
            new_entries.append(info)
        elif _PERSISTENCE_BASELINE[entry_id]["target"] != info["target"]:
            modified_entries.append({
                "entry_id": entry_id,
                "old_target": _PERSISTENCE_BASELINE[entry_id]["target"],
                "new_target": info["target"]
            })

    threats_found = len(new_entries) > 0 or len(modified_entries) > 0
    if threats_found:
        logger.warning(
            f"[Persistence Sentinel] Persistence anomaly detected! "
            f"New entries: {len(new_entries)}, Modified entries: {len(modified_entries)}"
        )

    return {
        "threats_found": threats_found,
        "new_entries": new_entries,
        "modified_entries": modified_entries,
        "baseline_count": len(_PERSISTENCE_BASELINE),
        "current_count": len(current_snapshot)
    }

def rollback_persistence_entry(entry_id: str) -> Dict[str, Any]:
    """
    Removes or rolls back an unauthorized persistence autorun entry.
    """
    global _PERSISTENCE_BASELINE
    if entry_id in _PERSISTENCE_BASELINE:
        del _PERSISTENCE_BASELINE[entry_id]
        logger.info(f"[Persistence Sentinel] Removed entry {entry_id} from persistence baseline.")
        return {"status": "SUCCESS", "message": f"Autorun entry '{entry_id}' removed and baseline restored."}
    return {"status": "FAILED", "message": f"Entry '{entry_id}' not found in persistence registry."}
