import os
import logging
import asyncio
import json
import time
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

class MemoryNode(BaseModel):
    id: str
    category: str = "preference" # preference, fact, decision, snippet
    content: str
    confidence: float = 0.9
    created_at: float = Field(default_factory=time.time)
    source_session: Optional[str] = None
    tags: List[str] = []

class ConsolidationRequest(BaseModel):
    session_id: Optional[str] = None
    messages: List[Dict[str, str]] = []
    auto_prune_duplicates: bool = True

class ConsolidationResult(BaseModel):
    summary: str
    key_topics: List[str]
    extracted_nodes: List[MemoryNode]
    messages_processed: int
    consolidated_at: float = Field(default_factory=time.time)

class MemoryConsolidationEngine:
    """Handles conversation summarization, semantic entity extraction, and memory consolidation into long-term storage."""

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or os.path.join(os.path.dirname(__file__), "..", "..", "meridian_memory", "memory.db")
        self._history: List[ConsolidationResult] = []

    def summarize_messages(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Generate structured summary and key points from a list of user/assistant messages."""
        if not messages:
            return {
                "summary": "No messages provided.",
                "key_topics": [],
                "decisions": [],
                "user_facts": []
            }

        text_lines = []
        user_facts = []
        decisions = []
        key_topics = set()

        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "").strip()
            if not content:
                continue

            text_lines.append(f"{role.capitalize()}: {content}")

            # Basic rule-based semantic extraction fallback
            lower = content.lower()
            if "prefer" in lower or "like" in lower or "use" in lower or "setting" in lower:
                user_facts.append(content)
                key_topics.add("User Preferences")
            if "decided" in lower or "agree" in lower or "plan" in lower or "build" in lower:
                decisions.append(content)
                key_topics.add("Decisions & Planning")
            if "error" in lower or "bug" in lower or "fix" in lower:
                key_topics.add("Bugfix & Debugging")
            if "model" in lower or "quant" in lower:
                key_topics.add("Local Models & AI")

        if not key_topics:
            key_topics.add("General Conversation")

        first_few = [m.get("content", "")[:100] for m in messages[:3]]
        summary_text = f"Conversation covering {', '.join(list(key_topics))}. Primary topics included: {' '.join(first_few)}"

        return {
            "summary": summary_text,
            "key_topics": list(key_topics),
            "decisions": decisions,
            "user_facts": user_facts
        }

    async def consolidate(self, request: ConsolidationRequest) -> ConsolidationResult:
        """Run full consolidation pipeline on provided messages or active session."""
        summary_info = self.summarize_messages(request.messages)

        extracted_nodes: List[MemoryNode] = []
        node_id_counter = int(time.time() * 1000)

        for fact in summary_info["user_facts"]:
            extracted_nodes.append(MemoryNode(
                id=f"mem_{node_id_counter}",
                category="preference",
                content=fact,
                confidence=0.92,
                source_session=request.session_id,
                tags=["extracted", "user_fact"]
            ))
            node_id_counter += 1

        for decision in summary_info["decisions"]:
            extracted_nodes.append(MemoryNode(
                id=f"mem_{node_id_counter}",
                category="decision",
                content=decision,
                confidence=0.95,
                source_session=request.session_id,
                tags=["extracted", "decision"]
            ))
            node_id_counter += 1

        if not extracted_nodes and summary_info["summary"]:
            extracted_nodes.append(MemoryNode(
                id=f"mem_{node_id_counter}",
                category="summary",
                content=summary_info["summary"],
                confidence=0.88,
                source_session=request.session_id,
                tags=["summary"]
            ))

        result = ConsolidationResult(
            summary=summary_info["summary"],
            key_topics=summary_info["key_topics"],
            extracted_nodes=extracted_nodes,
            messages_processed=len(request.messages)
        )

        self._history.append(result)
        logger.info(f"Consolidated {len(request.messages)} messages into {len(extracted_nodes)} memory nodes.")
        return result

    def get_status(self) -> Dict[str, Any]:
        """Return memory consolidation metrics."""
        total_runs = len(self._history)
        total_nodes = sum(len(r.extracted_nodes) for r in self._history)
        total_msgs = sum(r.messages_processed for r in self._history)
        latest_summary = self._history[-1].summary if self._history else "No consolidation runs yet."

        return {
            "total_consolidation_runs": total_runs,
            "total_nodes_extracted": total_nodes,
            "total_messages_processed": total_msgs,
            "latest_summary": latest_summary,
            "last_consolidated_at": self._history[-1].consolidated_at if self._history else None
        }

memory_consolidation_engine = MemoryConsolidationEngine()
_last_consolidated_turn: int = 0

def check_milestone_memory_consolidation(current_turn: int, threshold: int = 5) -> bool:
    """Proactively triggers memory consolidation at conversation turn milestones."""
    global _last_consolidated_turn
    if current_turn < threshold:
        return False

    if current_turn - _last_consolidated_turn < threshold:
        return False

    _last_consolidated_turn = current_turn
    try:
        from database import consolidate_memory_sleep_cycle
        consolidate_memory_sleep_cycle()
        logger.info(f"[MemoryConsolidation] Proactive milestone consolidation executed at turn {current_turn}.")
        return True
    except Exception as e:
        logger.debug(f"[MemoryConsolidation] Milestone consolidation skipped: {e}")
        return False
