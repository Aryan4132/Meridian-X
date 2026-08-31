"""
fim_sentinel.py — Ransomware Canary & File Integrity Watcher (SEC-31)
Deploys honeypot canary files in critical user paths, records baseline SHA-256 hashes,
and detects mass modification/rename/encryption tripwires to trigger instant process quarantine.
"""

import os
import hashlib
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger("meridian_fim_sentinel")

_CANARY_REGISTRY: Dict[str, str] = {} # {path: sha256_hash}
_CANARY_FILENAMES = [
    ".meridian_canary_financial_data.xlsx",
    ".meridian_canary_passwords_backup.kdbx",
    ".meridian_canary_confidential_plan.docx"
]
_CANARY_CONTENT = b"CRITICAL_SYSTEM_CANARY_HONEYPOT_DATA_MERIDIAN_X_SEC_31_DO_NOT_MODIFY"

def _compute_sha256(path: str) -> Optional[str]:
    """Computes SHA-256 hash of a file."""
    if not os.path.exists(path):
        return None
    try:
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def deploy_canaries(target_directories: Optional[List[str]] = None) -> List[str]:
    """
    Deploys honey-pot canary files into specified directories or default workspace roots.
    Records baseline SHA-256 hashes in memory registry.
    """
    global _CANARY_REGISTRY
    if target_directories is None:
        user_home = os.path.expanduser("~")
        target_directories = [
            os.path.join(user_home, "Documents"),
            os.path.join(user_home, "Desktop"),
            os.getcwd()
        ]

    deployed = []
    for directory in target_directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok=True)
            except Exception:
                continue

        for filename in _CANARY_FILENAMES:
            canary_path = os.path.join(directory, filename)
            try:
                if not os.path.exists(canary_path):
                    with open(canary_path, "wb") as f:
                        f.write(_CANARY_CONTENT)

                file_hash = _compute_sha256(canary_path)
                if file_hash:
                    _CANARY_REGISTRY[canary_path] = file_hash
                    deployed.append(canary_path)
            except Exception as e:
                logger.error(f"[FIM Sentinel] Failed to deploy canary at {canary_path}: {e}")

    logger.info(f"[FIM Sentinel] Deployed {len(deployed)} ransomware canary files.")
    return deployed

def check_canaries() -> Dict[str, Any]:
    """
    Scans all registered canary files.
    If hash mismatch, file rename, or file deletion is detected:
    Trips ransomware alert and invokes system defense isolate_rogue_processes.
    """
    global _CANARY_REGISTRY
    tampered_files = []
    missing_files = []

    for path, expected_hash in list(_CANARY_REGISTRY.items()):
        if not os.path.exists(path):
            missing_files.append(path)
        else:
            current_hash = _compute_sha256(path)
            if current_hash != expected_hash:
                tampered_files.append(path)

    total_violations = len(tampered_files) + len(missing_files)
    tripwire_triggered = total_violations > 0

    quarantined_pids = []
    if tripwire_triggered:
        logger.critical(
            f"[FIM Sentinel] RANSOMWARE TRIPWIRE TRIGGERED! "
            f"Tampered files: {len(tampered_files)}, Missing files: {len(missing_files)}"
        )
        try:
            from src.core.system_defense import isolate_rogue_processes
            quarantined_pids = isolate_rogue_processes(max_cpu_pct=50.0)
        except Exception as e:
            logger.error(f"[FIM Sentinel] Could not invoke process quarantine: {e}")

        try:
            from src.core.proactive import publish_nudge_sync
            publish_nudge_sync(
                nudge_type="ransomware_tripwire",
                title="🚨 Ransomware Canary Tripwire Alert!",
                message=f"Ransomware activity detected ({total_violations} canary files modified). Rogue processes quarantined.",
                action_hint="Inspect isolated processes",
                icon="🚨",
                mascot_state="alert"
            )
        except Exception:
            pass

    return {
        "tripwire_triggered": tripwire_triggered,
        "tampered_files": tampered_files,
        "missing_files": missing_files,
        "quarantined_pids": quarantined_pids,
        "total_canaries_checked": len(_CANARY_REGISTRY)
    }

def get_canary_registry() -> Dict[str, str]:
    """Returns copy of active canary baseline registry."""
    return dict(_CANARY_REGISTRY)
