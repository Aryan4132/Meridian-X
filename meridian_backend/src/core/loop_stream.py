"""
loop_stream.py — SSE Event Stream & Token Budget Sub-module
Formats Server-Sent Events (SSE), handles mid-stream cancellation signals,
and tracks token budget heuristics for context window management.
"""

import json
import asyncio
import time
import inspect
from typing import Dict, Any, Optional, List, AsyncGenerator

# Global mid-stream cancellation flags: {session_id: (timestamp, cancel_requested_bool)}
_cancel_signals: Dict[str, tuple[float, bool]] = {}
_SIGNAL_TTL_SECONDS: float = 3600.0


def _prune_expired_signals(now: Optional[float] = None) -> None:
    """Removes stale cancellation entries older than TTL to avoid memory leaks."""
    current_time = now if now is not None else time.time()
    expired = [
        sid for sid, (ts, _) in _cancel_signals.items()
        if (current_time - ts) > _SIGNAL_TTL_SECONDS
    ]
    for sid in expired:
        _cancel_signals.pop(sid, None)


def request_stream_cancellation(session_id: str) -> None:
    """Sets mid-stream cancel flag for the active session."""
    _prune_expired_signals()
    _cancel_signals[session_id] = (time.time(), True)


def is_cancellation_requested(session_id: str) -> bool:
    """Checks if user requested stream cancellation."""
    _prune_expired_signals()
    entry = _cancel_signals.get(session_id)
    return entry[1] if entry is not None else False


def clear_cancellation_signal(session_id: str) -> None:
    """Clears cancel flag on session startup or completion."""
    _cancel_signals.pop(session_id, None)
    _prune_expired_signals()

def reset_cancel_flag(session_id: str = "default") -> None:
    """Clears cancel flag on session startup or completion."""
    clear_cancellation_signal(session_id)


TOOL_SIGNATURES: Dict[str, str] = {
    "browser_use_task": 'browser_use_task(task="<goal_or_instruction>", start_url="<optional_url>", visible=True)',
    "browser_open": 'browser_open(url="<url>", visible=True)',
    "browser_navigate": 'browser_navigate(url="<url>")',
    "browser_click_element": 'browser_click_element(index_or_selector="<1 or selector>")',
    "browser_type_element": 'browser_type_element(index_or_selector="<1 or selector>", text="<text>", press_enter=True)',
    "browser_press_key": 'browser_press_key(key="<Enter|Escape|Tab|ArrowDown>")',
    "browser_scroll": 'browser_scroll(direction="down", amount=500)',
    "browser_wait": 'browser_wait(seconds=2)',
    "browser_get_text": 'browser_get_text()',
    "browser_screenshot": 'browser_screenshot()',
    "browser_close": 'browser_close()',
    "read_file": 'read_file(path="<path>")',
    "write_file": 'write_file(path="<path>", content="<content>")',
    "list_directory": 'list_directory(path="<path>")',
    "universal_search": 'universal_search(query="<query>", domain_filter="all|code|docs|memory|files")',
    "search_web": 'search_web(query="<query>")',
    "shell": 'shell(command="<command>")',
    "terminal": 'terminal(command="<command>")',
    "run_command": 'run_command(command="<command>")',
    "nl_run": 'nl_run(command="<command_or_instruction>")',
}

CORE_TOOLS_LIST = [
    # Filesystem (5)
    "read_file", "write_file", "list_directory", "search_files", "delete_file",
    # Shell (3)
    "shell", "nl_run", "run_python",
    # Developer (7)
    "git_status", "git_commit", "git_diff", "search_codebase", "run_tests", "lint_file", "review_file",
    # Browser (4)
    "browser_use_task", "browser_open", "browser_close", "browser_get_text",
    # Desktop (7)
    "screenshot", "ocr_screen", "vision_analyze", "list_windows", "focus_window", "open_app", "open_file",
    # System & Tasks (9)
    "get_system_info", "get_hardware_info", "list_processes", "kill_process", "clipboard_get", "clipboard_set", "schedule_task", "schedule_once", "list_scheduled",
    # Memory & Knowledge (4)
    "universal_search", "kg_query", "kg_search", "kg_add_fact",
    # Communications (4)
    "send_notification", "send_email", "read_emails", "send_whatsapp_message",
    # Documents (3)
    "read_document_text", "create_word_document", "create_pdf_document",
    # Vault & Dynamic (3)
    "vault_get", "vault_set", "generate_dynamic_tool",
    # Voice (2)
    "voice_record_and_transcribe", "voice_speak"
]

