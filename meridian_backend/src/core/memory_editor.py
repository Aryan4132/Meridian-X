"""
memory_editor.py — Agent Memory Management & Editing Engine (TRUST-01)
Provides structured access, search, modification, deletion ("forgetting"), and JSON export of agent memories.
"""

import time
import json
from typing import Dict, Any, List, Optional
import database
from src.core.temporal_memory import TemporalMemoryGraph


class MemoryEditor:
    """Core memory engine allowing users to view, search, edit, forget, and export agent memories."""

    def __init__(self, temporal_graph: Optional[TemporalMemoryGraph] = None):
        self.temporal_graph = temporal_graph or TemporalMemoryGraph()

    def get_all_memories(self, query: Optional[str] = None, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns all aggregated memory items (preferences, facts, temporal nodes, journals) matching optional filter."""
        memories: List[Dict[str, Any]] = []

        # 1. User Preferences from database
        try:
            prefs = database.get_user_profile()
            for key, val in prefs.items():
                if category and category.lower() not in ["preference", "user_preference"]:
                    continue
                item = {
                    "id": f"pref:{key}",
                    "type": "user_preference",
                    "category": "preference",
                    "key": key,
                    "value": val,
                    "source": "database_user_profile",
                    "timestamp": time.time(),
                }
                memories.append(item)
        except Exception as e:
            print(f"[MemoryEditor] Failed to fetch preferences: {e}")

        # 2. Temporal Memory Graph Nodes
        try:
            now = time.time()
            for node_id, node in self.temporal_graph.nodes.items():
                if category and category.lower() not in [node.get("type", "").lower(), "temporal"]:
                    continue
                score = self.temporal_graph.calculate_temporal_relevance(node_id, now)
                item = {
                    "id": node_id,
                    "type": node.get("type", "temporal_node"),
                    "category": "temporal",
                    "entity_id": node.get("entity_id"),
                    "state": node.get("state"),
                    "timestamp": node.get("timestamp"),
                    "created_at": node.get("created_at"),
                    "temporal_relevance": score,
                    "source": "temporal_memory_graph",
                }
                memories.append(item)
        except Exception as e:
            print(f"[MemoryEditor] Failed to fetch temporal graph nodes: {e}")

        # 3. Daily Journals
        try:
            db = database.get_mongo_db()
            if db is not None:
                journals = list(db["daily_journals"].find({}, {"_id": 0}).limit(30))
                for j in journals:
                    if category and category.lower() not in ["journal", "daily_journal"]:
                        continue
                    memories.append({
                        "id": f"journal:{j.get('date')}",
                        "type": "daily_journal",
                        "category": "journal",
                        "date": j.get("date"),
                        "summary": j.get("summary"),
                        "key_decisions": j.get("key_decisions", []),
                        "timestamp": j.get("created_at", time.time()),
                        "source": "daily_journals",
                    })
        except Exception as e:
            print(f"[MemoryEditor] Failed to fetch journals: {e}")

        # Search Query Filtering
        if query and query.strip():
            q_clean = query.strip().lower()
            filtered = []
            for mem in memories:
                dumped = json.dumps(mem, default=str).lower()
                if q_clean in dumped:
                    filtered.append(mem)
            return filtered

        return memories

    def update_memory_entry(self, entry_id: str, new_value: Any) -> bool:
        """Updates specific memory entry state or preference value."""
        if not entry_id:
            return False

        # If User Preference
        if entry_id.startswith("pref:"):
            key = entry_id.split("pref:", 1)[1]
            try:
                database.save_user_preference(key, str(new_value))
                return True
            except Exception as e:
                print(f"[MemoryEditor] Failed updating preference '{key}': {e}")
                return False

        # If Temporal Node
        if entry_id in self.temporal_graph.nodes:
            try:
                if isinstance(new_value, dict):
                    self.temporal_graph.nodes[entry_id]["state"] = new_value
                else:
                    self.temporal_graph.nodes[entry_id]["state"] = {"value": new_value}
                return True
            except Exception as e:
                print(f"[MemoryEditor] Failed updating temporal node '{entry_id}': {e}")
                return False

        return False

    def forget_entity(self, entity_id: str) -> int:
        """Forgets/deletes all memory entries associated with an entity ID or key."""
        deleted_count = 0

        # Remove from user preferences if matching key
        if entity_id.startswith("pref:"):
            key = entity_id.split("pref:", 1)[1]
        else:
            key = entity_id

        try:
            conn = database.get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user_profile WHERE key = ?", (key,))
            deleted_count += cursor.rowcount
            conn.commit()
        except Exception as e:
            print(f"[MemoryEditor] SQLite preference delete failed: {e}")

        # Remove from temporal memory graph
        to_delete_nodes = [
            nid for nid, node in self.temporal_graph.nodes.items()
            if node.get("entity_id") == entity_id or node.get("id") == entity_id or nid == entity_id
        ]
        for nid in to_delete_nodes:
            del self.temporal_graph.nodes[nid]
            deleted_count += 1

        # Remove edges pointing to/from deleted nodes
        self.temporal_graph.edges = [
            edge for edge in self.temporal_graph.edges
            if edge.get("source") not in to_delete_nodes and edge.get("target") not in to_delete_nodes
        ]

        return deleted_count

    def export_memory_json(self) -> Dict[str, Any]:
        """Exports complete agent memory state as a structured JSON object."""
        return {
            "version": "1.0",
            "exported_at": time.time(),
            "exported_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "preferences": database.get_user_profile(),
            "temporal_nodes": list(self.temporal_graph.nodes.values()),
            "temporal_edges": self.temporal_graph.edges,
            "all_memories_flat": self.get_all_memories(),
        }
