"""
loop_parser.py — Parsing, Model Resolution, and Response Formatting Sub-module
Extracts structured JSON/XML tool calls, handles model name tag matching,
and formats final speech and text responses.
"""

import re
import json
import asyncio
import time
from typing import Dict, Any, Optional, List
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
            result = model_name or ""
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

        result = model_name or ""
        _model_name_cache[cache_key] = {"result": result, "expires": now + _MODEL_CACHE_TTL}
        return result
    except Exception as e:
        print(f"[Ollama Resolver] Error resolving model name: {e}")
        return model_name


def invalidate_model_name_cache() -> None:
    """Clears the model name cache, forcing a fresh Ollama client.list() on next call."""
    _model_name_cache.clear()


from src.core.loop_stream import estimate_token_count, generate_tools_doc, TOOL_SIGNATURES




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



def repair_and_extract_json(text: str) -> Optional[Dict[str, Any]]:
    """Tries multiple recovery strategies to extract or repair structured response JSON."""
    if not text or not text.strip():
        return None
    cleaned = text.strip()

    # 1. Direct attempt
    try:
        data = json.loads(cleaned)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    # 2. Normalize common malformed action shell("...") patterns and unescaped quotes
    def _fix_shell_action(m: re.Match) -> str:
        cmd = m.group(1).strip("'\"")
        return '"action": ' + json.dumps(cmd)

    repaired = re.sub(
        r'"action"\s*:\s*"shell\((.*?)\)"',
        _fix_shell_action,
        cleaned
    )
    repaired = re.sub(
        r'("action"\s*:\s*")([^"]*)"([^",}\]]*)"(\s*[,}\]])',
        r'\1\2\"\3\"\4',
        repaired
    )

    try:
        data = json.loads(repaired)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    # 3. Substring between outer braces
    start_idx = repaired.find('{')
    end_idx = repaired.rfind('}')
    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        potential = repaired[start_idx:end_idx+1]
        try:
            data = json.loads(potential)
            if isinstance(data, dict):
                return data
        except Exception:
            pass

    # 4. Strip trailing unbalanced brackets (e.g. from proactive_suggestions array dumps)
    stripped = repaired.rstrip(']}').strip()
    if stripped.startswith('{'):
        try:
            data = json.loads(stripped + '}')
            if isinstance(data, dict):
                if "title" in data and "action" in data and "chat" not in data:
                    return {"proactive_suggestions": [data]}
                return data
        except Exception:
            pass

    # 5. Model returned a list: [{"title": ...}]
    if repaired.startswith('[') and repaired.endswith(']'):
        try:
            data = json.loads(repaired)
            if isinstance(data, list):
                return {"proactive_suggestions": data}
        except Exception:
            pass

    # 6. Regex extraction of key fields
    chat_match = re.search(r'"chat"\s*:\s*"((?:[^"\\]|\\.)*)"', repaired)
    speech_match = re.search(r'"speech"\s*:\s*"((?:[^"\\]|\\.)*)"', repaired)
    lang_match = re.search(r'"lang"\s*:\s*"((?:[^"\\]|\\.)*)"', repaired)

    if chat_match or speech_match:
        res = {
            "chat": chat_match.group(1) if chat_match else "",
            "speech": speech_match.group(1) if speech_match else (chat_match.group(1) if chat_match else ""),
            "lang": lang_match.group(1) if lang_match else "en"
        }
        sug_match = re.search(r'"proactive_suggestions"\s*:\s*(\[[^\]]+\])', repaired)
        if sug_match:
            try:
                res["proactive_suggestions"] = json.loads(sug_match.group(1))
            except Exception:
                pass
        return res

    # 7. Check if text is only a suggestion object: {"title": "...", "action": "..."}
    title_match = re.search(r'"title"\s*:\s*"([^"]+)"', repaired)
    action_match = re.search(r'"action"\s*:\s*(?:"([^"]+)"|"shell\((.*?)\)")', repaired)
    type_match = re.search(r'"type"\s*:\s*"([^"]+)"', repaired)
    if title_match:
        act = action_match.group(1) if action_match and action_match.group(1) else (action_match.group(2) if action_match else "")
        act = (act or "").strip().strip("'\"")
        return {
            "proactive_suggestions": [{
                "title": title_match.group(1).strip(),
                "action": act,
                "type": type_match.group(1).strip() if type_match else "command"
            }]
        }

    return None