MODE_SPECIALIZED_TOOLS = {
    "ENGINEER": ["git_create_snapshot", "git_rollback", "lsp_get_definition", "lsp_get_references", "lsp_get_hover_info", "lsp_diagnose_file", "format_file", "scaffold_project"],
    "REVIEWER": ["review_diff", "review_directory", "export_review", "run_security_audit"],
    "OPERATOR": ["gui_click", "gui_type", "browser_click_element", "browser_type_element", "browser_press_key", "browser_scroll", "browser_wait", "browser_screenshot"],
    "ANALYST": ["db_query", "db_schema", "watch_log", "tail_log", "get_network_connections", "get_wifi_networks", "get_disk_info"],
    "RESEARCHER": ["search_web", "search_news", "fetch_page", "scrape_table", "autonomous_research"],
}

KEYWORD_SKILLS_MAP = {
    ("bill", "invoice", "due"): ["register_recurring_bill", "get_bill_due_radar"],
    ("expiry", "passport", "visa"): ["add_expiry_document", "check_document_expiries", "list_expiry_documents"],
    ("flight", "trip", "travel", "leave"): ["create_trip", "calculate_leave_by_time", "get_upcoming_trips"],
    ("stock", "portfolio", "networth", "crypto", "price"): ["analyze_stock_sentiment", "get_market_watchlist", "get_networth_summary", "add_watched_product"],
    ("grocery", "chore", "download", "bookmark", "reading"): ["add_grocery_item", "add_household_chore", "get_household_summary", "scan_downloads_folder", "organize_downloads", "add_bookmark", "add_to_learning_queue"],
    ("health", "step", "sleep", "heart", "hydration"): ["sync_wearable_health_data", "get_health_metrics_summary", "track_hydration", "trigger_ergonomic_break", "calculate_daily_wellness_score"],
    ("weather", "location", "geo"): ["resolve_location", "get_localized_weather", "bias_query_spatially"],
    ("phishing", "password", "totp", "wifi", "dns", "usb", "sandbox", "audit"): ["check_url_reputation", "generate_totp_code", "audit_password_strength", "assess_wifi_security", "audit_dns_health", "audit_usb_peripherals", "detonate_attachment_sample"],
}

def get_dynamic_tool_signature(name: str, func: Any) -> str:
    """Extract readable callable signature dynamically using inspect."""
    if not func or not callable(func):
        return name
    try:
        sig = inspect.signature(func)
        params = []
        for p in sig.parameters.values():
            if p.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY):
                if p.default == inspect.Parameter.empty:
                    params.append(f'{p.name}="<{p.name}>"')
                else:
                    params.append(f'{p.name}={repr(p.default)}')
        return f"{name}({', '.join(params)})"
    except Exception:
        return name


def generate_tools_doc(mode: Optional[str] = None, prompt: Optional[str] = None) -> str:
    """Returns formatted string documentation presenting <70 core and mode-specialized tools."""
    from src.tools.registry import TOOL_REGISTRY

    selected_tools = set(CORE_TOOLS_LIST)

    # 1. Mode-based skill injection
    if mode and mode.upper() in MODE_SPECIALIZED_TOOLS:
        for t in MODE_SPECIALIZED_TOOLS[mode.upper()]:
            selected_tools.add(t)

    # 2. Keyword-based lazy skill injection
    if prompt:
        p_lower = prompt.lower()
        for kws, tools in KEYWORD_SKILLS_MAP.items():
            if any(kw in p_lower for kw in kws):
                for t in tools:
                    selected_tools.add(t)

    # 3. Data-driven skill packs (plugins/skills/*/SKILL.md + tools.yaml).
    #    Additive only; any loader failure keeps the hardcoded maps above.
    try:
        from src.core.skills_loader import load_skill_packs, match_skills_for_prompt
        for t in match_skills_for_prompt(prompt or "", load_skill_packs()):
            selected_tools.add(t)
    except Exception:
        pass

    lines = []
    for name in selected_tools:
        info = TOOL_REGISTRY.get(name)
        if not info:
            continue
        desc = info.get("description", "")
        sig = TOOL_SIGNATURES.get(name)
        if not sig:
            sig = get_dynamic_tool_signature(name, info.get("func"))
        if desc:
            lines.append(f"- {sig}: Tier {info['tier']} — {desc}")
        else:
            lines.append(f"- {sig}: Tier {info['tier']}")
    return "\n".join(lines)

