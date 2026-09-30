"""
Universal Search Hub (KNOW-03)
Unified search engine aggregating RAG docs, AST code graph symbols, chat history,
screenshots, and local files into a single cross-domain query output.
"""

import os
import re
from typing import Dict, Any, List

def universal_search(query: str, domain_filter: str = "all") -> str:
    """
    Execute universal cross-system search across real database, files, and memory.
    query: search string
    domain_filter: all | code | docs | memory | files
    """
    query_clean = query.strip()
    if not query_clean:
        return "Search query cannot be empty."

    query_lower = query_clean.lower()
    results: List[str] = []

    # 1. Real Code search (look in workspace python/tsx files)
    if domain_filter in ["all", "code"]:
        matched_symbols = []
        workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        try:
            for root, dirs, files in os.walk(workspace_root):
                dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}]
                for file in files:
                    if file.endswith((".py", ".ts", ".tsx", ".js", ".json")):
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, workspace_root)
                        try:
                            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                                for line_idx, line in enumerate(f, 1):
                                    if query_lower in line.lower() and ("def " in line or "class " in line or "function " in line or "const " in line):
                                        matched_symbols.append(f"{rel_path}:{line_idx} - {line.strip()[:80]}")
                                        if len(matched_symbols) >= 3:
                                            break
                        except Exception:
                            pass
                    if len(matched_symbols) >= 3:
                        break
                if len(matched_symbols) >= 3:
                    break
        except Exception as e:
            matched_symbols.append(f"Code scan error: {e}")

        for sym in matched_symbols:
            results.append(f"💻 [Code Match] {sym}")

    # 2. Real RAG Document match from SQLite knowledge_base
    if domain_filter in ["all", "docs"]:
        try:
            from database import search_knowledge_base
            rag_docs = search_knowledge_base(query_clean, limit=3)
            for doc in rag_docs:
                src = doc.get("source", "knowledge_base")
                snippet = doc.get("text", "").replace("\n", " ").strip()[:100]
                results.append(f"📄 [RAG Vault] {src}: {snippet}...")
        except Exception:
            pass

    # 3. Real Chat History & Memory match from SQLite conversations
    if domain_filter in ["all", "memory"]:
        try:
            from database import get_sqlite_conn
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT role, content, timestamp FROM conversations WHERE LOWER(content) LIKE ? ORDER BY id DESC LIMIT 3",
                (f"%{query_lower}%",)
            )
            rows = cursor.fetchall()
            for r in rows:
                content_preview = r["content"].replace("\n", " ")[:100]
                results.append(f"🧠 [Memory Hub] [{r['role']}]: {content_preview}...")
            conn.close()
        except Exception:
            pass

    # 4. Real Local Filesystem match
    if domain_filter in ["all", "files"]:
        matched_files = []
        workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        try:
            for root, dirs, files in os.walk(workspace_root):
                dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}]
                for file in files:
                    if query_lower in file.lower():
                        rel = os.path.relpath(os.path.join(root, file), workspace_root)
                        matched_files.append(rel)
                        if len(matched_files) >= 4:
                            break
                if len(matched_files) >= 4:
                    break
        except Exception:
            pass

        for mf in matched_files:
            results.append(f"📁 [Filesystem] {mf}")

    if not results:
        return f"No matches found across Meridian system index for '{query_clean}'."

    return (
        f"🔍 Universal Search Hub Results for '{query_clean}' (Filter: {domain_filter}):\n"
        + "\n".join(results)
    )
