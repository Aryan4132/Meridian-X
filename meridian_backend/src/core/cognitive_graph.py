"""
cognitive_graph.py — Unified Cognitive Graph Memory System
Replaces siloed vector RAG with a multi-hop, relational knowledge graph
linking code symbols, API routes, user memories, and task execution history.
"""

import os
import time
import json
import sqlite3
import logging
from typing import Dict, List, Any, Optional, Set, Tuple

logger = logging.getLogger("cognitive_graph")

DEFAULT_DB_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "meridian_data", "cognitive_graph.db"
)


class UnifiedCognitiveGraph:
    """
    Unified Cognitive Graph (🕸️)
    Stores interconnected entities, code AST symbols, API endpoints, memories, and actions
    with multi-hop associative traversal and prompt enrichment.
    """

    def __init__(self, db_path: Optional[str] = None):
        if not db_path:
            db_path = os.getenv("COGNITIVE_GRAPH_DB_PATH", DEFAULT_DB_PATH)
        self.db_path = os.path.abspath(db_path)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=10.0)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA busy_timeout = 5000;")
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def _init_db(self) -> None:
        """Initializes tables, FTS5 virtual table, triggers, and indexes."""
        with self._get_connection() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS cognitive_nodes (
                    id TEXT PRIMARY KEY,
                    type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    metadata TEXT,
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_cog_nodes_type ON cognitive_nodes(type);
                CREATE INDEX IF NOT EXISTS idx_cog_nodes_name ON cognitive_nodes(name);

                CREATE TABLE IF NOT EXISTS cognitive_edges (
                    id TEXT PRIMARY KEY,
                    source TEXT NOT NULL,
                    target TEXT NOT NULL,
                    relation TEXT NOT NULL,
                    weight REAL DEFAULT 1.0,
                    metadata TEXT,
                    timestamp REAL NOT NULL,
                    FOREIGN KEY(source) REFERENCES cognitive_nodes(id) ON DELETE CASCADE,
                    FOREIGN KEY(target) REFERENCES cognitive_nodes(id) ON DELETE CASCADE
                );
                CREATE INDEX IF NOT EXISTS idx_cog_edges_src ON cognitive_edges(source);
                CREATE INDEX IF NOT EXISTS idx_cog_edges_tgt ON cognitive_edges(target);
                CREATE INDEX IF NOT EXISTS idx_cog_edges_rel ON cognitive_edges(relation);

                CREATE VIRTUAL TABLE IF NOT EXISTS cognitive_nodes_fts USING fts5(
                    id UNINDEXED,
                    name,
                    content,
                    tokenize='porter unicode61'
                );

                CREATE TRIGGER IF NOT EXISTS trg_cog_nodes_ai AFTER INSERT ON cognitive_nodes BEGIN
                    INSERT INTO cognitive_nodes_fts(id, name, content)
                    VALUES (new.id, new.name, coalesce(new.metadata, ''));
                END;

                CREATE TRIGGER IF NOT EXISTS trg_cog_nodes_ad AFTER DELETE ON cognitive_nodes BEGIN
                    DELETE FROM cognitive_nodes_fts WHERE id = old.id;
                END;

                CREATE TRIGGER IF NOT EXISTS trg_cog_nodes_au AFTER UPDATE ON cognitive_nodes BEGIN
                    DELETE FROM cognitive_nodes_fts WHERE id = old.id;
                    INSERT INTO cognitive_nodes_fts(id, name, content)
                    VALUES (new.id, new.name, coalesce(new.metadata, ''));
                END;
            """)

    def add_node(
        self,
        node_id: str,
        node_type: str,
        name: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Upserts a node into the cognitive graph."""
        now = time.time()
        meta_str = json.dumps(metadata or {})
        with self._get_connection() as conn:
            conn.execute(
                """
                INSERT INTO cognitive_nodes (id, type, name, metadata, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    type=excluded.type,
                    name=excluded.name,
                    metadata=excluded.metadata,
                    updated_at=excluded.updated_at
                """,
                (node_id, node_type, name, meta_str, now, now)
            )
        return {"id": node_id, "type": node_type, "name": name, "metadata": metadata or {}}

    def add_edge(
        self,
        source: str,
        target: str,
        relation: str,
        weight: float = 1.0,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Creates or strengthens an edge between two existing nodes."""
        edge_id = f"{source}->{relation}->{target}"
        now = time.time()
        meta_str = json.dumps(metadata or {})
        with self._get_connection() as conn:
            # Check source and target exist
            conn.execute(
                """
                INSERT INTO cognitive_edges (id, source, target, relation, weight, metadata, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    weight=cognitive_edges.weight + ?,
                    metadata=excluded.metadata,
                    timestamp=excluded.timestamp
                """,
                (edge_id, source, target, relation, weight, meta_str, now, weight)
            )
        return {
            "id": edge_id,
            "source": source,
            "target": target,
            "relation": relation,
            "weight": weight
        }

    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Fetches a node by ID."""
        with self._get_connection() as conn:
            row = conn.execute("SELECT * FROM cognitive_nodes WHERE id = ?", (node_id,)).fetchone()
            if not row:
                return None
            return {
                "id": row["id"],
                "type": row["type"],
                "name": row["name"],
                "metadata": json.loads(row["metadata"] or "{}"),
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }

    def get_neighbors(
        self,
        node_id: str,
        direction: str = "both",
        relation_filter: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Returns direct neighbors connected to node_id."""
        results = []
        with self._get_connection() as conn:
            query_out = """
                SELECT e.relation, e.weight, n.* FROM cognitive_edges e
                JOIN cognitive_nodes n ON e.target = n.id
                WHERE e.source = ?
            """
            query_in = """
                SELECT e.relation, e.weight, n.* FROM cognitive_edges e
                JOIN cognitive_nodes n ON e.source = n.id
                WHERE e.target = ?
            """
            
            if direction in ("out", "both"):
                for row in conn.execute(query_out, (node_id,)).fetchall():
                    if not relation_filter or row["relation"] in relation_filter:
                        results.append({
                            "direction": "out",
                            "relation": row["relation"],
                            "weight": row["weight"],
                            "node": {
                                "id": row["id"],
                                "type": row["type"],
                                "name": row["name"],
                                "metadata": json.loads(row["metadata"] or "{}")
                            }
                        })

            if direction in ("in", "both"):
                for row in conn.execute(query_in, (node_id,)).fetchall():
                    if not relation_filter or row["relation"] in relation_filter:
                        results.append({
                            "direction": "in",
                            "relation": row["relation"],
                            "weight": row["weight"],
                            "node": {
                                "id": row["id"],
                                "type": row["type"],
                                "name": row["name"],
                                "metadata": json.loads(row["metadata"] or "{}")
                            }
                        })
        return results

    def traverse(
        self,
        start_node_id: str,
        max_hops: int = 2,
        relation_filter: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Executes Breadth-First Search (BFS) graph traversal out to max_hops.
        Returns connected subgraph with nodes, edges, and hop distances.
        """
        start = self.get_node(start_node_id)
        if not start:
            return {"start_node": None, "nodes": [], "edges": [], "hops": 0}

        visited_nodes: Dict[str, Dict[str, Any]] = {start_node_id: {**start, "hop": 0}}
        discovered_edges: List[Dict[str, Any]] = []
        queue: List[Tuple[str, int]] = [(start_node_id, 0)]

        while queue:
            curr_id, curr_hop = queue.pop(0)
            if curr_hop >= max_hops:
                continue

            neighbors = self.get_neighbors(curr_id, direction="both", relation_filter=relation_filter)
            for item in neighbors:
                n = item["node"]
                nid = n["id"]
                discovered_edges.append({
                    "source": curr_id if item["direction"] == "out" else nid,
                    "target": nid if item["direction"] == "out" else curr_id,
                    "relation": item["relation"],
                    "weight": item["weight"]
                })
                if nid not in visited_nodes:
                    visited_nodes[nid] = {**n, "hop": curr_hop + 1}
                    queue.append((nid, curr_hop + 1))

        return {
            "start_node": start,
            "nodes": list(visited_nodes.values()),
            "edges": discovered_edges,
            "total_nodes": len(visited_nodes),
            "total_edges": len(discovered_edges)
        }

    def find_nodes(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Fuzzy/keyword match for nodes by id, name, or metadata."""
        q = f"%{query.strip().lower()}%"
        matches = []
        with self._get_connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM cognitive_nodes
                WHERE lower(id) LIKE ? OR lower(name) LIKE ? OR lower(metadata) LIKE ?
                ORDER BY updated_at DESC LIMIT ?
                """,
                (q, q, q, limit)
            ).fetchall()
            for r in rows:
                matches.append({
                    "id": r["id"],
                    "type": r["type"],
                    "name": r["name"],
                    "metadata": json.loads(r["metadata"] or "{}")
                })
        return matches

    def auto_link_endpoints(self) -> int:
        """
        Scans registered routes and standard components, linking API endpoints
        to backend core handlers and frontend consumers.
        """
        links_created = 0
        endpoints = [
            ("api:/api/chat/stream", "FastAPI Chat Stream Endpoint", "backend_route"),
            ("api:/api/voice/interrupt", "Voice Interrupt Endpoint", "backend_route"),
            ("api:/api/action/undo", "Action Undo Endpoint", "backend_route"),
            ("api:/api/guard/resources", "System Resource Guard Endpoint", "backend_route"),
            ("api:/api/context/scan", "Deep Context Scan Endpoint", "backend_route"),
            ("code:meridian_backend/src/core/loop.py", "Core Agent Loop Engine", "core_backend"),
            ("code:meridian_backend/src/core/workspace_orchestrator.py", "Multi-App Orchestrator", "core_backend"),
            ("code:meridian_backend/src/core/proactive_system_guard.py", "Resource Guard Sentinel", "core_backend"),
            ("code:meridian_frontend/src/views/Timeline.tsx", "Interactive Timeline HUD", "frontend_view"),
            ("code:meridian_frontend/src/Mascot.tsx", "Desktop Voice Companion", "frontend_mascot")
        ]

        for nid, name, ntype in endpoints:
            self.add_node(nid, ntype, name)

        # Wire inter-system edges
        edges = [
            ("code:meridian_frontend/src/views/Timeline.tsx", "api:/api/chat/stream", "calls"),
            ("code:meridian_frontend/src/Mascot.tsx", "api:/api/chat/stream", "calls"),
            ("code:meridian_frontend/src/views/Timeline.tsx", "api:/api/action/undo", "calls"),
            ("api:/api/chat/stream", "code:meridian_backend/src/core/loop.py", "invokes"),
            ("api:/api/guard/resources", "code:meridian_backend/src/core/proactive_system_guard.py", "queries")
        ]

        for src, tgt, rel in edges:
            self.add_edge(src, tgt, rel)
            links_created += 1

        return links_created

    def get_unified_context(self, query: str, max_hops: int = 2) -> str:
        """
        Given a user prompt or topic, finds relevant graph nodes, traverses their
        multi-hop neighborhood, and formats an interconnected relationship block for prompt injection.
        """
        words = [w for w in query.replace("?", " ").replace(".", " ").split() if len(w) >= 3]
        matched_nodes = []
        for word in words[:4]:
            found = self.find_nodes(word, limit=2)
            for fn in found:
                if not any(m["id"] == fn["id"] for m in matched_nodes):
                    matched_nodes.append(fn)

        if not matched_nodes:
            # Fallback to key system nodes if no explicit keyword hit
            matched_nodes = self.find_nodes("loop", limit=1)

        if not matched_nodes:
            return ""

        context_lines = [
            "════════════════════════════════════════════",
            "COGNITIVE GRAPH — Interconnected System Map",
            "════════════════════════════════════════════"
        ]

        seen_edges = set()
        for root in matched_nodes[:2]:
            subgraph = self.traverse(root["id"], max_hops=max_hops)
            for edge in subgraph.get("edges", [])[:8]:
                edge_sig = (edge["source"], edge["relation"], edge["target"])
                if edge_sig not in seen_edges:
                    seen_edges.add(edge_sig)
                    context_lines.append(f"• [{edge['source']}] ──({edge['relation']})──> [{edge['target']}]")

        if len(context_lines) <= 3:
            return ""

        context_lines.append("════════════════════════════════════════════\n")
        return "\n".join(context_lines)

    def fts_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Performs full-text keyword search across cognitive nodes via FTS5."""
        clean_q = "".join(c if c.isalnum() or c.isspace() else " " for c in query).strip()
        if not clean_q:
            return []
        tokens = [f'"{w}"*' for w in clean_q.split() if len(w) > 1]
        if not tokens:
            tokens = [f'"{w}"*' for w in clean_q.split()]
        if not tokens:
            return []
        match_expr = " AND ".join(tokens)
        
        results = []
        with self._get_connection() as conn:
            try:
                rows = conn.execute(
                    """
                    SELECT n.*, bm25(cognitive_nodes_fts) as rank
                    FROM cognitive_nodes_fts f
                    JOIN cognitive_nodes n ON f.id = n.id
                    WHERE cognitive_nodes_fts MATCH ?
                    ORDER BY rank ASC
                    LIMIT ?
                    """,
                    (match_expr, limit)
                ).fetchall()
                for row in rows:
                    results.append({
                        "id": row["id"],
                        "type": row["type"],
                        "name": row["name"],
                        "metadata": json.loads(row["metadata"] or "{}"),
                        "created_at": row["created_at"],
                        "updated_at": row["updated_at"],
                        "rank": row["rank"]
                    })
            except Exception as e:
                logger.warning(f"FTS5 search error: {e}")
                rows = conn.execute(
                    "SELECT * FROM cognitive_nodes WHERE name LIKE ? LIMIT ?",
                    (f"%{clean_q}%", limit)
                ).fetchall()
                for row in rows:
                    results.append({
                        "id": row["id"],
                        "type": row["type"],
                        "name": row["name"],
                        "metadata": json.loads(row["metadata"] or "{}"),
                        "created_at": row["created_at"],
                        "updated_at": row["updated_at"]
                    })
        return results

    def compute_decayed_weight(
        self,
        base_weight: float,
        timestamp: float,
        node_type: str = "default",
        half_life_days: float = 14.0
    ) -> float:
        """Applies exponential time decay to edge/node weights so transient items fade."""
        import math
        # Architecture symbols, code AST, and backend routes never decay
        if node_type in ("ast_symbol", "backend_route", "frontend_route", "schema"):
            return base_weight
        # Tasks decay faster (3 days half-life)
        if node_type in ("task_outcome", "transient_action", "execution_log"):
            half_life_days = 3.0
            
        elapsed_seconds = max(0.0, time.time() - timestamp)
        half_life_seconds = half_life_days * 86400.0
        decay = math.pow(0.5, elapsed_seconds / half_life_seconds)
        return round(base_weight * decay, 4)



# Module-level singleton
_GRAPH_INSTANCE: Optional[UnifiedCognitiveGraph] = None

def get_cognitive_graph() -> UnifiedCognitiveGraph:
    """Returns initialized singleton UnifiedCognitiveGraph instance."""
    global _GRAPH_INSTANCE
    if _GRAPH_INSTANCE is None:
        _GRAPH_INSTANCE = UnifiedCognitiveGraph()
        # Seed core links on first boot
        try:
            _GRAPH_INSTANCE.auto_link_endpoints()
        except Exception as e:
            import logging
            logging.getLogger("meridian.cognitive_graph").warning(f"Initial endpoint auto-link non-fatal error: {e}")
    return _GRAPH_INSTANCE
