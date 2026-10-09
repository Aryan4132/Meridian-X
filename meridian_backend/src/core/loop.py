import os
import json
import asyncio
import time
import threading
from typing import Dict, Any, List, AsyncGenerator, Tuple, Optional

from src.tools.registry import call_tool, TOOL_REGISTRY
from database import (
    add_to_task_log,
    add_to_conversations,
    get_conversation_history,
    check_semantic_cache,
    add_to_semantic_cache,
    get_auditor_model,
    get_user_profile,
    get_ollama_client,
)
from src.core.bus import event_bus
from src.core.speculative import preheat_tool
from src.core.confirmations import (
    active_confirmations,
    get_confirmations_lock,
    register_confirmation,
    approve_confirmation,
    pop_confirmation,
    check_approval_gate,
)

from src.core.llm_clients import (
    get_cached_ollama_client,
    get_gpu_vram_usage,
)

from src.core.loop_planning import (
    detect_complex_prompt,
    run_self_question_check,
    route_model_by_complexity,
    run_memory_summarization_background,
    run_htp_pipeline,
    enrich_system_prompt,
)

from src.core.loop_executor import (
    clean_final_text,
    prune_and_compress_history,
    check_llm_tool_output_anomaly,
    execute_single_tool_async,
)

from src.core.loop_parser import (
    StreamingXMLParser,
    resolve_local_model_name,
)

from src.core.loop_dispatcher import (
    process_tool_turn,
    EXEMPT_TOOLS,
)

from src.core.loop_stream import (
    generate_tools_doc,
    create_model_response_stream,
    async_iter_stream,
    extract_chunk_content,
)

from src.core.consensus_engine import (
    handle_turn_finish,
)

# Active tree and debate state tables
active_trees: Dict[str, Dict[str, Any]] = {}
active_debates: Dict[str, Dict[str, Any]] = {}
_temporal_graphs: Dict[str, Any] = {}

_interrupt_event = threading.Event()
_session_interrupts: Dict[str, threading.Event] = {}
_session_interrupt_lock = threading.Lock()


def get_session_interrupt_event(session_id: str = "default") -> threading.Event:
    """Returns or creates the session-scoped interruption event."""
    with _session_interrupt_lock:
        if session_id not in _session_interrupts:
            _session_interrupts[session_id] = threading.Event()
        return _session_interrupts[session_id]


def interrupt_agent_loop(session_id: Optional[str] = None):
    """Signal active agent loop(s) to stop at the next safe checkpoint."""
    _interrupt_event.set()
    with _session_interrupt_lock:
        if session_id:
            if session_id in _session_interrupts:
                _session_interrupts[session_id].set()
        else:
            for ev in _session_interrupts.values():
                ev.set()


