import json
import time
import re
import math
import numpy as np
from typing import Optional, List, Dict, Any, Tuple

from src.db.connection import get_db_cursor, get_sqlite_conn, get_mongo_db
from src.db.embeddings import get_embedding, normalize_vector
import src.db.vectors as vectors

def ingest_into_knowledge_base(source: str, text: str, metadata: Optional[dict] = None):
    """Chunks text and ingests vectors into knowledge_base SQLite table and Turbovec index."""
    try:
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

        ids_to_add = []
        vectors_to_add = []
        with get_db_cursor() as cursor:
            for index, chunk in enumerate(chunks):
                meta_json = json.dumps(metadata or {})
                cursor.execute(
                    "INSERT INTO knowledge_base (source, chunk_text, metadata) VALUES (?, ?, ?)",
                    (source, chunk, meta_json)
                )
                inserted_id = cursor.lastrowid
                vector = get_embedding(chunk)
                if vector is None:
                    print(f"[RAG] Skipped Turbovec index for chunk {index} (embedding unavailable).")
                    continue
                ids_to_add.append(inserted_id)
                vectors_to_add.append(normalize_vector(vector))

        if ids_to_add and vectors.kb_index is not None:
            ids_np = np.array(ids_to_add, dtype=np.uint64)
            vectors_np = np.array(vectors_to_add, dtype=np.float32)
            with vectors._turbovec_lock:
                vectors.kb_index.add_with_ids(vectors_np, ids=ids_np)
                vectors.kb_index.write(vectors.KB_INDEX_PATH)
            print(f"[RAG] Ingested {len(ids_to_add)} chunks from '{source}' into SQLite and Turbovec.")
    except Exception as e:
        print("[RAG] Ingestion failed:", e)

