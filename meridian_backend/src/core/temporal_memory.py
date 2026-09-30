"""
temporal_memory.py — Temporal Memory Graph Engine (BK-25)
Tracks entity evolution over time with timestamped memory nodes, relationship edges, and time-decay relevance scoring.
"""

import time
import math
from typing import Dict, Any, List, Optional


class TemporalMemoryGraph:
    """Time-aware knowledge graph tracking project entity states and temporal decay."""

    def __init__(self, decay_lambda: float = 0.0001):
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.edges: List[Dict[str, Any]] = []
        self.decay_lambda = decay_lambda

    def add_event(self, entity_id: str, entity_type: str, state: Dict[str, Any], timestamp: Optional[float] = None) -> str:
        """Adds a timestamped memory event node for an entity."""
        ts = timestamp or time.time()
        node_id = f"{entity_id}:{ts}"
        
        node_data = {
            "id": node_id,
            "entity_id": entity_id,
            "type": entity_type,
            "state": state,
            "timestamp": ts,
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
        }
        self.nodes[node_id] = node_data

        # Automatically link previous state of the same entity if exists
        prev_nodes = [
            n for n in self.nodes.values()
            if n["entity_id"] == entity_id and n["id"] != node_id
        ]
        if prev_nodes:
            latest_prev = max(prev_nodes, key=lambda x: x["timestamp"])
            self.add_edge(latest_prev["id"], node_id, relation="supersedes", timestamp=ts)

        return node_id

    def add_edge(self, source_id: str, target_id: str, relation: str, timestamp: Optional[float] = None):
        """Adds a timestamped relationship edge between two memory nodes."""
        ts = timestamp or time.time()
        self.edges.append({
            "source": source_id,
            "target": target_id,
            "relation": relation,
            "timestamp": ts
        })

    def calculate_temporal_relevance(self, node_id: str, current_time: Optional[float] = None) -> float:
        """Calculates exponential time-decay score S(t) = S0 * e^(-lambda * dt)."""
        if node_id not in self.nodes:
            return 0.0
        
        now = current_time or time.time()
        node_ts = self.nodes[node_id]["timestamp"]
        dt = max(0.0, now - node_ts)
        decay_score = math.exp(-self.decay_lambda * dt)
        return round(decay_score, 4)

    def query_entity_history(self, entity_id: str) -> List[Dict[str, Any]]:
        """Queries timeline history for a specific entity sorted by timestamp."""
        entity_nodes = [
            node for node in self.nodes.values()
            if node["entity_id"] == entity_id
        ]
        entity_nodes.sort(key=lambda x: x["timestamp"])
        
        now = time.time()
        for node in entity_nodes:
            node["temporal_relevance"] = self.calculate_temporal_relevance(node["id"], now)
            
        return entity_nodes

    def extract_user_preference_node(self, category: str, preference_key: str, preference_value: Any) -> str:
        """Extracts and stores user preference or coding habit into preference graph (AST-01)."""
        entity_id = f"pref:{category}:{preference_key}"
        return self.add_event(
            entity_id=entity_id,
            entity_type="user_preference",
            state={"category": category, "key": preference_key, "value": preference_value}
        )

# Global Temporal Memory Graph Instance
temporal_graph = TemporalMemoryGraph()

def capture_voice_thought(transcript: str, tags: Optional[List[str]] = None) -> Dict[str, Any]:
    """BUTLER-25: Captures instant voice thought, auto-tags keywords, and indexes in temporal graph."""
    if not transcript:
        return {"status": "error", "message": "Transcript cannot be empty."}

    # Simple auto-tagging heuristic
    words = [w.strip("#,.!?").lower() for w in transcript.split() if len(w) > 4]
    extracted_tags = tags or list(set(words[:4]))

    entity_id = f"thought:{int(time.time())}"
    node_id = temporal_graph.add_event(
        entity_id=entity_id,
        entity_type="voice_thought",
        state={
            "transcript": transcript,
            "tags": extracted_tags,
            "captured_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    )

    return {
        "status": "success",
        "node_id": node_id,
        "transcript": transcript,
        "tags": extracted_tags,
        "message": f"Voice thought captured and tagged: [{', '.join(extracted_tags)}]"
    }

def query_voice_thoughts(query_tag: str = "") -> List[Dict[str, Any]]:
    """BUTLER-25: Queries captured voice thoughts with temporal decay relevance scoring."""
    now = time.time()
    results = []
    for node_id, node in temporal_graph.nodes.items():
        if node.get("type") == "voice_thought":
            state = node.get("state", {})
            tags = state.get("tags", [])
            if not query_tag or any(query_tag.lower() in t.lower() for t in tags) or query_tag.lower() in state.get("transcript", "").lower():
                item = dict(state)
                item["node_id"] = node_id
                item["temporal_relevance"] = temporal_graph.calculate_temporal_relevance(node_id, now)
                results.append(item)

    results.sort(key=lambda x: x["temporal_relevance"], reverse=True)
    return results

