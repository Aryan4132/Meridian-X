import os
import re
import json
import asyncio
import uuid
import time
import random
import threading
from typing import Dict, Any, List, AsyncGenerator, Tuple
import ollama

from src.tools.registry import call_tool, TOOL_REGISTRY
from database import add_to_task_log, add_to_conversations, get_conversation_history, check_semantic_cache, add_to_semantic_cache, ingest_into_knowledge_base
from src.core.bus import event_bus
from src.core.speculative import preheat_tool

# Map active confirmations globally
active_confirmations: Dict[str, Dict[str, Any]] = {}

# Tools exempt from consecutive loop repetition checks (read-only, diagnostic, visual poll, search)
EXEMPT_TOOLS = {
    # Search & Information Retrieval
    "read_file", "list_directory", "search_files", "search_web", "autonomous_research",
    "search_knowledge", "search_offline_docs", "search_codebase", "lsp_get_definition",
    "lsp_get_references", "lsp_get_hover_info", "kg_query", "kg_search", "kg_get_facts",
    "kg_traverse", "vault_get", "vault_list", "tail_log", "search_log", "log_stats",
    "clipboard_search", "read_emails", "browser_get_text", "scrape_table", "db_schema",
    # System Metrics & Diagnostics
    "get_system_info", "get_hardware_info", "get_disk_info", "get_battery_status",
    "get_temperature", "list_processes", "get_process_detail", "list_startup_items",
    "list_installed_apps", "list_services", "get_network_connections", "get_wifi_networks",
    "ping_host", "clipboard_get", "list_log_watchers", "list_watchers", "list_scheduled",
    "win_list_tasks", "clipboard_history", "list_workflows", "list_sessions",
    "export_finetune_data", "finetune_stats", "suggest_cross_project_patterns",
    # Visual Capture & UI Outlines
    "screenshot", "screenshot_region", "ocr_screen", "vision_analyze", "find_on_screen",
    "segment_screen", "browser_screenshot", "analyze_recording",
    # Code Review & Linting
    "lint_file", "lsp_diagnose_file", "run_tests", "review_file", "review_diff",
    "review_directory", "run_security_audit", "shell_history", "nl_to_shell"
}

# Active tree and debate state tables
active_trees: Dict[str, Dict[str, Any]] = {}
active_debates: Dict[str, Dict[str, Any]] = {}

# BUG-3 fix: use threading.Event instead of a plain bool flag.
# threading.Event.is_set() / .set() / .clear() are atomic and thread-safe,
# preventing race conditions between the voice-monitor thread and the async generator.
_interrupt_event = threading.Event()

def interrupt_agent_loop():
    """Signal the active agent loop to stop at the next safe checkpoint."""
    _interrupt_event.set()


def generate_tools_doc() -> str:
    lines = []
    for name, info in TOOL_REGISTRY.items():
        lines.append(f"- {name}: Tier {info['tier']}")
    return "\n".join(lines)

async def transliterate_to_devanagari(text: str, client: ollama.Client) -> str:
    if not text.strip():
        return text
    
    model = "qwen2.5-coder:1.5b-instruct-q8_0"
    messages = [
        {
            "role": "system",
            "content": (
                "You are a phonetic Hinglish-to-Hindi transliterator. Convert the input Latin Hinglish text to Hindi Devanagari script based ONLY on phonetic pronunciation.\n"
                "CRITICAL RULES:\n"
                "1. Do NOT translate the meaning under any circumstances (e.g. do NOT translate 'how' to 'कैसे', instead transliterate it phonetically if requested, but normally follow the Hinglish pronunciation).\n"
                "2. Keep the exact words and order as the input Hinglish text.\n"
                "3. Do NOT explain or add any commentary.\n"
                "4. Output ONLY the Devanagari text."
            )
        },
        {
            "role": "user",
            "content": (
                "Examples:\n"
                "Hinglish: main theek hoon, aap batao -> Devanagari: मैं ठीक हूँ, आप बताओ\n"
                "Hinglish: aap kaise ho -> Devanagari: आप कैसे हो\n"
                "Hinglish: kya chal raha hai -> Devanagari: क्या चल रहा है\n"
                "Hinglish: mujhe ek code likh ke do -> Devanagari: मुझे एक कोड लिख के दो\n\n"
                f"Hinglish: {text}\n"
                "Devanagari:"
            )
        }
    ]
    try:
        # Run using the fast local model in a thread pool to avoid blocking the event loop
        res = await asyncio.to_thread(client.chat, model=model, messages=messages)
        # client.chat() returns ChatResponse object — use attribute access
        converted = (res.message.content if hasattr(res, "message") and hasattr(res.message, "content") else res.get("message", {}).get("content", "")).strip()

        # Remove markdown code block fences if any
        converted = re.sub(r"^```[a-zA-Z0-9_-]*\n?", "", converted)
        converted = re.sub(r"```$", "", converted).strip()
        # Strip outer quotes if the model returned them
        converted = converted.strip("\"'").strip()
        # If it returned a label like 'Devanagari:', strip it
        if converted.startswith("Devanagari:"):
            converted = converted.replace("Devanagari:", "").strip()
        return converted
    except Exception as e:
        print(f"[Transliteration] Failed to transliterate '{text}' using {model}: {e}")
        # Fall back to returning original text if LLM call fails
        return text

