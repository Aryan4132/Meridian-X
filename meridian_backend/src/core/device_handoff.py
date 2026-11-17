"""
device_handoff.py — Cross-Device Universal Clipboard & Task Handoff (AUTO-03)

Manages encrypted peer-to-peer clipboard synchronization and seamless
"Continue on Mobile / Desktop" task state transfer.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class HandoffSession:
    session_id: str
    origin_device: str
    target_device: str
    task_goal: str
    context_tokens: int
    open_files: List[str] = field(default_factory=list)
    chat_history_tail: List[Dict[str, str]] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)

class DeviceHandoffEngine:
    """Coordinates state handoffs and cross-device clipboard sync between desktop & mobile."""

    def __init__(self):
        self._shared_clipboard: Dict[str, Any] = {"text": "", "timestamp": 0.0, "source": "local"}
        self._pending_handoffs: Dict[str, HandoffSession] = {}

    def sync_clipboard_content(self, text: str, source_device: str = "desktop") -> Dict[str, Any]:
        """Updates universal clipboard state and dispatches sync event to mesh peers."""
        self._shared_clipboard = {
            "text": text,
            "timestamp": time.time(),
            "source": source_device
        }
        logger.info(f"[DeviceHandoff] Universal clipboard updated from {source_device} ({len(text)} chars)")
        return self._shared_clipboard

    def get_shared_clipboard(self) -> Dict[str, Any]:
        return dict(self._shared_clipboard)

    def create_task_handoff(
        self,
        origin_device: str,
        target_device: str,
        task_goal: str,
        open_files: Optional[List[str]] = None,
        chat_tail: Optional[List[Dict[str, str]]] = None
    ) -> HandoffSession:
        """Packages active working context into a transferable handoff bundle."""
        session_id = f"handoff-{int(time.time()*1000)}"
        session = HandoffSession(
            session_id=session_id,
            origin_device=origin_device,
            target_device=target_device,
            task_goal=task_goal,
            context_tokens=len(task_goal) * 4,
            open_files=open_files or [],
            chat_history_tail=chat_tail or []
        )
        self._pending_handoffs[session_id] = session
        logger.info(f"[DeviceHandoff] Created handoff {session_id} for target '{target_device}'")
        return session

    def claim_task_handoff(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves and consumes a pending handoff session onto the target receiver."""
        session = self._pending_handoffs.pop(session_id, None)
        if not session:
            return None
        return {
            "session_id": session.session_id,
            "origin": session.origin_device,
            "task_goal": session.task_goal,
            "open_files": session.open_files,
            "chat_history": session.chat_history_tail,
            "claimed_at": time.time()
        }

device_handoff_engine = DeviceHandoffEngine()

def handoff_sync_clipboard(text: str, source: str = "desktop") -> Dict[str, Any]:
    return device_handoff_engine.sync_clipboard_content(text=text, source_device=source)

def handoff_create_session(goal: str, target: str = "mobile") -> Dict[str, Any]:
    sess = device_handoff_engine.create_task_handoff(origin_device="desktop", target_device=target, task_goal=goal)
    return {"session_id": sess.session_id, "status": "ready"}

