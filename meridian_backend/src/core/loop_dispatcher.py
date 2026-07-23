"""
loop_dispatcher.py — Tool Execution Dispatcher Sub-module
Manages per-tool retry budgets, batch call tagging, and execution dispatches.
"""

import asyncio
import time
from typing import Dict, Any, List, Tuple, Optional
from src.tools.registry import call_tool, TOOL_REGISTRY

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
    """
    results = []
    tasks = []

    for idx, call in enumerate(tool_calls):
        tool_name = call.get("name")
        tool_args = call.get("arguments", {})

        if not check_and_increment_retry(session_id, tool_name):
            results.append({
                "index": idx,
                "tool": tool_name,
                "status": "EXCEEDED_RETRY_BUDGET",
                "result": f"Error: Tool '{tool_name}' has exceeded its retry budget of {MAX_RETRY_PER_TOOL} attempts."
            })
            continue

        # Create explicit tagged execution task
        async def _exec(index: int, name: str, args: dict):
            try:
                out = await asyncio.to_thread(call_tool, name, args)
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