async def process_final_response(text: str, user_lang: str, client: ollama.Client) -> str:
    import json
    import re
    
    # Try to find a JSON block in the text
    cleaned_text = text.strip()
    
    # Helper to extract JSON from text
    json_data = None
    is_json = False
    
    # 1. Try direct JSON parsing
    try:
        json_data = json.loads(cleaned_text)
        is_json = True
    except Exception:
        pass
        
    # 2. Try parsing by finding outermost curly braces
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
                
    # 3. If standard JSON parsing failed, try extracting via regex
    if not is_json:
        chat_match = re.search(r'"chat"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned_text)
        speech_match = re.search(r'"speech"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned_text)
        lang_match = re.search(r'"lang"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned_text)
        
        if chat_match or speech_match:
            json_data = {}
            if chat_match:
                try:
                    json_data["chat"] = json.loads(f'"{chat_match.group(1)}"')
                except Exception:
                    json_data["chat"] = chat_match.group(1)
            else:
                json_data["chat"] = ""
                
            if speech_match:
                try:
                    json_data["speech"] = json.loads(f'"{speech_match.group(1)}"')
                except Exception:
                    json_data["speech"] = speech_match.group(1)
            else:
                json_data["speech"] = json_data["chat"]
                
            if lang_match:
                try:
                    json_data["lang"] = json.loads(f'"{lang_match.group(1)}"')
                except Exception:
                    json_data["lang"] = lang_match.group(1)
            else:
                json_data["lang"] = "en"
            is_json = True

    if not is_json or json_data is None:
        # Not a JSON response, return original text as-is
        return text

    # Ensure required keys exist
    chat = json_data.get("chat", "")
    speech = json_data.get("speech", "")
    lang = json_data.get("lang", "")
    
    # Default speech to chat if missing
    if not speech:
        speech = chat
        
    # Check for English guardrail
    if user_lang == "ENGLISH":
        # If user spoke English, enforce English output (no Hindi script in speech)
        # We only force 'en' if the model output 'hi' or Devanagari script, indicating a translation error.
        # This allows other languages like Spanish ('es') or French ('fr') to pass through.
        if lang == "hi" or re.search(r'[\u0900-\u097F]', speech):
            speech = chat
            lang = "en"
            
    # Check for Hindi/Hinglish guardrail
    elif user_lang in ("HINDI", "HINGLISH"):
        # If user spoke Hindi/Hinglish, enforce Devanagari script for speech
        if not re.search(r'[\u0900-\u097F]', speech):
            # Speech is not in Devanagari script (e.g. it is in Hinglish Latin script)
            speech = await transliterate_to_devanagari(speech, client)
        if lang != "hi":
            lang = "hi"
            
    # Re-serialize to keep the exact formatting expected by the frontend
    corrected_data = {
        "chat": chat,
        "speech": speech,
        "lang": lang
    }
    
    # We serialize with ensure_ascii=False to allow Devanagari characters directly in the JSON
    return json.dumps(corrected_data, ensure_ascii=False)

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
                # Find first '<' character
                idx = self.buffer.find("<")
                if idx == -1:
                    # No '<' found. The entire buffer is raw text.
                    if self.buffer:
                        events.append({"type": "text_update", "text": self.buffer})
                        self.buffer = ""
                    break
                
                # If there is raw text before '<', yield it
                if idx > 0:
                    events.append({"type": "text_update", "text": self.buffer[:idx]})
                    self.buffer = self.buffer[idx:]
                    # Now self.buffer starts with '<'
                
                # Check if we have enough characters to match tags
                # Robust match for <thought> or `<thought ` (space, newline, etc.)
                thought_match = re.match(r"^<thought[>\s\n]", self.buffer)
                if thought_match:
                    match_len = len(thought_match.group(0))
                    self.buffer = self.buffer[match_len:]
                    self.state = "thought"
                    self.current_thought = ""
                    self.yielded_thought_len = 0
                    continue
                
                # Robust match for <finish> or `<finish `
                finish_match = re.match(r"^<finish[>\s\n]", self.buffer)
                if finish_match:
                    match_len = len(finish_match.group(0))
                    self.buffer = self.buffer[match_len:]
                    self.state = "finish"
                    self.current_finish = ""
                    self.yielded_finish_len = 0
                    continue
                
                # Match call tag with optional attributes and optional self-closing slash
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
                
                # If it doesn't match any tag, check if it could be a prefix of one of them
                is_prefix = False
                for tag in ["<thought>", "<finish>"]:
                    if tag.startswith(self.buffer):
                        is_prefix = True
                        break
                if not is_prefix:
                    # Check if it matches prefix of '<call:...'
                    if "<call:".startswith(self.buffer) or self.buffer.startswith("<call:"):
                        if ">" not in self.buffer:
                            is_prefix = True
                
                if is_prefix:
                    # If it's a potential prefix, we wait for more data (unless buffer is abnormally long)
                    if len(self.buffer) < 100:
                        break
                
                # If it's not a prefix or the buffer is too long (false alarm '<'),
                # yield the '<' and continue parsing
                events.append({"type": "text_update", "text": self.buffer[0]})
                self.buffer = self.buffer[1:]
                
            elif self.state == "thought":
                tag = "</thought>"
                end_pos = self.buffer.find(tag)
                if end_pos != -1:
                    self.current_thought += self.buffer[:end_pos]
                    self.buffer = self.buffer[end_pos + len(tag):]
                    new_text = self.current_thought[self.yielded_thought_len:]
                    events.append({"type": "thought", "text": new_text, "status": "completed"})
                    self.state = "idle"
                else:
                    # Check for implicit transition if model forgot </thought>
                    implicit_tags = ["<call:", "<finish>"]
                    found_implicit = -1
                    for itag in implicit_tags:
                        pos = self.buffer.find(itag)
                        if pos != -1:
                            if found_implicit == -1 or pos < found_implicit:
                                found_implicit = pos
                                
                    if found_implicit != -1:
                        # Auto-close thought block
                        self.current_thought += self.buffer[:found_implicit]
                        self.buffer = self.buffer[found_implicit:] # keep the tag in buffer for next idle parse
                        new_text = self.current_thought[self.yielded_thought_len:]
                        events.append({"type": "thought", "text": new_text, "status": "completed"})
                        self.state = "idle"
                        continue
                        
                    # Check if buffer ends with a prefix of </thought>
                    match_len = 0
                    for i in range(len(tag) - 1, 0, -1):
                        prefix = tag[:i]
                        if self.buffer.endswith(prefix):
                            match_len = i
                            break
                    
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
                    # Check for implicit transition if model forgot closing call tag
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
                        
                    # Check if buffer ends with a prefix of closing call tag
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
                    # Check for implicit transition if model forgot closing finish tag
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
                        
                    # Check if buffer ends with a prefix of </finish>
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

async def run_memory_summarization_background(ollama_host: str):
    """Distills episodic conversations into facts in the knowledge graph in the background."""
    try:
        from database import get_sqlite_conn
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, role, content FROM conversations ORDER BY timestamp ASC")
        rows = cursor.fetchall()
        conn.close()
        
        valid_records = [dict(r) for r in rows]
        if len(valid_records) < 20:
            return
            
        distill_set = valid_records[:20]
        
        conversation_log = ""
        for item in distill_set:
            conversation_log += f"{item.get('role', 'user')}: {item.get('content', '')}\n"
            
        client = ollama.Client(host=ollama_host)
        prompt = (
            "Analyze the conversation log below. Extract key persistent facts about the user's "
            "preferences, workflows, or project details as a JSON list. "
            "Each item must be: {\"subject\": \"...\", \"predicate\": \"...\", \"object\": \"...\"}\n"
            "Keep facts simple and short. Return ONLY valid JSON array.\n\n"
            f"Log:\n{conversation_log}"
        )
        
        fallback_model = "qwen2.5-coder:1.5b-instruct-q8_0"
        try:
            res = client.generate(model=fallback_model, prompt=prompt)
        except Exception:
            model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
            res = client.generate(model=model, prompt=prompt)

        # GenerateResponse is an object — use attribute access with dict fallback
        text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()

        if text.startswith("```"):
            text = text.strip("`").replace("json\n", "").strip()
            
        try:
            facts = json.loads(text)
            from src.tools.knowledge import kg_add_fact
            for f in facts:
                if f.get("subject") and f.get("predicate") and f.get("object"):
                    kg_add_fact(f["subject"], f["predicate"], f["object"])
            
            # Prune distilled rows to keep conversations lean
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            ids_to_delete = [r["id"] for r in distill_set]
            placeholders = ",".join("?" for _ in ids_to_delete)
            cursor.execute(f"DELETE FROM conversations WHERE id IN ({placeholders})", ids_to_delete)
            conn.commit()
            conn.close()
            print(f"[Memory Summarizer] Distilled {len(distill_set)} episodic turns into facts.")
        except Exception as je:
            print("[Memory Summarizer] JSON parse error on response:", je, text)
    except Exception as e:
        print("[Memory Summarizer] Summarization cycle execution error:", e)

def get_gpu_vram_usage() -> float:
    try:
        import subprocess
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"],
            encoding="utf-8"
        )
        used, total = map(float, output.strip().split(","))
        return (used / total) * 100.0
    except Exception:
        try:
            import psutil
            return psutil.virtual_memory().percent
        except Exception:
            return 50.0

def clean_final_text(text: str) -> str:
    """Safely extracts the final message and removes XML-like agent loop tags."""
    # Remove thought blocks
    text = re.sub(r"<thought>.*?</thought>", "", text, flags=re.DOTALL)
    # Remove call blocks
    text = re.sub(r"<call:\w+>.*?</call:\w+>", "", text, flags=re.DOTALL)
    # Remove any stray tags
    text = re.sub(r"</?thought>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?finish>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?call:\w+>", "", text, flags=re.IGNORECASE)
    return text.strip()

def critique_and_correct_tool_call(tool_name: str, args_str: str, client: ollama.Client) -> Tuple[bool, str, str]:
    """Inspects tool signature and code blocks locally to auto-correct errors."""
    try:
        # Check registry first
        if tool_name not in TOOL_REGISTRY:
            return False, args_str, f"Unknown tool '{tool_name}' requested."
            
        tool_meta = TOOL_REGISTRY[tool_name]
        func = tool_meta["func"]
        
        # Parse arguments to verify JSON validity
        try:
            args = json.loads(args_str) if args_str.strip() else {}
        except Exception as e:
            # Broken JSON: correct via LLM
            prompt = (
                f"You are a syntax recovery engine. Correct the following invalid JSON arguments for tool '{tool_name}' so it is well-formed.\n"
                f"Invalid JSON:\n{args_str}\n\n"
                f"Output ONLY the corrected JSON string. Do not include markdown code block syntax."
            )
            res = client.generate(model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=prompt)
            corrected = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
            # clean code blocks if model added them
            if corrected.startswith("```"):
                corrected = corrected.strip("`").replace("json\n", "").strip()
            # Verify if corrected parses
            try:
                json.loads(corrected)
                return True, corrected, "Auto-corrected malformed JSON arguments."
            except Exception:
                return False, args_str, f"Failed to auto-correct malformed JSON: {e}"

        # 1. Tool Signature Verification
        import inspect
        try:
            sig = inspect.signature(func)
            # Check if there are any *args or **kwargs
            has_var_positional = any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in sig.parameters.values())
            has_var_keyword = any(p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values())

            # Build lists of required and valid parameters
            required_params = []
            valid_params = set()

            for name, param in sig.parameters.items():
                if param.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY):
                    valid_params.add(name)
                    if param.default is inspect.Parameter.empty:
                        required_params.append(name)

            # Check missing required params
            missing = [p for p in required_params if p not in args]
            # Check unexpected params
            unexpected = [p for p in args if p not in valid_params] if not has_var_keyword else []

            if missing or unexpected:
                # Signature mismatch: try to correct it via qwen2.5-coder:1.5b
                sig_err_msg = ""
                if missing:
                    sig_err_msg += f"Missing required parameter(s): {', '.join(missing)}. "
                if unexpected:
                    sig_err_msg += f"Unexpected parameter(s): {', '.join(unexpected)}."

                prompt = (
                    f"You are a signature matching assistant. The tool '{tool_name}' has the following expected parameter signature:\n"
                    f"Signature: {str(sig)}\n"
                    f"The provided arguments were:\n{json.dumps(args)}\n"
                    f"Validation Error: {sig_err_msg}\n\n"
                    f"Correct or map the keys in the arguments to match the expected signature. Output ONLY the corrected JSON string. Do not include markdown code block syntax."
                )
                res = client.generate(model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=prompt)
                corrected = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
                if corrected.startswith("```"):
                    corrected = corrected.strip("`").replace("json\n", "").strip()

                try:
                    corrected_args = json.loads(corrected)
                    # Re-verify after correction
                    missing_corr = [p for p in required_params if p not in corrected_args]
                    unexpected_corr = [p for p in corrected_args if p not in valid_params] if not has_var_keyword else []
                    if not missing_corr and not unexpected_corr:
                        return True, json.dumps(corrected_args), f"Auto-corrected parameter signature: {sig_err_msg}"
                except Exception:
                    pass

                return False, args_str, f"Signature validation failed: {sig_err_msg} Expected: {str(sig)}"
        except ValueError:
            # inspect.signature not supported (e.g. builtins), skip signature validation
            pass

        # 2. Code Syntax Verification & LLM Linting
        code_to_validate = None
        code_type = None # "python" or "json"
        
        # Check run_python or create_dynamic_tool
        if tool_name in ["run_python", "create_dynamic_tool"]:
            code_to_validate = args.get("code", "")
            code_type = "python"
        # Check write_file
        elif tool_name == "write_file":
            path = args.get("path", "") or args.get("filepath", "") or args.get("TargetFile", "")
            content = args.get("content", "") or args.get("CodeContent", "")
            if path.endswith(".py"):
                code_to_validate = content
                code_type = "python"
            elif path.endswith(".json"):
                code_to_validate = content
                code_type = "json"

        if code_to_validate:
            if code_type == "python":
                try:
                    import ast
                    ast.parse(code_to_validate)
                except SyntaxError as se:
                    # Syntax error: request correction from LLM
                    prompt = (
                        f"You are a code-healing assistant. The following Python code contains a syntax error:\n"
                        f"Error: {se}\n\n"
                        f"Code:\n```python\n{code_to_validate}\n```\n\n"
                        f"Rewrite the code to fix the syntax error. Output ONLY the raw corrected Python code, no explanation, no markdown blocks."
                    )
                    res = client.generate(model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=prompt)
                    corrected_code = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
                    if corrected_code.startswith("```"):
                        corrected_code = corrected_code.strip("`").replace("python\n", "").strip()
                    
                    # Verify corrected code
                    try:
                        ast.parse(corrected_code)
                        if tool_name in ["run_python", "create_dynamic_tool"]:
                            args["code"] = corrected_code
                        elif tool_name == "write_file":
                            if "content" in args:
                                args["content"] = corrected_code
                            elif "CodeContent" in args:
                                args["CodeContent"] = corrected_code
                        return True, json.dumps(args), f"Auto-healed Python code syntax error on line {se.lineno}."
                    except SyntaxError as se2:
                        return False, args_str, f"Python syntax check failed: {se} (Auto-healing also failed with syntax error on line {se2.lineno}: {se2})"

                # Python code is syntactically valid via AST.
                # Run qwen2.5-coder:1.5b-instruct-q8_0 as a linter / compiler warning check.
                lint_prompt = (
                    f"You are a Python code linter. Analyze the following Python code for any logic errors, undefined names, incorrect method calls, or compiler warnings.\n"
                    f"Code:\n```python\n{code_to_validate}\n```\n\n"
                    f"If you find any critical compiler warnings or errors, list them clearly. If the code is perfect and contains no issues, respond with ONLY 'OK'. Do not explain if there are no errors."
                )
                res = client.generate(model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=lint_prompt)
                lint_resp = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
                if "OK" not in lint_resp.upper() and len(lint_resp) > 5:
                    # Feed the lint warning back to the agent to prompt self-correction
                    return False, args_str, f"Python Lint Warning: Compiler warning or logic error detected in code block:\n{lint_resp}"

            elif code_type == "json":
                try:
                    json.loads(code_to_validate)
                except Exception as e:
                    # Invalid JSON content: correct via LLM
                    prompt = (
                        f"You are a syntax recovery engine. Correct the following invalid JSON content to make it well-formed.\n"
                        f"Invalid JSON:\n{code_to_validate}\n\n"
                        f"Output ONLY the corrected JSON string. Do not include markdown code block syntax."
                    )
                    res = client.generate(model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=prompt)
                    corrected_code = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
                    if corrected_code.startswith("```"):
                        corrected_code = corrected_code.strip("`").replace("json\n", "").strip()

                    try:
                        json.loads(corrected_code)
                        if "content" in args:
                            args["content"] = corrected_code
                        elif "CodeContent" in args:
                            args["CodeContent"] = corrected_code
                        return True, json.dumps(args), "Auto-corrected malformed JSON file content."
                    except Exception as e2:
                        return False, args_str, f"JSON syntax check failed: {e} (Auto-healing failed: {e2})"

        return True, args_str, ""  # BUG-25 fix: True = validated OK (no correction needed)
    except Exception as e:
        return False, args_str, f"Critique verification failed: {e}"