def search_knowledge_base(query: str, limit: int = 2) -> List[Dict[str, Any]]:
    """Performs semantic similarity search across knowledge base chunks."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM knowledge_base")
        count = cursor.fetchone()[0]
        if count == 0:
            return []

        vector = get_embedding(query)
        if vector is None:
            return []
        vector_np = np.array([normalize_vector(vector)], dtype=np.float32)

        if vectors.kb_index is None:
            return []

        k_search = min(limit + 5, count)
        with vectors._turbovec_lock:
            scores, ids = vectors.kb_index.search(vector_np, k=k_search)

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

                    clean_results.append({
                        "source": res["source"],
                        "chunk_text": res["chunk_text"],
                        "similarity": float(score),
                        "metadata": meta_dict
                    })
        return clean_results[:limit]
    except Exception as e:
        print("[RAG] Search failed:", e)
        return []
    finally:
        if conn:
            conn.close()

def compute_bm25_scores(query: str, docs: List[Dict[str, Any]], k1: float = 1.5, b: float = 0.75) -> Dict[int, float]:
    """Computes BM25 keyword matching scores for candidate documents."""
    query_tokens = re.findall(r"\w+", query.lower())
    if not query_tokens or not docs:
        return {}

    N = len(docs)
    doc_tokens = {}
    for d in docs:
        text = d.get("content") or d.get("chunk_text") or ""
        doc_tokens[d["id"]] = re.findall(r"\w+", text.lower())

    avgdl = sum(len(toks) for toks in doc_tokens.values()) / max(1, N)

    scores: Dict[int, float] = {}
    for q_term in set(query_tokens):
        n_q = sum(1 for toks in doc_tokens.values() if q_term in toks)
        if n_q == 0:
            continue
        idf = math.log((N - n_q + 0.5) / (n_q + 0.5) + 1.0)
        for doc in docs:
            doc_id = doc["id"]
            toks = doc_tokens[doc_id]
            f = toks.count(q_term)
            if f > 0:
                doc_len = len(toks)
                num = f * (k1 + 1)
                den = f + k1 * (1 - b + b * (doc_len / max(1.0, avgdl)))
                scores[doc_id] = scores.get(doc_id, 0.0) + idf * (num / den)
    return scores

def hybrid_search_knowledge_base(query: str, limit: int = 5, bm25_weight: float = 0.5) -> List[Dict[str, Any]]:
    """Executes Hybrid Sparse-Dense (BM25 + Turbovec RRF) search on knowledge_base chunks."""
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, source, chunk_text, metadata FROM knowledge_base")
        all_rows = [dict(row) for row in cursor.fetchall()]
        if not all_rows:
            return []

        # 1. Dense ranking via Turbovec
        dense_ranks: Dict[int, int] = {}
        vector = get_embedding(query)
        if vector is not None and vectors.kb_index is not None:
            vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
            k_search = min(limit * 3, len(all_rows))
            with vectors._turbovec_lock:
                scores, ids = vectors.kb_index.search(vector_np, k=k_search)
            if ids.size > 0 and ids[0].size > 0:
                for rank, id_val in enumerate(ids[0]):
                    dense_ranks[int(id_val)] = rank + 1

        # 2. Sparse ranking via SQLite FTS5 (C-level BM25) or pure Python BM25 fallback
        sparse_ranks: Dict[int, int] = {}
        try:
            fts_query = re.sub(r'[^\w\s]', '', query).strip()
            if fts_query:
                # Query SQLite FTS5 for ranked matches
                cursor.execute(
                    "SELECT rowid FROM knowledge_base_fts WHERE knowledge_base_fts MATCH ? ORDER BY bm25(knowledge_base_fts) LIMIT ?",
                    (fts_query, len(all_rows))
                )
                fts_rows = cursor.fetchall()
                for rank, r in enumerate(fts_rows):
                    sparse_ranks[int(r[0])] = rank + 1
        except Exception:
            pass

        if not sparse_ranks:
            bm25_scores = compute_bm25_scores(query, all_rows)
            bm25_sorted = sorted(bm25_scores.items(), key=lambda x: x[1], reverse=True)
            sparse_ranks = {doc_id: rank + 1 for rank, (doc_id, _) in enumerate(bm25_sorted)}

        # 3. Reciprocal Rank Fusion (RRF)
        docs_by_id = {doc["id"]: doc for doc in all_rows}
        rrf_scores: List[Tuple[float, Dict[str, Any]]] = []
        c = 60.0

        dense_w = 1.0 - bm25_weight
        sparse_w = bm25_weight

        for doc_id, doc in docs_by_id.items():
            d_rank = dense_ranks.get(doc_id, 9999)
            s_rank = sparse_ranks.get(doc_id, 9999)
            if d_rank >= 9999 and s_rank >= 9999:
                continue
            score = (dense_w / (c + d_rank)) + (sparse_w / (c + s_rank))
            rrf_scores.append((score, doc))

        rrf_scores.sort(key=lambda x: x[0], reverse=True)

        results = []
        for score, doc in rrf_scores[:limit]:
            meta_val = doc.get("metadata")
            meta_dict = {}
            if isinstance(meta_val, str) and meta_val:
                try:
                    meta_dict = json.loads(meta_val)
                except Exception:
                    pass
            elif isinstance(meta_val, dict):
                meta_dict = meta_val
            results.append({
                "id": doc["id"],
                "source": doc["source"],
                "chunk_text": doc["chunk_text"],
                "score": round(score, 5),
                "metadata": meta_dict
            })
        return results
    except Exception as e:
        print("[RAG] Hybrid search failed:", e)
        return []
    finally:
        if conn:
            conn.close()

def add_knowledge_fact(entity: str, relation: str, target: str):
    """Saves structured knowledge graph triple into MongoDB with SQLite offline sync/fallback."""
    now = time.time()
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["knowledge_graph"]
            collection.update_one(
                {"entity": entity, "relation": relation, "target": target},
                {"$set": {"timestamp": now}},
                upsert=True
            )
            print(f"[MongoDB Graph] Saved fact: {entity} --({relation})--> {target}")
        except Exception as e:
            print("[MongoDB Graph] Save failed, syncing to SQLite:", e)

    # SQLite fallback / dual-sync
    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                "DELETE FROM knowledge_graph WHERE entity = ? AND relation = ? AND target = ?",
                (entity, relation, target)
            )
            cursor.execute(
                "INSERT INTO knowledge_graph (entity, relation, target, timestamp) VALUES (?, ?, ?, ?)",
                (entity, relation, target, now)
            )
            print(f"[SQLite Graph] Synced fact: {entity} --({relation})--> {target}")
    except Exception as e:
        print("[SQLite Graph] Save failed:", e)

def get_knowledge_facts(entity: str) -> List[Dict[str, Any]]:
    """Fetches knowledge graph relations for a specific entity from MongoDB or SQLite fallback."""
    db_conn = get_mongo_db()
    if db_conn is not None:
        try:
            collection = db_conn["knowledge_graph"]
            facts = list(collection.find({"entity": entity}, {"_id": 0}))
            if facts:
                return facts
        except Exception as e:
            print("[MongoDB Graph] Fetch failed, falling back to SQLite:", e)

    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT entity, relation, target, timestamp FROM knowledge_graph WHERE entity = ?", (entity,))
        rows = cursor.fetchall()
        return [{"entity": r["entity"], "relation": r["relation"], "target": r["target"], "timestamp": r["timestamp"]} for r in rows]
    except Exception as e:
        print("[SQLite Graph] Fetch failed:", e)
        return []
    finally:
        if conn:
            conn.close()
