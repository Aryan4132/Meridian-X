"""
rag_optimizer.py — RAG Pipeline Context & Reranking Optimizer (BK-24)
Performs hybrid search relevance scoring, document reranking, noise reduction, and token context budgeting.
"""

import math
import re
from typing import Dict, Any, List, Optional


class RAGContextOptimizer:
    """Optimizes RAG retrieval context via hybrid BM25 vector scoring and noise trimming."""

    def __init__(self, min_relevance_threshold: float = 0.25, default_top_k: int = 5):
        self.min_relevance_threshold = min_relevance_threshold
        self.default_top_k = default_top_k

    def _calculate_bm25_score(self, query: str, document: str) -> float:
        """Calculates lightweight BM25 TF-IDF relevance score between query and document."""
        query_terms = set(re.findall(r'\w+', query.lower()))
        doc_terms = re.findall(r'\w+', document.lower())
        
        if not doc_terms or not query_terms:
            return 0.0

        doc_len = len(doc_terms)
        score = 0.0
        for term in query_terms:
            tf = doc_terms.count(term)
            if tf > 0:
                # Term frequency scaling with length normalization
                idf = math.log(1 + 1.0 / (tf + 0.5))
                score += (tf * (1.5 + 1)) / (tf + 1.5 * (1 - 0.75 + 0.75 * (doc_len / 100.0))) * idf

        return round(score, 4)

    def rerank_and_optimize(
        self,
        query: str,
        documents: List[Dict[str, Any]],
        vector_scores: Optional[List[float]] = None,
        top_k: Optional[int] = None,
        max_token_budget: Optional[int] = 4000
    ) -> List[Dict[str, Any]]:
        """
        Reranks retrieved documents combining dense vector scores and sparse BM25 scores.
        Filters noise below threshold and enforces max token budget.
        """
        k = top_k or self.default_top_k
        results = []

        for idx, doc in enumerate(documents):
            content = doc.get("content", doc.get("text", str(doc)))
            sparse_score = self._calculate_bm25_score(query, content)
            dense_score = vector_scores[idx] if vector_scores and idx < len(vector_scores) else 0.5

            # Hybrid score combination
            hybrid_score = round(0.6 * dense_score + 0.4 * sparse_score, 4)

            if hybrid_score >= self.min_relevance_threshold:
                results.append({
                    "document": doc,
                    "hybrid_score": hybrid_score,
                    "sparse_score": sparse_score,
                    "dense_score": dense_score,
                    "estimated_tokens": len(content.split()) * 1.3
                })

        # Sort descending by hybrid relevance score
        results.sort(key=lambda x: x["hybrid_score"], reverse=True)

        # Apply top_k and token budget ceiling
        final_docs = []
        accumulated_tokens = 0

        for res in results[:k]:
            tokens = res["estimated_tokens"]
            if max_token_budget and (accumulated_tokens + tokens > max_token_budget):
                break
            final_docs.append(res)
            accumulated_tokens += tokens

        return final_docs
