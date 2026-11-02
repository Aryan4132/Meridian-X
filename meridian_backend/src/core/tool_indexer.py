"""
tool_indexer.py — Semantic & Inverted Index Tool Retrieval Engine
Extracts tokenized capabilities from all tools in TOOL_REGISTRY and
dynamically scores and retrieves the most relevant tools for a given user prompt.
"""

import re
import math
from typing import Dict, List, Set, Any, Optional

STOPWORDS = {
    "a", "about", "above", "after", "again", "all", "am", "an", "and", "any", "are",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
    "but", "by", "can", "did", "do", "does", "doing", "don", "down", "during", "each",
    "few", "for", "from", "further", "had", "has", "have", "having", "he", "her", "here",
    "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is",
    "it", "its", "itself", "just", "me", "more", "most", "my", "myself", "no", "nor",
    "not", "now", "of", "off", "on", "once", "only", "or", "other", "our", "ours",
    "ourselves", "out", "over", "own", "same", "she", "should", "so", "some", "such",
    "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there",
    "these", "they", "this", "those", "through", "to", "too", "under", "until", "up",
    "very", "was", "we", "were", "what", "when", "where", "which", "while", "who",
    "whom", "why", "will", "with", "you", "your", "yours", "yourself", "yourselves"
}

_TOOL_INDEX_CACHE: Optional[Dict[str, Dict[str, Any]]] = None
_CACHE_REGISTRY_SIZE: int = 0


def tokenize(text: str) -> List[str]:
    """Tokenize camelCase, snake_case, and prose into clean alphanumeric stems."""
    if not text:
        return []

    # Split camelCase / PascalCase
    s1 = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', text)
    # Split snake_case and non-alphanumeric
    words = re.findall(r'[a-zA-Z0-9]+', s1.lower())

    tokens = []
    for w in words:
        if len(w) <= 1 or w in STOPWORDS:
            continue
        # Basic suffix normalization
        if w.endswith("ies") and len(w) > 4:
            w = w[:-3] + "y"
        elif w.endswith("es") and len(w) > 4:
            w = w[:-2]
        elif w.endswith("s") and not w.endswith("ss") and len(w) > 3:
            w = w[:-1]
        elif w.endswith("ing") and len(w) > 5:
            w = w[:-3]
        tokens.append(w)
    return tokens


def build_tool_index(force_refresh: bool = False) -> Dict[str, Dict[str, Any]]:
    """Builds token inverted index across TOOL_REGISTRY."""
    global _TOOL_INDEX_CACHE, _CACHE_REGISTRY_SIZE
    from src.tools.registry import TOOL_REGISTRY

    current_size = len(TOOL_REGISTRY)
    if not force_refresh and _TOOL_INDEX_CACHE is not None and current_size == _CACHE_REGISTRY_SIZE:
        return _TOOL_INDEX_CACHE

    index: Dict[str, Dict[str, Any]] = {}
    for name, meta in TOOL_REGISTRY.items():
        name_tokens = set(tokenize(name))
        desc = meta.get("description", "")
        desc_tokens = set(tokenize(desc))

        func = meta.get("func")
        doc = getattr(func, "__doc__", "") or ""
        doc_tokens = set(tokenize(doc))

        index[name] = {
            "tier": meta.get("tier", 1),
            "name_tokens": name_tokens,
            "desc_tokens": desc_tokens,
            "doc_tokens": doc_tokens,
            "all_tokens": name_tokens | desc_tokens | doc_tokens
        }

    _TOOL_INDEX_CACHE = index
    _CACHE_REGISTRY_SIZE = current_size
    return index


def find_relevant_tools(prompt: str, top_k: int = 6, min_score: float = 1.5) -> List[str]:
    """
    Ranks and retrieves the top-k most relevant tools for a prompt based on token similarity.
    Weights: name token match = 3.5, description token match = 2.0, docstring = 1.0.
    """
    if not prompt or not prompt.strip():
        return []

    index = build_tool_index()
    prompt_tokens = tokenize(prompt)
    if not prompt_tokens:
        return []

    scores: Dict[str, float] = {}

    for name, data in index.items():
        score = 0.0
        # Exact substring match in prompt gives instant bonus
        if name in prompt:
            score += 10.0

        for pt in prompt_tokens:
            if pt in data["name_tokens"]:
                score += 3.5
            if pt in data["desc_tokens"]:
                score += 2.0
            elif pt in data["doc_tokens"]:
                score += 1.0

        if score >= min_score:
            scores[name] = score

    # Sort descending by score
    sorted_tools = sorted(scores.keys(), key=lambda t: scores[t], reverse=True)
    return sorted_tools[:top_k]

