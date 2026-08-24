- [ ] Task 20.1: Multi-Provider RAG Vector Embeddings Pipeline (`PL-08`)
  - Acceptance: `database.py` generates embeddings via OpenAI `text-embedding-3-small` if key present, Ollama if online, or in-memory hashing fallback if offline.
  - Verify: Unit test in `test_day7_features.py`.
  - Files: `meridian_backend/database.py`

- [ ] Task 20.2: Hybrid Sparse-Dense RAG & AST Code Chunking (`PL-11`)
  - Acceptance: `doc_indexer.py` performs BM25 + dense Turbovec hybrid search using RRF fusion and parses `.py` files into AST function/class chunks.
  - Verify: Unit test in `test_day7_features.py`.
  - Files: `meridian_backend/src/core/doc_indexer.py`, `meridian_backend/database.py`

- [ ] Task 20.3: Native Pure-Python PDF Layout & Table Extractor (`PL-17`)
  - Acceptance: `documents.py` uses XY-Cut sorting for multi-column text and detects horizontal text alignment for markdown table extraction.
  - Verify: Unit test in `test_day7_features.py`.
  - Files: `meridian_backend/src/tools/documents.py`

- [ ] Task 20.4: Multi-Cloud Vault Fallback Chain (`PL-09`)
  - Acceptance: `llm_provider.py` retrieves keys from encrypted Vault, and auto-fails over from primary cloud to secondary cloud to local Ollama on API errors.
  - Verify: Unit test in `test_day7_features.py`.
  - Files: `meridian_backend/src/core/llm_provider.py`, `meridian_backend/src/core/vault.py`

- [ ] Task 20.5: Day 7 Unit Test Suite Verification
  - Acceptance: All Day 7 unit tests pass 100%.
  - Verify: `python -m pytest tests/test_day7_features.py -v`.
  - Files: `meridian_backend/tests/test_day7_features.py`
