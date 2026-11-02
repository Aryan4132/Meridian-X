import time
import shutil
import platform
import pyperclip
from bson.objectid import ObjectId
from typing import List, Dict, Any
from database import get_mongo_db

def _check_linux_clipboard_support() -> bool:
    if platform.system() == "Linux":
        if shutil.which("xclip") or shutil.which("xsel") or shutil.which("wl-copy"):
            return True
        return False
    return True

def clipboard_history(n: int = 10) -> str:
    """Retrieve the last N entries copied to the clipboard."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline. Clipboard history unavailable."
        
    try:
        col = db["smart_clipboard"]
        records = list(col.find({}, {"text": 1, "timestamp": 1, "pinned": 1}).sort("timestamp", -1).limit(n))
        if not records:
            return "Clipboard history is empty."
            
        lines = ["Recent Clipboard History:"]
        for r in records:
            time_str = time.strftime('%H:%M:%S', time.localtime(r.get("timestamp", 0.0)))
            pinned_str = " [PINNED]" if r.get("pinned") else ""
            text_preview = r['text'] if len(r['text']) <= 50 else r['text'][:50] + '...'
            lines.append(f"- ID: {r['_id']} | Time: {time_str} | Text: '{text_preview}'{pinned_str}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error loading clipboard history: {e}"

def clipboard_search(query: str) -> str:
    """Perform a text search across all recorded clipboard history entries."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["smart_clipboard"]
        # Regex case-insensitive search
        records = list(col.find({"text": {"$regex": query, "$options": "i"}}, {"text": 1, "timestamp": 1, "pinned": 1}).sort("timestamp", -1).limit(10))
        if not records:
            return f"No clipboard history entries matching '{query}' found."
            
        lines = [f"Found {len(records)} clipboard entries matching '{query}':"]
        for r in records:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(r.get("timestamp", 0.0)))
            pinned_str = " [PINNED]" if r.get("pinned") else ""
            text_preview = r['text'] if len(r['text']) <= 60 else r['text'][:60] + '...'
            lines.append(f"- ID: {r['_id']} | Date: {time_str} | Text: '{text_preview}'{pinned_str}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error searching clipboard: {e}"

def clipboard_pin(entry_id: str) -> str:
    """Pin a clipboard history entry so that it is preserved permanently."""
    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["smart_clipboard"]
        res = col.update_one({"_id": ObjectId(entry_id)}, {"$set": {"pinned": True}})
        if res.matched_count > 0:
            return f"Successfully pinned clipboard entry '{entry_id}'."
        return f"Error: Clipboard entry '{entry_id}' not found."
    except Exception as e:
        return f"Failed to pin clipboard entry: {e}"

def clipboard_restore(entry_id: str) -> str:
    """Restore a historical clipboard entry back to the active operating system clipboard."""
    if not _check_linux_clipboard_support():
        return "Error: System clipboard utility ('xclip', 'xsel', or 'wl-clipboard') is not installed on Linux. Please install via: sudo apt install xclip"

    db = get_mongo_db()
    if db is None:
        return "MongoDB is offline."
        
    try:
        col = db["smart_clipboard"]
        record = col.find_one({"_id": ObjectId(entry_id)})
        if not record:
            return f"Error: Clipboard entry '{entry_id}' not found."
            
        try:
            pyperclip.copy(record["text"])
        except Exception as clip_err:
            return f"Failed to copy text to system clipboard: {clip_err}. Ensure xclip/xsel is installed."

        return f"Successfully restored text to system clipboard: '{record['text'][:50]}...'"
    except Exception as e:
        return f"Failed to restore clipboard entry: {e}"


def smart_clipboard_action(mode: str = "auto") -> str:
    """Analyze current OS clipboard content, auto-detect its type (JSON, code, stack trace, URL, text), and format or diagnose it."""
    try:
        raw_text = pyperclip.paste()
    except Exception as e:
        return f"Unable to read OS clipboard: {str(e)}"

    if not raw_text or not raw_text.strip():
        return "Clipboard is empty or does not contain plain text."

    content = raw_text.strip()
    length = len(content)

    # 1. JSON Detection & Formatting
    if (content.startswith("{") and content.endswith("}")) or (content.startswith("[") and content.endswith("]")):
        import json
        try:
            parsed = json.loads(content)
            formatted = json.dumps(parsed, indent=2)
            try:
                pyperclip.copy(formatted)
                copied_note = " (Prettified JSON copied to clipboard)"
            except Exception:
                copied_note = ""
            return (
                f"**Clipboard Content**: Valid JSON ({length} chars){copied_note}\n\n"
                f"```json\n{formatted[:1500]}\n```"
                + (f"\n*...truncated {len(formatted) - 1500} chars*" if len(formatted) > 1500 else "")
            )
        except Exception as json_err:
            return (
                f"**Clipboard Content**: Malformed JSON detected.\n"
                f"**Parse Error**: `{json_err}`\n"
                f"**Raw Preview**:\n```text\n{content[:500]}\n```\n"
                f"💡 Propose asking agent to repair this JSON."
            )

    # 2. Stack Trace / Crash Detection
    stack_indicators = ["Traceback (most recent call last):", "Error:", "Exception:", "at line", "Fatal error", "panic:"]
    if any(ind in content for ind in stack_indicators):
        lines = content.splitlines()
        first_few = "\n".join(lines[:6])
        last_few = "\n".join(lines[-4:])
        return (
            f"**Clipboard Content**: Error Stack Trace Detected ({len(lines)} lines)\n\n"
            f"```text\n{first_few}\n...\n{last_few}\n```\n"
            f"💡 **Diagnosis**: Clipboard holds an active crash or error. Ask me *'Fix the error in my clipboard'* to resolve it."
        )

    # 3. URL Detection
    if content.startswith(("http://", "https://")):
        import urllib.parse
        parsed = urllib.parse.urlparse(content)
        query_params = urllib.parse.parse_qs(parsed.query)
        param_desc = f" ({len(query_params)} query parameters)" if query_params else ""
        return (
            f"**Clipboard Content**: Web URL\n"
            f"**Host**: `{parsed.netloc}`\n"
            f"**Path**: `{parsed.path or '/'}`{param_desc}\n"
            f"💡 Ask me *'Fetch and summarize this URL'* or *'Open in browser'*."
        )

    # 4. Code Snippet Detection
    code_indicators = ["def ", "class ", "import ", "function ", "const ", "export ", "public class ", "<div", "return "]
    if any(ind in content for ind in code_indicators):
        lines = content.splitlines()
        return (
            f"**Clipboard Content**: Code Snippet ({len(lines)} lines, {length} chars)\n\n"
            f"```text\n{content[:1200]}\n```"
            + (f"\n*...truncated {length - 1200} chars*" if length > 1200 else "")
            + "\n💡 Ask me to *'Explain this code'*, *'Refactor this'*, or *'Write unit tests for this'*."
        )

    # 5. General Plain Text
    words = content.split()
    preview = content[:300] + ("..." if length > 300 else "")
    return (
        f"**Clipboard Content**: Plain Text ({len(words)} words, {length} characters)\n\n"
        f"> {preview}\n\n"
        f"💡 Ready to rewrite, translate, proofread, or ingest into knowledge base."
    )
