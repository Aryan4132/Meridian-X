# Implementation Plan: Day 7 — Multi-Provider RAG, PDF Extractor & Vault Fallback Chain

## Overview
Implement Day 7 features for Meridian-X: Multi-Provider Embeddings Pipeline (`PL-08`), Hybrid Sparse-Dense RAG & AST Code Chunking (`PL-11`), Native Pure-Python PDF Layout & Table Extractor (`PL-17`), and Multi-Cloud Vault Fallback Chain (`PL-09`).

## Task List

### Phase 1: RAG & Document Pipeline
- [ ] Task 20.1: Multi-Provider RAG Vector Embeddings Pipeline (`database.py`)
- [ ] Task 20.2: Hybrid Sparse-Dense RAG & AST Code Chunking (`src/core/doc_indexer.py`)
- [ ] Task 20.3: Native Pure-Python PDF Layout & Table Extractor (`src/tools/documents.py`)

### Phase 2: Resilience & Verification
- [ ] Task 20.4: Multi-Cloud Vault Fallback Chain (`src/core/llm_provider.py`)
- [ ] Task 20.5: Day 7 Unit Test Suite Verification (`tests/test_day7_features.py`)

## Risks and Mitigations
| Risk | Impact | Mitigation |
|---|---|---|
| OpenAI / Ollama embedding dimension mismatch (1536 vs 4096) | Medium | Normalize and zero-pad / slice vectors or track model dimension metadata per index. |
| In-memory embedding fallback overhead | Low | Use lightweight deterministic hashing vectorizer as offline zero-dependency fallback. |
| PDF layout text fragment overlap | Medium | Group text fragments by Y-coordinate bands before X-sorting (XY-Cut algorithm). |