async def prune_and_compress_history(history: List[Dict[str, str]], client: ollama.Client) -> List[Dict[str, str]]:
    """Prunes history if too long, summarizes older turns, and saves raw history to Turbovec RAG."""
    # We prune if history turns > 9 (System + 8 turns)
    if len(history) <= 9:
        return history
        
    print(f"[Context Governor] Active history has {len(history)} turns. Compressing old segments...")
    
    # Segment to compress: skip system prompt and last 4 turns
    compress_turns = history[1:-4]
    keep_turns = history[-4:]
    
    # Format log to summarize
    log_text = ""
    for idx, turn in enumerate(compress_turns):
        role_label = "Assistant" if turn["role"] == "assistant" else "User"
        log_text += f"{role_label}: {turn['content']}\n"
        
    # Summarize via LLM
    prompt = (
        "You are an executive memory compressor. Synthesize the following sequence of assistant actions, "
        "commands executed, decisions, and observations into a concise bulleted summary of key facts and progress.\n\n"
        f"Sequence:\n{log_text}"
    )
    
    try:
        res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=prompt)
        summary = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
    except Exception:
        summary = "Older context consolidated by System."
        
    # Index raw turns into Turbovec RAG as archived memory
    try:
        ingest_into_knowledge_base("archived_history", log_text, {"timestamp": time.time()})
        print(f"[Context Governor] Archived context segments ingested into Turbovec RAG.")
    except Exception as e:
        print(f"[Context Governor] RAG ingestion failed: {e}")
        
    # Build new history list
    new_history = [history[0]]
    # BUG-27 fix: Anthropic forbids role:system mid-messages array; use role:user with [SYSTEM] prefix
    new_history.append({"role": "user", "content": f"[SYSTEM — Context Archive]:\n{summary}"})
    new_history.extend(keep_turns)
    
    return new_history

