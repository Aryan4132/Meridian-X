import re
import json
import asyncio
import os
from typing import Dict, Any

# Speculative cache to keep track of already preheated contexts
_preheated_cache = set()

def try_parse_partial_json(partial_str: str) -> Dict[str, Any]:
    """Attempts to parse a partially completed JSON string by balancing brackets."""
    partial_str = partial_str.strip()
    if not partial_str:
        return {}
    
    # Try direct parse first
    try:
        return json.loads(partial_str)
    except Exception:
        pass
    
    # Attempt to close open braces and brackets
    balanced = partial_str
    open_braces = balanced.count("{") - balanced.count("}")
    open_brackets = balanced.count("[") - balanced.count("]")
    
    if open_brackets > 0:
        balanced += "]" * open_brackets
    if open_braces > 0:
        # If inside a string, close quote first
        if balanced.count('"') % 2 != 0:
            balanced += '"'
        balanced += "}" * open_braces
        
    try:
        return json.loads(balanced)
    except Exception:
        return {}

async def preheat_tool(tool_name: str, partial_args_str: str):
    """
    Speculatively preheats system resources for tools based on streaming partial args.
    #13 FIX: Expanded from 3 tool types to cover file writes, browser, LSP, and KG tools.
    """
    args = try_parse_partial_json(partial_args_str)
    if not args:
        return

    # BUG-52 fix: json.dumps is safe for mixed-type values (None, int, str, etc.).
    # sorted(args.items()) raises TypeError when values are non-comparable (e.g. None < 'str').
    import json as _json
    cache_key = f"{tool_name}:{_json.dumps(args, sort_keys=True, default=str)}"
    if cache_key in _preheated_cache:
        return
    _preheated_cache.add(cache_key)

    try:
        # --- File read/write/delete: resolve path existence ---
        if tool_name in ["read_file", "write_file", "delete_file"]:
            path = args.get("path") or args.get("filepath") or args.get("TargetFile")
            if path:
                await asyncio.to_thread(os.path.abspath, path)
                print(f"[Speculative Engine] Preheating file path: {path}")
                # #13 FIX: For write_file, also warm parent directory existence check
                if tool_name == "write_file":
                    parent = os.path.dirname(os.path.abspath(path))
                    await asyncio.to_thread(os.path.exists, parent)
                    print(f"[Speculative Engine] Prewarming write target directory: {parent}")

        # --- Web/browser tools: DNS resolution ---
        elif tool_name in ["search_web", "fetch_page", "browser_get_text", "scrape_table", "browser_screenshot"]:
            url = args.get("url") or args.get("Url") or args.get("query")
            if url and url.startswith("http"):
                import socket
                from urllib.parse import urlparse
                parsed = urlparse(url)
                hostname = parsed.hostname
                if hostname:
                    print(f"[Speculative Engine] Speculative DNS resolution for: {hostname}")
                    await asyncio.to_thread(socket.gethostbyname, hostname)

        # --- Vision / OCR: pre-open image file ---
        elif tool_name in ["vision_analyze", "ocr_screen"]:
            image_path = args.get("image_path")
            if image_path:
                await asyncio.to_thread(os.path.exists, image_path)
                print(f"[Speculative Engine] Preheating image file access: {image_path}")

        # --- Shell / Python execution: warm the pipeline ---
        elif tool_name in ["nl_run", "run_python", "run_command"]:
            print(f"[Speculative Engine] Pre-heating shell/python execution pipeline environment.")

        # --- #13 FIX: LSP tools: pre-check if LSP socket/port is reachable ---
        elif tool_name.startswith("lsp_"):
            import socket as _sock
            lsp_port = int(os.environ.get("LSP_PORT", "2087"))
            lsp_host = os.environ.get("LSP_HOST", "127.0.0.1")
            try:
                conn = _sock.create_connection((lsp_host, lsp_port), timeout=0.2)
                conn.close()
                print(f"[Speculative Engine] LSP server reachable at {lsp_host}:{lsp_port}")
            except Exception:
                print(f"[Speculative Engine] LSP pre-check: server not yet reachable, skipping warm.")

        # --- #13 FIX: Knowledge Graph tools: pre-warm DB handle (import triggers connection pool) ---
        elif tool_name.startswith("kg_") or tool_name in ["search_knowledge", "search_offline_docs"]:
            try:
                from database import get_sqlite_conn
                conn = get_sqlite_conn()
                conn.close()
                print(f"[Speculative Engine] KG/knowledge DB connection pre-warmed for: {tool_name}")
            except Exception as db_e:
                print(f"[Speculative Engine] KG pre-warm skipped: {db_e}")

        # --- #13 FIX: Clipboard tools: pre-import pyperclip to avoid first-call latency ---
        elif tool_name in ["clipboard_get", "clipboard_search", "clipboard_history"]:
            try:
                import importlib
                importlib.import_module("pyperclip")
                print(f"[Speculative Engine] Clipboard module pre-imported for: {tool_name}")
            except Exception:
                pass

    except Exception as e:
        print(f"[Speculative Engine] Speculative preheat failed: {e}")
