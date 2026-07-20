import os
import time
import json
import sqlite3
import numpy as np
from turbovec import IdMapIndex
from database import get_sqlite_conn, get_embedding, normalize_vector, db_dir, _turbovec_lock

DOCS_INDEX_PATH = os.path.join(db_dir, "docs_index.tq")
docs_index = None

def init_docs_index():
    global docs_index
    if docs_index is not None:
        return
    
    # Initialize SQLite table for docs metadata
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
        
        # Check if we need to add the embedding column for backward compatibility
        try:
            cursor.execute("ALTER TABLE offline_docs ADD COLUMN embedding TEXT")
        except Exception:
            pass # Column already exists
            
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
            pass # already exists
        conn.commit()
        conn.close()
    except Exception as e:
        print("[Docs Indexer] SQLite initialization failed:", e)

    # Initialize Turbovec index
    if os.path.exists(DOCS_INDEX_PATH):
        try:
            docs_index = IdMapIndex.load(DOCS_INDEX_PATH)
            print("[Docs Indexer] Loaded existing docset index.")
        except Exception as e:
            print("[Docs Indexer] Failed to load index, creating new:", e)
            docs_index = IdMapIndex(dim=768, bit_width=4)
    else:
        docs_index = IdMapIndex(dim=768, bit_width=4)

def index_docs_directory(docs_dir: str):
    """Scans and incrementally indexes all markdown (.md) documents in a directory."""
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
        
        # Load last modified times and SHA-256 of already indexed files
        cursor.execute("SELECT file_path, last_modified, sha256 FROM indexed_files")
        indexed_info = {row["file_path"]: (row["last_modified"], row["sha256"]) for row in cursor.fetchall()}
        
        any_changed = False
        
        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.lower().endswith(".md"):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, docs_dir).replace("\\", "/")
                    
                    mtime = os.path.getmtime(file_path)
                    sha256 = get_file_sha256(file_path)
                    # Skip indexing if the file has not been modified since the last run OR sha256 matches
                    if rel_path in indexed_info:
                        db_mtime, db_sha = indexed_info[rel_path]
                        if db_mtime >= mtime or (db_sha and db_sha == sha256):
                            continue
                        
                    any_changed = True
                    print(f"[Docs Indexer] Re-indexing modified file: {rel_path}")
                    
                    # Delete existing entries for this file
                    cursor.execute("DELETE FROM offline_docs WHERE file_path = ?", (rel_path,))
                    
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            text = f.read()
                            
                        # Simple chunking by headers or double newlines
                        chunks = []
                        current_section = "General"
                        lines = text.splitlines()
                        current_chunk = []
                        
                        for line in lines:
                            if line.startswith("#"):
                                # Save current chunk if exists
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
                                
                            # Generate embedding
                            vector = get_embedding(chunk_txt)
                            vector_json = json.dumps(vector)
                            
                            # Insert metadata and serialized vector into SQLite
                            cursor.execute(
                                "INSERT INTO offline_docs (file_path, section, content, embedding) VALUES (?, ?, ?, ?)",
                                (rel_path, sec, chunk_txt, vector_json)
                            )
                            
                        # Update modification log table
                        cursor.execute(
                            "INSERT OR REPLACE INTO indexed_files (file_path, last_modified, sha256) VALUES (?, ?, ?)",
                            (rel_path, mtime, sha256)
                        )
                            
                    except Exception as fe:
                        print(f"[Docs Indexer] Failed to read/parse '{file}': {fe}")
                        
        if any_changed:
            conn.commit()
            
            # Rebuild the entire Turbovec docs index from stored SQLite vectors
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
            print("[Docs Indexer] All documents are up to date (0 files changed).")
    finally:
        conn.close()

def search_offline_docs(query: str, limit: int = 5):
    """Executes offline vector search on indexed manuals and documentation."""
    init_docs_index()
    global docs_index
    
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM offline_docs")
        count = cursor.fetchone()[0]
        if count == 0:
            conn.close()
            return []
            
        vector = get_embedding(query)
        vector_np = np.array([normalize_vector(vector)], dtype=np.float32)
        
        k_search = min(limit, count)
        scores, ids = docs_index.search(vector_np, k=k_search)
        
        clean_results = []
        if ids.size > 0 and ids[0].size > 0:
            placeholders = ",".join("?" for _ in ids[0])
            cursor.execute(
                f"SELECT id, file_path, section, content FROM offline_docs WHERE id IN ({placeholders})",
                [int(x) for x in ids[0]]
            )
            rows = {row["id"]: row for row in cursor.fetchall()}
            
            for score, id_val in zip(scores[0], ids[0]):
                id_int = int(id_val)
                if id_int in rows:
                    res = rows[id_int]
                    clean_results.append({
                        "id": res["id"],
                        "file_path": res["file_path"],
                        "section": res["section"],
                        "content": res["content"],
                        "score": float(score)
                    })
        conn.close()
        return clean_results
    except Exception as e:
        print("[Docs Indexer] Search failed:", e)
        return []
