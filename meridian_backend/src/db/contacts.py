import re
import time
from typing import Dict, Any, List, Optional

from src.db.connection import get_db_cursor, get_sqlite_conn, get_mongo_db

def save_whatsapp_contact(name: str, phone_number: str, alias: str = "", notes: str = "") -> Dict[str, Any]:
    """Stores or updates a WhatsApp contact record in local database."""
    name_clean = name.strip()
    phone_clean = phone_number.strip()
    if not name_clean or not phone_clean:
        raise ValueError("Both contact name and phone number are required.")

    db = get_mongo_db()
    if db is not None:
        try:
            col = db["whatsapp_contacts"]
            doc = {
                "name": name_clean,
                "phone_number": phone_clean,
                "alias": alias.strip(),
                "notes": notes.strip(),
                "updated_at": time.time()
            }
            col.update_one({"name": {"$regex": f"^{re.escape(name_clean)}$", "$options": "i"}}, {"$set": doc}, upsert=True)
        except Exception as e:
            print("[DB] MongoDB contact save error, continuing to SQLite sync:", e)

    # SQLite dual-write & offline sync
    try:
        with get_db_cursor() as cursor:
            cursor.execute("""
                INSERT INTO whatsapp_contacts (name, phone_number, alias, notes, updated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    phone_number=excluded.phone_number,
                    alias=excluded.alias,
                    notes=excluded.notes,
                    updated_at=excluded.updated_at
            """, (name_clean, phone_clean, alias.strip(), notes.strip(), time.time()))
    except Exception as e:
        print("[SQLite Contact] Save failed:", e)

    return {"name": name_clean, "phone_number": phone_clean, "alias": alias, "notes": notes}

def get_whatsapp_contacts() -> List[Dict[str, Any]]:
    """Retrieves all saved WhatsApp contacts."""
    db = get_mongo_db()
    if db is not None:
        try:
            col = db["whatsapp_contacts"]
            docs = list(col.find({}, {"_id": 0}))
            if docs:
                return docs
        except Exception:
            pass

    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone_number, alias, notes FROM whatsapp_contacts")
        rows = cursor.fetchall()
        return [{"name": r["name"], "phone_number": r["phone_number"], "alias": r["alias"], "notes": r["notes"]} for r in rows]
    except Exception:
        return []
    finally:
        if conn:
            conn.close()

def resolve_whatsapp_contact(identifier: str) -> Optional[Dict[str, Any]]:
    """Resolves contact name, phone number, or relationship alias to contact record."""
    if not identifier:
        return None
    target = identifier.strip().lower()

    if re.match(r"^\+?[0-9]{7,15}$", target):
        return {"name": identifier, "phone_number": identifier, "alias": ""}

    contacts = get_whatsapp_contacts()
    for c in contacts:
        if c.get("name", "").lower() == target or c.get("alias", "").lower() == target:
            return c
    for c in contacts:
        if target in c.get("name", "").lower() or (c.get("alias") and target in c.get("alias", "").lower()):
            return c
    return None