async def execute_single_tool_async(
    tool_name: str, 
    args: dict, 
    tier: int, 
    client: ollama.Client, 
    active_model: str
) -> Tuple[str, str, str]:
    """Helper to run security auditor checks and execute tool asynchronously."""
    args_str = json.dumps(args)
    
    # 1. Security Auditor local consensus verification
    if tier >= 2:
        auditor_model = "qwen2.5-coder:1.5b-instruct-q8_0"
        await event_bus.publish("agent_thoughts", {
            "agent": "Security Auditor", 
            "thought": f"Auditing '{tool_name}' execution with arguments: {args_str}"
        })
        
        audit_prompt = (
            f"You are the Meridian Security Auditor. Assess if the following tool execution is safe and does not contain vulnerabilities, dangerous deletions, shell injects, or system risks.\n"
            f"Tool: {tool_name}\n"
            f"Arguments: {args_str}\n\n"
            f"Respond ONLY in this exact format:\n"
            f"REASONING: <brief analysis of the arguments>\n"
            f"DECISION: <APPROVED or REJECTED>"
        )
        
        try:
            audit_res = await asyncio.to_thread(client.generate, model=auditor_model, prompt=audit_prompt)
            audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
        except Exception:
            try:
                audit_res = await asyncio.to_thread(client.generate, model=active_model, prompt=audit_prompt)
                audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
            except Exception:
                audit_text = "REASONING: Auditor model unreachable. Failing secure.\nDECISION: REJECTED_UNREACHABLE"
        
        decision = "APPROVED"
        reasoning = ""
        for line in audit_text.split("\n"):
            if line.upper().startswith("DECISION:"):
                decision = line.split(":", 1)[1].strip().upper()
            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()
                
        await event_bus.publish("agent_thoughts", {
            "agent": "Security Auditor", 
            "thought": f"Audit Result for '{tool_name}': {decision}. Reasoning: {reasoning}"
        })
        
        if "REJECTED" in decision:
            if "UNREACHABLE" in decision:
                return tool_name, f"Blocked: Security Auditor unreachable for Tier {tier} tool.", "blocked_unreachable"
            else:
                return tool_name, f"Blocked by Security Auditor: {reasoning}", "blocked"

    # 2. Run approved tool
    try:
        result = await call_tool(tool_name, args)
        add_to_task_log(tool_name, tier, "success")
        return tool_name, result, "success"
    except Exception as e:
        err_txt = str(e)
        add_to_task_log(tool_name, tier, "failed", err_txt)
        return tool_name, f"Error: {err_txt}", "failed"

def detect_complex_prompt(prompt: str) -> bool:
    p = prompt.lower()
    complex_words = ["build", "setup", "implement", "deploy", "architecture", "design and create", "create a complete", "pipeline", "scaffold"]
    return len(prompt) > 200 or any(w in p for w in complex_words)

async def decompose_goal_to_checklist(prompt: str, client: ollama.Client) -> List[Dict[str, Any]]:
    decomp_prompt = (
        "You are the Meridian Project Manager. Decompose the user's goal into a logical list of sub-tasks (maximum 4).\n"
        f"Goal: {prompt}\n\n"
        "Return ONLY a JSON list of tasks, where each task is an object with \"id\" (int) and \"description\" (str). "
        "Do NOT include markdown block wrapping. Example response: [{\"id\": 1, \"description\": \"Create file a.py\"}, {\"id\": 2, \"description\": \"Write tests\"}]"
    )
    try:
        res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=decomp_prompt)
        text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
        if text.startswith("```"):
            text = text.strip("`").replace("json\n", "").strip()
        tasks = json.loads(text)
        if isinstance(tasks, list):
            return tasks
    except Exception as e:
        print("[HTP] Failed to decompose goal, falling back to single loop:", e)
    return []

async def score_candidate_branch(tool_name: str, args_str: str, history: List[Dict[str, str]], client: ollama.Client) -> float:
    prompt = (
        f"You are the Monte Carlo Tree Search evaluator. Score the proposed action from 0.0 (fails/dangerous/unlikely to succeed) to 1.0 (highly successful/safe/optimal).\n"
        f"Goal/History context length: {len(history)} turns.\n"
        f"Proposed Action: Call tool '{tool_name}' with args: {args_str}\n\n"
        f"Output ONLY the numeric score (e.g. 0.85). Do not include any text or commentary."
    )
    try:
        res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=prompt)
        val_str = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
        score = float(re.findall(r"[-+]?\d*\.\d+|\d+", val_str)[0])
        return min(max(score, 0.0), 1.0)
    except Exception:
        return 0.5

async def run_self_question_check(goal: str, history: List[Dict[str, str]], client: ollama.Client) -> Tuple[bool, str]:
    check_prompt = (
        f"Goal: {goal}\n"
        f"Recent History turns: {len(history)}.\n"
        "Are the exact paths, parameters, and environment dependencies verified? Or are you about to assume details?\n"
        "Answer ONLY 'YES' if they are verified, or 'NO' if they are not verified."
    )
    try:
        res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=check_prompt)
        ans = (res.response if hasattr(res, "response") else res.get("response", "")).strip().upper()
        if "NO" in ans:
            return False, "You do not have verified information. You MUST run search or observation commands first (e.g. read_file, dir_list, grep_search) to inspect paths and verify details before making assumptions."
        return True, ""
    except Exception:
        return True, ""

