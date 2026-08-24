import os
import time
import json
import sqlite3
import ast
import re
import math
import numpy as np
from typing import List, Tuple, Dict, Any

try:
    from turbovec import IdMapIndex  # type: ignore # pyright: ignore[reportMissingImports]
except ImportError:
    IdMapIndex = None

from database import get_sqlite_conn, get_embedding, normalize_vector, db_dir, _turbovec_lock

DOCS_INDEX_PATH = os.path.join(db_dir, "docs_index.tq")
docs_index = None

def init_docs_index():
    global docs_index
    if docs_index is not None or IdMapIndex is None:
        return
    
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS offline_docs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT,
                section TEXT,
                content TEXT,
                embedding TEXT
            )
        """)
        
        try:
            cursor.execute("ALTER TABLE offline_docs ADD COLUMN embedding TEXT")
        except Exception:
            pass
            
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS indexed_files (
                file_path TEXT PRIMARY KEY,
                last_modified REAL,
                sha256 TEXT
            )
        """)
        try:
            cursor.execute("ALTER TABLE indexed_files ADD COLUMN sha256 TEXT")
        except Exception:
            pass
        conn.commit()
        conn.close()
    except Exception as e:
        print("[Docs Indexer] SQLite initialization failed:", e)

    if IdMapIndex is not None:
        if os.path.exists(DOCS_INDEX_PATH):
            try:
                docs_index = IdMapIndex.load(DOCS_INDEX_PATH)
                print("[Docs Indexer] Loaded existing docset index.")
            except Exception as e:
                print("[Docs Indexer] Failed to load index, creating new:", e)
                docs_index = IdMapIndex(dim=768, bit_width=4)
        else:
            docs_index = IdMapIndex(dim=768, bit_width=4)

def _extract_ast_chunks(code_text: str) -> List[Tuple[str, str]]:
    """Parses Python source code into semantic AST chunks (classes, methods, functions)."""
    chunks: List[Tuple[str, str]] = []
    try:
        tree = ast.parse(code_text)
        lines = code_text.splitlines()

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                sec_name = f"Function: {node.name}"
                start_line = max(1, node.lineno) - 1
                end_line = getattr(node, 'end_lineno', start_line + 20)
                body = "\n".join(lines[start_line:end_line])
                chunks.append((sec_name, body))
            elif isinstance(node, ast.ClassDef):
                sec_name = f"Class: {node.name}"
                start_line = max(1, node.lineno) - 1
                end_line = getattr(node, 'end_lineno', start_line + 30)
                body = "\n".join(lines[start_line:end_line])
                chunks.append((sec_name, body))
    except Exception:
        pass
    if not chunks:
        chunks.append(("Code", code_text))
    return chunks

def _tokenize(text: str) -> List[str]:
    """Simple lowercase alphanumeric tokenizer for BM25."""
    return re.findall(r"\w+", text.lower())

def compute_bm25_scores(query: str, docs: List[Dict[str, Any]], k1: float = 1.5, b: float = 0.75) -> Dict[int, float]:
    """Computes BM25 keyword matching scores for candidate documents."""
    query_tokens = _tokenize(query)
    if not query_tokens or not docs:
        return {}

    N = len(docs)
    doc_tokens = {d["id"]: _tokenize(d["content"]) for d in docs}
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

