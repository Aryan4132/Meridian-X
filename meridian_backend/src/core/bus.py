import asyncio
from typing import Dict, List, Any

class LocalEventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[asyncio.Queue]] = {}

    def subscribe(self, topic: str) -> asyncio.Queue:
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        queue = asyncio.Queue()
        self._subscribers[topic].append(queue)
        return queue

    def unsubscribe(self, topic: str, queue: asyncio.Queue):
        if topic in self._subscribers:
            try:
                self._subscribers[topic].remove(queue)
            except ValueError:
                pass
            if not self._subscribers[topic]:
                del self._subscribers[topic]

    async def publish(self, topic: str, message: Any):
        if topic in self._subscribers:
            # Publish to all active queues for this topic
            for queue in self._subscribers[topic]:
                await queue.put(message)

# Global event bus instance for the process
event_bus = LocalEventBus()
