"""
parental_controls.py — Kids Mode & Screen Limits Sentinel (FAM-02)

Manages device screen time quotas, bedtime lockouts, and content category filtering
for protected family profiles.
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class ParentalControlsSentinel:
    """Enforces digital wellness and screen quotas on family devices."""

    def __init__(self):
        self._profiles: Dict[str, Dict[str, Any]] = {
            "kids_profile": {
                "name": "Junior",
                "daily_budget_minutes": 90,
                "used_minutes_today": 35,
                "bedtime_lockout": "20:30",
                "blocked_domains": ["tiktok.com", "instagram.com", "gaminghub.gg"],
                "is_locked": False
            }
        }

    def set_screen_quota(self, profile_id: str, minutes: int, bedtime: str = "21:00") -> Dict[str, Any]:
        prof = self._profiles.get(profile_id)
        if not prof:
            prof = {"name": profile_id, "daily_budget_minutes": minutes, "used_minutes_today": 0, "bedtime_lockout": bedtime, "blocked_domains": [], "is_locked": False}
            self._profiles[profile_id] = prof

        prof["daily_budget_minutes"] = minutes
        prof["bedtime_lockout"] = bedtime
        logger.info(f"[ParentalControls] Updated quota for {profile_id}: {minutes} mins, bedtime {bedtime}")
        return prof

    def log_screen_usage(self, profile_id: str, elapsed_minutes: int) -> Dict[str, Any]:
        prof = self._profiles.get(profile_id)
        if not prof:
            return {"status": "error", "message": "Profile not found"}

        prof["used_minutes_today"] += elapsed_minutes
        remaining = max(0, prof["daily_budget_minutes"] - prof["used_minutes_today"])
        if remaining == 0:
            prof["is_locked"] = True

        return {
            "profile_id": profile_id,
            "used_minutes": prof["used_minutes_today"],
            "remaining_minutes": remaining,
            "locked": prof["is_locked"]
        }

    def check_url_allowed(self, profile_id: str, url: str) -> Dict[str, Any]:
        prof = self._profiles.get(profile_id, self._profiles.get("kids_profile", {}))
        blocked = prof.get("blocked_domains", [])
        is_blocked = any(b in url.lower() for b in blocked)
        return {
            "url": url,
            "allowed": not is_blocked,
            "reason": "Domain blocked by parental filter" if is_blocked else "Safe"
        }

parental_controls_sentinel = ParentalControlsSentinel()

def set_kids_screen_budget(profile_id: str, minutes: int, bedtime: str = "20:30") -> Dict[str, Any]:
    return parental_controls_sentinel.set_screen_quota(profile_id=profile_id, minutes=minutes, bedtime=bedtime)

def check_kids_url(profile_id: str, url: str) -> Dict[str, Any]:
    return parental_controls_sentinel.check_url_allowed(profile_id=profile_id, url=url)

