import pytest
import sqlite3
from src.db.rag import compute_bm25_scores, hybrid_search_knowledge_base
from database import hybrid_search_knowledge_base as facade_hybrid_search

def test_compute_bm25_scores():
    docs = [
        {"id": 1, "content": "FastAPI python backend server for Meridian-X"},
        {"id": 2, "content": "React TypeScript frontend user interface"},
        {"id": 3, "content": "Turbovec vector database and hybrid search"}
    ]
    scores = compute_bm25_scores("Turbovec vector", docs)
    assert 3 in scores
    assert scores[3] > 0
    # Doc 3 should have highest score for query 'Turbovec vector'
    best_id = max(scores, key=lambda k: scores[k])
    assert best_id == 3

def test_hybrid_search_knowledge_base_fallback_and_ranking(monkeypatch):
    test_docs = [
        {"id": 10, "source": "guide.md", "chunk_text": "OAuth authentication flow and token refresh", "metadata": {}},
        {"id": 11, "source": "api.md", "chunk_text": "Endpoint for user login and JWT generation", "metadata": {}},
        {"id": 12, "source": "tools.md", "chunk_text": "Playwright browser automation click and type", "metadata": {}}
    ]

    # Mock get_sqlite_conn to return mock rows
    class MockCursor:
        def execute(self, query, params=None):
            pass
        def fetchone(self):
            return (len(test_docs),)
        def fetchall(self):
            return test_docs

    class MockConn:
        def cursor(self):
            return MockCursor()
        def close(self):
            pass

    monkeypatch.setattr("src.db.rag.get_sqlite_conn", lambda: MockConn())
    
    # Query for exact keyword 'Playwright'
    results = hybrid_search_knowledge_base("Playwright browser", limit=2)
    assert len(results) > 0
    assert results[0]["source"] == "tools.md"
    assert "Playwright" in results[0]["chunk_text"]
    assert "score" in results[0]

def test_facade_re_export():
    assert callable(facade_hybrid_search)