async def process_final_response(text: str, user_lang: str, client: ollama.Client) -> str:
    """Processes final model response JSON block, formatting speech and transliteration if needed."""
    cleaned_text = text.strip()
    json_data = repair_and_extract_json(cleaned_text)

    if json_data is None:
        # Check if cleaned_text looks like an internal JSON or tool dump
        if re.search(r'^\s*[\{\[]', cleaned_text) or '"action":' in cleaned_text or '"title":' in cleaned_text:
            title_m = re.search(r'"title"\s*:\s*"([^"]+)"', cleaned_text)
            fallback_msg = f"Task completed. Suggested follow-up: {title_m.group(1)}." if title_m else "Task completed."
            json_data = {"chat": fallback_msg, "speech": fallback_msg, "lang": "en"}
        else:
            return text

    # Ensure chat is populated if only proactive suggestions exist
    chat = json_data.get("chat", "")
    if not isinstance(chat, str) or not chat.strip():
        sugs = json_data.get("proactive_suggestions", [])
        if sugs and isinstance(sugs, list) and len(sugs) > 0:
            first_sug = sugs[0]
            sug_title = first_sug.get("title") if isinstance(first_sug, dict) else str(first_sug)
            chat = f"Task processed. Recommended next step: {sug_title}."
        else:
            chat = "Task completed successfully."
        json_data["chat"] = chat

    speech = json_data.get("speech", "") or chat
    lang = (json_data.get("lang") or "en").lower().strip()
    u_lang = (user_lang or "english").lower().strip()

    # Only transliterate if input/output is explicitly Hindi/Hinglish AND speech is not already in Devanagari script.
    # Never transliterate if user language is English, eliminating 2-6s unnecessary LLM latency.
    is_hindi_target = (u_lang in ["hi", "hi-in", "hinglish", "hindi"] or lang in ["hi", "hi-in", "hinglish", "hindi"]) and u_lang not in ["english", "en", "na"]
    already_devanagari = bool(re.search(r'[\u0900-\u097F]', speech)) if speech else False

    if is_hindi_target and not already_devanagari and speech.strip():
        speech = await transliterate_to_devanagari(speech, client)

    json_data["speech"] = speech

    # Preserve and normalize proactive_suggestions if present
    if "proactive_suggestions" in json_data and isinstance(json_data["proactive_suggestions"], list):
        sanitized_suggestions = []
        for item in json_data["proactive_suggestions"]:
            if isinstance(item, dict) and item.get("title"):
                act_str = str(item.get("action", "")).strip()
                # Clean any outer shell(...) wrapper
                shell_match = re.match(r'^shell\((.*)\)$', act_str, flags=re.IGNORECASE)
                if shell_match:
                    act_str = shell_match.group(1).strip().strip("'\"")
                sanitized_suggestions.append({
                    "title": str(item.get("title", "")).strip(),
                    "action": act_str,
                    "type": str(item.get("type", "suggestion")).strip().lower()
                })
            elif isinstance(item, str) and item.strip():
                sanitized_suggestions.append({
                    "title": item.strip(),
                    "action": item.strip(),
                    "type": "suggestion"
                })
        json_data["proactive_suggestions"] = sanitized_suggestions

    return json.dumps(json_data, ensure_ascii=False)


def parse_attributes(attr_str: str) -> Dict[str, Any]:
    attrs = {}
    if not attr_str:
        return attrs
    matches = re.findall(r'(\w+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', attr_str)
    for m in matches:
        key = m[0]
        val = m[1] if m[1] else m[2]
        attrs[key] = val
    return attrs


