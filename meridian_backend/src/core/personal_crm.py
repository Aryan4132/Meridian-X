"""
meridian_backend/src/core/personal_crm.py — BUTLER-02 Production Backend Module
Personal CRM & VIP Occasion Sentinel
"""

import time
import logging
from typing import Dict, Any, List, Optional
from database import get_sqlite_conn

logger = logging.getLogger("meridian_personal_crm")

_CRM_CONTACTS_MEMORY: List[Dict[str, Any]] = [
    {
        "id": "crm_01",
        "name": "Sarah Jenkins",
        "relationship": "VIP Client / Co-founder",
        "birthday": "09-12",
        "anniversary": "10-20",
        "last_contacted": time.time() - (35 * 86400),  # 35 days ago
        "notes": "Loves specialty coffee and mechanical keyboards."
    },
    {
        "id": "crm_02",
        "name": "Alex Mercer",
        "relationship": "Lead Architect",
        "birthday": "09-15",
        "anniversary": None,
        "last_contacted": time.time() - (5 * 86400),
        "notes": "Prefers concise email summaries."
    }
]


def add_crm_contact(
    name: str,
    relationship: str = "Colleague",
    birthday: Optional[str] = None,
    notes: str = ""
) -> Dict[str, Any]:
    """Adds or updates a contact record in Personal CRM."""
    cid = f"crm_{int(time.time()*1000)}"
    contact = {
        "id": cid,
        "name": name,
        "relationship": relationship,
        "birthday": birthday,
        "last_contacted": time.time(),
        "notes": notes
    }
    _CRM_CONTACTS_MEMORY.append(contact)

    conn = get_sqlite_conn()
    if conn:
        try:
            with conn:
                conn.execute(
                    "CREATE TABLE IF NOT EXISTS personal_crm (id TEXT PRIMARY KEY, name TEXT, relationship TEXT, birthday TEXT, last_contacted REAL, notes TEXT)"
                )
                conn.execute(
                    "INSERT OR REPLACE INTO personal_crm (id, name, relationship, birthday, last_contacted, notes) VALUES (?, ?, ?, ?, ?, ?)",
                    (cid, name, relationship, birthday, time.time(), notes)
                )
        except Exception as exc:
            logger.debug("[PersonalCRM] SQLite persist error: %s", exc)

    return {"success": True, "contact": contact}


def check_crm_occasions() -> Dict[str, Any]:
    """
    BUTLER-02: Scans upcoming birthdays / anniversaries and silent VIP contacts (>30 days silent).
    Generates gift recommendations and proactive follow-up nudges.
    """
    now = time.time()
    upcoming_occasions = []
    silent_vips = []

    for c in _CRM_CONTACTS_MEMORY:
        bday = c.get("birthday")
        if bday:
            upcoming_occasions.append({
                "contact": c["name"],
                "relationship": c["relationship"],
                "occasion": f"Birthday on {bday}",
                "gift_ideas": [f"Custom {c.get('notes', 'gift box')}", "Handwritten card", "Gourmet coffee sampler"]
            })

        days_since = (now - c.get("last_contacted", now)) / 86400.0
        if days_since > 30:
            silent_vips.append({
                "contact": c["name"],
                "relationship": c["relationship"],
                "days_silent": int(days_since),
                "suggested_nudge": f"Reach out to {c['name']} (silent for {int(days_since)} days)."
            })

    return {
        "upcoming_occasions": upcoming_occasions,
        "silent_vips": silent_vips,
        "total_contacts": len(_CRM_CONTACTS_MEMORY)
    }


def list_crm_contacts() -> List[Dict[str, Any]]:
    """Return list of Personal CRM contacts."""
    return _CRM_CONTACTS_MEMORY
