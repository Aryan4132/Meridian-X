"""
updater.py — Self-Updater with Safe Swap & Health Probe Rollback (OPS-01)
Handles version check, release download, SHA256 checksum verification, binary swap, and 15s health probe auto-rollback.
"""

import os
import sys
import time
import shutil
import hashlib
import logging
import httpx
from typing import Dict, Any, Tuple, Optional

logger = logging.getLogger("meridian_updater")

CURRENT_VERSION = "0.1.4"
GITHUB_RELEASES_URL = "https://api.github.com/repos/Aryan4132/Meridian-X/releases/latest"


class SystemUpdater:
    """Automated self-updater with binary swap and health probe rollback."""

    def __init__(self, version: str = CURRENT_VERSION):
        self.current_version = version

    def check_for_updates(self) -> Dict[str, Any]:
        """Checks GitHub releases API or manifest for newer release tag."""
        try:
            res = httpx.get(GITHUB_RELEASES_URL, timeout=5.0, headers={"User-Agent": "Meridian-X-Updater"})
            if res.status_code == 200:
                data = res.json()
                tag_name = data.get("tag_name", "v0.1.0").lstrip("v")
                has_update = tag_name != self.current_version
                assets = data.get("assets", [])
                
                return {
                    "update_available": has_update,
                    "current_version": self.current_version,
                    "latest_version": tag_name,
                    "release_notes": data.get("body", "Bug fixes & stability improvements."),
                    "published_at": data.get("published_at"),
                    "assets": [{"name": a.get("name"), "url": a.get("browser_download_url")} for a in assets],
                }
        except Exception as e:
            logger.debug(f"[Updater] Release check network error: {e}")

        # Fallback offline status
        return {
            "update_available": False,
            "current_version": self.current_version,
            "latest_version": self.current_version,
            "release_notes": "Up to date.",
            "assets": [],
        }

    def verify_sha256(self, file_path: str, expected_sha256: str) -> bool:
        """Verifies SHA256 checksum of downloaded asset."""
        if not os.path.exists(file_path):
            return False
        h = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        calculated = h.hexdigest().lower()
        return calculated == expected_sha256.lower().strip()

    def safe_swap_binary(self, target_binary: str, new_binary: str) -> Tuple[bool, str]:
        """Backs up existing target binary to target.bak and replaces with new binary."""
        if not os.path.exists(new_binary):
            return False, "New binary asset file does not exist."

        backup_path = f"{target_binary}.bak"
        try:
            # Step 1: Create backup copy
            if os.path.exists(target_binary):
                shutil.copy2(target_binary, backup_path)

            # Step 2: Swap new binary
            shutil.copy2(new_binary, target_binary)
            logger.info(f"[Updater] Successfully swapped '{new_binary}' -> '{target_binary}'. Backup: '{backup_path}'")
            return True, backup_path
        except Exception as e:
            logger.error(f"[Updater] Swap failed: {e}")
            # Restore if partial failure
            if os.path.exists(backup_path):
                try:
                    shutil.copy2(backup_path, target_binary)
                except Exception:
                    pass
            return False, str(e)

    def health_probe_rollback(self, target_binary: str, backup_binary: str, health_url: Optional[str] = None, timeout_seconds: float = 15.0) -> bool:
        if health_url is None:
            port = os.getenv("PORT", os.getenv("MERIDIAN_PORT", "4132"))
            health_url = f"http://127.0.0.1:{port}/api/health"
        """
        Probes local API health endpoint post-swap.
        If system fails to respond with HTTP 200 within timeout_seconds, automatically restores backup binary.
        """
        logger.info(f"[Updater] Starting {timeout_seconds}s health probe at {health_url}...")
        start_t = time.time()
        healthy = False

        while time.time() - start_t < timeout_seconds:
            try:
                res = httpx.get(health_url, timeout=2.0)
                if res.status_code == 200:
                    healthy = True
                    break
            except Exception:
                pass
            time.sleep(1.0)

        if healthy:
            logger.info("[Updater] Health probe PASSED! Update verified.")
            return True

        logger.warning(f"[Updater] Health probe FAILED after {timeout_seconds}s! Triggering automatic rollback...")
        if os.path.exists(backup_binary):
            try:
                shutil.copy2(backup_binary, target_binary)
                logger.info(f"[Updater] Successfully rolled back '{backup_binary}' -> '{target_binary}'.")
            except Exception as re:
                logger.error(f"[Updater] Rollback restoration error: {re}")
        return False
