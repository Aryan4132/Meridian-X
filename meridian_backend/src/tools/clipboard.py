import time
import pyperclip
from bson.objectid import ObjectId
from typing import List, Dict, Any
from database import get_mongo_db

def clipboard_history(n: int = 10) -> str:
    """Retrieve the last N entries copied to the clipboard."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Clipboard history unavailable."
        
    try:
        col = db["smart_clipboard"]
        records = list(col.find({}, {"text": 1, "timestamp": 1, "pinned": 1}).sort("timestamp", -1).limit(n))
        if not records:
            return "Clipboard history is empty."
            
        lines = ["Recent Clipboard History:"]
        for r in records:
            time_str = time.strftime('%H:%M:%S', time.localtime(r.get("timestamp", 0.0)))
            pinned_str = " [PINNED]" if r.get("pinned") else ""
            text_preview = r['text'] if len(r['text']) <= 50 else r['text'][:50] + '...'
            lines.append(f"- ID: {r['_id']} | Time: {time_str} | Text: '{text_preview}'{pinned_str}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error loading clipboard history: {e}"

def clipboard_search(query: str) -> str:
    """Perform a text search across all recorded clipboard history entries."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["smart_clipboard"]
        # Regex case-insensitive search
        records = list(col.find({"text": {"$regex": query, "$options": "i"}}, {"text": 1, "timestamp": 1, "pinned": 1}).sort("timestamp", -1).limit(10))
        if not records:
            return f"No clipboard history entries matching '{query}' found."
            
        lines = [f"Found {len(records)} clipboard entries matching '{query}':"]
        for r in records:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(r.get("timestamp", 0.0)))
            pinned_str = " [PINNED]" if r.get("pinned") else ""
            text_preview = r['text'] if len(r['text']) <= 60 else r['text'][:60] + '...'
            lines.append(f"- ID: {r['_id']} | Date: {time_str} | Text: '{text_preview}'{pinned_str}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error searching clipboard: {e}"

def clipboard_pin(entry_id: str) -> str:
    """Pin a clipboard history entry so that it is preserved permanently."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["smart_clipboard"]
        res = col.update_one({"_id": ObjectId(entry_id)}, {"$set": {"pinned": True}})
        if res.matched_count > 0:
            return f"Successfully pinned clipboard entry '{entry_id}'."
        return f"Error: Clipboard entry '{entry_id}' not found."
    except Exception as e:
        return f"Failed to pin clipboard entry: {e}"

def clipboard_restore(entry_id: str) -> str:
    """Restore a historical clipboard entry back to the active operating system clipboard."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["smart_clipboard"]
        record = col.find_one({"_id": ObjectId(entry_id)})
        if not record:
            return f"Error: Clipboard entry '{entry_id}' not found."
            
        pyperclip.copy(record["text"])
        return f"Successfully restored text to system clipboard: '{record['text'][:50]}...'"
    except Exception as e:
        return f"Failed to restore clipboard entry: {e}"
