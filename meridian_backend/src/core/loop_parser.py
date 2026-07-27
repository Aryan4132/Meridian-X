"""
loop_parser.py — Parsing, Model Resolution, and Response Formatting Sub-module
Extracts structured JSON/XML tool calls, handles model name tag matching,
and formats final speech and text responses.
"""

import re
import json
import asyncio
from typing import Dict, Any, Optional
import ollama

from database import get_auditor_model
from src.tools.registry import TOOL_REGISTRY


def resolve_local_model_name(model_name: str, client: ollama.Client) -> str:
    """
    Checks Ollama's list of installed models and matches the requested model
    to the best available real local model (excluding cloud pointers/tags).
    """
    try:
        res = client.list()
        raw_models = []
        if hasattr(res, 'models'):
            raw_models = res.models
        elif isinstance(res, dict) and 'models' in res:
            raw_models = res['models']
        elif isinstance(res, list):
            raw_models = res

        installed_models = []
        for m in raw_models:
            name = m.model if hasattr(m, 'model') else (m.get('model') or m.get('name') if isinstance(m, dict) else "")
            size = getattr(m, 'size', 0) if hasattr(m, 'size') else (m.get('size', 0) if isinstance(m, dict) else 0)
            if name and "cloud" not in name.lower() and (size == 0 or size > 1000000):
                installed_models.append(name)

        if not installed_models:
            return "llama3.2:3b"

        # 1. Exact match if valid local model
        if model_name in installed_models:
            return model_name

        # 2. Match base model name if requested model was cloud or mismatched
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
            return matches[0]

        # 3. Fallback to preferred installed local models
        for preferred in ["qwen2.5-coder:7b-instruct-q4_K_M", "llama3.2:3b", "qwen3.5:latest"]:
            if preferred in installed_models:
                return preferred
        return installed_models[0]
    except Exception as e:
        print(f"[Ollama Resolver] Error resolving model name: {e}")

    return "llama3.2:3b"


def generate_tools_doc() -> str:
    """Returns formatted string documentation of all registered tools and their tiers."""
    lines = []
    for name, info in TOOL_REGISTRY.items():
        lines.append(f"- {name}: Tier {info['tier']}")
    return "\n".join(lines)


async def transliterate_to_devanagari(text: str, client: ollama.Client) -> str:
    """Phonetic Hinglish to Devanagari script converter."""
    if not text.strip():
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
        converted = (
            res.message.content if hasattr(res, "message") and hasattr(res.message, "content")
            else res.get("message", {}).get("content", "")
        ).strip()

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
