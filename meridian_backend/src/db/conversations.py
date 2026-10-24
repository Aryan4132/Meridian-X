import os
import re
import time
import numpy as np
from typing import List, Dict, Any

from src.db.connection import get_db_cursor, get_sqlite_conn
from src.db.embeddings import get_embedding, normalize_vector
import src.db.vectors as vectors

TRANSIENT_CONVERSATION_PHRASES = {
    "try again", "retry", "redo", "again", "try again.", "retry.", "redo.",
    "ok", "okay", "yes", "no", "thanks", "thank you", "nevermind", "never mind",
    "clear", "cancel", "stop", "continue", "go ahead", "k", "kk", "sure", "yep", "nope"
}

_TRANSIENT_REGEX = re.compile(r"[^\w\s]")

def is_transient_phrase(text: str) -> bool:
    """Returns True if input text is a short transient filler phrase that should not be saved into DB history."""
    if not text or not text.strip():
        return True
    cleaned = _TRANSIENT_REGEX.sub("", text.strip().lower())
    return cleaned in TRANSIENT_CONVERSATION_PHRASES

def add_to_conversations(role: str, content: str, summary: str = ""):
    """Stores a message into SQLite conversations and indexes it in Turbovec."""
    if is_transient_phrase(content):
        print(f"[Conversations Log] Skipped storing transient phrase: '{content.strip()}'")
        return

    inserted_id = None
    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                "INSERT INTO conversations (timestamp, role, content, summary) VALUES (?, ?, ?, ?)",
                (time.time(), role, content, summary)
            )
            inserted_id = cursor.lastrowid
    except Exception as e:
        print("[Conversations Log] SQLite write failed:", e)

    if inserted_id is not None and vectors.conv_index is not None:
        try:
            vector = get_embedding(content)
            if vector is None:
                print("[Conversations Log] Skipped Turbovec index save (embedding unavailable).")
            else:
                vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
                with vectors._turbovec_lock:
                    vectors.conv_index.add_with_ids(vector_np, ids=np.array([inserted_id], dtype=np.uint64))
                    vectors.conv_index.write(vectors.CONV_INDEX_PATH)
                print(f"[Conversations Log] Saved to Turbovec index (ID: {inserted_id})")
        except Exception as e:
            print("[Conversations Log] Turbovec index save failed:", e)

def get_conversation_history(limit: int = 10) -> List[Dict[str, Any]]:
    """Retrieves recent conversation turns in chronological order."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, timestamp, role, content, summary FROM conversations ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        results = []
        for r in rows:
            results.append({
                "id": str(r["id"]),
                "timestamp": r["timestamp"],
                "role": r["role"],
                "content": r["content"],
                "summary": r["summary"],
                "vector": [0.0] * 768
            })
        return list(reversed(results))
    except Exception as e:
        print("[Conversations Log] Retrieval failed:", e)
        return []
    finally:
        if conn:
            conn.close()

def clear_conversations():
    """Clears all conversation records and resets the Turbovec conversations index."""
    try:
        with get_db_cursor() as cursor:
            cursor.execute("DELETE FROM conversations")
    except Exception as e:
        print("[Conversations Log] Failed to clear conversations from SQLite:", e)

    if vectors.IdMapIndex is None:
        print("[Conversations Log] Turbovec not installed — skipping index reset.")
        return

    try:
        with vectors._turbovec_lock:
            vectors.conv_index = vectors.IdMapIndex(dim=768, bit_width=4)
            if os.path.exists(vectors.CONV_INDEX_PATH):
                try:
                    os.remove(vectors.CONV_INDEX_PATH)
                except Exception:
                    pass
            vectors.conv_index.write(vectors.CONV_INDEX_PATH)
        print("[Conversations Log] Safely cleared all conversations and reset index.")
    except Exception as e:
        print("[Conversations Log] Clear failed:", e)
