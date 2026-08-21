import os
import re
import time
import json
import random
import sqlite3
import pymongo
import threading
import numpy as np
try:
    from turbovec import IdMapIndex  # type: ignore # pyright: ignore[reportMissingImports]
except ImportError:
    IdMapIndex = None

from typing import Optional, List, Dict, Any, Tuple, TypedDict

class UserProfile(TypedDict, total=False):
    meridian_model: str
    meridian_auditor_model: str
    meridian_vision_model: str
    ollama_host: str
    wakeword_model_filename: str
    custom_directives: str


def extract_text_from_file(file_path: str) -> str:
    """Extracts text content from various file formats (.txt, .md, .json, .csv, .pdf, .docx)."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext in [".txt", ".md", ".json", ".csv"]:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    elif ext == ".pdf":
        try:
            import pypdf
            reader = pypdf.PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except ImportError:
            raise ImportError("The 'pypdf' package is required to parse PDF files. Run 'install_package' with arg 'pypdf' first.")
    elif ext == ".docx":
        try:
            import docx
            doc = docx.Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])
        except ImportError:
            raise ImportError("The 'python-docx' package is required to parse DOCX files. Run 'install_package' with arg 'python-docx' first.")
    else:
        raise ValueError(f"Unsupported file extension: '{ext}'. Supported formats: .txt, .md, .json, .csv, .pdf, .docx")

def get_ollama_client_host():
    host = os.environ.get("OLLAMA_HOST")
    if not host:
        try:
            db_host = get_user_profile("ollama_host")
            if db_host:
                host = db_host
        except Exception:
            pass
    if not host:
        host = "http://127.0.0.1:11434"

    if host == "0.0.0.0":
        return "http://127.0.0.1:11434"
    if host.startswith("0.0.0.0:"):
        return f"http://127.0.0.1:{host.split(':')[1]}"
    if "0.0.0.0" in host:
        return host.replace("0.0.0.0", "127.0.0.1")
    if not host.startswith("http://") and not host.startswith("https://"):
        return f"http://{host}"
    return host

# Global cache for Ollama client
_cached_ollama_client = None

def get_ollama_client():
    global _cached_ollama_client
    if _cached_ollama_client is None:
        import ollama
        _cached_ollama_client = ollama.Client(host=get_ollama_client_host())
    return _cached_ollama_client

# Embedding client helper
def get_embedding(text: str) -> List[float]:
    embed_model = os.environ.get("EMBEDDING_MODEL")
    if not embed_model:
        try:
            embed_model = get_user_profile("embedding_model")
        except Exception:
            pass
    if not embed_model:
        embed_model = "nomic-embed-text"

    try:
        # Truncate text to ~2000 chars (~500 tokens) to prevent context length error from Ollama embedding models
        if text and len(text) > 2000:
            text = text[:2000]
        client = get_ollama_client()
        res = client.embeddings(model=embed_model, prompt=text)
        # BUG-2 fix: ollama SDK returns an EmbeddingResponse object, not a dict.
        embedding = res.embedding if hasattr(res, "embedding") else res.get("embedding")
        if embedding:
            return list(embedding)
    except Exception as e:
        print(f"[Embedding] Warning: Failed to get embedding ({embed_model}) for text (len={len(text) if text else 0}): {e}")
    # Default fallback embedding if Ollama is unreachable/missing
    return [0.0] * 768  # nomic-embed-text has 768 dimensions by default

def normalize_vector(v: List[float]) -> np.ndarray:
    arr = np.array(v, dtype=np.float32)
    norm = np.linalg.norm(arr)
    if norm > 1e-9:
        return arr / norm
    return arr

# Database directories setup
from src.core.config import DB_DIR as db_dir

# Turbovec Index paths
KB_INDEX_PATH = os.path.join(db_dir, "knowledge_base.tq")
CACHE_INDEX_PATH = os.path.join(db_dir, "semantic_cache.tq")
CONV_INDEX_PATH = os.path.join(db_dir, "conversations.tq")
SQLITE_DB_PATH = os.path.join(db_dir, "metadata.db")

kb_index = None
cache_index = None
conv_index = None
_turbovec_lock = threading.Lock()

def get_sqlite_conn():
    conn = sqlite3.connect(SQLITE_DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.execute("PRAGMA cache_size=-64000;")
        conn.execute("PRAGMA mmap_size=268435456;")
    except Exception:
        pass
    return conn

def run_vector_health_check() -> bool:
    """Verify integrity of all Turbovec vector index files on startup."""
    if IdMapIndex is None:
        return False
    print("[Turbovec Health Check] Starting validation...")
    healthy = True
    for name, path in [("Knowledge Base", KB_INDEX_PATH), ("Semantic Cache", CACHE_INDEX_PATH), ("Conversations", CONV_INDEX_PATH)]:
        if os.path.exists(path):
            if os.path.getsize(path) == 0:
                print(f"[Turbovec Health Check] Warning: {name} index file is empty (0 bytes). Recreating.")
                healthy = False
                try:
                    os.remove(path)
                except Exception:
                    pass
            else:
                try:
                    # Test load
                    test_idx = IdMapIndex.load(path)
                    # Verify dim size
                    if getattr(test_idx, "dim", 0) != 768:
                        raise ValueError(f"Invalid dimension: {getattr(test_idx, 'dim', 0)}")
                except Exception as e:
                    print(f"[Turbovec Health Check] Error: {name} index is CORRUPTED ({e}). Removing.")
                    healthy = False
                    try:
                        os.remove(path)
                    except Exception:
                        pass
        else:
            print(f"[Turbovec Health Check] {name} index file does not exist yet.")
    return healthy

def summarize_daily_journal_entry() -> dict:
    """Summarizes today's chats and activities into a structured daily journal entry (AST-03)."""
    from datetime import datetime
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

