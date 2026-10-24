import time
import threading
import numpy as np
from collections import OrderedDict
from typing import Optional, Dict, Any

from src.db.connection import get_db_cursor, get_sqlite_conn
from src.db.embeddings import get_embedding, normalize_vector
import src.db.vectors as vectors

# Cache statistics
_cache_stats: Dict[str, int] = {
    "hits": 0,
    "misses": 0,
    "tier1_hits": 0,
    "tier2_hits": 0,
    "requests": 0
}
_cache_stats_lock = threading.Lock()

# Tier-1 LRU Cache with dedicated thread-lock
_exact_match_cache: OrderedDict = OrderedDict()
_exact_cache_lock = threading.RLock()
_EXACT_CACHE_MAX_SIZE = 500

def check_semantic_cache(query_text: str) -> Optional[str]:
    """Two-tier semantic cache check (Tier-1: Memory LRU, Tier-2: Turbovec Vector Search)."""
    global _cache_stats
    with _cache_stats_lock:
        _cache_stats["requests"] += 1

    now = time.time()

    # Tier-1: Thread-Safe Exact Match LRU Cache (0ms, skips embedding generation)
    with _exact_cache_lock:
        if query_text in _exact_match_cache:
            val, expires_at = _exact_match_cache[query_text]
            if expires_at > now:
                _exact_match_cache.move_to_end(query_text)
                with _cache_stats_lock:
                    _cache_stats["hits"] += 1
                    _cache_stats["tier1_hits"] += 1
                print(f"[Semantic Cache] Tier-1 Exact Match HIT: '{query_text}'")
                return val
            else:
                del _exact_match_cache[query_text]

    # Tier-2: Cosine Similarity Vector Cache (Turbovec + SQLite lookup)
    # PERF-FIX: Stop running expensive disk DELETE operations on the read path.
    # Expiry is filtered in the SELECT query.
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM semantic_cache WHERE expires_at > ?", (now,))
        count = cursor.fetchone()[0]

        if count > 0 and vectors.cache_index is not None:
            vector = get_embedding(query_text)
            if vector is not None:
                vector_np = np.array([normalize_vector(vector)], dtype=np.float32)

                # Thread-safe Turbovec search
                with vectors._turbovec_lock:
                    scores, ids = vectors.cache_index.search(vector_np, k=min(2, count))

                if ids.size > 0 and ids[0].size > 0:
                    for score, id_val in zip(scores[0], ids[0]):
                        if score > 0.96:
                            cursor.execute(
                                "SELECT response_text, expires_at FROM semantic_cache WHERE id = ? AND expires_at > ?",
                                (int(id_val), now)
                            )
                            res = cursor.fetchone()
                            if res and res["response_text"] and res["response_text"].strip():
                                print(f"[Semantic Cache] Tier-2 Vector Match HIT: '{query_text}' (similarity: {score:.4f})")
                                with _exact_cache_lock:
                                    _exact_match_cache[query_text] = (res["response_text"], res["expires_at"])
                                    _exact_match_cache.move_to_end(query_text)
                                    if len(_exact_match_cache) > _EXACT_CACHE_MAX_SIZE:
                                        _exact_match_cache.popitem(last=False)
                                with _cache_stats_lock:
                                    _cache_stats["hits"] += 1
                                    _cache_stats["tier2_hits"] += 1
                                return res["response_text"]
    except Exception as e:
        print("[Semantic Cache] Search failed:", e)
    finally:
        if conn:
            conn.close()

    with _cache_stats_lock:
        _cache_stats["misses"] += 1
    return None

