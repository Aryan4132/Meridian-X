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
    """Speculatively preheats system resources for tools based on streaming partial args."""
    args = try_parse_partial_json(partial_args_str)
    if not args:
        return

    # Create a unique key for the preheating run to avoid duplicate preheating
    cache_key = f"{tool_name}:{sorted(args.items())}"
    if cache_key in _preheated_cache:
        return
    _preheated_cache.add(cache_key)

    try:
        if tool_name in ["read_file", "write_file", "delete_file"]:
            path = args.get("path") or args.get("filepath") or args.get("TargetFile")
            if path:
                # Preheat: Check existence or pre-resolve full path in thread pool
                await asyncio.to_thread(os.path.abspath, path)
                print(f"[Speculative Engine] Preheating file path: {path}")
                
        elif tool_name in ["search_web", "fetch_page"]:
            url = args.get("url") or args.get("Url")
            if url:
                # Preheat: Warm connection pool / resolve DNS in background
                import socket
                from urllib.parse import urlparse
                parsed = urlparse(url)
                hostname = parsed.hostname
                if hostname:
                    print(f"[Speculative Engine] Speculative DNS resolution for: {hostname}")
                    await asyncio.to_thread(socket.gethostbyname, hostname)

        elif tool_name in ["vision_analyze", "ocr_screen"]:
            image_path = args.get("image_path")
            if image_path:
                await asyncio.to_thread(os.path.exists, image_path)
                print(f"[Speculative Engine] Preheating image file access: {image_path}")

        elif tool_name in ["nl_run", "run_python"]:
            # Pre-heat subprocess pipelines if shell command detected
            print(f"[Speculative Engine] Pre-heating shell/python execution pipeline environment.")
            
    except Exception as e:
        print(f"[Speculative Engine] Speculative preheat failed: {e}")