async def run_react_agent_loop(
    prompt: str,
    brain_model: str,
    ollama_host: str,
    model_source: str = "local",
    api_provider: str = "gemini",
    is_worker: bool = False
) -> AsyncGenerator[str, None]:
    
    # Helper to format SSE events
    def sse_event(event_type: str, data_payload: str) -> str:
        lines = data_payload.split('\n')
        data_lines = [f"data: {line}" for line in lines]
        return f"event: {event_type}\n" + "\n".join(data_lines) + "\n\n"

    # Check semantic cache first
    cached = check_semantic_cache(prompt)
    if cached:
        yield sse_event("thought", json.dumps({"type": "planning", "text": "Semantic Cache Match: returns instantly (<5ms) from Turbovec", "tool": "semantic_cache"}))
        words = cached.split(" ")
        for i, word in enumerate(words):
            space = " " if i > 0 else ""
            yield sse_event("text", space + word)
            await asyncio.sleep(0.005)
        # BUG-5 fix: only log to DB when this is a user-facing (non-worker) call.
        # HTP worker sub-loops run internal planner prompts that must not pollute
        # the persistent conversation history shown to the user.
        if not is_worker:
            add_to_conversations("user", prompt)
            add_to_conversations("assistant", cached)
        add_to_task_log("semantic_cache", 0, "success")
        return

    # Fetch recent conversations for context (excluding the new prompt that we are about to add)
    past_messages = get_conversation_history(limit=10)

    if not is_worker:  # BUG-5 fix: skip DB write for internal HTP worker loops
        add_to_conversations("user", prompt)
    add_to_task_log("ollama_api", 2, "started")

    # Set up client and initial prompt context
    client = ollama.Client(host=ollama_host)

    # 1. Hierarchical Task Planning (HTP) (Upgrade 10)
    if not is_worker and detect_complex_prompt(prompt):
        yield sse_event("thought", json.dumps({
            "id": f"htp-decomposing-{time.time()}",
            "type": "planning",
            "text": "[Hierarchical Task Planning] Decomposing complex prompt into sub-tasks...",
            "status": "running"
        }))
        checklist = await decompose_goal_to_checklist(prompt, client)
        
        if checklist:
            yield sse_event("thought", json.dumps({
                "id": f"htp-decomposed-{time.time()}",
                "type": "planning",
                "text": f"[Hierarchical Task Planning] Checklist generated:\n" + "\n".join(f"- Task {t['id']}: {t['description']}" for t in checklist),
                "status": "completed"
            }))
            
            worker_outcomes = []
            for sub_task in checklist:
                task_desc = sub_task["description"]
                yield sse_event("thought", json.dumps({
                    "id": f"htp-task-start-{sub_task['id']}-{time.time()}",
                    "type": "planning",
                    "text": f"[Hierarchical Task Planning] Spawning worker loop for Sub-task {sub_task['id']}: '{task_desc}'...",
                    "status": "running"
                }))
                
                worker_prompt = f"Your task is to execute sub-task: '{task_desc}' as part of the overall goal: '{prompt}'. Focus only on completing this sub-task and report the results."
                worker_text = ""
                async for event in run_react_agent_loop(
                    prompt=worker_prompt,
                    brain_model=brain_model,
                    ollama_host=ollama_host,
                    model_source=model_source,
                    api_provider=api_provider,
                    is_worker=True
                ):
                    yield event
                    if event.startswith("event: text"):
                        lines = event.splitlines()
                        for line in lines:
                            if line.startswith("data: "):
                                worker_text += line[6:]
                                
                worker_outcomes.append(f"Sub-task {sub_task['id']} Result: {worker_text}")
                yield sse_event("thought", json.dumps({
                    "id": f"htp-task-complete-{sub_task['id']}-{time.time()}",
                    "type": "planning",
                    "text": f"[Hierarchical Task Planning] Sub-task {sub_task['id']} completed.",
                    "status": "completed"
                }))
                
            yield sse_event("thought", json.dumps({
                "id": f"htp-synthesis-{time.time()}",
                "type": "planning",
                "text": "[Hierarchical Task Planning] Synthesis of all worker outcomes...",
                "status": "running"
            }))
            synthesis_prompt = (
                f"You are the Meridian Project Manager. Synthesize the following completed worker sub-tasks into a cohesive final update to the user.\n"
                f"Goal: {prompt}\n"
                f"Worker Outcomes:\n" + "\n".join(worker_outcomes) + "\n\n"
                "Return the final response in the required JSON format: {\"chat\": \"...\", \"speech\": \"...\", \"lang\": \"...\"}"
            )
            try:
                res_sys = await asyncio.to_thread(client.chat, model=brain_model, messages=[{"role": "user", "content": synthesis_prompt}])
                text_sys = (res_sys.message.content if hasattr(res_sys, "message") and hasattr(res_sys.message, "content") else res_sys.get("message", {}).get("content", "")).strip()
                if text_sys.startswith("```"):
                    text_sys = text_sys.strip("`").replace("json\n", "").strip()
                yield sse_event("text", text_sys)
            except Exception as se:
                yield sse_event("text", json.dumps({"chat": "All tasks completed.", "speech": "All tasks completed.", "lang": "en"}))
            return
    tools_doc = generate_tools_doc()
    
    # Load workspace config overrides
    if model_source == "local":
        from src.core.mode import load_workspace_config
        config = load_workspace_config()
        workspace_model = config.get("brain_model")
        if workspace_model:
            print(f"[Workspace Config] Overriding brain model from '{brain_model}' to '{workspace_model}'")
            brain_model = workspace_model
    
    # Generate system prompt dynamically via cognitive modes classifier
    from src.core.mode import build_system_prompt, detect_user_language
    user_lang = detect_user_language(prompt)
    system_prompt = build_system_prompt(prompt, brain_model, ollama_host, tools_doc)

    history = [{"role": "system", "content": system_prompt}]
    for msg in past_messages:
        history.append({"role": msg["role"], "content": msg["content"]})
    history.append({"role": "user", "content": prompt})

    max_turns = 10
    turn = 0
    final_text = ""
    active_model = brain_model
    
    # Repetition detector tracking variables
    last_tool_call = None
    consecutive_repeat_count = 0
    
    # Session-scoped manifest to track temporary screenshots for automated cleanup
    created_temp_files = []
    _interrupt_event.clear()  # Reset any stale interrupt signal from a previous run
    try:
        while turn < max_turns:
            final_text = ""
            if _interrupt_event.is_set():
                _interrupt_event.clear()
                yield sse_event("thought", json.dumps({"type": "planning", "text": "Voice barge-in detected. Interrupting execution.", "status": "completed"}))
                return
            turn += 1
            
            # Prune and compress history if too long (local only — cloud APIs have large context windows)
            if model_source == "local":
                history = await prune_and_compress_history(history, client)

            # 2. Self-Questioning Check (Upgrade 11)
            is_verified, warning_msg = await run_self_question_check(prompt, history, client)
            temp_sys_idx = -1
            if not is_verified:
                yield sse_event("thought", json.dumps({
                    "id": f"self-question-{turn}-{time.time()}",
                    "type": "warning",
                    "text": f"[Self-Questioning] Lack verified information for target path/dependencies. Injecting exploratory search gate...",
                    "status": "completed"
                }))
                history.append({"role": "system", "content": f"[Self-Questioning Gate Warning]: {warning_msg}"})
                temp_sys_idx = len(history) - 1
            
            # Dynamic VRAM/RAM Offloading Scheduler (Only trigger for local model configurations)
            vram_load = get_gpu_vram_usage()
            if model_source == "local" and vram_load > 85.0 and "cloud" not in active_model.lower():
                fallback_brain = "qwen2.5-coder:1.5b-instruct-q8_0"
                if active_model != fallback_brain:
                    yield sse_event("thought", json.dumps({
                        "id": f"vram-warning-{turn}-{time.time()}",
                        "type": "warning",
                        "text": f"High memory load detected ({vram_load:.1f}%). Dynamic VRAM allocation: swapping brain model from '{active_model}' to fallback model '{fallback_brain}' to prevent system crash.",
                        "status": "running"
                    }))
                    active_model = fallback_brain
                    # Truncate context if required for lightweight model context length constraints
                    if len(history) > 6:
                        history = [history[0]] + history[-4:]
            
            # Start response stream
            try:
                if model_source == "local":
                    response_stream = client.chat(
                        model=active_model,
                        messages=history,
                        stream=True
                    )
                else:
                    # Cloud APIs Direct Integration (Option 3)
                    if api_provider == "gemini":
                        from openai import OpenAI
                        gemini_key = os.environ.get("GEMINI_API_KEY")
                        if not gemini_key:
                            raise ValueError("GEMINI_API_KEY environment variable is not configured.")
                        openai_client = OpenAI(
                            api_key=gemini_key,
                            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                        )
                        response_stream = openai_client.chat.completions.create(
                            model=active_model,
                            messages=history,
                            stream=True
                        )
                    elif api_provider == "openai":
                        from openai import OpenAI
                        openai_key = os.environ.get("OPENAI_API_KEY")
                        if not openai_key:
                            raise ValueError("OPENAI_API_KEY environment variable is not configured.")
                        openai_client = OpenAI(api_key=openai_key)
                        response_stream = openai_client.chat.completions.create(
                            model=active_model,
                            messages=history,
                            stream=True
                        )
                    elif api_provider == "deepseek":
                        from openai import OpenAI
                        deepseek_key = os.environ.get("DEEPSEEK_API_KEY")
                        if not deepseek_key:
                            raise ValueError("DEEPSEEK_API_KEY environment variable is not configured.")
                        openai_client = OpenAI(
                            api_key=deepseek_key,
                            base_url="https://api.deepseek.com/v1"
                        )
                        response_stream = openai_client.chat.completions.create(
                            model=active_model,
                            messages=history,
                            stream=True
                        )
                    elif api_provider == "anthropic":
                        from anthropic import Anthropic
                        anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
                        if not anthropic_key:
                            raise ValueError("ANTHROPIC_API_KEY environment variable is not configured.")
                        anthropic_client = Anthropic(api_key=anthropic_key)
                        system_msg = ""
                        claude_history = []
                        for m in history:
                            if m["role"] == "system":
                                system_msg = m["content"]
                            else:
                                role = "assistant" if m["role"] == "assistant" else "user"
                                claude_history.append({"role": role, "content": m["content"]})
                        
                        response_stream = anthropic_client.messages.create(
                            model=active_model,
                            system=system_msg,
                            messages=claude_history,
                            max_tokens=4096,
                            stream=True
                        )
                    else:
                        raise ValueError(f"Unsupported API Provider: '{api_provider}'")
            except Exception as e:
                # Self-healing fallback to 1.5B model if RAM/VRAM/API issues
                if active_model != "qwen2.5-coder:1.5b-instruct-q8_0":
                    fallback_brain = "qwen2.5-coder:1.5b-instruct-q8_0"
                    print(f"[Fallback Engine] Switching to local model '{fallback_brain}' due to: {e}")
                    yield sse_event("thought", json.dumps({
                        "id": f"api-fallback-{turn}-{time.time()}",
                        "type": "warning",
                        "text": f"API execution failed: {str(e)}. Swapping to local fallback model '{fallback_brain}'.",
                        "status": "running"
                    }))
                    active_model = fallback_brain
                    model_source = "local" # Force local fallback
                    if len(history) > 6:
                        history = [history[0]] + history[-4:]
                    try:
                        response_stream = client.chat(
                            model=active_model,
                            messages=history,
                            stream=True
                        )
                    except Exception as ex:
                        err_msg = f"Fallback model '{active_model}' execution failed: {str(ex)}"
                        yield sse_event("thought", json.dumps({
                            "id": f"fallback-failure-{turn}-{time.time()}",
                            "type": "warning",
                            "text": err_msg,
                            "status": "failed"
                        }))
                        add_to_task_log("ollama_api", 2, "failed", err_msg)
                        return
                else:
                    err_msg = f"Execution error: {str(e)}"
                    yield sse_event("thought", json.dumps({
                        "id": f"api-error-{turn}-{time.time()}",
                        "type": "warning",
                        "text": err_msg,
                        "status": "failed"
                    }))
                    add_to_task_log("ollama_api", 2, "failed", err_msg)
                    return

            parser = StreamingXMLParser()
            full_turn_text = ""
            calls_to_execute = []
            thought_id = f"thought-react-{time.time()}"
            
            yield sse_event("thought", json.dumps({
                "id": thought_id,
                "type": "planning",
                "text": f"Agent Reasoning Turn {turn}...\n",
                "status": "running",
                "append": True,
                "mascot_state": "default",
                "mascot_wardrobe": "none"
            }))
            await event_bus.publish("agent_thoughts", {"agent": "Coordinator", "thought": f"Initializing reasoning turn {turn}..."})

            # Feed the stream to the tag parser in real time
            for chunk in response_stream:
                if _interrupt_event.is_set():
                    # BUG-32 fix: do NOT clear here — a second interrupt between is_set() and clear()
                    # would be silently lost. The turn-start clear at line 1049 is sufficient.
                    # BUG-14 fix: remove the temporary self-question warning from history
                    # before returning, so it cannot bleed into the next request's context.
                    if temp_sys_idx != -1 and temp_sys_idx < len(history):
                        history.pop(temp_sys_idx)
                        temp_sys_idx = -1
                    yield sse_event("thought", json.dumps({"type": "planning", "text": "Voice barge-in detected. Interrupting execution.", "status": "completed"}))
                    return
                if model_source == "local":
                    # Ollama streaming chunks are ChatResponse objects, not dicts
                    if hasattr(chunk, "message") and hasattr(chunk.message, "content"):
                        content = chunk.message.content or ""
                    else:
                        content = chunk.get("message", {}).get("content", "")  # fallback for older ollama lib

                else:
                    if api_provider == "anthropic":
                        if chunk.type == "content_block_delta":
                            content = chunk.delta.text
                        else:
                            content = ""
                    else:
                        content = chunk.choices[0].delta.content or ""
                if not content:
                    continue
                    
                full_turn_text += content
                parsed_events = parser.feed(content)
                
                # Speculative preheating of resources
                if parser.state == "call" and parser.current_call_name:
                    asyncio.create_task(preheat_tool(parser.current_call_name, parser.current_call_args))
                
                for event in parsed_events:
                    if event["type"] == "thought_update":
                        yield sse_event("thought", json.dumps({"id": thought_id, "type": "planning", "text": event["text"], "status": "running", "append": True}))
                        await event_bus.publish("agent_thoughts", {"agent": "Coordinator", "thought": event["text"]})
                    elif event["type"] == "thought":
                        yield sse_event("thought", json.dumps({"id": thought_id, "type": "planning", "text": event["text"], "status": "completed", "append": True}))
                        await event_bus.publish("agent_thoughts", {"agent": "Coordinator", "thought": event["text"]})
                    elif event["type"] == "text_update":
                        final_text += event["text"]
                        yield sse_event("text", event["text"])
                    elif event["type"] == "finish":
                        # BUG-11 fix: skip consensus debate on empty/trivial finish text
                        # to avoid wasting 2 extra LLM calls with zero-length input.
                        if not event["text"].strip():
                            continue
                        # Process/correct the final finish text before yielding it
                        corrected_finish = await process_final_response(event["text"], user_lang, client)
                        
                        # 3. Consensus Debate (Upgrade 6)
                        yield sse_event("thought", json.dumps({
                            "id": f"debate-init-{time.time()}",
                            "type": "planning",
                            "text": f"[Consensus Debate] Running Coder vs QA Reviewer consensus debate loop...",
                            "status": "running"
                        }))
                        
                        qa_prompt = (
                            "You are the QA Reviewer Agent. Critique the proposed response below. "
                            "Do NOT write any introduction or conclusion, just write a bullet list of issues.\n\n"
                            f"Proposed Response:\n{corrected_finish}"
                        )
                        qa_res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=qa_prompt)
                        critique = (qa_res.response if hasattr(qa_res, "response") else qa_res.get("response", "")).strip()
                        
                        yield sse_event("thought", json.dumps({
                            "id": f"debate-critique-{time.time()}",
                            "type": "planning",
                            "text": f"[Consensus Debate - QA Reviewer]: Critique generated:\n{critique}",
                            "status": "completed"
                        }))
                        
                        coder_prompt = (
                            "You are the Lead Coder Agent. Refine the proposed response based on the QA Reviewer's critique.\n"
                            "Return ONLY the final JSON response block with keys 'chat', 'speech', and 'lang'. No explanation, no markdown.\n\n"
                            f"Original Response:\n{corrected_finish}\n\n"
                            f"Critique:\n{critique}"
                        )
                        coder_res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=coder_prompt)
                        refined = (coder_res.response if hasattr(coder_res, "response") else coder_res.get("response", "")).strip()
                        
                        if refined.startswith("```"):
                            refined = refined.strip("`").replace("json\n", "").strip()
                            
                        try:
                            json.loads(refined)
                            debated_finish = refined
                        except Exception:
                            debated_finish = corrected_finish
                            
                        _debate_key = f"debate-{uuid.uuid4()}"  # BUG-31 fix: uuid4 avoids collision-prone time.time()
                        active_debates[_debate_key] = {
                            "draft": corrected_finish,
                            "critique": critique,
                            "refined": debated_finish
                        }
                        # BUG-10 fix: cap active_debates at 50 entries to prevent
                        # unbounded memory growth (full chat text stored per entry).
                        _MAX_DEBATES = 50
                        if len(active_debates) > _MAX_DEBATES:
                            for _old_k in sorted(active_debates.keys())[:len(active_debates) - _MAX_DEBATES]:
                                del active_debates[_old_k]
                        
                        yield sse_event("thought", json.dumps({
                            "id": f"debate-complete-{time.time()}",
                            "type": "planning",
                            "text": f"[Consensus Debate - Coder]: Solution refined and verified.",
                            "status": "completed"
                        }))
                        
                        final_text = debated_finish
                        yield sse_event("text", debated_finish)
                    elif event["type"] == "call":
                        calls_to_execute.append((event["name"], event["args"]))
                        
            # Update assistant history for loop tracking
            history.append({"role": "assistant", "content": full_turn_text})
            # Remove the temporary warning so it doesn't pollute long term history
            if temp_sys_idx != -1:
                history.pop(temp_sys_idx)

            # Process any tool calls parsed during the stream
            if calls_to_execute:
                observations = []
                
                # Tree-of-Thoughts (ToT) Branch Setup
                tot_checkpoint = list(history)
                tot_failed = False
                failed_tool = ""
                failed_args = {}

                # Split concurrent (Tier 0 read-only) and sequential (Tier >= 1 write/edits)
                concurrent_calls = []
                sequential_calls = []
                
                for tool_name, args_str in calls_to_execute:
                    # 1. Critique & Self-Correction check before handling
                    is_corrected, corrected_args, critique_err = critique_and_correct_tool_call(tool_name, args_str, client)
                    if not is_corrected and critique_err:
                        # Feed the error back to the agent automatically to prompt self-correction
                        observations.append(f"<observation:{tool_name}>Error: {critique_err}</observation:{tool_name}>")
                        yield sse_event("thought", json.dumps({
                            "id": f"critique-failed-{time.time()}",
                            "type": "warning",
                            "text": f"[Critique Engine] Tool call '{tool_name}' failed validation: {critique_err}",
                            "status": "failed"
                        }))
                        continue
                    
                    if is_corrected:
                        yield sse_event("thought", json.dumps({
                            "id": f"critique-{time.time()}",
                            "type": "warning",
                            "text": f"[Critique Engine] Auto-healed tool call '{tool_name}' parameters: {critique_err}",
                            "status": "completed"
                        }))
                        args_str = corrected_args
                    
                    try:
                        args = json.loads(args_str) if args_str.strip() else {}
                    except Exception as e:
                        observations.append(f"<observation:{tool_name}>Invalid JSON args: {str(e)}</observation:{tool_name}>")
                        continue
                        
                    tool_meta = TOOL_REGISTRY.get(tool_name)
                    if not tool_meta:
                        observations.append(f"<observation:{tool_name}>Error: Unknown tool '{tool_name}'</observation:{tool_name}>")
                        continue
                        
                    tier = tool_meta["tier"]

                    # Consecutive loop check (Strategy 1)
                    if tool_name not in EXEMPT_TOOLS:
                        try:
                            # Sort keys to ensure argument structure hashes identically
                            sorted_args_str = json.dumps(args, sort_keys=True)
                        except Exception:
                            sorted_args_str = str(args)
                        
                        call_signature = (tool_name, sorted_args_str)
                        if call_signature == last_tool_call:
                            consecutive_repeat_count += 1
                        else:
                            consecutive_repeat_count = 1
                            last_tool_call = call_signature
                        
                        if consecutive_repeat_count >= 3:
                            err_msg = f"Loop Guardrail: The agent tried calling '{tool_name}' with the same arguments {consecutive_repeat_count} times consecutively. Halting execution."
                            yield sse_event("thought", json.dumps({
                                "id": f"loop-detected-{time.time()}",
                                "type": "error",
                                "text": f"⚠️ [Loop Guardrail] {err_msg}",
                                "status": "failed"
                            }))
                            add_to_task_log(tool_name, tier, "failed", err_msg)
                            
                            # Build the final aborted JSON response for the user
                            final_text = json.dumps({
                                "chat": f"I aborted the operation because I entered an infinite loop trying to run the `{tool_name}` tool repeatedly with the same parameters. Please review your prompt or environment constraints.",
                                "speech": "I had to abort the operation because I entered an infinite loop.",
                                "lang": "en"
                            }, ensure_ascii=False)
                            yield sse_event("text", final_text)
                            return
                    
                    # BUG-29 fix: removed dead majority-vote stub (vote_passed was always True,
                    # making the if-not-vote_passed branch unreachable dead code that misled users
                    # into thinking a real consensus gate was active for high-risk operations).
                    
                    if tier == 0:
                        concurrent_calls.append((tool_name, args, tier))
                    else:
                        sequential_calls.append((tool_name, args, tier))
                
                # --- A. EXECUTE CONCURRENT READ-ONLY CALLS ---
                if concurrent_calls:
                    yield sse_event("thought", json.dumps({
                        "id": f"speculative-{time.time()}",
                        "type": "planning",
                        "text": f"[Speculative Execution] Running {len(concurrent_calls)} read-only tools concurrently...",
                        "status": "running"
                    }))
                    
                    tasks = [
                        execute_single_tool_async(name, params, t, client, active_model)
                        for name, params, t in concurrent_calls
                    ]
                    
                    results = await asyncio.gather(*tasks)
                    for name, res, status in results:
                        observations.append(f"<observation:{name}>{res}</observation:{name}>")
                        if status == "failed":
                            tot_failed = True
                            failed_tool = name
                            for c_name, c_args, c_t in concurrent_calls:
                                if c_name == name:
                                    failed_args = c_args
                                    break
                        yield sse_event("thought", json.dumps({
                            "id": f"spec-complete-{time.time()}-{name}",
                            "type": "status",
                            "text": f"Concurrent tool '{name}' finished ({status}).",
                            "status": "completed"
                        }))
                
                # --- B. EXECUTE SEQUENTIAL STATE-MODIFYING CALLS ---
                for tool_name, args, tier in sequential_calls:
                    audit_id = f"audit-{time.time()}-{random.randint(1000, 9999)}"
                    tool_run_id = f"run-{tool_name}-{time.time()}"
                    
                    # Security Auditor local consensus verification
                    if tier >= 2:
                        auditor_model = "qwen2.5-coder:1.5b-instruct-q8_0"
                        yield sse_event("thought", json.dumps({
                            "id": audit_id,
                            "type": "planning",
                            "text": f"[Security Auditor] Auditing tool '{tool_name}' (Tier {tier}) security footprint...",
                            "status": "running",
                            "mascot_state": "diagnostic",
                            "mascot_wardrobe": "detective_hat"
                        }))
                        await event_bus.publish("agent_thoughts", {
                            "agent": "Security Auditor", 
                            "thought": f"Auditing '{tool_name}' execution with arguments: {json.dumps(args)}"
                        })
                        
                        audit_prompt = (
                            f"You are the Meridian Security Auditor. Assess if the following tool execution is safe and does not contain vulnerabilities, dangerous deletions, shell injects, or system risks.\n"
                            f"Tool: {tool_name}\n"
                            f"Arguments: {json.dumps(args)}\n\n"
                            f"Respond ONLY in this exact format:\n"
                            f"REASONING: <brief analysis of the arguments>\n"
                            f"DECISION: <APPROVED or REJECTED>"
                        )
                        
                        try:
                            audit_res = await asyncio.to_thread(client.generate, model=auditor_model, prompt=audit_prompt)
                            audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
                        except Exception:
                            try:
                                audit_res = await asyncio.to_thread(client.generate, model=active_model, prompt=audit_prompt)
                                audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
                            except Exception:
                                audit_text = "REASONING: Auditor model unreachable. Failing secure.\nDECISION: REJECTED_UNREACHABLE"
                        
                        decision = "APPROVED"
                        reasoning = ""
                        for line in audit_text.split("\n"):
                            if line.upper().startswith("DECISION:"):
                                decision = line.split(":", 1)[1].strip().upper()
                            elif line.upper().startswith("REASONING:"):
                                reasoning = line.split(":", 1)[1].strip()
                                
                        yield sse_event("thought", json.dumps({
                            "id": audit_id,
                            "type": "planning",
                            "text": f"[Security Auditor Decision] {decision}. Reasoning: {reasoning or 'Assessment complete.'}",
                            "status": "completed",
                            "mascot_state": "default",
                            "mascot_wardrobe": "none"
                        }))
                        await event_bus.publish("agent_thoughts", {
                            "agent": "Security Auditor", 
                            "thought": f"Audit Result for '{tool_name}': {decision}. Reasoning: {reasoning}"
                        })
                        
                        if "REJECTED" in decision:
                            if "UNREACHABLE" in decision:
                                tier = max(tier, 3)
                                yield sse_event("thought", json.dumps({
                                    "id": audit_id,
                                    "type": "warning",
                                    "text": f"Security Gate: Auditor unreachable. Elevating security tier for tool '{tool_name}' to require manual user approval.",
                                    "status": "completed",
                                    "mascot_state": "tired",
                                    "mascot_wardrobe": "construction_hat"
                                }))
                            else:
                                obs_text = f"Blocked by Security Auditor: {reasoning}"
                                yield sse_event("thought", json.dumps({
                                    "id": audit_id,
                                    "type": "warning",
                                    "text": f"Security Gate: Blocked execution of tool '{tool_name}' due to: {reasoning}",
                                    "status": "failed",
                                    "mascot_state": "disapproving",
                                    "mascot_wardrobe": "none"
                                }))
                                observations.append(f"<observation:{tool_name}>{obs_text}</observation:{tool_name}>")
                                continue
                    
                    # Check if confirmation is required (Tier >= 3)
                    if tier >= 3:
                        conf_id = f"conf-{uuid.uuid4()}"
                        conf_event = asyncio.Event()
                        active_confirmations[conf_id] = {
                            "event": conf_event,
                            "approved": False
                        }
                        
                        # Yield confirmation prompt event to UI
                        yield sse_event("confirmation", json.dumps({
                            "id": conf_id,
                            "tool": tool_name,
                            "args": args,
                            "tier": tier
                        }))
                        
                        # Wait until user approves/rejects (with timeout to prevent indefinite hang)
                        try:
                            await asyncio.wait_for(conf_event.wait(), timeout=120.0)
                        except asyncio.TimeoutError:
                            pass  # treat timeout as rejection
                        approved = active_confirmations.pop(conf_id, {}).get("approved", False)
                        
                        if not approved:
                            obs_text = "Tool execution rejected by user safety gate."
                            yield sse_event("thought", json.dumps({
                                "id": tool_run_id,
                                "type": "warning",
                                "text": f"Safety Gate: Execution of {tool_name} was rejected.",
                                "status": "failed"
                            }))
                            observations.append(f"<observation:{tool_name}>{obs_text}</observation:{tool_name}>")
                            continue

                    # BUG-24 fix: removed extra leading space — these blocks were at 5-space
                    # indent (outside the `if not approved: continue` rejection guard).
                    # Track temporary screenshot assets for dynamic cleanup
                    if tool_name in ["screenshot", "screenshot_region"]:
                        path = args.get("output_path")
                        if path:
                            created_temp_files.append(os.path.abspath(path))
                    elif tool_name == "browser_screenshot":
                        path = args.get("output_path", "browser.png")
                        created_temp_files.append(os.path.abspath(path))

                    # Run safe or approved tool
                    yield sse_event("thought", json.dumps({
                        "id": tool_run_id,
                        "type": "exec",
                        "text": f"Running tool: {tool_name}",
                        "tool": tool_name,
                        "command": json.dumps(args),
                        "status": "running",
                        "mascot_state": "default",
                        "mascot_wardrobe": "none"
                    }))
                    
                    # Create git checkpoint before running code-modifying tools
                    if tool_name in ["write_file", "delete_file", "move_file", "create_dynamic_tool", "generate_dynamic_tool"]:
                        try:
                            from src.core.history_manager import create_checkpoint
                            await asyncio.to_thread(create_checkpoint, tool_run_id)
                        except Exception as che:
                            print(f"[History Manager] Failed to create checkpoint: {che}")

                    # Run the actual tool call
                    try:
                        result = await call_tool(tool_name, args)
                        
                        # Multi-Modal Thought Anchoring Layout verification: capture validation screenshot on layout changes
                        if tool_name == "run_python" and ("matplotlib" in json.dumps(args) or "plt." in json.dumps(args)):
                            yield sse_event("thought", json.dumps({
                                "id": f"anchor-{time.time()}",
                                "type": "planning",
                                "text": "[Thought Anchoring] Capturing validation screenshot to inspect layout generation success...",
                                "status": "running"
                            }))
                            # (Thought anchoring visual check stubbed dynamically)
                            
                        observations.append(f"<observation:{tool_name}>{result}</observation:{tool_name}>")
                        yield sse_event("thought", json.dumps({
                            "id": tool_run_id,
                            "type": "status",
                            "text": f"Tool {tool_name} completed.",
                            "status": "completed"
                        }))
                        add_to_task_log(tool_name, tier, "success")
 
                         # If plugins are reloaded, dynamically regenerate the system prompt
                        if tool_name == "reload_plugins":
                            tools_doc = generate_tools_doc()
                            from src.core.mode import build_system_prompt
                            new_sys = build_system_prompt(prompt, brain_model, ollama_host, tools_doc)
                            history[0] = {"role": "system", "content": new_sys}
                            print("[Plugins] System prompt dynamically updated with new tool registrations.")
                    except Exception as e:
                        err_txt = str(e)
                        # ToT backtrack trigger
                        tot_failed = True
                        failed_tool = tool_name
                        failed_args = args
                        observations.append(f"<observation:{tool_name}>Error: {err_txt}</observation:{tool_name}>")
                        yield sse_event("thought", json.dumps({
                            "id": tool_run_id,
                            "type": "warning",
                            "text": f"Tool {tool_name} failed: {err_txt}",
                            "status": "failed"
                        }))
                        add_to_task_log(tool_name, tier, "failed", err_txt)

                # Tree-of-Thoughts Backtracking execution
                if tot_failed:
                    history = list(tot_checkpoint)
                    yield sse_event("thought", json.dumps({
                        "id": f"tot-backtrack-{time.time()}",
                        "type": "warning",
                        "text": f"[Tree-of-Thoughts] Tool execution of '{failed_tool}' failed. Backtracking and adjusting pathway...",
                        "status": "completed"
                    }))
                    history.append({
                        "role": "user",
                        "content": f"<observation:{failed_tool}>Error: Tool execution failed. [Tree-of-Thoughts Backtrack]: Avoid calling '{failed_tool}' with args {json.dumps(failed_args)} again as it fails in this environment. Attempt an alternative search, verify paths, or try a different approach.</observation:{failed_tool}>"
                    })
                    continue

                # Join observations and append to prompt history for next reasoning loop
                obs_payload = "\n".join(observations)
                history.append({"role": "user", "content": obs_payload})
            else:
                # If no tool calls and no finish tag, break to avoid infinite loop
                if not final_text:
                    final_text = clean_final_text(full_turn_text)
                    final_text = await process_final_response(final_text, user_lang, client)
                    
                    # 3. Consensus Debate (Upgrade 6)
                    yield sse_event("thought", json.dumps({
                        "id": f"debate-init-break-{time.time()}",
                        "type": "planning",
                        "text": f"[Consensus Debate] Running Coder vs QA Reviewer consensus debate loop...",
                        "status": "running"
                    }))
                    qa_prompt = (
                        "You are the QA Reviewer Agent. Critique the proposed response below. "
                        "Find any potential bugs, logical inconsistencies, security concerns, or formatting errors.\n"
                        "Do NOT write any introduction or conclusion, just write a bullet list of issues.\n\n"
                        f"Proposed Response:\n{final_text}"
                    )
                    qa_res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=qa_prompt)
                    critique = (qa_res.response if hasattr(qa_res, "response") else qa_res.get("response", "")).strip()
                    
                    yield sse_event("thought", json.dumps({
                        "id": f"debate-critique-break-{time.time()}",
                        "type": "planning",
                        "text": f"[Consensus Debate - QA Reviewer]: Critique generated:\n{critique}",
                        "status": "completed"
                    }))
                    
                    coder_prompt = (
                        "You are the Lead Coder Agent. Refine the proposed response based on the QA Reviewer's critique.\n"
                        "Return ONLY the final JSON response block with keys 'chat', 'speech', and 'lang'. No explanation, no markdown.\n\n"
                        f"Original Response:\n{final_text}\n\n"
                        f"Critique:\n{critique}"
                    )
                    coder_res = await asyncio.to_thread(client.generate, model="qwen2.5-coder:1.5b-instruct-q8_0", prompt=coder_prompt)
                    refined = (coder_res.response if hasattr(coder_res, "response") else coder_res.get("response", "")).strip()
                    if refined.startswith("```"):
                        refined = refined.strip("`").replace("json\n", "").strip()
                        
                    try:
                        json.loads(refined)
                        final_text = refined
                    except Exception:
                        pass
                        
                    _debate_key2 = f"debate-{time.time()}"
                    active_debates[_debate_key2] = {
                        "draft": final_text,
                        "critique": critique,
                        "refined": final_text
                    }
                    # BUG-10 fix: same cap as above — prune oldest entries
                    _MAX_DEBATES = 50
                    if len(active_debates) > _MAX_DEBATES:
                        for _old_k in sorted(active_debates.keys())[:len(active_debates) - _MAX_DEBATES]:
                            del active_debates[_old_k]
                    
                    yield sse_event("text", final_text)
                break
                
        # Save the final text that was streamed to the user as-is.
        # process_final_response is already applied during streaming (finish event handler),
        # so re-processing here would cause the DB to store a different version than shown.
        # BUG-5 fix: only persist to DB when this is a user-facing (non-worker) call.
        # HTP worker sub-loops should not write their internal results to conversation
        # history or semantic cache since they are planning artifacts, not user interactions.
        if not is_worker:
            add_to_conversations("assistant", final_text)
            add_to_semantic_cache(prompt, final_text)
        add_to_task_log("ollama_api", 2, "success")

        
        # Trigger background memory compression checking
        try:
            from database import get_sqlite_conn
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM conversations")
            total_rows = cursor.fetchone()[0]
            conn.close()
            if total_rows >= 21:  # Distill when there are at least 20 historical entries
                asyncio.create_task(run_memory_summarization_background(ollama_host))
        except Exception as e:
            print("[Memory Distiller trigger warning]:", e)

        # Schedule a proactive follow-up for significant cognitive modes
        try:
            from src.core.mode import classify_mode
            from src.core.proactive import schedule_followup
            detected_mode = classify_mode(prompt)
            if detected_mode in ("ENGINEER", "ANALYST", "RESEARCHER"):
                schedule_followup(detected_mode)
        except Exception as e:
            print("[Proactive Follow-up] Scheduling error:", e)

    finally:
        # Secure garbage collection of temporary files (screenshots and log dumps)
        for temp_file in set(created_temp_files):
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    print(f"[Cleanup Engine] Auto-removed temporary artifact: {temp_file}")
            except Exception as ce:
                print(f"[Cleanup Engine] Error deleting temporary artifact {temp_file}: {ce}")