def index_docs_directory(docs_dir: str):
    """Scans and incrementally indexes all markdown (.md) and python (.py) files in a directory."""
    init_docs_index()
    global docs_index

    if not os.path.exists(docs_dir):
        print(f"[Docs Indexer] Directory not found: {docs_dir}")
        return

    import hashlib
    def get_file_sha256(filepath: str) -> str:
        h = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                while chunk := f.read(8192):
                    h.update(chunk)
            return h.hexdigest()
        except Exception:
            return ""

    conn = get_sqlite_conn()
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT file_path, last_modified, sha256 FROM indexed_files")
        indexed_info = {row["file_path"]: (row["last_modified"], row["sha256"]) for row in cursor.fetchall()}

        any_changed = False

        for root, _, files in os.walk(docs_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in [".md", ".py"]:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, docs_dir).replace("\\", "/")

                    mtime = os.path.getmtime(file_path)
                    sha256 = get_file_sha256(file_path)

                    if rel_path in indexed_info:
                        db_mtime, db_sha = indexed_info[rel_path]
                        if db_mtime >= mtime or (db_sha and db_sha == sha256):
                            continue

                    any_changed = True
                    print(f"[Docs Indexer] Re-indexing modified file: {rel_path}")

                    cursor.execute("DELETE FROM offline_docs WHERE file_path = ?", (rel_path,))

                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            text = f.read()

                        chunks = []
                        if ext == ".py":
                            chunks = _extract_ast_chunks(text)
                        else:
                            current_section = "General"
                            lines = text.splitlines()
                            current_chunk = []
                            for line in lines:
                                if line.startswith("#"):
                                    if current_chunk:
                                        chunks.append((current_section, "\n".join(current_chunk).strip()))
                                        current_chunk = []
                                    current_section = line.strip("# ")
                                else:
                                    current_chunk.append(line)
                            if current_chunk:
                                chunks.append((current_section, "\n".join(current_chunk).strip()))

                        for sec, chunk_txt in chunks:
                            if not chunk_txt.strip():
                                continue

                            vector = get_embedding(chunk_txt)
                            if vector is None:
                                continue
                            vector_json = json.dumps(vector)

                            cursor.execute(
                                "INSERT INTO offline_docs (file_path, section, content, embedding) VALUES (?, ?, ?, ?)",
                                (rel_path, sec, chunk_txt, vector_json)
                            )

                        cursor.execute(
                            "INSERT OR REPLACE INTO indexed_files (file_path, last_modified, sha256) VALUES (?, ?, ?)",
                            (rel_path, mtime, sha256)
                        )

                    except Exception as fe:
                        print(f"[Docs Indexer] Failed to read/parse '{file}': {fe}")

        if any_changed:
            conn.commit()

            if IdMapIndex is not None:
                print("[Docs Indexer] Rebuilding Turbovec docs index...")
                cursor.execute("SELECT id, embedding FROM offline_docs")
                all_rows = cursor.fetchall()

                new_index = IdMapIndex(dim=768, bit_width=4)
                ids_to_add = []
                vectors_to_add = []

                for r in all_rows:
                    if r["embedding"]:
                        try:
                            vector = json.loads(r["embedding"])
                            ids_to_add.append(r["id"])
                            vectors_to_add.append(normalize_vector(vector))
                        except Exception:
                            pass

                if ids_to_add:
                    ids_np = np.array(ids_to_add, dtype=np.uint64)
                    vectors_np = np.array(vectors_to_add, dtype=np.float32)
                    new_index.add_with_ids(vectors_np, ids=ids_np)

                with _turbovec_lock:
                    docs_index = new_index
                    docs_index.write(DOCS_INDEX_PATH)
                print("[Docs Indexer] Rebuild complete.")
            else:
                print("[Docs Indexer] SQLite metadata updated (Turbovec disabled on this platform).")
        else:
            print("[Docs Indexer] All documents are up to date (0 files changed).")
    finally:
        conn.close()

def search_offline_docs(query: str, limit: int = 5):
    """Executes Hybrid Sparse-Dense (BM25 + Turbovec RRF) search on indexed documents and AST code."""
    init_docs_index()
    global docs_index

    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, file_path, section, content, embedding FROM offline_docs")
        all_rows = [dict(row) for row in cursor.fetchall()]
        conn.close()

        if not all_rows:
            return []

        dense_ranks: Dict[int, int] = {}
        query_vector = get_embedding(query)
        if query_vector is not None:
            query_arr = np.array(normalize_vector(query_vector), dtype=np.float32)
            dense_scores = []
            for doc in all_rows:
                if doc["embedding"]:
                    try:
                        doc_v = np.array(normalize_vector(json.loads(doc["embedding"])), dtype=np.float32)
                        sim = float(np.dot(query_arr, doc_v))
                        dense_scores.append((doc["id"], sim))
                    except Exception:
                        pass
            dense_scores.sort(key=lambda x: x[1], reverse=True)
            for rank, (doc_id, _) in enumerate(dense_scores):
                dense_ranks[doc_id] = rank + 1

        bm25_scores = compute_bm25_scores(query, all_rows)
        bm25_sorted = sorted(bm25_scores.items(), key=lambda x: x[1], reverse=True)
        sparse_ranks: Dict[int, int] = {doc_id: rank + 1 for rank, (doc_id, _) in enumerate(bm25_sorted)}

        docs_by_id = {doc["id"]: doc for doc in all_rows}
        rrf_scores: List[Tuple[float, dict]] = []

        for doc_id, doc in docs_by_id.items():
            d_rank = dense_ranks.get(doc_id, 999)
            s_rank = sparse_ranks.get(doc_id, 999)
            rrf_score = (0.5 / (60.0 + d_rank)) + (0.5 / (60.0 + s_rank))
            rrf_scores.append((rrf_score, doc))

        rrf_scores.sort(key=lambda x: x[0], reverse=True)

        clean_results = [
            {
                "id": doc["id"],
                "file_path": doc["file_path"],
                "section": doc["section"],
                "content": doc["content"],
                "score": score
            }
            for score, doc in rrf_scores[:limit]
        ]
        return clean_results
    except Exception as e:
        print("[Docs Indexer] Hybrid Search failed:", e)
        return []
