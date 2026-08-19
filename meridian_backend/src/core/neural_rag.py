"""
neural_rag.py — JARVIS-09 Subconscious Codebase Memory & Neural RAG Synthesizer
Background AST semantic synthesizer building real-time project intent knowledge graphs.
"""

import os
import time
import math
from typing import Dict, Any, List, Optional
from src.core.code_graph import parse_python_ast, search_codebase_symbols


class NeuralRAGSynthesizer:
    """
    Subconscious background AST semantic synthesizer.
    Indexes symbols, docstrings, and module responsibilities to construct
    a real-time project intent graph for zero-latency neural RAG queries.
    """

    def __init__(self, workspace_dir: Optional[str] = None):
        from src.core.history_manager import find_workspace_root
        self.workspace_dir = workspace_dir or find_workspace_root()
        self.intent_nodes: List[Dict[str, Any]] = []
        self.intent_links: List[Dict[str, Any]] = []
        self.last_indexed_time: float = 0.0

    def build_intent_graph(self) -> Dict[str, Any]:
        """
        Scans workspace AST symbols and constructs semantic intent concepts & relationships.
        """
        start_time = time.time()
        nodes = []
        links = []
        concept_map: Dict[str, List[str]] = {}

        exclude_dirs = {"venv", ".venv", "env", "node_modules", ".git", "build", "dist", "__pycache__"}

        for root, dirs, files in os.walk(self.workspace_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.workspace_dir).replace("\\", "/")

                    ast_data = parse_python_ast(full_path)
                    for sym in ast_data["symbols"]:
                        node_id = f"{rel_path}::{sym['name']}"
                        domain = rel_path.split("/")[1] if "/" in rel_path else "root"

                        nodes.append({
                            "id": node_id,
                            "name": sym["name"],
                            "kind": sym["kind"],
                            "domain": domain,
                            "file": rel_path,
                            "docstring": sym["docstring"][:120] if sym["docstring"] else ""
                        })

                        if domain not in concept_map:
                            concept_map[domain] = []
                        concept_map[domain].append(node_id)

        # Build links between symbols in same domain
        for domain, node_ids in concept_map.items():
            for i in range(min(len(node_ids) - 1, 10)):
                links.append({
                    "source": node_ids[i],
                    "target": node_ids[i + 1],
                    "relation": "co_located_intent"
                })

        self.intent_nodes = nodes
        self.intent_links = links
        self.last_indexed_time = time.time()

        return {
            "status": "success",
            "nodes_count": len(nodes),
            "links_count": len(links),
            "build_time_sec": round(time.time() - start_time, 3),
            "nodes": nodes,
            "links": links
        }

    def query_intent(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Performs semantic intent lookup across indexed project intent graph.
        """
        if not self.intent_nodes:
            self.build_intent_graph()

        query_terms = [t.lower() for t in query.split() if len(t) > 2]
        scored_nodes = []

        for node in self.intent_nodes:
            score = 0.0
            name_lower = node["name"].lower()
            doc_lower = node["docstring"].lower()
            file_lower = node["file"].lower()

            for term in query_terms:
                if term in name_lower:
                    score += 3.0
                if term in doc_lower:
                    score += 1.5
                if term in file_lower:
                    score += 1.0

            if score > 0:
                scored_nodes.append((score, node))

        scored_nodes.sort(key=lambda x: x[0], reverse=True)
        return [node for _, node in scored_nodes[:top_k]]

    def get_intent_graph(self) -> Dict[str, Any]:
        """Returns active project intent graph."""
        if not self.intent_nodes:
            self.build_intent_graph()

        return {
            "nodes": self.intent_nodes,
            "links": self.intent_links,
            "last_indexed_time": self.last_indexed_time
        }


# Global Neural RAG singleton
_neural_rag_instance: Optional[NeuralRAGSynthesizer] = None


def get_neural_rag_synthesizer() -> NeuralRAGSynthesizer:
    global _neural_rag_instance
    if _neural_rag_instance is None:
        _neural_rag_instance = NeuralRAGSynthesizer()
    return _neural_rag_instance
