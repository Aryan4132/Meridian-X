"""
Household Ops: Grocery, Pantry & Chore Tracker (BUTLER-05)
Voice/NL list capture, low-stock pantry suggestions, chore tracking, and WhatsApp list sharing.
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Any

from src.core.atomic_storage import atomic_write_json, safe_load_json

HOUSEHOLD_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "household_ops.json")

def _load_household() -> Dict[str, Any]:
    return safe_load_json(HOUSEHOLD_FILE, default={"pantry": [], "groceries": [], "chores": []})

def _save_household(data: Dict[str, Any]) -> None:
    atomic_write_json(HOUSEHOLD_FILE, data, indent=2)

def add_grocery_item(item_name: str, quantity: str = "1", priority: str = "normal") -> str:
    """Add an item to the household grocery shopping list."""
    data = _load_household()
    item = {
        "id": f"g_{int(datetime.now().timestamp())}",
        "name": item_name,
        "quantity": quantity,
        "priority": priority,
        "added_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    data["groceries"].append(item)
    _save_household(data)
    return f"🛒 Added '{item_name}' (Qty: {quantity}) to grocery list."

def add_household_chore(chore_name: str, assigned_to: str = "Self", due_date: str = "Today") -> str:
    """Add a household chore or routine task."""
    data = _load_household()
    chore = {
        "id": f"c_{int(datetime.now().timestamp())}",
        "title": chore_name,
        "assigned_to": assigned_to,
        "due_date": due_date,
        "completed": False
    }
    data["chores"].append(chore)
    _save_household(data)
    return f"🧹 Registered chore '{chore_name}' assigned to {assigned_to} due {due_date}."

def get_household_summary() -> str:
    """Get active grocery list and household chores summary."""
    data = _load_household()
    g_items = data.get("groceries", [])
    c_items = [c for c in data.get("chores", []) if not c.get("completed")]

    g_str = "\n".join(f"- {i['name']} ({i['quantity']})" for i in g_items) if g_items else "No grocery items pending."
    c_str = "\n".join(f"- {c['title']} (Assigned: {c['assigned_to']}, Due: {c['due_date']})" for c in c_items) if c_items else "No pending chores."

    return (
        f"🏠 Household Ops Digest:\n\n"
        f"🛒 Grocery List:\n{g_str}\n\n"
        f"🧹 Pending Chores:\n{c_str}"
    )
