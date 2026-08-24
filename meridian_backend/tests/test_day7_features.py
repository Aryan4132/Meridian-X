import os
import sys
import pytest
import json
import numpy as np

# Ensure backend root is on Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import get_embedding, _get_fallback_embedding, _get_openai_embedding
from src.core.doc_indexer import _extract_ast_chunks, compute_bm25_scores, search_offline_docs, index_docs_directory
from src.tools.documents import _extract_pdf_layout_and_tables, read_document_text, create_pdf_document
from src.core.llm_provider import get_api_key, call_llm_sync
from src.core.vault import vault_set, vault_get


def test_multi_provider_embeddings():
    """Verify get_embedding and fallback vector generation."""
    text = "Autonomous AI Agent Meridian-X"
    vec = get_embedding(text)
    assert vec is not None
    assert isinstance(vec, list)
    assert len(vec) == 768
    assert any(x != 0 for x in vec)

    # Test fallback vector generator directly
    fallback_vec = _get_fallback_embedding("Test Fallback Query")
    assert len(fallback_vec) == 768
    norm = np.linalg.norm(np.array(fallback_vec))
    assert abs(norm - 1.0) < 1e-4


def test_ast_code_chunking():
    """Verify AST function/class extraction from Python source."""
    sample_code = '''
class MemoryManager:
    """Manages local vector memory."""
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def search(self, query: str):
        return []

def global_helper():
    return 42
'''
    chunks = _extract_ast_chunks(sample_code)
    assert len(chunks) >= 3
    section_names = [c[0] for c in chunks]
    assert any("Class: MemoryManager" in s for s in section_names)
    assert any("Function: __init__" in s or "Function: search" in s or "Function: global_helper" in s for s in section_names)


def test_bm25_and_hybrid_search(tmp_path):
    """Verify BM25 keyword matching and hybrid RRF search."""
    docs = [
        {"id": 1, "content": "FastAPI async core backend server for Meridian-X"},
        {"id": 2, "content": "React 19 TypeScript desktop UI powered by Tauri v2"},
        {"id": 3, "content": "Turbovec local vector RAG database with SQLite WAL"}
    ]
    bm25_scores = compute_bm25_scores("Tauri desktop UI", docs)
    assert 2 in bm25_scores
    assert bm25_scores[2] > bm25_scores.get(1, 0)

    # Test indexing directory with md and py files
    doc_dir = tmp_path / "docs"
    doc_dir.mkdir()
    (doc_dir / "guide.md").write_text("# Overview\nMeridian-X is an autonomous desktop companion.", encoding="utf-8")
    (doc_dir / "service.py").write_text("def run_agent():\n    return 'Running'", encoding="utf-8")

    index_docs_directory(str(doc_dir))
    results = search_offline_docs("autonomous desktop", limit=5)
    assert isinstance(results, list)


def test_pure_python_pdf_table_parser(tmp_path):
    """Verify PDF layout and table extraction."""
    pytest.importorskip("pypdf")
    pdf_path = str(tmp_path / "sample.pdf")
    markdown_content = "# System Report\n\n| Component | Status |\n| Engine | Active |\n| Vector | Ready |"
    
    create_pdf_document(pdf_path, markdown_content)
    assert os.path.exists(pdf_path)

    extracted_text = read_document_text(pdf_path)
    assert "System Report" in extracted_text or "Component" in extracted_text or "Engine" in extracted_text


def test_vault_key_lookup():
    """Verify get_api_key resolves keys from encrypted Vault."""
    os.environ["MERIDIAN_VAULT_PASSPHRASE"] = "TestPassphrase123!"
    vault_set("testcloud_key", "sk-test-cloud-vault-key-999")
    
    key = get_api_key("testcloud")
    assert key == "sk-test-cloud-vault-key-999"