async def run_react_agent_loop(
    prompt: str,
    brain_model: str,
    ollama_host: str,
    model_source: str = "local",
    api_provider: str = "gemini",
    is_worker: bool = False,
    session_id: str = "default",
) -> AsyncGenerator[str, None]:
    """Autonomous ReAct agent loop with HTP, speculative preheating, and consensus validation."""
    # Sanitize input prompt for prompt injection & jailbreaks (SEC-08)
    from src.core.prompt_injection import sanitize_prompt
    prompt, injection_detected, injection_cats = sanitize_prompt(prompt)

    # Helper to format SSE events
    def sse_event(event_type: str, data_payload: str) -> str:
        lines = data_payload.split('\n')
        data_lines = [f"data: {line}" for line in lines]
        return f"event: {event_type}\n" + "\n".join(data_lines) + "\n\n"

    # Check semantic cache first
    cached = check_semantic_cache(prompt)
    if cached:
        yield sse_event("thought", json.dumps({"type": "planning", "text": "Semantic Cache Match: returns instantly (<5ms) from Turbovec", "tool": "semantic_cache"}))
        yield sse_event("text", cached)
        if not is_worker:
            add_to_conversations("user", prompt)
            add_to_conversations("assistant", cached)
        add_to_task_log("semantic_cache", 0, "success")
        return

    _near_miss_ctx = None
    try:
        from database import get_near_miss_semantic_cache
        _near_miss_ctx = get_near_miss_semantic_cache(prompt, min_score=0.60, max_score=0.85)
    except Exception:
        pass

    if _near_miss_ctx:
        yield sse_event("thought", json.dumps({
            "type": "planning",
            "text": "[Semantic Cache] Near-miss detected. Injecting prior context as starting point...",
            "tool": "semantic_cache"
        }))

    past_messages = get_conversation_history(limit=10)
    if not is_worker:
        add_to_conversations("user", prompt)
    add_to_task_log("ollama_api", 2, "started")

    try:
        from database import get_ollama_client_host as _get_host
        _ollama_host = _get_host()
    except Exception:
        _ollama_host = ollama_host
    client = get_cached_ollama_client(_ollama_host)

    resolved_auditor_model = get_auditor_model()
    if model_source == "local":
        brain_model = resolve_local_model_name(brain_model, client)
    try:
        resolved_auditor_model = resolve_local_model_name(resolved_auditor_model, client)
    except Exception:
        pass

    # 1. Hierarchical Task Planning (HTP) (Upgrade 10) — Skip for cloud models to achieve minimum TTFT
    if not is_worker and model_source not in ("cloud", "api") and detect_complex_prompt(prompt):
        async for sse_chunk in run_htp_pipeline(
            prompt=prompt,
            client=client,
            brain_model=brain_model,
            ollama_host=ollama_host,
            model_source=model_source,
            api_provider=api_provider,
            run_loop_fn=run_react_agent_loop,
            sse_event_fn=sse_event,
        ):
            yield sse_chunk
        return

    from src.core.mode import build_system_prompt, detect_user_language, classify_mode
    detected_mode = classify_mode(prompt)
    tools_doc = generate_tools_doc(mode=detected_mode, prompt=prompt)

    # Load workspace config overrides
    if model_source == "local":
        from src.core.mode import load_workspace_config
        config = load_workspace_config()
        workspace_model = config.get("brain_model")
        if workspace_model:
            print(f"[Workspace Config] Overriding brain model from '{brain_model}' to '{workspace_model}'")
            brain_model = resolve_local_model_name(workspace_model, client)

    user_lang = detect_user_language(prompt)
    system_prompt = build_system_prompt(prompt, brain_model, ollama_host, tools_doc)
    system_prompt = enrich_system_prompt(system_prompt, prompt, session_id, _near_miss_ctx, _temporal_graphs)

    history = [{"role": "system", "content": system_prompt}]
    for msg in past_messages:
        history.append({"role": msg["role"], "content": msg["content"]})
    history.append({"role": "user", "content": prompt})

    try:
        from database import get_autonomous_mode
        max_turns = 25 if get_autonomous_mode() else 1
    except Exception:
        max_turns = 20

    turn = 0
    final_text = ""
    active_model = route_model_by_complexity(prompt, brain_model, model_source)

    last_tool_call = None
    consecutive_repeat_count = 0
    tool_retry_counts = {}
    created_temp_files = []
    session_ev = get_session_interrupt_event(session_id)
    session_ev.clear()
    _interrupt_event.clear()
    executed_tools_all_turns: List[str] = []

    try:
        while turn < max_turns:
            final_text = ""
            if _interrupt_event.is_set() or session_ev.is_set():
                _interrupt_event.clear()
                session_ev.clear()
                yield sse_event("thought", json.dumps({"type": "planning", "text": "Voice barge-in detected. Interrupting execution.", "status": "completed"}))
                return
            turn += 1

            # Token budget estimation (char heuristic, warn at 80% of user-configured context limit)
            total_chars = sum(len(m["content"]) for m in history)
            estimated_tokens = int(total_chars / 4)

            raw_user_limit = get_user_profile("context_token_limit")
            try:
                user_context_limit = int(raw_user_limit) if raw_user_limit else 8192
            except Exception:
                user_context_limit = 8192

            warn_limit = int(user_context_limit * 0.8)
            if estimated_tokens > warn_limit:
                pct = (estimated_tokens / user_context_limit) * 100
                yield sse_event("thought", json.dumps({
                    "id": f"token-budget-{turn}-{time.time()}",
                    "type": "warning",
                    "text": f"⚠️ Context window budget warning: Estimated token count ({estimated_tokens}) is at {pct:.1f}% of context limit ({user_context_limit:,} tokens). Compressing history.",
                    "status": "completed"
                }))
                history = await prune_and_compress_history(history, client, model_source=model_source)
            elif model_source == "local" and len(history) > 9:
                history = await prune_and_compress_history(history, client, model_source=model_source)

            # Self-Questioning Check
            if any(k in prompt.lower() for k in ["file", "path", "directory", "folder", "config", "refactor", "codebase"]):
                is_verified, warning_msg = await run_self_question_check(prompt, history, client, model=resolved_auditor_model)
            else:
                is_verified, warning_msg = True, ""

            temp_sys_idx = -1
            if not is_verified:
                yield sse_event("thought", json.dumps({
                    "id": f"self-question-{turn}-{time.time()}",
                    "type": "warning",
                    "text": "[Self-Questioning] Lack verified information for target path/dependencies. Injecting exploratory search gate...",
                    "status": "completed"
                }))
                history.append({"role": "user", "content": f"[SYSTEM — Self-Questioning Gate Warning]: {warning_msg}"})
                temp_sys_idx = len(history) - 1

            # Dynamic VRAM/RAM Offloading Scheduler
            vram_load = get_gpu_vram_usage()
            if model_source == "local" and vram_load > 85.0 and "cloud" not in active_model.lower():
                fallback_brain = get_auditor_model()
                if active_model != fallback_brain:
                    yield sse_event("thought", json.dumps({
                        "id": f"vram-warning-{turn}-{time.time()}",
                        "type": "warning",
                        "text": f"High memory load detected ({vram_load:.1f}%). Dynamic VRAM allocation: swapping brain model from '{active_model}' to fallback model '{fallback_brain}' to prevent system crash.",
                        "status": "running"
                    }))
                    active_model = fallback_brain
                    if len(history) > 6:
                        history = [history[0]] + history[-4:]

            # Start response stream
            try:
                response_stream = create_model_response_stream(
                    client=client,
                    active_model=active_model,
                    history=history,
                    model_source=model_source,
                    api_provider=api_provider,
                    brain_model=brain_model,
                    ollama_host=ollama_host,
                )
            except Exception as e:
                if model_source == "local" and active_model != get_auditor_model():
                    fallback_brain = get_auditor_model()
                    print(f"[Fallback Engine] Switching to local model '{fallback_brain}' due to: {e}")
                    yield sse_event("thought", json.dumps({
                        "id": f"api-fallback-{turn}-{time.time()}",
                        "type": "warning",
                        "text": f"API execution failed: {str(e)}. Swapping to local fallback model '{fallback_brain}'.",
                        "status": "running"
                    }))
                    active_model = fallback_brain
                    model_source = "local"
                    if len(history) > 6:
                        history = [history[0]] + history[-4:]
                    try:
                        response_stream = create_model_response_stream(
                            client=client,
                            active_model=active_model,
                            history=history,
                            model_source="local",
                            api_provider="ollama",
                        )
                    except Exception as ex:
                        err_msg = f"Fallback model '{active_model}' execution failed: {str(ex)}"
                        yield sse_event("thought", json.dumps({"id": f"fallback-failure-{turn}-{time.time()}", "type": "warning", "text": err_msg, "status": "failed"}))
                        add_to_task_log("ollama_api", 2, "failed", err_msg)
                        return
                else:
                    err_msg = f"API execution failed: {str(e)}"
                    print(f"[Engine Error] Cloud API call failed: {e}")
                    yield sse_event("thought", json.dumps({"id": f"api-failure-{turn}-{time.time()}", "type": "warning", "text": err_msg, "status": "completed"}))
                    yield sse_event("text", f"\nError: {err_msg}\n")
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

            async for chunk in async_iter_stream(response_stream):
                if isinstance(chunk, dict) and "error" in chunk:
                    err_msg = f"Stream execution failed: {chunk['error']}"
                    print(f"[Engine Error] {err_msg}")
                    yield sse_event("thought", json.dumps({"id": f"stream-error-{turn}-{time.time()}", "type": "warning", "text": err_msg, "status": "failed"}))
                    yield sse_event("text", f"\nError: {err_msg}\n")
                    add_to_task_log("ollama_api", 2, "failed", err_msg)
                    return

                if _interrupt_event.is_set():
                    if temp_sys_idx != -1 and temp_sys_idx < len(history):
                        history.pop(temp_sys_idx)
                        temp_sys_idx = -1
                    yield sse_event("thought", json.dumps({"type": "planning", "text": "Voice barge-in detected. Interrupting execution.", "status": "completed"}))
                    return

                content = extract_chunk_content(chunk, model_source=model_source, api_provider=api_provider)
                if not content:
                    continue

                full_turn_text += content
                parsed_events = parser.feed(content)

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
                        if not event["text"].strip():
                            continue
                        async for etype, epayload in handle_turn_finish(
                            finish_text=event["text"],
                            prompt=prompt,
                            active_model=active_model,
                            user_lang=user_lang,
                            client=client,
                            executed_tools=executed_tools_all_turns,
                            history=history,
                            active_debates=active_debates,
                        ):
                            if etype == "text":
                                final_text = epayload
                            yield sse_event(etype, epayload)
                    elif event["type"] == "call":
                        executed_tools_all_turns.append(event["name"])
                        calls_to_execute.append((event["name"], event["args"]))

            if temp_sys_idx != -1 and temp_sys_idx < len(history):
                history.pop(temp_sys_idx)
                temp_sys_idx = -1

            if calls_to_execute:
                turn_state = {
                    "last_tool_call": last_tool_call,
                    "consecutive_repeat_count": consecutive_repeat_count,
                    "interrupted": False,
                    "reloaded_plugins": False,
                }
                async for sse_chunk in process_tool_turn(
                    calls_to_execute=calls_to_execute,
                    history=history,
                    client=client,
                    active_model=active_model,
                    model_source=model_source,
                    session_id=session_id,
                    tool_retry_counts=tool_retry_counts,
                    created_temp_files=created_temp_files,
                    state=turn_state,
                    interrupt_event=session_ev,
                    exempt_tools=EXEMPT_TOOLS,
                    prompt=prompt,
                    brain_model=brain_model,
                    ollama_host=ollama_host,
                ):
                    yield sse_chunk

                last_tool_call = turn_state.get("last_tool_call")
                consecutive_repeat_count = turn_state.get("consecutive_repeat_count", 0)

                if turn_state.get("interrupted"):
                    return

                if turn_state.get("reloaded_plugins"):
                    tools_doc = generate_tools_doc(mode=detected_mode, prompt=prompt)
                    from src.core.mode import build_system_prompt
                    new_sys = build_system_prompt(prompt, brain_model, ollama_host, tools_doc)
                    history[0] = {"role": "system", "content": new_sys}
                    print("[Plugins] System prompt dynamically updated with new tool registrations.")
            else:
                if not final_text:
                    raw_cleaned = clean_final_text(full_turn_text)
                    async for etype, epayload in handle_turn_finish(
                        finish_text=raw_cleaned,
                        prompt=prompt,
                        active_model=active_model,
                        user_lang=user_lang,
                        client=client,
                        executed_tools=executed_tools_all_turns,
                        history=history,
                        active_debates=active_debates,
                    ):
                        if etype == "text":
                            final_text = epayload
                        yield sse_event(etype, epayload)
                break

        if not is_worker and final_text.strip():
            add_to_conversations("assistant", final_text)
            add_to_semantic_cache(prompt, final_text)
        add_to_task_log("ollama_api", 2, "success")

        try:
            from database import get_sqlite_conn
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM conversations")
            total_rows = cursor.fetchone()[0]
            conn.close()
            if total_rows >= 10:
                asyncio.create_task(run_memory_summarization_background(ollama_host))
        except Exception as e:
            print("[Memory Distiller trigger warning]:", e)

        try:
            from src.core.mode import classify_mode
            from src.core.proactive import schedule_followup
            detected_mode = classify_mode(prompt)
            if detected_mode in ("ENGINEER", "ANALYST", "RESEARCHER"):
                schedule_followup(detected_mode)
        except Exception as e:
            print("[Proactive Follow-up] Scheduling error:", e)

    finally:
        for temp_file in set(created_temp_files):
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    print(f"[Cleanup Engine] Auto-removed temporary artifact: {temp_file}")
            except Exception as ce:
                print(f"[Cleanup Engine] Error deleting temporary artifact {temp_file}: {ce}")
