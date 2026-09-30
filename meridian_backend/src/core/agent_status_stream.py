import asyncio
import logging
import time
from typing import Dict, Any, List, Set, Optional
from pydantic import BaseModel, Field
from fastapi import WebSocket

logger = logging.getLogger(__name__)

class AgentActivityEvent(BaseModel):
    event_id: str
    timestamp: float = Field(default_factory=time.time)
    status: str = "idle" # idle, thinking, executing_tool, verifying, completed, error
    current_task: Optional[str] = None
    active_tool: Optional[str] = None
    subagent: Optional[str] = None
    message: str = ""
    progress_percentage: Optional[float] = None
    details: Dict[str, Any] = {}

class AgentStatusStreamManager:
    """Manages real-time agent state, rolling activity logs, and WebSocket client subscriptions."""

    def __init__(self):
        self.active_status: str = "idle"
        self.current_task: Optional[str] = None
        self.active_tool: Optional[str] = None
        self.active_subagent: Optional[str] = None
        self.history: List[AgentActivityEvent] = []
        self.active_connections: Set[WebSocket] = set()
        self._event_counter = 0

    def broadcast_event(self, status: str, message: str, tool: Optional[str] = None, subagent: Optional[str] = None, task: Optional[str] = None, details: Optional[Dict[str, Any]] = None, progress: Optional[float] = None) -> AgentActivityEvent:
        """Publish a new agent activity event to all subscribers and update status state."""
        self.active_status = status
        if task is not None:
            self.current_task = task
        if tool is not None:
            self.active_tool = tool
        if subagent is not None:
            self.active_subagent = subagent

        self._event_counter += 1
        event = AgentActivityEvent(
            event_id=f"evt_{self._event_counter}_{int(time.time())}",
            status=status,
            current_task=self.current_task,
            active_tool=self.active_tool,
            subagent=self.active_subagent,
            message=message,
            progress_percentage=progress,
            details=details or {}
        )

        self.history.append(event)
        if len(self.history) > 100:
            self.history = self.history[-100:]

        # Non-blocking async broadcast schedule
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self._broadcast_ws(event))
        except RuntimeError:
            pass # No running event loop yet

        return event

    async def _broadcast_ws(self, event: AgentActivityEvent):
        """Send event payload to connected WebSocket clients."""
        if not self.active_connections:
            return

        payload = event.model_dump_json()
        disconnected = set()

        for ws in self.active_connections:
            try:
                await ws.send_text(payload)
            except Exception as e:
                logger.debug(f"Disconnecting WS client: {e}")
                disconnected.add(ws)

        for ws in disconnected:
            self.active_connections.remove(ws)

    async def register_connection(self, ws: WebSocket):
        """Add WebSocket connection and send current snapshot."""
        await ws.accept()
        self.active_connections.add(ws)
        # Send initial snapshot event
        initial_event = AgentActivityEvent(
            event_id="evt_init",
            status=self.active_status,
            current_task=self.current_task,
            active_tool=self.active_tool,
            subagent=self.active_subagent,
            message="Connected to Agent Activity Stream."
        )
        await ws.send_text(initial_event.model_dump_json())

    def unregister_connection(self, ws: WebSocket):
        """Remove WebSocket connection."""
        self.active_connections.discard(ws)

    def get_snapshot(self) -> Dict[str, Any]:
        """Return current status state and recent activity history."""
        return {
            "status": self.active_status,
            "current_task": self.current_task,
            "active_tool": self.active_tool,
            "active_subagent": self.active_subagent,
            "connected_clients": len(self.active_connections),
            "recent_events": [e.model_dump() for e in self.history[-20:]]
        }

agent_status_stream_manager = AgentStatusStreamManager()
