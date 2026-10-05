"""
loop_dispatcher.py — Tool Execution Dispatcher Sub-module
Manages per-tool retry budgets, batch call tagging, and execution dispatches.
"""

import os
import re
import json
import uuid
import random
import threading
import asyncio
import time
from typing import Dict, Any, List, Tuple, Optional, AsyncGenerator
from src.tools.registry import call_tool, TOOL_REGISTRY
from database import add_to_task_log
from src.core.loop_executor import critique_and_correct_tool_call
from src.core.loop_planning import score_candidate_branch
from src.core.confirmations import check_approval_gate, register_confirmation, pop_confirmation
from src.core.checkpoints import create_tool_checkpoint

# Tools exempt from consecutive loop repetition checks (read-only, diagnostic, visual poll, search)
EXEMPT_TOOLS = {
    "read_file", "list_directory", "search_files", "search_web", "autonomous_research",
    "search_knowledge", "search_offline_docs", "search_codebase", "lsp_get_definition",
    "lsp_get_references", "lsp_get_hover_info", "kg_query", "kg_search", "kg_get_facts",
    "kg_traverse", "vault_get", "vault_list", "tail_log", "search_log", "log_stats",
    "clipboard_search", "read_emails", "browser_get_text", "scrape_table", "db_schema",
    "get_system_info", "get_hardware_info", "get_disk_info", "get_battery_status",
    "get_temperature", "list_processes", "get_process_detail", "list_startup_items",
    "list_installed_apps", "list_services", "get_network_connections", "get_wifi_networks",
    "ping_host", "clipboard_get", "list_log_watchers", "list_watchers", "list_scheduled",
    "win_list_tasks", "clipboard_history", "list_workflows", "list_sessions",
    "export_finetune_data", "finetune_stats", "suggest_cross_project_patterns",
    "screenshot", "screenshot_region", "ocr_screen", "vision_analyze", "find_on_screen",
    "segment_screen", "browser_screenshot", "analyze_recording",
    "lint_file", "lsp_diagnose_file", "run_tests", "review_file", "review_diff",
    "review_directory", "run_security_audit", "shell_history", "nl_to_shell"
}

# Per-tool retry budget tracker: {(session_id, tool_name): attempt_count}
_tool_retry_budgets: Dict[Tuple[str, str], int] = {}
MAX_RETRY_PER_TOOL = 3


def reset_tool_retry_budget(session_id: str, tool_name: Optional[str] = None) -> None:
    """Resets retry counter for a specific tool or an entire session."""
    global _tool_retry_budgets
    if tool_name:
        _tool_retry_budgets.pop((session_id, tool_name), None)
    else:
        keys_to_remove = [k for k in _tool_retry_budgets.keys() if k[0] == session_id]
        for k in keys_to_remove:
            _tool_retry_budgets.pop(k, None)


def check_and_increment_retry(session_id: str, tool_name: str) -> bool:
    """
    Returns True if the tool can be executed within its retry budget.
    Increments the retry counter for the specified tool.
    """
    key = (session_id, tool_name)
    count = _tool_retry_budgets.get(key, 0)
    if count >= MAX_RETRY_PER_TOOL:
        return False
    _tool_retry_budgets[key] = count + 1
    return True


