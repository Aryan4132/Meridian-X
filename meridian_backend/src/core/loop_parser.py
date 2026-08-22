"""
loop_parser.py — Parsing, Model Resolution, and Response Formatting Sub-module
Extracts structured JSON/XML tool calls, handles model name tag matching,
and formats final speech and text responses.
"""

import re
import json
import asyncio
import time
from typing import Dict, Any, Optional
import ollama

from database import get_auditor_model
from src.tools.registry import TOOL_REGISTRY


# ---------------------------------------------------------------------------
# #10 FIX: 60-second TTL cache for resolve_local_model_name.
# client.list() is a network call to Ollama. Caching avoids redundant round-trips
# on every request when the installed model set rarely changes.
# ---------------------------------------------------------------------------
_model_name_cache: Dict[str, Any] = {}  # key → {"result": str, "expires": float}
_MODEL_CACHE_TTL = 60.0  # seconds


def resolve_local_model_name(model_name: str, client: ollama.Client) -> str:
    """
    Checks Ollama's list of installed models and matches the requested model
    to the best available model (preserving user-selected cloud model tags).
    Results are cached for 60 seconds to avoid redundant network calls.
    """
    cache_key = model_name or ""
    now = time.monotonic()
    cached = _model_name_cache.get(cache_key)
    if cached and cached["expires"] > now:
        return cached["result"]

    try:
        res = client.list()
        raw_models = []
        if hasattr(res, 'models'):
            raw_models = res.models
        elif isinstance(res, dict) and 'models' in res:
            raw_models = res['models']
        elif isinstance(res, list):
            raw_models = res

        all_names = []
        installed_models = []
        for m in raw_models:
            name = m.model if hasattr(m, 'model') else (m.get('model') or m.get('name') if isinstance(m, dict) else "")
            size = getattr(m, 'size', 0) if hasattr(m, 'size') else (m.get('size', 0) if isinstance(m, dict) else 0)
            if name:
                all_names.append(name)
                if "cloud" not in name.lower() and (size == 0 or size > 1000000):
                    installed_models.append(name)

        if not all_names:
            result = model_name or "llama3.2:3b"
            _model_name_cache[cache_key] = {"result": result, "expires": now + _MODEL_CACHE_TTL}
            return result

        # 1. Exact match if valid model in Ollama (including cloud model tags like gemma4:31b-cloud)
        if model_name in all_names:
            _model_name_cache[cache_key] = {"result": model_name, "expires": now + _MODEL_CACHE_TTL}
            return model_name

        if not installed_models:
            installed_models = all_names

        # 2. Match base model name if requested model tag was mismatched
        clean_name = model_name.split(":")[0] if ":" in model_name else model_name
        prefix = f"{clean_name}:"
        matches = [m for m in installed_models if m.startswith(prefix) or m.startswith(clean_name)]
        if matches:
            def match_key(m):
                tag = m.lower()
                if "coder" in tag and "instruct" in tag:
                    return (0, tag)
                if "instruct" in tag:
                    return (1, tag)
                if "latest" in tag:
                    return (2, tag)
                return (3, tag)
            matches.sort(key=match_key)
            result = matches[0]
            _model_name_cache[cache_key] = {"result": result, "expires": now + _MODEL_CACHE_TTL}
            return result

        # 3. Fallback to first installed local model
        if installed_models:
            result = installed_models[0]
            _model_name_cache[cache_key] = {"result": result, "expires": now + _MODEL_CACHE_TTL}
            return result

        result = model_name or "for ex: model name"
        _model_name_cache[cache_key] = {"result": result, "expires": now + _MODEL_CACHE_TTL}
        return result
    except Exception as e:
        print(f"[Ollama Resolver] Error resolving model name: {e}")
        return model_name


def invalidate_model_name_cache() -> None:
    """Clears the model name cache, forcing a fresh Ollama client.list() on next call."""
    _model_name_cache.clear()