def format_sse_event(event_type: str, data: Any) -> str:
    """Formats payload as standard Server-Sent Event string."""
    payload = json.dumps({"event": event_type, "data": data}, ensure_ascii=False)
    return f"data: {payload}\n\n"



def format_thought_event(thought_text: str, session_id: str = "default", step_index: int = 0, tool_name: str = "") -> str:
    """BK-08: Formats SSE event for thought introspection and persists to database."""
    try:
        from database import add_thought_log
        add_thought_log(thought_text, session_id=session_id, step_index=step_index, tool_name=tool_name)
    except Exception as e:
        print("[Loop Stream] Failed to persist thought log:", e)
    return format_sse_event("thought", {"text": thought_text, "session_id": session_id, "step": step_index, "tool": tool_name})




import re

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
    cjk_count = len(_CJK_RE.findall(text))
    if cjk_count > length * 0.10:
        return max(1, int(length / 1.2))
    if _CODE_RE.search(text):
        return max(1, int(length / 3.0))
    return max(1, int(length / 4.0))




def trim_history_to_token_budget(messages: list, max_tokens: int = 8000) -> list:
    """
    Trims conversation message history from the top (preserving system prompt)
    if estimated total tokens exceeds max_tokens budget.
    """
    if not messages:
        return messages

    system_msg = messages[0] if messages[0].get("role") == "system" else None
    working = messages[1:] if system_msg else list(messages)

    current_tokens = sum(estimate_token_count(m.get("content", "")) for m in messages)
    while current_tokens > max_tokens and len(working) > 2:
        # Drop oldest user/assistant pair
        working.pop(0)
        current_tokens = (estimate_token_count(system_msg.get("content", "")) if system_msg else 0) + sum(estimate_token_count(m.get("content", "")) for m in working)

    return ([system_msg] + working) if system_msg else working