async def dispatch_tool_batch(tool_calls: List[Dict[str, Any]], session_id: str = "default") -> List[Dict[str, Any]]:
    """
    Executes a list of tool calls in parallel or sequence based on Tier rules,
    tagging outputs explicitly with tool name and call index for mismatch prevention.

    #7 FIX: Previously used asyncio.to_thread(call_tool, ...) which is WRONG because
    call_tool is an async function. Wrapping an async fn in to_thread schedules it on a
    thread-pool executor that lacks the event loop — causing coroutine-was-never-awaited
    errors or silently swallowed exceptions. Now uses direct `await call_tool()`.
    """
    results = []
    tasks = []

    for idx, call in enumerate(tool_calls):
        tool_name = str(call.get("name") or "")
        tool_args = call.get("arguments", {})

        if not check_and_increment_retry(session_id, tool_name):
            results.append({
                "index": idx,
                "tool": tool_name,
                "status": "EXCEEDED_RETRY_BUDGET",
                "result": f"Error: Tool '{tool_name}' has exceeded its retry budget of {MAX_RETRY_PER_TOOL} attempts."
            })
            continue

        # #7 FIX: Direct async await — call_tool is already an async function.
        async def _exec(index: int, name: str, args: dict):
            try:
                out = await call_tool(name, args)  # was: await asyncio.to_thread(call_tool, name, args)
                return {"index": index, "tool": name, "status": "SUCCESS", "result": out}
            except Exception as e:
                return {"index": index, "tool": name, "status": "ERROR", "result": f"Error executing {name}: {e}"}

        tasks.append(_exec(idx, tool_name, tool_args))

    if tasks:
        batch_outputs = await asyncio.gather(*tasks)
        results.extend(batch_outputs)

    # Sort results by original call index
    results.sort(key=lambda x: x["index"])
    return results


def _format_sse(event_type: str, data_payload: str) -> str:
    lines = data_payload.split('\n')
    data_lines = [f"data: {line}" for line in lines]
    return f"event: {event_type}\n" + "\n".join(data_lines) + "\n\n"


