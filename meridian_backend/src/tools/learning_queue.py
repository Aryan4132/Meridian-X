"""
learning_queue.py — Learning Queue & Spaced Reading Digest (BUTLER-08)
"""

import time
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class LearningQueueManager:
    """Manages 'save for later' reading items, SM-2 flashcard review, and reading digests."""

    def __init__(self):
        self._queue: List[Dict[str, Any]] = []
        self._flashcards: List[Dict[str, Any]] = []

    def add_to_queue(self, url: str, title: str, tags: Optional[List[str]] = None) -> Dict[str, Any]:
        item = {
            "id": f"item-{int(time.time()*1000)}",
            "url": url,
            "title": title,
            "tags": tags or ["general"],
            "added_at": time.time(),
            "status": "unread",
        }
        self._queue.append(item)
        logger.info(f"[LearningQueue] Added item: {title}")
        return item

    def list_queue(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        if status:
            return [i for i in self._queue if i["status"] == status]
        return list(self._queue)

    def generate_sm2_flashcards(self, topic: str = "general") -> List[Dict[str, Any]]:
        cards = [
            {
                "card_id": f"card-{int(time.time()*1000)}-1",
                "question": f"Key concept in {topic}?",
                "answer": "Core architecture principle and separation of concerns.",
                "interval_days": 1,
                "ease_factor": 2.5,
            }
        ]
        self._flashcards.extend(cards)
        return cards

    def generate_reading_digest(self) -> Dict[str, Any]:
        unread = [i for i in self._queue if i["status"] == "unread"]
        return {
            "digest_title": "Weekly Spaced Reading Summary",
            "total_unread": len(unread),
            "top_picks": unread[:3],
            "generated_at": time.time(),
        }

# Global instance
_queue_manager = LearningQueueManager()

def add_to_learning_queue(url: str, title: str, tags: Optional[List[str]] = None) -> Dict[str, Any]:
    return _queue_manager.add_to_queue(url, title, tags)

def list_learning_queue(status: Optional[str] = None) -> List[Dict[str, Any]]:
    return _queue_manager.list_queue(status)

def generate_sm2_flashcards(topic: str = "general") -> List[Dict[str, Any]]:
    return _queue_manager.generate_sm2_flashcards(topic)

def generate_reading_digest() -> Dict[str, Any]:
    return _queue_manager.generate_reading_digest()
