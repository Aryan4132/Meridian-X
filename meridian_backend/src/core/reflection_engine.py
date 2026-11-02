"""
reflection_engine.py — Continuous Self-Improvement & Reflexion Engine
Captures user corrections, extracts actionable rules from mistakes,
persists lessons to CognitiveGraph, and recalls past successful trajectories.
"""

import re
import time
import json
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger("reflection_engine")

CORRECTION_PATTERNS = [
    r'^(?:no|nope|wrong|stop)[,:\s]+(?:don\'t|do not|never|instead|always|use)\s+(.+)',
    r'(?:remember that|note that|in this (?:project|repo|workspace))[,\s]+(?:always|never|do not|don\'t|only)\s+(.+)',
    r'(?:always|never|only)\s+(?:use|run|format|install|call)\s+(.+)',
    r'(?:don\'t|do not)\s+(?:use|touch|delete|edit|run)\s+(.+)'
]


def detect_user_correction(text: str) -> Optional[str]:
    """Detects explicit correction cues in user messages and extracts the constraint."""
    if not text or len(text.strip()) < 5:
        return None
    cleaned = text.strip()
    for pattern in CORRECTION_PATTERNS:
        match = re.search(pattern, cleaned, re.IGNORECASE)
        if match:
            rule = match.group(0).strip().rstrip('.!?')
            return rule
    return None


class ReflectionEngine:
    """Manages continuous adaptation through lessons, corrections, and experience replay."""

    def __init__(self, cg: Any = None):
        self._cg = cg

    @property
    def cg(self) -> Any:
        if self._cg is None:
            from src.core.cognitive_graph import get_cognitive_graph
            self._cg = get_cognitive_graph()
        return self._cg

    def record_learned_lesson(self, rule: str, category: str = "correction", context: Optional[str] = None) -> Dict[str, Any]:
        """Persists a learned lesson node in the cognitive graph."""
        node_id = f"lesson_{int(time.time() * 1000)}"
        meta = {
            "rule": rule,
            "category": category,
            "context": context or "",
            "confidence": 0.95 if category == "correction" else 0.85,
            "timestamp": time.time()
        }
        return self.cg.add_node(
            node_id=node_id,
            node_type="learned_rule",
            name=rule[:120],
            metadata=meta
        )

    def record_task_experience(self, goal: str, tools_used: List[str], outcome: str) -> Dict[str, Any]:
        """Saves a successful task trajectory for few-shot experience replay."""
        node_id = f"exp_{int(time.time() * 1000)}"
        meta = {
            "goal": goal,
            "tools_used": tools_used,
            "outcome": outcome[:300],
            "timestamp": time.time()
        }
        return self.cg.add_node(
            node_id=node_id,
            node_type="task_experience",
            name=goal[:120],
            metadata=meta
        )

    def get_relevant_lessons(self, query: str, limit: int = 4) -> List[str]:
        """Retrieves top learned rules and constraints relevant to the active query."""
        if not query or not query.strip():
            return []
        try:
            nodes = self.cg.find_nodes(query, limit=limit * 2)
            lessons = []
            for n in nodes:
                if n.get("type") == "learned_rule":
                    meta = n.get("metadata", {})
                    rule = meta.get("rule") or n.get("name")
                    if rule and rule not in lessons:
                        lessons.append(rule)
                    if len(lessons) >= limit:
                        break

            # If FTS returned fewer, query recent learned rules
            if len(lessons) < limit:
                with self.cg._get_connection() as conn:
                    rows = conn.execute(
                        "SELECT metadata, name FROM cognitive_nodes WHERE type = 'learned_rule' ORDER BY created_at DESC LIMIT ?",
                        (limit - len(lessons),)
                    ).fetchall()
                    for r in rows:
                        meta = json.loads(r["metadata"] or "{}")
                        rule = meta.get("rule") or r["name"]
                        if rule and rule not in lessons:
                            lessons.append(rule)
            return lessons
        except Exception as e:
            logger.debug(f"Failed to query lessons: {e}")
            return []

    def get_relevant_experiences(self, query: str, limit: int = 2) -> List[Dict[str, Any]]:
        """Retrieves top past successful trajectories relevant to the active query."""
        if not query or not query.strip():
            return []
        try:
            nodes = self.cg.find_nodes(query, limit=limit * 2)
            experiences = []
            for n in nodes:
                if n.get("type") == "task_experience":
                    meta = n.get("metadata", {})
                    experiences.append({
                        "goal": meta.get("goal") or n.get("name"),
                        "tools": meta.get("tools_used", []),
                        "outcome": meta.get("outcome", "")
                    })
                    if len(experiences) >= limit:
                        break

            # If FTS returned fewer, query recent task experiences
            if len(experiences) < limit:
                with self.cg._get_connection() as conn:
                    rows = conn.execute(
                        "SELECT metadata, name FROM cognitive_nodes WHERE type = 'task_experience' ORDER BY created_at DESC LIMIT ?",
                        (limit - len(experiences),)
                    ).fetchall()
                    for r in rows:
                        meta = json.loads(r["metadata"] or "{}")
                        experiences.append({
                            "goal": meta.get("goal") or r["name"],
                            "tools": meta.get("tools_used", []),
                            "outcome": meta.get("outcome", "")
                        })

            return experiences
        except Exception as e:
            logger.debug(f"Failed to query experiences: {e}")
            return []


_reflection_engine_instance: Optional[ReflectionEngine] = None


def get_reflection_engine() -> ReflectionEngine:
    global _reflection_engine_instance
    if _reflection_engine_instance is None:
        _reflection_engine_instance = ReflectionEngine()
    return _reflection_engine_instance