def create_model_response_stream(
    client: Any,
    active_model: str,
    history: List[Dict[str, Any]],
    model_source: str,
    api_provider: str,
    brain_model: str = "",
    ollama_host: str = "",
) -> Any:
    """Configures and starts the streaming response for local or cloud LLM providers."""
    # OPS-04: Local-Only Air-Gap Mode Check
    try:
        from src.core.mode import get_local_only_mode
        if get_local_only_mode():
            if (api_provider or "").lower() != "ollama" or model_source in ("cloud", "api"):
                raise PermissionError("Error: Local-Only Air-Gap Mode is active. Outbound cloud API requests are hard-blocked.")

            model_lower = (active_model or brain_model or "").lower()
            if ":cloud" in model_lower or "cloud" in model_lower:
                raise PermissionError(f"Error: Local-Only Air-Gap Mode is active. Cloud Ollama model '{active_model}' is hard-blocked.")

            host_lower = (ollama_host or "").lower()
            local_loopbacks = ["localhost", "127.0.0.1", "0.0.0.0", "::1"]
            if not any(lh in host_lower for lh in local_loopbacks):
                raise PermissionError(f"Error: Local-Only Air-Gap Mode is active. Remote Ollama host '{ollama_host}' is hard-blocked.")
    except PermissionError:
        raise
    except Exception:
        pass

    if model_source == "local" or (api_provider or "").lower() == "ollama":
        return client.chat(
            model=active_model,
            messages=history,
            stream=True,
            options={
                "temperature": 0.7,
                "repeat_penalty": 1.15,
                "top_p": 0.9
            }
        )

    from src.core.llm_provider import get_api_key
    from src.core.llm_clients import get_cached_openai_client, get_cached_anthropic_client

    if api_provider == "gemini":
        gemini_key = get_api_key("gemini")
        if not gemini_key:
            raise ValueError("GEMINI_API_KEY is not configured in environment or database profile.")
        openai_client = get_cached_openai_client(
            api_key=gemini_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        return openai_client.chat.completions.create(
            model=active_model,
            messages=history,
            stream=True
        )
    elif api_provider == "openai":
        openai_key = get_api_key("openai")
        if not openai_key:
            raise ValueError("OPENAI_API_KEY is not configured in environment or database profile.")
        openai_client = get_cached_openai_client(api_key=openai_key)
        return openai_client.chat.completions.create(
            model=active_model,
            messages=history,
            stream=True
        )
    elif api_provider == "deepseek":
        deepseek_key = get_api_key("deepseek")
        if not deepseek_key:
            raise ValueError("DEEPSEEK_API_KEY is not configured in environment or database profile.")
        openai_client = get_cached_openai_client(
            api_key=deepseek_key,
            base_url="https://api.deepseek.com/v1"
        )
        return openai_client.chat.completions.create(
            model=active_model,
            messages=history,
            stream=True
        )
    elif api_provider in ("anthropic", "claude"):
        anthropic_key = get_api_key("anthropic") or get_api_key("claude")
        if not anthropic_key:
            raise ValueError("ANTHROPIC_API_KEY is not configured in environment or database profile.")
        anthropic_client = get_cached_anthropic_client(api_key=anthropic_key)
        system_msg = ""
        claude_history = []
        for m in history:
            if m.get("role") == "system":
                system_msg = m.get("content", "")
            else:
                role = "assistant" if m.get("role") == "assistant" else "user"
                claude_history.append({"role": role, "content": m.get("content", "")})

        return anthropic_client.messages.create(
            model=active_model,
            system=system_msg,
            messages=claude_history,
            max_tokens=4096,
            stream=True
        )
    elif (api_provider or "").lower() == "ollama":
        return client.chat(
            model=active_model,
            messages=history,
            stream=True
        )
    else:
        raise ValueError(f"Unsupported API Provider: '{api_provider}'")


async def async_iter_stream(stream: Any) -> AsyncGenerator[Any, None]:
    """Wraps synchronous generator streams in a threadsafe async generator queue."""
    queue: asyncio.Queue = asyncio.Queue(maxsize=512)
    loop = asyncio.get_running_loop()
    _END = object()

    def _producer():
        try:
            for item in stream:
                while True:
                    try:
                        loop.call_soon_threadsafe(queue.put_nowait, item)
                        break
                    except asyncio.QueueFull:
                        time.sleep(0.01)
        except Exception as exc:
            try:
                loop.call_soon_threadsafe(queue.put_nowait, {"error": str(exc)})
            except Exception:
                pass
        finally:
            try:
                loop.call_soon_threadsafe(queue.put_nowait, _END)
            except Exception:
                pass

    producer_task = asyncio.create_task(asyncio.to_thread(_producer))
    try:
        while True:
            item = await queue.get()
            if item is _END:
                break
            yield item
    finally:
        if not producer_task.done():
            producer_task.cancel()
            try:
                await producer_task
            except (asyncio.CancelledError, Exception):
                pass


def extract_chunk_content(chunk: Any, model_source: str, api_provider: str) -> str:
    """Extracts raw text delta from varied LLM provider streaming chunk formats."""
    if model_source == "local" or (api_provider or "").lower() == "ollama":
        if hasattr(chunk, "message") and hasattr(chunk.message, "content"):
            return chunk.message.content or ""
        elif isinstance(chunk, dict):
            return chunk.get("message", {}).get("content", "") if isinstance(chunk.get("message"), dict) else ""
        return ""
    if api_provider == "anthropic":
        if getattr(chunk, "type", None) == "content_block_delta" or (isinstance(chunk, dict) and chunk.get("type") == "content_block_delta"):
            delta = getattr(chunk, "delta", None) or (chunk.get("delta") if isinstance(chunk, dict) else None)
            return getattr(delta, "text", "") if delta else (delta.get("text", "") if isinstance(delta, dict) else "")
        return ""
    choices = getattr(chunk, "choices", None) or (chunk.get("choices") if isinstance(chunk, dict) else None)
    if choices and len(choices) > 0:
        first_choice = choices[0]
        delta = getattr(first_choice, "delta", None) or (first_choice.get("delta") if isinstance(first_choice, dict) else None)
        if delta:
            return getattr(delta, "content", "") or (delta.get("content", "") if isinstance(delta, dict) else "")
    return ""

