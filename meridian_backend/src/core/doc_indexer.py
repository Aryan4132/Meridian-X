import os
import time
import sqlite3
import numpy as np
from turbovec import IdMapIndex
from database import get_sqlite_conn, get_embedding, normalize_vector, db_dir

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
                content TEXT
            )
        """)
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
    """Scans and indexes all markdown (.md) documents in a directory."""
    init_docs_index()
    global docs_index
    
    if not os.path.exists(docs_dir):
        print(f"[Docs Indexer] Directory not found: {docs_dir}")
        return
        
    ids_to_add = []
    vectors_to_add = []
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.lower().endswith(".md"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, docs_dir).replace("\\", "/")
                
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
                            
                        # Insert metadata into SQLite
                        cursor.execute(
                            "INSERT INTO offline_docs (file_path, section, content) VALUES (?, ?, ?)",
                            (rel_path, sec, chunk_txt)
                        )
                        inserted_id = cursor.lastrowid
                        
                        # Generate embedding
                        vector = get_embedding(chunk_txt)
                        
                        ids_to_add.append(inserted_id)
                        vectors_to_add.append(normalize_vector(vector))
                        
                except Exception as fe:
                    print(f"[Docs Indexer] Failed to read/parse '{file}': {fe}")
                    
    conn.commit()
    conn.close()
    
    # Add to Turbovec index
    if ids_to_add:
        ids_np = np.array(ids_to_add, dtype=np.uint64)
        vectors_np = np.array(vectors_to_add, dtype=np.float32)
        docs_index.add_with_ids(vectors_np, ids=ids_np)
        docs_index.write(DOCS_INDEX_PATH)
        print(f"[Docs Indexer] Ingested {len(ids_to_add)} document chunks into index.")

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
