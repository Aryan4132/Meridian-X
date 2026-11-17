"""
family_board.py — Shared Family Board & Multi-User Lists (FAM-01)

Collaborative shared board for household members: synchronized checklists,
announcements, chore assignments, and event notifications.
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class FamilyBoardSentinel:
    """Manages multi-member shared lists and household announcements."""

    def __init__(self):
        self._announcements: List[Dict[str, Any]] = [
            {"id": "msg-1", "author": "Aryan", "content": "Welcome to Meridian-X Family Hub", "timestamp": time.time()}
        ]
        self._shared_tasks: Dict[str, Dict[str, Any]] = {}

    def post_announcement(self, author: str, content: str) -> Dict[str, Any]:
        """Broadcasts an announcement to all household companion devices."""
        msg = {
            "id": f"msg-{int(time.time()*1000)}",
            "author": author,
            "content": content,
            "timestamp": time.time()
        }
        self._announcements.append(msg)
        logger.info(f"[FamilyBoard] New announcement from {author}: {content}")
        return msg

    def add_shared_task(self, title: str, assigned_to: str, due_date: str = "") -> Dict[str, Any]:
        """Creates a synchronized chore/task on the household board."""
        task_id = f"task-{int(time.time()*1000)}"
        task = {
            "task_id": task_id,
            "title": title,
            "assigned_to": assigned_to,
            "due_date": due_date,
            "completed": False,
            "created_at": time.time()
        }
        self._shared_tasks[task_id] = task
        return task

    def complete_shared_task(self, task_id: str) -> Dict[str, Any]:
        task = self._shared_tasks.get(task_id)
        if not task:
            return {"status": "error", "message": "Task not found"}
        task["completed"] = True
        return {"status": "success", "task_id": task_id, "completed": True}

    def get_board_summary(self) -> Dict[str, Any]:
        return {
            "announcements": self._announcements[-5:],
            "active_tasks": [t for t in self._shared_tasks.values() if not t["completed"]],
            "completed_tasks": [t for t in self._shared_tasks.values() if t["completed"]]
        }

family_board_sentinel = FamilyBoardSentinel()

def family_post_announcement(author: str, content: str) -> Dict[str, Any]:
    return family_board_sentinel.post_announcement(author=author, content=content)

def family_add_task(title: str, assigned_to: str, due_date: str = "") -> Dict[str, Any]:
    return family_board_sentinel.add_shared_task(title=title, assigned_to=assigned_to, due_date=due_date)

def family_get_board() -> Dict[str, Any]:
    return family_board_sentinel.get_board_summary()

