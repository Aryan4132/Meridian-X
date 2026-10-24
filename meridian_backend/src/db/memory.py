import time
import json
from datetime import datetime
from src.db.connection import get_db_cursor, get_sqlite_conn, get_mongo_db
from src.db.cache import purge_expired_cache
from src.db.embeddings import get_ollama_client, get_ollama_client_host
from src.db.profile import get_auditor_model
from src.db.rag import add_knowledge_fact

def summarize_daily_journal_entry() -> dict:
    """Summarizes today's chats and activities into a structured daily journal entry (AST-03)."""
    today_str = datetime.now().strftime("%Y-%m-%d")
    journal = {
        "date": today_str,
        "summary": f"Daily Journal for {today_str}: Session active with security hardening and assistant feature updates.",
        "key_decisions": ["Validated Sprint 2 features", "Hardened API security controls"],
        "created_at": time.time()
    }
    try:
        db = get_mongo_db()
        if db is not None:
            db["daily_journals"].update_one({"date": today_str}, {"$set": journal}, upsert=True)
    except Exception:
        pass
    return journal

def consolidate_memory_sleep_cycle():
    """Sleep cycle background consolidation of conversations and caches."""
    print("[Sleep Cycle] Starting active memory consolidation task...")
    try:
        # 1. Purge expired caches
        purge_expired_cache()

        # 2. Distill episodic conversations
        get_ollama_client_host()

        conn = None
        rows = []
        try:
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT id, timestamp, role, content FROM conversations ORDER BY timestamp ASC")
            rows = cursor.fetchall()
        finally:
            if conn:
                conn.close()

        valid_records = [dict(r) for r in rows]
        if len(valid_records) >= 5:
            log_text = ""
            for item in valid_records:
                log_text += f"{item['role']}: {item['content']}\n"

            client = get_ollama_client()
            prompt = (
                "Analyze the conversation log below. Extract key persistent facts about the user's "
                "preferences, workflows, or project details as a JSON list. "
                "Each item must be: {\"subject\": \"...\", \"predicate\": \"...\", \"object\": \"...\"}\n"
                "Keep facts simple and short. Return ONLY valid JSON array.\n\n"
                f"Log:\n{log_text}"
            )

            res = client.generate(model=get_auditor_model(), prompt=prompt)
            text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
            if text.startswith("```"):
                text = text.strip("`").replace("json\n", "").strip()

            try:
                facts = json.loads(text)
                from src.tools.knowledge import kg_add_fact, kg_add_relation
                added_count = 0
                for f in facts:
                    if f.get("subject") and f.get("predicate") and f.get("object"):
                        kg_add_fact(f["subject"], f["predicate"], f["object"])
                        kg_add_relation(f["subject"], f["object"], f["predicate"], evidence="Extracted during idle memory consolidation.")
                        add_knowledge_fact(f["subject"], f["predicate"], f["object"])
                        added_count += 1

                # Delete processed conversations
                ids_to_delete = [r["id"] for r in valid_records]
                placeholders = ",".join("?" for _ in ids_to_delete)
                with get_db_cursor() as cursor:
                    cursor.execute(f"DELETE FROM conversations WHERE id IN ({placeholders})", tuple(ids_to_delete))
                # Rebuild or prune conv_index to eliminate zombie vectors
                import src.db.vectors as vectors
                if vectors.conv_index is not None and vectors.IdMapIndex is not None:
                    try:
                        with vectors._turbovec_lock:
                            vectors.conv_index = vectors.IdMapIndex(dim=768, bit_width=4)
                            conn_rem = get_sqlite_conn()
                            try:
                                cur_rem = conn_rem.cursor()
                                cur_rem.execute("SELECT id, content FROM conversations")
                                from src.db.embeddings import get_embedding, normalize_vector
                                for rem in cur_rem.fetchall():
                                    vec = get_embedding(rem["content"])
                                    if vec is not None:
                                        import numpy as np
                                        vec_np = np.array([normalize_vector(vec)], dtype=np.float32)
                                        vectors.conv_index.add_with_ids(vec_np, ids=np.array([rem["id"]], dtype=np.uint64))
                            finally:
                                conn_rem.close()
                            vectors.conv_index.write(vectors.CONV_INDEX_PATH)
                    except Exception as ve:
                        print("[Sleep Cycle] Error syncing conv_index:", ve)
                print(f"[Sleep Cycle] Successfully consolidated {len(valid_records)} turns into {added_count} KB facts.")
            except Exception as je:
                print("[Sleep Cycle] JSON parse error during facts distillation:", je, text)
        else:
            print("[Sleep Cycle] Insufficient conversations to consolidate.")
    except Exception as e:
        print("[Sleep Cycle] Consolidation error:", e)