async def process_tool_turn(
    calls_to_execute: List[Tuple[str, str]],
    history: List[Dict[str, str]],
    client: Any,
    active_model: str,
    model_source: str,
    session_id: str,
    tool_retry_counts: Dict[str, int],
    created_temp_files: List[str],
    state: Dict[str, Any],
    interrupt_event: threading.Event,
    exempt_tools: set,
    prompt: str = "",
    brain_model: str = "",
    ollama_host: str = "",
) -> AsyncGenerator[str, None]:
    """Processes validated tool executions for both concurrent read-only and sequential mutating calls."""
    if interrupt_event.is_set():
        interrupt_event.clear()
        state["interrupted"] = True
        yield _format_sse("thought", json.dumps({"type": "planning", "text": "Task interrupted by user.", "status": "completed"}))
        return

    observations = []
    tot_checkpoint = list(history)
    tot_failed = False
    failed_tool = ""
    failed_args = {}

    concurrent_calls = []
    sequential_calls = []

    last_tool_call = state.get("last_tool_call")
    consecutive_repeat_count = state.get("consecutive_repeat_count", 0)

    for tool_name, args_str in calls_to_execute:
        is_corrected, corrected_args, critique_err = critique_and_correct_tool_call(tool_name, args_str, client, model_source=model_source)
        if not is_corrected and critique_err:
            observations.append(f"<observation:{tool_name}>Error: {critique_err}</observation:{tool_name}>")
            yield _format_sse("thought", json.dumps({
                "id": f"critique-failed-{time.time()}",
                "type": "warning",
                "text": f"[Critique Engine] Tool call '{tool_name}' failed validation: {critique_err}",
                "status": "failed"
            }))
            continue

        if is_corrected:
            if critique_err:
                yield _format_sse("thought", json.dumps({
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

        if tool_name not in exempt_tools:
            try:
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
                err_msg = f"Loop Guardrail & Critic Switcher: Tool '{tool_name}' called {consecutive_repeat_count} times with identical parameters."
                yield _format_sse("thought", json.dumps({
                    "id": f"loop-detected-{time.time()}",
                    "type": "warning",
                    "text": f"⚠️ [Critic Strategy Switcher] {err_msg} Injecting strategy-shift instruction...",
                    "status": "running"
                }))
                add_to_task_log(tool_name, tier, "failed", err_msg)

                critic_nudge = (
                    f"[CRITIC STRATEGY NUDGE — Mandatory Approach Switch]\n"
                    f"The tool '{tool_name}' with parameters {sorted_args_str} has failed or repeated {consecutive_repeat_count} times.\n"
                    f"You MUST NOT call '{tool_name}' with these exact parameters again.\n"
                    f"Switch your strategy immediately (e.g. use alternative tools like `run_command` via OS/python, search alternative directories, or report blocked state)."
                )
                history.append({"role": "user", "content": critic_nudge})
                consecutive_repeat_count = 0
                observations.append(f"<observation:{tool_name}>[CRITIC NUDGE] Repeated tool execution blocked. Strategy shift required: try an alternative tool or path.</observation:{tool_name}>")
                continue

        try:
            if tier >= 1:
                mcts_score = await score_candidate_branch(
                    tool_name=tool_name,
                    args_str=json.dumps(args),
                    history=history,
                    client=client,
                    model=active_model if model_source == "local" else None
                )
                if mcts_score < 0.35:
                    yield _format_sse("thought", json.dumps({
                        "id": f"mcts-reject-{time.time()}",
                        "type": "warning",
                        "text": f"[MCTS] Tool '{tool_name}' scored {mcts_score:.2f} (below threshold 0.35). Skipping — low-value branch.",
                        "status": "failed"
                    }))
                    observations.append(
                        f"<observation:{tool_name}>[MCTS] Skipped low-value action (score={mcts_score:.2f}). "
                        f"Try a different approach to achieve the goal.</observation:{tool_name}>"
                    )
                    continue
        except Exception:
            pass

        if tier == 0:
            concurrent_calls.append((tool_name, args, tier))
        else:
            sequential_calls.append((tool_name, args, tier))

    state["last_tool_call"] = last_tool_call
    state["consecutive_repeat_count"] = consecutive_repeat_count

    # --- A. EXECUTE CONCURRENT READ-ONLY CALLS ---
    if concurrent_calls:
        yield _format_sse("thought", json.dumps({
            "id": f"speculative-{time.time()}",
            "type": "planning",
            "text": f"[Speculative Execution] Running {len(concurrent_calls)} read-only tools concurrently...",
            "status": "running"
        }))

        _batch_calls = [{"name": n, "arguments": p} for n, p, t in concurrent_calls]
        _batch_results = await dispatch_tool_batch(_batch_calls, session_id=session_id)

        for br in _batch_results:
            name = br["tool"]
            res = br["result"]
            status = "success" if br["status"] == "SUCCESS" else "failed"
            observations.append(f"<observation:{name}>{res}</observation:{name}>")
            if status == "failed":
                tot_failed = True
                failed_tool = name
                for c_name, c_args, c_t in concurrent_calls:
                    if c_name == name:
                        failed_args = c_args
                        break
                r_count = tool_retry_counts.get(name, 0) + 1
                tool_retry_counts[name] = r_count
                if r_count >= 3:
                    yield _format_sse("thought", json.dumps({
                        "id": f"retry-warn-{time.time()}-{name}",
                        "type": "warning",
                        "text": f"⚠️ Tool '{name}' has failed {r_count} times. Injecting recovery system guidelines.",
                        "status": "completed"
                    }))
                    history.append({
                        "role": "user",
                        "content": f"[SYSTEM ALERT]: Tool '{name}' has failed {r_count} times in this session. Do NOT attempt to run it again. Try alternative methods."
                    })
            yield _format_sse("thought", json.dumps({
                "id": f"spec-complete-{time.time()}-{name}",
                "type": "status",
                "text": f"Concurrent tool '{name}' finished ({status}).",
                "status": "completed"
            }))

    # --- B. EXECUTE SEQUENTIAL STATE-MODIFYING CALLS ---
    for tool_name, args, tier in sequential_calls:
        if interrupt_event.is_set():
            interrupt_event.clear()
            state["interrupted"] = True
            yield _format_sse("thought", json.dumps({"type": "planning", "text": "Task interrupted by user.", "status": "completed"}))
            return
        tool_run_id = f"run-{tool_name}-{time.time()}"
        requires_approval, approval_reason = check_approval_gate(tool_name, args)
        if requires_approval:
            conf_id = f"conf-{uuid.uuid4()}"
            conf_event = asyncio.Event()
            await register_confirmation(conf_id, conf_event)

            yield _format_sse("confirmation", json.dumps({
                "id": conf_id,
                "tool": tool_name,
                "args": args,
                "tier": tier,
                "reason": approval_reason
            }))

            try:
                await asyncio.wait_for(conf_event.wait(), timeout=120.0)
            except asyncio.TimeoutError:
                pass
            approved = await pop_confirmation(conf_id)

            if not approved:
                obs_text = "Tool execution rejected by user safety gate."
                yield _format_sse("thought", json.dumps({
                    "id": tool_run_id,
                    "type": "warning",
                    "text": f"Safety Gate: Execution of {tool_name} was rejected.",
                    "status": "failed"
                }))
                observations.append(f"<observation:{tool_name}>{obs_text}</observation:{tool_name}>")
                continue

        if tool_name in ["screenshot", "screenshot_region"]:
            path = args.get("output_path")
            if path:
                created_temp_files.append(os.path.abspath(path))
        elif tool_name == "browser_screenshot":
            path = args.get("output_path", "browser.png")
            created_temp_files.append(os.path.abspath(path))

        yield _format_sse("thought", json.dumps({
            "id": tool_run_id,
            "type": "exec",
            "text": f"Running tool: {tool_name}",
            "tool": tool_name,
            "command": json.dumps(args),
            "status": "running",
            "mascot_state": "default",
            "mascot_wardrobe": "none"
        }))

        await create_tool_checkpoint(tool_name, tool_run_id)

        try:
            result = await call_tool(tool_name, args)
            if tool_name == "run_python" and ("matplotlib" in json.dumps(args) or "plt." in json.dumps(args)):
                yield _format_sse("thought", json.dumps({
                    "id": f"anchor-{time.time()}",
                    "type": "planning",
                    "text": "[Thought Anchoring] Capturing validation screenshot to inspect layout generation success...",
                    "status": "running"
                }))

            observations.append(f"<observation:{tool_name}>{result}</observation:{tool_name}>")
            yield _format_sse("thought", json.dumps({
                "id": tool_run_id,
                "type": "status",
                "text": f"Tool {tool_name} completed.",
                "status": "completed"
            }))
            add_to_task_log(tool_name, tier, "success")
            if tool_name == "reload_plugins":
                state["reloaded_plugins"] = True
        except Exception as e:
            err_txt = str(e)
            tot_failed = True
            failed_tool = tool_name
            failed_args = args
            observations.append(f"<observation:{tool_name}>Error: {err_txt}</observation:{tool_name}>")

            r_count = tool_retry_counts.get(tool_name, 0) + 1
            tool_retry_counts[tool_name] = r_count
            if r_count >= 3:
                yield _format_sse("thought", json.dumps({
                    "id": f"retry-warn-{time.time()}-{tool_name}",
                    "type": "warning",
                    "text": f"⚠️ Tool '{tool_name}' has failed {r_count} times. Injecting recovery system guidelines.",
                    "status": "completed"
                }))
                history.append({
                    "role": "user",
                    "content": f"[SYSTEM ALERT]: Tool '{tool_name}' has failed {r_count} times in this session. Do NOT attempt to run it again. Try alternative methods."
                })

            yield _format_sse("thought", json.dumps({
                "id": tool_run_id,
                "type": "warning",
                "text": f"Tool {tool_name} failed: {err_txt}",
                "status": "failed"
            }))
            add_to_task_log(tool_name, tier, "failed", err_txt)

        if interrupt_event.is_set():
            interrupt_event.clear()
            state["interrupted"] = True
            yield _format_sse("thought", json.dumps({"type": "planning", "text": "Task interrupted by user.", "status": "completed"}))
            return

    # Tree-of-Thoughts Backtracking execution
    if tot_failed:
        history[:] = list(tot_checkpoint)
        yield _format_sse("thought", json.dumps({
            "id": f"tot-backtrack-{time.time()}",
            "type": "warning",
            "text": f"[Tree-of-Thoughts] Tool execution of '{failed_tool}' failed. Backtracking and adjusting pathway...",
            "status": "completed"
        }))
        history.append({
            "role": "user",
            "content": f"<observation:{failed_tool}>Error: Tool execution failed. [Tree-of-Thoughts Backtrack]: Avoid calling '{failed_tool}' with args {json.dumps(failed_args)} again as it fails in this environment. Attempt an alternative search, verify paths, or try a different approach.</observation:{failed_tool}>"
        })
    else:
        obs_payload = "\n".join(observations)
        history.append({"role": "user", "content": obs_payload})