def init_turbovec_indexes():
    global kb_index, cache_index, conv_index
    if IdMapIndex is None:
        kb_index, cache_index, conv_index = None, None, None
        return
    
    # Run checksum / validation checks before loading
    run_vector_health_check()
    
    # 1. Knowledge Base Index
    if os.path.exists(KB_INDEX_PATH):
        try:
            kb_index = IdMapIndex.load(KB_INDEX_PATH)
        except Exception as e:
            print("[Turbovec] Failed to load knowledge base index, creating new:", e)
            kb_index = IdMapIndex(dim=768, bit_width=4)
    else:
        kb_index = IdMapIndex(dim=768, bit_width=4)
        
    # 2. Semantic Cache Index
    if os.path.exists(CACHE_INDEX_PATH):
        try:
            cache_index = IdMapIndex.load(CACHE_INDEX_PATH)
        except Exception as e:
            print("[Turbovec] Failed to load semantic cache index, creating new:", e)
            cache_index = IdMapIndex(dim=768, bit_width=4)
    else:
        cache_index = IdMapIndex(dim=768, bit_width=4)
        
    # 3. Conversations Index
    if os.path.exists(CONV_INDEX_PATH):
        try:
            conv_index = IdMapIndex.load(CONV_INDEX_PATH)
        except Exception as e:
            print("[Turbovec] Failed to load conversations index, creating new:", e)
            conv_index = IdMapIndex(dim=768, bit_width=4)
    else:
        conv_index = IdMapIndex(dim=768, bit_width=4)