def generate_tools_doc() -> str:
    """Returns formatted string documentation of all registered tools and their tiers."""
    lines = []
    for name, info in TOOL_REGISTRY.items():
        lines.append(f"- {name}: Tier {info['tier']}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# #15 FIX: Content-aware token estimation.
# Simple divide-by-4 is wrong for code (denser, ~3 chars/token) and CJK text
# (1 CJK char ≈ 1 token). This function detects the dominant content type and
# applies the correct ratio, giving more accurate context window budgeting.
# ---------------------------------------------------------------------------
_CJK_RE = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]')
_CODE_RE = re.compile(r'```[\s\S]*?```|def |class |import |from .+ import|function |const |let |var ')


def estimate_token_count(text: str) -> int:
    """
    Content-aware token estimation.
    - Code-heavy text: ~3.0 chars/token
    - CJK-dominant text: ~1.2 chars/token
    - Default prose: ~4.0 chars/token
    """
    if not text:
        return 0
    length = len(text)
    # Detect CJK dominance (>10% CJK chars)
    cjk_count = len(_CJK_RE.findall(text))
    if cjk_count > length * 0.10:
        return max(1, int(length / 1.2))
    # Detect code dominance (code block markers or function/class keywords)
    if _CODE_RE.search(text):
        return max(1, int(length / 3.0))
    # Default prose
    return max(1, int(length / 4.0))


async def transliterate_to_devanagari(text: str, client: ollama.Client) -> str:
    """Phonetic Hinglish to Devanagari script converter."""
    if not text or not text.strip():
        return text

    model = get_auditor_model()
    messages = [
        {
            "role": "system",
            "content": (
                "You are a phonetic Hinglish-to-Hindi transliterator. Convert the input Latin Hinglish text to Hindi Devanagari script based ONLY on phonetic pronunciation.\n"
                "CRITICAL RULES:\n"
                "1. Do NOT translate the meaning.\n"
                "2. Keep the exact words and order as the input Hinglish text.\n"
                "3. Output ONLY the Devanagari text."
            )
        },
        {
            "role": "user",
            "content": f"Hinglish: {text}\nDevanagari:"
        }
    ]
    try:
        res = await asyncio.to_thread(client.chat, model=model, messages=messages)
        raw_content = (
            res.message.content if hasattr(res, "message") and hasattr(res.message, "content")
            else (res.get("message", {}).get("content", "") if isinstance(res, dict) else "")
        )
        converted = (raw_content or "").strip()

        converted = re.sub(r"^```[a-zA-Z0-9_-]*\n?", "", converted)
        converted = re.sub(r"```$", "", converted).strip().strip("\"'").strip()
        if converted.startswith("Devanagari:"):
            converted = converted.replace("Devanagari:", "").strip()
        return converted
    except Exception as e:
        print(f"[Transliteration] Failed to transliterate '{text}' using {model}: {e}")
        return text



async def process_final_response(text: str, user_lang: str, client: ollama.Client) -> str:
    """Processes final model response JSON block, formatting speech and transliteration if needed."""
    cleaned_text = text.strip()
    json_data = None
    is_json = False

    try:
        json_data = json.loads(cleaned_text)
        is_json = True
    except Exception:
        pass

    if not is_json:
        start_idx = cleaned_text.find('{')
        end_idx = cleaned_text.rfind('}')
        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            potential_json = cleaned_text[start_idx:end_idx+1]
            try:
                json_data = json.loads(potential_json)
                is_json = True
            except Exception:
                pass

    if not is_json:
        chat_match = re.search(r'"chat"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned_text)
        speech_match = re.search(r'"speech"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned_text)
        lang_match = re.search(r'"lang"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned_text)

        if chat_match or speech_match:
            json_data = {}
            json_data["chat"] = chat_match.group(1) if chat_match else ""
            json_data["speech"] = speech_match.group(1) if speech_match else json_data["chat"]
            json_data["lang"] = lang_match.group(1) if lang_match else "en"
            is_json = True

    if not is_json or json_data is None:
        return text

    chat = json_data.get("chat", "")
    speech = json_data.get("speech", "") or chat
    lang = json_data.get("lang", "en")

    if user_lang in ["hi", "hi-IN", "hinglish"] or lang in ["hi", "hi-IN", "hinglish"]:
        speech = await transliterate_to_devanagari(speech, client)

    json_data["speech"] = speech
    return json.dumps(json_data, ensure_ascii=False)
