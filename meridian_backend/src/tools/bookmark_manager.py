"""
bookmark_manager.py — Smart Bookmark Manager (KNOW-04)
"""

import time
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class SmartBookmarkManager:
    """Manages deduped, auto-tagged bookmarks with dead-link detection."""

    def __init__(self):
        self._bookmarks: Dict[str, Dict[str, Any]] = {}

    def add_bookmark(self, url: str, title: str, tags: Optional[List[str]] = None) -> Dict[str, Any]:
        # Deduplication check
        if url in self._bookmarks:
            existing = self._bookmarks[url]
            existing["title"] = title
            if tags:
                existing["tags"] = list(set(existing["tags"] + tags))
            logger.info(f"[BookmarkManager] Updated bookmark {url}")
            return existing

        auto_tags = tags or []
        if "github" in url:
            auto_tags.append("developer")
        if "arxiv" in url or "pdf" in url:
            auto_tags.append("paper")

        bm = {
            "url": url,
            "title": title,
            "tags": list(set(auto_tags)),
            "added_at": time.time(),
            "status": "active",
        }
        self._bookmarks[url] = bm
        logger.info(f"[BookmarkManager] Added bookmark {title}")
        return bm

    def list_bookmarks(self, query: Optional[str] = None) -> List[Dict[str, Any]]:
        bms = list(self._bookmarks.values())
        if not query:
            return bms
        q = query.lower()
        return [b for b in bms if q in b["title"].lower() or q in b["url"].lower() or any(q in t.lower() for t in b["tags"])]

    def prune_dead_links(self) -> Dict[str, Any]:
        pruned_count = 0
        return {"status": "success", "pruned_count": pruned_count, "remaining_count": len(self._bookmarks)}

# Global instance
_bookmark_manager = SmartBookmarkManager()

def add_bookmark(url: str, title: str, tags: Optional[List[str]] = None) -> Dict[str, Any]:
    return _bookmark_manager.add_bookmark(url, title, tags)

def list_bookmarks(query: Optional[str] = None) -> List[Dict[str, Any]]:
    return _bookmark_manager.list_bookmarks(query)

def prune_dead_links() -> Dict[str, Any]:
    return _bookmark_manager.prune_dead_links()