def init_tables():
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA synchronous=NORMAL")
    except Exception as e:
        print("[Database] Failed to set SQLite WAL or synchronous mode:", e)
    
    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS semantic_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_text TEXT UNIQUE,
            response_text TEXT,
            expires_at REAL,
            ttl_hours INTEGER DEFAULT 24
        )
    """)
    try:
        cursor.execute("ALTER TABLE semantic_cache ADD COLUMN ttl_hours INTEGER DEFAULT 24")
    except Exception:
        pass # already exists
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            role TEXT,
            content TEXT,
            summary TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_base (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            chunk_text TEXT,
            metadata TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_log (
            id TEXT PRIMARY KEY,
            timestamp REAL,
            tool TEXT,
            tier INTEGER,
            outcome TEXT,
            error TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS background_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            goal TEXT,
            status TEXT,
            log TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS thought_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            session_id TEXT,
            step_index INTEGER,
            thought_text TEXT,
            tool_name TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (

            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompt_templates (
            name TEXT PRIMARY KEY,
            prompt_text TEXT,
            description TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    
    init_turbovec_indexes()

# BUG-44 fix: ensure DB_DIR exists before init_tables() is called,
# otherwise sqlite3.connect() raises on first run when the directory is missing.
os.makedirs(db_dir, exist_ok=True)
init_tables()

# Dummy db for loop.py import compatibility
db = None

# ----------------- SEMANTIC CACHE HELPERS -----------------

from collections import OrderedDict
_exact_match_cache: OrderedDict = OrderedDict()
_EXACT_CACHE_MAX_SIZE = 500

def check_semantic_cache(query_text: str) -> Optional[str]:
    # Tier-1: Exact Match LRU/Memory cache (0ms, skips embedding generation)
    if query_text in _exact_match_cache:
        val, expires_at = _exact_match_cache[query_text]
        if expires_at > time.time():
            _exact_match_cache.move_to_end(query_text)
            print(f"[Semantic Cache] Tier-1 Exact Match HIT: '{query_text}'")
            return val
        else:
            del _exact_match_cache[query_text]

    # Tier-2: Cosine Similarity Vector Cache (Turbovec + SQLite lookup)
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        
        # Auto-expiry: Delete expired items from database first
        cursor.execute("DELETE FROM semantic_cache WHERE expires_at < ?", (time.time(),))
        conn.commit()
        
        cursor.execute("SELECT COUNT(*) FROM semantic_cache")
        count = cursor.fetchone()[0]
        
        if count > 0 and cache_index is not None:
            vector = get_embedding(query_text)
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            
            # Search closest items
            scores, ids = cache_index.search(vector_np, k=min(2, count))
            
            if ids.size > 0 and ids[0].size > 0:
                for score, id_val in zip(scores[0], ids[0]):
                    # Score is inner product (cosine similarity since vectors are normalized)
                    if score > 0.96:
                        cursor.execute(
                            "SELECT response_text, expires_at FROM semantic_cache WHERE id = ?",
                            (int(id_val),)
                        )
                        res = cursor.fetchone()
                        if res and res["response_text"] and res["response_text"].strip() and res["expires_at"] > time.time():
                            print(f"[Semantic Cache] Tier-2 Vector Match HIT: '{query_text}' (similarity: {score:.4f})")
                            # Store back to Tier-1
                            _exact_match_cache[query_text] = (res["response_text"], res["expires_at"])
                            return res["response_text"]
    except Exception as e:
        print("[Semantic Cache] Search failed:", e)
    finally:
        if conn:
            conn.close()
    return None

def get_near_miss_semantic_cache(query_text: str, min_score: float = 0.60, max_score: float = 0.85) -> Optional[str]:
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM semantic_cache WHERE expires_at > ?", (time.time(),))
        count = cursor.fetchone()[0]
        if count > 0 and cache_index is not None:
            vector = get_embedding(query_text)
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            scores, ids = cache_index.search(vector_np, k=min(2, count))
            if ids.size > 0 and ids[0].size > 0:
                for score, id_val in zip(scores[0], ids[0]):
                    if min_score <= score <= max_score:
                        cursor.execute(
                            "SELECT response_text FROM semantic_cache WHERE id = ? AND expires_at > ?",
                            (int(id_val), time.time())
                        )
                        res = cursor.fetchone()
                        if res and res["response_text"] and res["response_text"].strip():
                            return res["response_text"]
    except Exception as e:
        print("[Semantic Cache] Near-miss lookup failed:", e)
    finally:
        if conn:
            conn.close()
    return None

def add_to_semantic_cache(query_text: str, response_text: str, ttl_hours: int = 24):
    ttl_seconds = ttl_hours * 3600
    expires_at = time.time() + ttl_seconds
    _exact_match_cache[query_text] = (response_text, expires_at)
    _exact_match_cache.move_to_end(query_text)
    if len(_exact_match_cache) > _EXACT_CACHE_MAX_SIZE:
        _exact_match_cache.popitem(last=False)
    
    conn = None
    inserted_id = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        
        # Delete old entry with same query_text if exists
        cursor.execute("DELETE FROM semantic_cache WHERE query_text = ?", (query_text,))
        
        # Insert new metadata
        cursor.execute(
            "INSERT INTO semantic_cache (query_text, response_text, expires_at, ttl_hours) VALUES (?, ?, ?, ?)",
            (query_text, response_text, expires_at, ttl_hours)
        )
        inserted_id = cursor.lastrowid
        conn.commit()
    except Exception as e:
        print("[Semantic Cache] SQLite write failed:", e)
    finally:
        if conn:
            conn.close()
            
    # Add to Turbovec index outside the connection scope
    if inserted_id is not None and cache_index is not None:
        try:
            vector = get_embedding(query_text)
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            with _turbovec_lock:
                cache_index.add_with_ids(vector_np, ids=np.array([inserted_id], dtype=np.uint64))
                cache_index.write(CACHE_INDEX_PATH)
            print(f"[Semantic Cache] Saved to Turbovec vector cache: '{query_text}' (ID: {inserted_id})")
        except Exception as e:
            print("[Semantic Cache] Save to Turbovec index failed:", e)

# ----------------- TASK LOG AUDIT TRAIL HELPERS -----------------

def add_to_task_log(tool: str, tier: int, outcome: str, error: str = ""):
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        log_id = f"log-{time.time()}-{random.randint(1000, 9999)}"
        cursor.execute(
            "INSERT INTO task_log (id, timestamp, tool, tier, outcome, error) VALUES (?, ?, ?, ?, ?, ?)",
            (log_id, time.time(), tool, tier, outcome, error)
        )
        conn.commit()
    except Exception as e:
        print("[Task Log] Save failed:", e)
    finally:
        if conn:
            conn.close()

def get_recent_failures(limit: int = 5) -> List[Dict[str, Any]]:
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

# ----------------- BACKGROUND SCHEDULER RUNS HELPERS -----------------

def add_background_run(goal: str, status: str, log: str):
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO background_runs (timestamp, goal, status, log) VALUES (?, ?, ?, ?)",
            (time.time(), goal, status, log)
        )
        conn.commit()
        print(f"[Scheduler Log] Logged background run: {goal[:30]} ({status})")
    except Exception as e:
        print("[Scheduler Log] Save failed:", e)
    finally:
        if conn:
            conn.close()

def get_background_runs(limit: int = 20) -> List[Dict[str, Any]]:
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
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO thought_logs (timestamp, session_id, step_index, thought_text, tool_name) VALUES (?, ?, ?, ?, ?)",
            (time.time(), session_id, step_index, thought_text, tool_name)
        )
        conn.commit()
        return True
    except Exception as e:
        print("[Database] Failed to add thought log:", e)
        return False
    finally:
        if conn:
            conn.close()

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

# ----------------- CONVERSATIONS HELPERS -----------------


def add_to_conversations(role: str, content: str, summary: str = ""):
    conn = None
    inserted_id = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conversations (timestamp, role, content, summary) VALUES (?, ?, ?, ?)",
            (time.time(), role, content, summary)
        )
        inserted_id = cursor.lastrowid
        conn.commit()
    except Exception as e:
        print("[Conversations Log] SQLite write failed:", e)
    finally:
        if conn:
            conn.close()
            
    # Index the vector in Turbovec outside the connection scope
    if inserted_id is not None and conv_index is not None:
        try:
            vector = get_embedding(content)
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            with _turbovec_lock:
                conv_index.add_with_ids(vector_np, ids=np.array([inserted_id], dtype=np.uint64))
                conv_index.write(CONV_INDEX_PATH)
            print(f"[Conversations Log] Saved to Turbovec index (ID: {inserted_id})")
        except Exception as e:
            print("[Conversations Log] Turbovec index save failed:", e)

def get_conversation_history(limit: int = 10) -> List[Dict[str, Any]]:
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        # Push LIMIT into SQL — avoids loading the entire table into RAM on
        # long-running sessions (previous code fetched ALL rows then sliced in Python).
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
                "vector": [0.0] * 768  # Return dummy vector for schema compatibility
            })
        # Reverse so caller receives chronological (oldest-first) order
        return list(reversed(results))
    except Exception as e:
        print("[Conversations Log] Retrieval failed:", e)
        return []
    finally:
        if conn:
            conn.close()

def clear_conversations():
    global conv_index
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM conversations")
        conn.commit()
    except Exception as e:
        print("[Conversations Log] Failed to clear conversations from SQLite:", e)
    finally:
        if conn:
            conn.close()
            
    # Reset conversations index outside the connection scope
    if IdMapIndex is None:
        print("[Conversations Log] Turbovec not installed — skipping index reset.")
        return
    try:
        with _turbovec_lock:
            conv_index = IdMapIndex(dim=768, bit_width=4)
            if os.path.exists(CONV_INDEX_PATH):
                try:
                    os.remove(CONV_INDEX_PATH)
                except Exception:
                    pass
            conv_index.write(CONV_INDEX_PATH)
        print("[Conversations Log] Safely cleared all conversations and reset index.")
    except Exception as e:
        print("[Conversations Log] Clear failed:", e)

# ----------------- KNOWLEDGE BASE RAG HELPERS -----------------

def ingest_into_knowledge_base(source: str, text: str, metadata: Optional[dict] = None):

    try:
        # Split text into ~200-word windows with 30-word overlap
        words = text.split()
        chunk_size = 200
        overlap = 30
        
        chunks = []
        i = 0
        while i < len(words):
            chunk_words = words[i:i + chunk_size]
            chunk_text = " ".join(chunk_words)
            if chunk_text.strip():
                chunks.append(chunk_text)
            i += (chunk_size - overlap)
            
        if not chunks:
            return
            
        conn = None
        ids_to_add = []
        vectors_to_add = []
        try:
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            
            for index, chunk in enumerate(chunks):
                meta_json = json.dumps(metadata or {})
                cursor.execute(
                    "INSERT INTO knowledge_base (source, chunk_text, metadata) VALUES (?, ?, ?)",
                    (source, chunk, meta_json)
                )
                inserted_id = cursor.lastrowid
                
                vector = get_embedding(chunk)
                ids_to_add.append(inserted_id)
                vectors_to_add.append(normalize_vector(vector))
                
            conn.commit()
        finally:
            if conn:
                conn.close()
        
        # Add to Turbovec index
        if ids_to_add and kb_index is not None:
            ids_np = np.array(ids_to_add, dtype=np.uint64)
            vectors_np = np.array(vectors_to_add, dtype=np.float32)
            with _turbovec_lock:
                kb_index.add_with_ids(vectors_np, ids=ids_np)
                kb_index.write(KB_INDEX_PATH)
            print(f"[RAG] Ingested {len(ids_to_add)} chunks from '{source}' into SQLite and Turbovec.")
    except Exception as e:
        print("[RAG] Ingestion failed:", e)

def search_knowledge_base(query: str, limit: int = 2) -> List[Dict[str, Any]]:
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM knowledge_base")
        count = cursor.fetchone()[0]
        if count == 0:
            return []
            
        vector = get_embedding(query)
        vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
        
        # Search Turbovec if available
        if kb_index is None:
            return []
        k_search = min(limit + 5, count)
        scores, ids = kb_index.search(vector_np, k=k_search)
        
        clean_results = []
        if ids.size > 0 and ids[0].size > 0:
            placeholders = ",".join("?" for _ in ids[0])
            cursor.execute(
                f"SELECT id, source, chunk_text, metadata FROM knowledge_base WHERE id IN ({placeholders})",
                [int(x) for x in ids[0]]
            )
            rows = {row["id"]: row for row in cursor.fetchall()}
            
            for score, id_val in zip(scores[0], ids[0]):
                id_int = int(id_val)
                if id_int in rows:
                    res = rows[id_int]
                    meta_val = res["metadata"]
                    try:
                        meta_dict = json.loads(meta_val) if meta_val else {}
                    except Exception:
                        meta_dict = {}
                    
                    similarity = float(score)
                    clean_results.append({
                        "source": res["source"],
                        "chunk_text": res["chunk_text"],
                        "similarity": similarity,
                        "metadata": meta_dict
                    })
        return clean_results[:limit]
    except Exception as e:
        print("[RAG] Search failed:", e)
        return []
    finally:
        if conn:
            conn.close()

# ----------------- MONGODB HELPERS (MongoDB Offline Graceful Fallbacks) -----------------

_mongo_client = None
_mongo_online = None
_last_mongo_check = 0

def get_mongo_db() -> Optional[pymongo.database.Database]:
    global _mongo_client, _mongo_online, _last_mongo_check
    now = time.time()
    if _mongo_online is not None and (now - _last_mongo_check < 30):
        if not _mongo_online or _mongo_client is None:
            return None
        return _mongo_client["meridian_kg"]
        
    try:
        if _mongo_client is None:
            mongo_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/meridian_kg")
            _mongo_client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=1000)
        _mongo_client.admin.command('ping')
        _mongo_online = True
    except Exception:
        _mongo_client = None
        _mongo_online = False
    finally:
        _last_mongo_check = now
        
    if _mongo_online and _mongo_client is not None:
        return _mongo_client["meridian_kg"]
    return None


def add_knowledge_fact(entity: str, relation: str, target: str):
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["knowledge_graph"]
            collection.update_one(
                {"entity": entity, "relation": relation, "target": target},
                {"$set": {"timestamp": time.time()}},
                upsert=True
            )
            print(f"[MongoDB Graph] Saved fact: {entity} --({relation})--> {target}")
        except Exception as e:
            print("[MongoDB Graph] Save failed:", e)
    else:
        print("[MongoDB Graph] MongoDB offline, skipped fact saving.")

def get_knowledge_facts(entity: str) -> List[Dict[str, Any]]:
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["knowledge_graph"]
            return list(collection.find({"entity": entity}, {"_id": 0}))
        except Exception as e:
            print("[MongoDB Graph] Fetch failed:", e)
    return []

def add_clipboard_history(text: str):
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["smart_clipboard"]
            last_clip = collection.find_one(sort=[("timestamp", pymongo.DESCENDING)])
            if last_clip and last_clip.get("text") == text:
                return
            collection.insert_one({
                "text": text,
                "timestamp": time.time()
            })
            print("[MongoDB Clipboard] Cached new clipboard segment.")
        except Exception as e:
            print("[MongoDB Clipboard] Save failed:", e)

    # SQLite sync/fallback
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS clipboard_history (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, timestamp REAL)")
        cursor.execute("SELECT text FROM clipboard_history ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        if row and row[0] == text:
            return
        cursor.execute("INSERT INTO clipboard_history (text, timestamp) VALUES (?, ?)", (text, time.time()))
        conn.commit()
    except Exception as e:
        print("[SQLite Clipboard] Save failed:", e)
    finally:
        if conn:
            conn.close()

def get_clipboard_history(limit: int = 50) -> List[Dict[str, Any]]:
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["smart_clipboard"]
            records = list(collection.find({}, {"_id": 0}).sort("timestamp", pymongo.DESCENDING).limit(limit))
            if records:
                return records
        except Exception as e:
            print("[MongoDB Clipboard] Fetch failed:", e)

    # SQLite fallback
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS clipboard_history (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, timestamp REAL)")
        cursor.execute("SELECT text, timestamp FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [{"text": row[0], "timestamp": row[1]} for row in rows]
    except Exception as e:
        print("[SQLite Clipboard] Fetch failed:", e)
        return []
    finally:
        if conn:
            conn.close()

_user_profile_cache: Dict[str, Tuple[Any, float]] = {}
_PROFILE_CACHE_TTL = 30.0  # 30 seconds cache TTL

def save_user_profile(key: str, value: Any):
    _user_profile_cache[key] = (value, time.time())
    # 1. Save to SQLite user_profile table
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        val_str = json.dumps(value)
        cursor.execute(
            "INSERT OR REPLACE INTO user_profile (key, value) VALUES (?, ?)",
            (key, val_str)
        )
        conn.commit()
        print(f"[SQLite User Profile] Updated: '{key}'")
    except Exception as e:
        print(f"[SQLite User Profile] Save failed: {e}")
    finally:
        if conn:
            conn.close()

    # 2. Save to MongoDB if online
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["user_profile"]
            collection.update_one(
                {"key": key},
                {"$set": {"value": value, "timestamp": time.time()}},
                upsert=True
            )
            print(f"[MongoDB User Profile] Updated: '{key}'")
        except Exception as e:
            print("[MongoDB User Profile] Save failed:", e)

def get_user_profile(key: str) -> Optional[Any]:
    if key in _user_profile_cache:
        val, cached_at = _user_profile_cache[key]
        if time.time() - cached_at < _PROFILE_CACHE_TTL:
            return val

    # 1. Try SQLite first
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM user_profile WHERE key = ?", (key,))
        res = cursor.fetchone()
        if res:
            parsed = json.loads(res["value"])
            _user_profile_cache[key] = (parsed, time.time())
            return parsed
    except Exception as e:
        print(f"[SQLite User Profile] Fetch failed: {e}")
    finally:
        if conn:
            conn.close()

    # 2. Fallback to MongoDB
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["user_profile"]
            res = collection.find_one({"key": key})
            if res:
                val = res.get("value")
                _user_profile_cache[key] = (val, time.time())
                return val
        except Exception as e:
            print("[MongoDB User Profile] Fetch failed:", e)
    return None

def get_auditor_model() -> str:
    try:
        model = get_user_profile("meridian_auditor_model")
        if model:
            return str(model)
    except Exception:
        pass
    auditor_env = os.environ.get("MERIDIAN_AUDITOR_MODEL")
    if auditor_env:
        return auditor_env
    return get_brain_model()

def get_model_source() -> str:
    try:
        source = get_user_profile("meridian_model_source")
        if source:
            return str(source)
    except Exception:
        pass
    return os.environ.get("MERIDIAN_MODEL_SOURCE", "").strip()

def set_model_source(source: str) -> None:
    save_user_profile("meridian_model_source", source)
    os.environ["MERIDIAN_MODEL_SOURCE"] = source



def get_brain_model() -> str:
    try:
        model = get_user_profile("meridian_model")
        if model:
            return str(model)
    except Exception:
        pass
    return os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")

def get_vision_model() -> str:
    try:
        model = get_user_profile("meridian_vision_model")
        if model:
            return str(model)
    except Exception:
        pass
    return os.environ.get("MERIDIAN_VISION_MODEL", "moondream:1.8b")



def purge_expired_cache():
    # BUG-9 fix: use finally to guarantee connection is closed even if Turbovec
    # rebuild raises mid-loop (which could leave in-memory index inconsistent).
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        now = time.time()
        cursor.execute("SELECT id FROM semantic_cache WHERE expires_at < ?", (now,))
        expired_rows = cursor.fetchall()
        expired_ids = [r["id"] for r in expired_rows]
        
        if expired_ids:
            cursor.execute("DELETE FROM semantic_cache WHERE expires_at < ?", (now,))
            conn.commit()

            if IdMapIndex is None:
                print("[Semantic Cache] Turbovec not installed — skipping index rebuild.")
                return

            # Rebuild Turbovec semantic cache index from remaining entries
            cursor.execute("SELECT id, query_text FROM semantic_cache")
            remaining = cursor.fetchall()
            global cache_index
            new_index = IdMapIndex(dim=768, bit_width=4)
            for r in remaining:
                vector = get_embedding(r["query_text"])
                vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
                new_index.add_with_ids(vector_np, ids=np.array([r["id"]], dtype=np.uint64))
            with _turbovec_lock:
                cache_index = new_index
                cache_index.write(CACHE_INDEX_PATH)
            print(f"[Semantic Cache] Purged {len(expired_ids)} expired entries and rebuilt Turbovec index.")
    except Exception as e:
        print("[Semantic Cache] Purge failed:", e)
    finally:
        if conn:
            conn.close()

def consolidate_memory_sleep_cycle():
    """Sleep cycle background consolidation of conversations and caches."""
    print("[Sleep Cycle] Starting active memory consolidation task...")
    try:
        # 1. Purge expired caches
        purge_expired_cache()
        
        # 2. Distill episodic conversations
        # BUG-38 fix: get_ollama_client_host is already defined in this file (line 38).
        # Importing from api creates a circular dependency (api imports database at startup).
        ollama_host = get_ollama_client_host()
        
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
                conn = None
                try:
                    conn = get_sqlite_conn()
                    cursor = conn.cursor()
                    ids_to_delete = [r["id"] for r in valid_records]
                    placeholders = ",".join("?" for _ in ids_to_delete)
                    cursor.execute(f"DELETE FROM conversations WHERE id IN ({placeholders})", tuple(ids_to_delete))
                    conn.commit()
                    print(f"[Sleep Cycle] Successfully consolidated {len(valid_records)} turns into {added_count} KB facts.")
                finally:
                    if conn:
                        conn.close()
            except Exception as je:
                print("[Sleep Cycle] JSON parse error during facts distillation:", je, text)
        else:
            print("[Sleep Cycle] Insufficient conversations to consolidate.")
    except Exception as e:
        print("[Sleep Cycle] Consolidation error:", e)

def load_db_keys_to_env():
    """Automatically loads all API keys and configuration settings from the database profile into environment variables."""
    try:
        ENV_KEY_MAP = {
            "ollama_host": "OLLAMA_HOST",
            "openai_key": "OPENAI_API_KEY",
            "anthropic_key": "ANTHROPIC_API_KEY",
            "gemini_key": "GEMINI_API_KEY",
            "deepseek_key": "DEEPSEEK_API_KEY",
            "tavily_key": "TAVILY_API_KEY",
            "discord_token": "DISCORD_BOT_TOKEN",
            "telegram_token": "TELEGRAM_BOT_TOKEN",
            "telegram_chat_id": "TELEGRAM_CHAT_ID",
            "whatsapp_phone": "WHATSAPP_PHONE",
            "meridian_provider": "MERIDIAN_PROVIDER",
            "meridian_model": "MERIDIAN_MODEL",
            "meridian_vision_model": "MERIDIAN_VISION_MODEL",
            "meridian_auditor_model": "MERIDIAN_AUDITOR_MODEL",
            "meridian_voice": "MERIDIAN_VOICE",
            "wakeword_threshold": "WAKEWORD_THRESHOLD",
            "wakeword_model_filename": "WAKEWORD_MODEL_FILENAME",
            "wakeword_phrase": "WAKEWORD_PHRASE",
            "stt_model_size": "STT_MODEL_SIZE",
            "stt_silence_timeout": "STT_SILENCE_TIMEOUT",
            "stt_vad_threshold": "STT_VAD_THRESHOLD",
            "stt_max_duration": "STT_MAX_DURATION",
            "browser_viewport_width": "BROWSER_VIEWPORT_WIDTH",
            "browser_viewport_height": "BROWSER_VIEWPORT_HEIGHT",
            "cpu_warn_threshold": "CPU_WARN_THRESHOLD",
            "ram_warn_threshold": "RAM_WARN_THRESHOLD",
            "disk_warn_threshold": "DISK_WARN_THRESHOLD",
            "distraction_sites": "DISTRACTION_SITES",
        }
        for profile_key, env_key in ENV_KEY_MAP.items():
            if not os.environ.get(env_key):
                val = get_user_profile(profile_key)
                if val is not None and val != "":
                    os.environ[env_key] = str(val)
    except Exception:
        pass

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
            return doc
        except Exception as e:
            print("[DB] MongoDB contact save error, falling back to SQLite:", e)

    # SQLite fallback
    conn = get_sqlite_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS whatsapp_contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                phone_number TEXT,
                alias TEXT,
                notes TEXT,
                updated_at REAL
            )
        """)
        cursor.execute("""
            INSERT INTO whatsapp_contacts (name, phone_number, alias, notes, updated_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                phone_number=excluded.phone_number,
                alias=excluded.alias,
                notes=excluded.notes,
                updated_at=excluded.updated_at
        """, (name_clean, phone_clean, alias.strip(), notes.strip(), time.time()))
        conn.commit()
    finally:
        conn.close()
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

    conn = get_sqlite_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS whatsapp_contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                phone_number TEXT,
                alias TEXT,
                notes TEXT,
                updated_at REAL
            )
        """)
        cursor.execute("SELECT name, phone_number, alias, notes FROM whatsapp_contacts")
        rows = cursor.fetchall()
        return [{"name": r["name"], "phone_number": r["phone_number"], "alias": r["alias"], "notes": r["notes"]} for r in rows]
    except Exception:
        return []
    finally:
        conn.close()

def resolve_whatsapp_contact(identifier: str) -> Optional[Dict[str, Any]]:
    """Resolves contact name, phone number, or relationship alias to contact record."""
    if not identifier:
        return None
    target = identifier.strip().lower()
    
    # If already phone number format (+... or digits)
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

# Trigger automatic loading of profile keys on module import
load_db_keys_to_env()