def get_near_miss_semantic_cache(query_text: str, min_score: float = 0.60, max_score: float = 0.85) -> Optional[str]:
    """Retrieves near-miss cached query responses for contextual adaptation."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        now = time.time()
        cursor.execute("SELECT COUNT(*) FROM semantic_cache WHERE expires_at > ?", (now,))
        count = cursor.fetchone()[0]
        if count > 0 and vectors.cache_index is not None:
            vector = get_embedding(query_text)
            if vector is not None:
                vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
                with vectors._turbovec_lock:
                    scores, ids = vectors.cache_index.search(vector_np, k=min(2, count))
                if ids.size > 0 and ids[0].size > 0:
                    for score, id_val in zip(scores[0], ids[0]):
                        if min_score <= score <= max_score:
                            cursor.execute(
                                "SELECT response_text FROM semantic_cache WHERE id = ? AND expires_at > ?",
                                (int(id_val), now)
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

def get_cache_statistics() -> dict:
    """Returns telemetry and hit rate statistics for semantic cache."""
    global _cache_stats
    with _cache_stats_lock:
        stats: Dict[str, Any] = dict(_cache_stats)

    total_requests = stats["requests"]
    if total_requests > 0:
        hit_rate = (stats["hits"] / total_requests) * 100
        tier1_rate = (stats["tier1_hits"] / total_requests) * 100
        tier2_rate = (stats["tier2_hits"] / total_requests) * 100
    else:
        hit_rate = tier1_rate = tier2_rate = 0.0

    with _exact_cache_lock:
        cache_len = len(_exact_match_cache)

    stats.update({
        "hit_rate_percent": round(hit_rate, 2),
        "tier1_rate_percent": round(tier1_rate, 2),
        "tier2_rate_percent": round(tier2_rate, 2),
        "cache_size": cache_len,
        "max_cache_size": _EXACT_CACHE_MAX_SIZE
    })
    return stats

def add_to_semantic_cache(query_text: str, response_text: str, ttl_hours: int = 24):
    """Persists query and response into memory LRU and Turbovec vector cache."""
    ttl_seconds = ttl_hours * 3600
    expires_at = time.time() + ttl_seconds

    with _exact_cache_lock:
        _exact_match_cache[query_text] = (response_text, expires_at)
        _exact_match_cache.move_to_end(query_text)
        if len(_exact_match_cache) > _EXACT_CACHE_MAX_SIZE:
            _exact_match_cache.popitem(last=False)

    inserted_id = None
    try:
        with get_db_cursor() as cursor:
            cursor.execute("DELETE FROM semantic_cache WHERE query_text = ?", (query_text,))
            cursor.execute(
                "INSERT INTO semantic_cache (query_text, response_text, expires_at, ttl_hours) VALUES (?, ?, ?, ?)",
                (query_text, response_text, expires_at, ttl_hours)
            )
            inserted_id = cursor.lastrowid
    except Exception as e:
        print("[Semantic Cache] SQLite write failed:", e)

    if inserted_id is not None and vectors.cache_index is not None:
        try:
            vector = get_embedding(query_text)
            if vector is None:
                print("[Semantic Cache] Skipped Turbovec index save (embedding unavailable).")
                return
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            with vectors._turbovec_lock:
                vectors.cache_index.add_with_ids(vector_np, ids=np.array([inserted_id], dtype=np.uint64))
                vectors.cache_index.write(vectors.CACHE_INDEX_PATH)
            print(f"[Semantic Cache] Saved to Turbovec vector cache: '{query_text}' (ID: {inserted_id})")
        except Exception as e:
            print("[Semantic Cache] Save to Turbovec index failed:", e)

def purge_expired_cache():
    """Purges expired entries from SQLite and rebuilds Turbovec vector index."""
    try:
        now = time.time()
        with get_db_cursor() as cursor:
            cursor.execute("SELECT id FROM semantic_cache WHERE expires_at < ?", (now,))
            expired_rows = cursor.fetchall()
            expired_ids = [r["id"] for r in expired_rows]

            if not expired_ids:
                return

            cursor.execute("DELETE FROM semantic_cache WHERE expires_at < ?", (now,))

            if vectors.IdMapIndex is None:
                print("[Semantic Cache] Turbovec not installed — skipping index rebuild.")
                return

            cursor.execute("SELECT id, query_text FROM semantic_cache")
            remaining = cursor.fetchall()

        # Rebuild Turbovec index outside SQLite transaction
        new_index = vectors.IdMapIndex(dim=768, bit_width=4)
        for r in remaining:
            vector = get_embedding(r["query_text"])
            if vector is None:
                continue
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            new_index.add_with_ids(vector_np, ids=np.array([r["id"]], dtype=np.uint64))

        with vectors._turbovec_lock:
            vectors.cache_index = new_index
            vectors.cache_index.write(vectors.CACHE_INDEX_PATH)
        print(f"[Semantic Cache] Purged {len(expired_ids)} expired entries and rebuilt Turbovec index.")
    except Exception as e:
        print("[Semantic Cache] Purge failed:", e)
