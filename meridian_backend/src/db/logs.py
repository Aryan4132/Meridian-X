import time
import random
import pymongo
from typing import List, Dict, Any

from src.db.connection import get_db_cursor, get_sqlite_conn, get_mongo_db

def add_to_task_log(tool: str, tier: int, outcome: str, error: str = ""):
    """Logs tool execution outcome to SQLite task_log table."""
    try:
        log_id = f"log-{time.time()}-{random.randint(1000, 9999)}"
        with get_db_cursor() as cursor:
            cursor.execute(
                "INSERT INTO task_log (id, timestamp, tool, tier, outcome, error) VALUES (?, ?, ?, ?, ?, ?)",
                (log_id, time.time(), tool, tier, outcome, error)
            )
    except Exception as e:
        print("[Task Log] Save failed:", e)

def get_recent_failures(limit: int = 5) -> List[Dict[str, Any]]:
    """Retrieves recent failed tool runs for RLEF / self-correction."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT tool, outcome, error FROM task_log WHERE outcome = 'failed' ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]
    except Exception as e:
        print("[RLEF] Failed to fetch task logs:", e)
        return []
    finally:
        if conn:
            conn.close()

def add_background_run(goal: str, status: str, log: str):
    """Logs background scheduler execution run."""
    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                "INSERT INTO background_runs (timestamp, goal, status, log) VALUES (?, ?, ?, ?)",
                (time.time(), goal, status, log)
            )
        print(f"[Scheduler Log] Logged background run: {goal[:30]} ({status})")
    except Exception as e:
        print("[Scheduler Log] Save failed:", e)

def get_background_runs(limit: int = 20) -> List[Dict[str, Any]]:
    """Retrieves list of recent background runs."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, timestamp, goal, status, log FROM background_runs ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]
    except Exception as e:
        print("[Scheduler Log] Retrieval failed:", e)
        return []
    finally:
        if conn:
            conn.close()

def add_thought_log(thought_text: str, session_id: str = "default", step_index: int = 0, tool_name: str = "") -> bool:
    """BK-08: Persist intermediate ReAct step reasoning thoughts to SQLite database."""
    if not thought_text:
        return False
    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                "INSERT INTO thought_logs (timestamp, session_id, step_index, thought_text, tool_name) VALUES (?, ?, ?, ?, ?)",
                (time.time(), session_id, step_index, thought_text, tool_name)
            )
        return True
    except Exception as e:
        print("[Database] Failed to add thought log:", e)
        return False

def get_thought_logs(session_id: str = "default", limit: int = 50) -> List[Dict[str, Any]]:
    """BK-08: Fetch persisted thought introspection logs for replay and debugging."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, timestamp, session_id, step_index, thought_text, tool_name FROM thought_logs WHERE session_id = ? ORDER BY id DESC LIMIT ?",
            (session_id, limit)
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]
    except Exception as e:
        print("[Database] Failed to get thought logs:", e)
        return []
    finally:
        if conn:
            conn.close()

def record_token_spend(provider: str, model: str, prompt_tokens: int, completion_tokens: int, cost_usd: float):
    """Records LLM token usage and estimated USD cost into SQLite token_spend_logs (TRUST-03)."""
    try:
        with get_db_cursor() as cursor:
            cursor.execute("""
                INSERT INTO token_spend_logs (timestamp, provider, model, prompt_tokens, completion_tokens, cost_usd)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (time.time(), provider, model, prompt_tokens, completion_tokens, cost_usd))
    except Exception as e:
        print(f"[Database] Failed recording token spend: {e}")

def get_spend_stats() -> Dict[str, Any]:
    """Returns token spend summary, breakdown by provider, monthly cost, and budget cap status."""
    from src.db.profile import get_budget_cap, get_budget_enabled
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        thirty_days_ago = time.time() - (30 * 86400)
        cursor.execute("SELECT SUM(cost_usd), SUM(prompt_tokens), SUM(completion_tokens) FROM token_spend_logs WHERE timestamp >= ?", (thirty_days_ago,))
        row = cursor.fetchone()
        monthly_cost = row[0] or 0.0
        prompt_t = row[1] or 0
        completion_t = row[2] or 0

        cursor.execute("""
            SELECT provider, SUM(cost_usd), SUM(prompt_tokens + completion_tokens)
            FROM token_spend_logs
            WHERE timestamp >= ?
            GROUP BY provider
        """, (thirty_days_ago,))
        by_provider = {r[0]: {"cost": round(r[1] or 0.0, 4), "tokens": r[2] or 0} for r in cursor.fetchall()}

        budget_cap = get_budget_cap()
        budget_enabled = get_budget_enabled()
        exceeded = (monthly_cost >= budget_cap) if budget_enabled else False

        return {
            "monthly_cost_usd": round(monthly_cost, 4),
            "total_prompt_tokens": prompt_t,
            "total_completion_tokens": completion_t,
            "total_tokens": prompt_t + completion_t,
            "budget_cap_usd": budget_cap,
            "budget_enabled": budget_enabled,
            "budget_exceeded": exceeded,
            "by_provider": by_provider
        }
    except Exception as e:
        print(f"[Database] Failed retrieving spend stats: {e}")
        return {"monthly_cost_usd": 0.0, "total_tokens": 0, "budget_cap_usd": 10.0, "budget_enabled": True, "budget_exceeded": False, "by_provider": {}}
    finally:
        if conn:
            conn.close()

def add_clipboard_history(text: str):
    """Caches new clipboard segment into MongoDB and SQLite."""
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["smart_clipboard"]
            last_clip = collection.find_one(sort=[("timestamp", pymongo.DESCENDING)])
            if last_clip and last_clip.get("text") == text:
                return
            collection.insert_one({"text": text, "timestamp": time.time()})
            print("[MongoDB Clipboard] Cached new clipboard segment.")
        except Exception as e:
            print("[MongoDB Clipboard] Save failed:", e)

    # SQLite sync/fallback
    try:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT text FROM clipboard_history ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            if row and row[0] == text:
                return
            cursor.execute("INSERT INTO clipboard_history (text, timestamp) VALUES (?, ?)", (text, time.time()))
    except Exception as e:
        print("[SQLite Clipboard] Save failed:", e)

def get_clipboard_history(limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieves clipboard history records."""
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["smart_clipboard"]
            records = list(collection.find({}, {"_id": 0}).sort("timestamp", pymongo.DESCENDING).limit(limit))
            if records:
                return records
        except Exception as e:
            print("[MongoDB Clipboard] Fetch failed:", e)

    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT text, timestamp FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [{"text": row[0], "timestamp": row[1]} for row in rows]
    except Exception as e:
        print("[SQLite Clipboard] Fetch failed:", e)
        return []
    finally:
        if conn:
            conn.close()