class StreamingXMLParser:
    def __init__(self):
        self.buffer = ""
        self.state = "idle"  # "idle", "thought", "call", "finish"
        self.current_thought = ""
        self.current_call_name = ""
        self.current_call_args = ""
        self.current_finish = ""
        
        self.yielded_thought_len = 0
        self.yielded_finish_len = 0

    def feed(self, chunk: str) -> List[Dict[str, Any]]:
        self.buffer += chunk
        events = []
        
        while True:
            if self.state == "idle":
                idx = self.buffer.find("<")
                if idx == -1:
                    if self.buffer:
                        events.append({"type": "text_update", "text": self.buffer})
                        self.buffer = ""
                    break
                
                if idx > 0:
                    events.append({"type": "text_update", "text": self.buffer[:idx]})
                    self.buffer = self.buffer[idx:]
                
                thought_match = re.match(r"^<(?:thought|think)[>\s\n]", self.buffer)
                if thought_match:
                    match_len = len(thought_match.group(0))
                    self.buffer = self.buffer[match_len:]
                    self.state = "thought"
                    self.current_thought = ""
                    self.yielded_thought_len = 0
                    continue
                
                finish_match = re.match(r"^<finish[>\s\n]", self.buffer)
                if finish_match:
                    match_len = len(finish_match.group(0))
                    self.buffer = self.buffer[match_len:]
                    self.state = "finish"
                    self.current_finish = ""
                    self.yielded_finish_len = 0
                    continue
                
                call_match = re.match(r"^<call:(\w+)(?:\s+([^>]*?))?(/?)\s*>", self.buffer)
                if call_match:
                    tag_len = len(call_match.group(0))
                    call_name = call_match.group(1)
                    attr_str = call_match.group(2) or ""
                    is_self_closing = call_match.group(3) == "/"
                    self.buffer = self.buffer[tag_len:]
                    
                    if is_self_closing:
                        args = parse_attributes(attr_str)
                        args.pop("charter", None)
                        events.append({"type": "call", "name": call_name, "args": json.dumps(args)})
                        self.state = "idle"
                    else:
                        self.state = "call"
                        self.current_call_name = call_name
                        self.current_call_args = ""
                    continue
                
                is_prefix = False
                for tag in ["<thought>", "<think>", "<finish>"]:
                    if tag.startswith(self.buffer):
                        is_prefix = True
                        break
                if not is_prefix:
                    if "<call:".startswith(self.buffer) or self.buffer.startswith("<call:"):
                        if ">" not in self.buffer:
                            is_prefix = True
                
                if is_prefix:
                    if len(self.buffer) < 100:
                        break
                
                events.append({"type": "text_update", "text": self.buffer[0]})
                self.buffer = self.buffer[1:]
                
            elif self.state == "thought":
                end_pos_thought = self.buffer.find("</thought>")
                end_pos_think = self.buffer.find("</think>")

                end_pos = -1
                tag_len = 0
                if end_pos_thought != -1 and end_pos_think != -1:
                    if end_pos_thought < end_pos_think:
                        end_pos = end_pos_thought
                        tag_len = len("</thought>")
                    else:
                        end_pos = end_pos_think
                        tag_len = len("</think>")
                elif end_pos_thought != -1:
                    end_pos = end_pos_thought
                    tag_len = len("</thought>")
                elif end_pos_think != -1:
                    end_pos = end_pos_think
                    tag_len = len("</think>")

                if end_pos != -1:
                    self.current_thought += self.buffer[:end_pos]
                    self.buffer = self.buffer[end_pos + tag_len:]
                    new_text = self.current_thought[self.yielded_thought_len:]
                    events.append({"type": "thought", "text": new_text, "status": "completed"})
                    self.state = "idle"
                else:
                    implicit_tags = ["<call:", "<finish>"]
                    found_implicit = -1
                    for itag in implicit_tags:
                        pos = self.buffer.find(itag)
                        if pos != -1:
                            if found_implicit == -1 or pos < found_implicit:
                                found_implicit = pos
                                
                    if found_implicit != -1:
                        self.current_thought += self.buffer[:found_implicit]
                        self.buffer = self.buffer[found_implicit:]
                        new_text = self.current_thought[self.yielded_thought_len:]
                        events.append({"type": "thought", "text": new_text, "status": "completed"})
                        self.state = "idle"
                        continue
                        
                    match_len = 0
                    for tag in ["</thought>", "</think>"]:
                        for i in range(len(tag) - 1, 0, -1):
                            prefix = tag[:i]
                            if self.buffer.endswith(prefix) and i > match_len:
                                match_len = i
                    
                    if match_len > 0:
                        consume_part = self.buffer[:-match_len]
                        self.current_thought += consume_part
                        self.buffer = self.buffer[-match_len:]
                    else:
                        self.current_thought += self.buffer
                        self.buffer = ""
                        
                    new_text = self.current_thought[self.yielded_thought_len:]
                    if new_text:
                        events.append({"type": "thought_update", "text": new_text})
                        self.yielded_thought_len = len(self.current_thought)
                    break
                    
            elif self.state == "call":
                tag = f"</call:{self.current_call_name}>"
                end_pos = self.buffer.find(tag)
                if end_pos != -1:
                    self.current_call_args += self.buffer[:end_pos]
                    self.buffer = self.buffer[end_pos + len(tag):]
                    events.append({"type": "call", "name": self.current_call_name, "args": self.current_call_args})
                    self.state = "idle"
                else:
                    implicit_tags = ["<thought>", "<finish>", "<call:"]
                    found_implicit = -1
                    for itag in implicit_tags:
                        pos = self.buffer.find(itag)
                        if pos != -1:
                            if found_implicit == -1 or pos < found_implicit:
                                found_implicit = pos
                                
                    if found_implicit != -1:
                        self.current_call_args += self.buffer[:found_implicit]
                        self.buffer = self.buffer[found_implicit:]
                        events.append({"type": "call", "name": self.current_call_name, "args": self.current_call_args})
                        self.state = "idle"
                        continue
                        
                    match_len = 0
                    for i in range(len(tag) - 1, 0, -1):
                        prefix = tag[:i]
                        if self.buffer.endswith(prefix):
                            match_len = i
                            break
                            
                    if match_len > 0:
                        consume_part = self.buffer[:-match_len]
                        self.current_call_args += consume_part
                        self.buffer = self.buffer[-match_len:]
                    else:
                        self.current_call_args += self.buffer
                        self.buffer = ""
                    break
                    
            elif self.state == "finish":
                tag = "</finish>"
                end_pos = self.buffer.find(tag)
                if end_pos != -1:
                    self.current_finish += self.buffer[:end_pos]
                    self.buffer = self.buffer[end_pos + len(tag):]
                    events.append({"type": "finish", "text": self.current_finish})
                    self.state = "idle"
                else:
                    implicit_tags = ["<thought>", "<call:"]
                    found_implicit = -1
                    for itag in implicit_tags:
                        pos = self.buffer.find(itag)
                        if pos != -1:
                            if found_implicit == -1 or pos < found_implicit:
                                found_implicit = pos
                                
                    if found_implicit != -1:
                        self.current_finish += self.buffer[:found_implicit]
                        self.buffer = self.buffer[found_implicit:]
                        events.append({"type": "finish", "text": self.current_finish})
                        self.state = "idle"
                        continue
                        
                    match_len = 0
                    for i in range(len(tag) - 1, 0, -1):
                        prefix = tag[:i]
                        if self.buffer.endswith(prefix):
                            match_len = i
                            break
                            
                    if match_len > 0:
                        consume_part = self.buffer[:-match_len]
                        self.current_finish += consume_part
                        self.buffer = self.buffer[-match_len:]
                    else:
                        self.current_finish += self.buffer
                        self.buffer = ""
                    break
                    
        return events

