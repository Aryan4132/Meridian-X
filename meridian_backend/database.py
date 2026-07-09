import os
import time
import json
import random
import sqlite3
import pymongo
import threading
import numpy as np
from turbovec import IdMapIndex
from typing import Optional, List, Dict, Any

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
    try:
        client = get_ollama_client()
        res = client.embeddings(model="nomic-embed-text", prompt=text)
        # BUG-2 fix: ollama SDK returns an EmbeddingResponse object, not a dict.
        # Use attribute access first, fall back to dict .get() for older lib versions.
        embedding = res.embedding if hasattr(res, "embedding") else res.get("embedding")
        if embedding:
            return embedding
    except Exception as e:
        print("Failed to get embedding:", e)
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
    conn = sqlite3.connect(SQLITE_DB_PATH, timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def init_turbovec_indexes():
    global kb_index, cache_index, conv_index
    
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
            expires_at REAL
        )
    """)
    
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
        CREATE TABLE IF NOT EXISTS user_profile (
            key TEXT PRIMARY KEY,
            value TEXT
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

_exact_match_cache = {}

def check_semantic_cache(query_text: str) -> Optional[str]:
    # Tier-1: Exact Match LRU/Memory cache (0ms, skips embedding generation)
    if query_text in _exact_match_cache:
        val, expires_at = _exact_match_cache[query_text]
        if expires_at > time.time():
            print(f"[Semantic Cache] Tier-1 Exact Match HIT: '{query_text}'")
            return val
        else:
            del _exact_match_cache[query_text]

    # Tier-2: Cosine Similarity Vector Cache (Turbovec + SQLite lookup)
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM semantic_cache")
        count = cursor.fetchone()[0]
        
        if count > 0:
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
                        if res and res["expires_at"] > time.time():
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

def add_to_semantic_cache(query_text: str, response_text: str, ttl_seconds: int = 86400):
    expires_at = time.time() + ttl_seconds
    _exact_match_cache[query_text] = (response_text, expires_at)
    
    conn = None
    inserted_id = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        
        # Delete old entry with same query_text if exists
        cursor.execute("DELETE FROM semantic_cache WHERE query_text = ?", (query_text,))
        
        # Insert new metadata
        cursor.execute(
            "INSERT INTO semantic_cache (query_text, response_text, expires_at) VALUES (?, ?, ?)",
            (query_text, response_text, expires_at)
        )
        inserted_id = cursor.lastrowid
        conn.commit()
    except Exception as e:
        print("[Semantic Cache] SQLite write failed:", e)
    finally:
        if conn:
            conn.close()
            
    # Add to Turbovec index outside the connection scope
    if inserted_id is not None:
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
    if inserted_id is not None:
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

def ingest_into_knowledge_base(source: str, text: str, metadata: dict = None):
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
        if ids_to_add:
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
        
        # Search Turbovec
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
        if not _mongo_online:
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
        
    if _mongo_online:
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

def get_clipboard_history(limit: int = 10) -> List[Dict[str, Any]]:
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["smart_clipboard"]
            return list(collection.find({}, {"_id": 0}).sort("timestamp", pymongo.DESCENDING).limit(limit))
        except Exception as e:
            print("[MongoDB Clipboard] Fetch failed:", e)
    return []

def save_user_profile(key: str, value: Any):
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
    # 1. Try SQLite first
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM user_profile WHERE key = ?", (key,))
        res = cursor.fetchone()
        if res:
            return json.loads(res["value"])
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
                return res.get("value")
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
    return os.environ.get("MERIDIAN_AUDITOR_MODEL", "qwen2.5-coder:1.5b-instruct-q8_0")

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
                    cursor.execute(f"DELETE FROM conversations WHERE id IN ({placeholders})", ids_to_delete)
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
