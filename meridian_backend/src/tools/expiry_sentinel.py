"""
Document Expiry Vault Sentinel (BUTLER-06)
Tracks passports, IDs, insurance policies, warranties, and vehicle registrations.
Provides proactive alert queues for 30, 14, 7, and 1-day threshold warnings.
"""

import os
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

from src.core.atomic_storage import atomic_write_json, safe_load_json

EXPIRY_STORE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "expiry_vault.json")

def _load_expiry_records() -> List[Dict[str, Any]]:
    return safe_load_json(EXPIRY_STORE_FILE, default=[])

def _save_expiry_records(records: List[Dict[str, Any]]) -> None:
    atomic_write_json(EXPIRY_STORE_FILE, records, indent=2)

def add_expiry_document(doc_title: str, doc_type: str, expiry_date: str, notes: str = "") -> str:
    """
    Register a document in the Expiry Sentinel vault.
    doc_type: passport | driver_license | insurance | warranty | subscription | custom
    expiry_date: YYYY-MM-DD format
    """
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Use YYYY-MM-DD."

    records = _load_expiry_records()
    record = {
        "id": f"exp_{int(datetime.now().timestamp())}_{len(records)}",
        "title": doc_title,
        "type": doc_type,
        "expiry_date": expiry_date,
        "notes": notes,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    records.append(record)
    _save_expiry_records(records)
    return f"Successfully registered document '{doc_title}' expiring on {expiry_date}."

def check_document_expiries(days_ahead: int = 30) -> str:
    """
    Check for documents expiring within specified days (default 30 days).
    Categorizes alerts by priority: CRITICAL (<=7 days), WARNING (<=14 days), NOTICE (<=30 days).
    """
    records = _load_expiry_records()
    if not records:
        return "No documents registered in Expiry Sentinel."

    today = datetime.now()
    alerts = []
    
    for doc in records:
        try:
            exp_dt = datetime.strptime(doc["expiry_date"], "%Y-%m-%d")
            delta = (exp_dt - today).days + 1
            if delta <= days_ahead:
                if delta < 0:
                    status = f"🔴 EXPIRED ({abs(delta)} days ago)"
                elif delta <= 7:
                    status = f"🔴 CRITICAL ({delta} days left)"
                elif delta <= 14:
                    status = f"🟠 WARNING ({delta} days left)"
                else:
                    status = f"🟡 NOTICE ({delta} days left)"
                alerts.append(f"- [{status}] {doc['title']} ({doc['type']}) — Expires: {doc['expiry_date']}. Notes: {doc['notes']}")
        except ValueError:
            continue

    if not alerts:
        return f"All documents healthy. No expiries in next {days_ahead} days."

    return f"📋 Expiry Sentinel Alerts (Next {days_ahead} Days):\n" + "\n".join(alerts)

def list_expiry_documents() -> str:
    """List all registered document expiries."""
    records = _load_expiry_records()
    if not records:
        return "No documents registered in Expiry Sentinel."
    lines = [f"- {d['title']} ({d['type']}) — Expiry: {d['expiry_date']} [ID: {d['id']}]" for d in records]
    return "Registered Documents:\n" + "\n".join(lines)
