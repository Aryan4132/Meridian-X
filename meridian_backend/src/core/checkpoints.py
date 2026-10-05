"""
checkpoints.py — Automatic git snapshots and rollback management for mutating tool calls.
"""

import asyncio
from typing import Optional, Dict, Any

CODE_MODIFYING_TOOLS = {
    "write_file",
    "delete_file",
    "move_file",
    "create_dynamic_tool",
    "generate_dynamic_tool",
}


async def create_tool_checkpoint(tool_name: str, tool_run_id: str) -> Optional[str]:
    """Creates a git checkpoint before executing any code-modifying tool."""
    if tool_name in CODE_MODIFYING_TOOLS:
        try:
            from src.core.history_manager import create_checkpoint
            await asyncio.to_thread(create_checkpoint, tool_run_id)
            return tool_run_id
        except Exception as che:
            print(f"[History Manager] Failed to create checkpoint: {che}")
    return None


async def rollback_checkpoint(checkpoint_id: str) -> bool:
    """Rolls back the workspace state to a specific git checkpoint."""
    try:
        from src.core.history_manager import rollback_to_checkpoint
        return await asyncio.to_thread(rollback_to_checkpoint, checkpoint_id)
    except Exception as re:
        print(f"[History Manager] Failed to rollback checkpoint {checkpoint_id}: {re}")
        return False
