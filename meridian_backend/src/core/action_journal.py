"""
action_journal.py — Reversible Action Journal & Undo Engine (BUTLER-14)
Tracks agent tool mutations with inverse restoration functions, enabling one-tap UI undo and "undo that" voice/chat commands.
"""

import time
import json
import logging
from typing import Dict, Any, List, Optional, Tuple
import database

logger = logging.getLogger("meridian_action_journal")


class ActionJournal:
    """Stack of reversible actions with inverse handlers for seamless undo execution."""

    def __init__(self):
        self._memory_stack: List[Dict[str, Any]] = []

    def record_action(
        self,
        tool: str,
        arguments: Dict[str, Any],
        inverse_tool: str,
        inverse_arguments: Dict[str, Any],
        description: str = ""
    ) -> str:
        """Records a reversible action into journal stack."""
        action_id = f"act_{int(time.time() * 1000)}"
        entry = {
            "id": action_id,
            "timestamp": time.time(),
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tool": tool,
            "arguments": arguments,
            "inverse_tool": inverse_tool,
            "inverse_arguments": inverse_arguments,
            "description": description or f"Executed {tool}",
            "undone": False
        }

        self._memory_stack.append(entry)

        # Persist to SQLite
        try:
            conn = database.get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS action_journal (
                    id TEXT PRIMARY KEY,
                    timestamp REAL,
                    tool TEXT,
                    arguments TEXT,
                    inverse_tool TEXT,
                    inverse_arguments TEXT,
                    description TEXT,
                    undone INTEGER DEFAULT 0
                )
            """)
            cursor.execute("""
                INSERT INTO action_journal (id, timestamp, tool, arguments, inverse_tool, inverse_arguments, description, undone)
                VALUES (?, ?, ?, ?, ?, ?, ?, 0)
            """, (
                action_id,
                entry["timestamp"],
                tool,
                json.dumps(arguments),
                inverse_tool,
                json.dumps(inverse_arguments),
                entry["description"]
            ))
            conn.commit()
            conn.close()
        except Exception as e:
            logger.debug(f"[ActionJournal] DB save error: {e}")

        return action_id

    def get_recent_actions(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Returns recent reversible actions from journal."""
        if self._memory_stack:
            return list(reversed(self._memory_stack[-limit:]))

        try:
            conn = database.get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS action_journal (
                    id TEXT PRIMARY KEY,
                    timestamp REAL,
                    tool TEXT,
                    arguments TEXT,
                    inverse_tool TEXT,
                    inverse_arguments TEXT,
                    description TEXT,
                    undone INTEGER DEFAULT 0
                )
            """)
            cursor.execute("SELECT id, timestamp, tool, arguments, inverse_tool, inverse_arguments, description, undone FROM action_journal ORDER BY timestamp DESC LIMIT ?", (limit,))
            rows = cursor.fetchall()
            conn.close()

            results = []
            for r in rows:
                results.append({
                    "id": r["id"],
                    "timestamp": r["timestamp"],
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(r["timestamp"])),
                    "tool": r["tool"],
                    "arguments": json.loads(r["arguments"]) if r["arguments"] else {},
                    "inverse_tool": r["inverse_tool"],
                    "inverse_arguments": json.loads(r["inverse_arguments"]) if r["inverse_arguments"] else {},
                    "description": r["description"],
                    "undone": bool(r["undone"])
                })
            return results
        except Exception as e:
            logger.debug(f"[ActionJournal] DB fetch error: {e}")
            return []

    def undo_action(self, action_id: Optional[str] = None) -> Dict[str, Any]:
        """Executes inverse tool handler for target action or last recorded action."""
        actions = self.get_recent_actions(50)
        target = None

        if action_id:
            for a in actions:
                if a["id"] == action_id and not a["undone"]:
                    target = a
                    break
        else:
            for a in actions:
                if not a["undone"]:
                    target = a
                    break

        if not target:
            return {"success": False, "message": "No reversible actions available to undo."}

        inv_tool = target.get("inverse_tool")
        inv_args = target.get("inverse_arguments", {})

        # Dispatch inverse tool call via tools registry
        try:
            from src.tools.registry import registry
            tool_fn = registry.get_tool(inv_tool)
            if tool_fn:
                result = tool_fn(**inv_args)
            else:
                result = f"Inverse tool '{inv_tool}' not registered."

            # Mark action as undone
            target["undone"] = True
            self._mark_undone_in_db(target["id"])

            return {
                "success": True,
                "action_id": target["id"],
                "tool_undone": target["tool"],
                "inverse_executed": inv_tool,
                "result": str(result),
                "message": f"Successfully undone action: {target['description']}"
            }
        except Exception as e:
            logger.error(f"[ActionJournal] Undo execution error: {e}")
            return {"success": False, "message": f"Undo failed: {e}"}

    def _mark_undone_in_db(self, action_id: str):
        try:
            conn = database.get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("UPDATE action_journal SET undone = 1 WHERE id = ?", (action_id,))
            conn.commit()
            conn.close()
        except Exception:
            pass


# Global singleton instance
global_action_journal = ActionJournal()
