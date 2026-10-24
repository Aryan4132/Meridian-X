# Database Inconsistencies & Issues in `database.py` — Resolution Status

Audit and resolution report for [`meridian_backend/database.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/database.py) and [`meridian_backend/src/db/`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/).

---

## 1. Schema & Runtime Bugs

### 1.1 `thought_logs` Column Mismatch
- **Status**: **RESOLVED**
- **Fix Applied**: Updated `_create_tables` in [`src/db/connection.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/connection.py#L82) to include `tool_name TEXT` in `CREATE TABLE IF NOT EXISTS thought_logs` alongside `metadata TEXT`. Added automatic self-healing `ALTER TABLE thought_logs ADD COLUMN tool_name TEXT` for existing databases.
- **Verification**: `test_thought_logs_schema_and_operations` in [`tests/test_database.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/tests/test_database.py) passes (verifies `add_thought_log` and `get_thought_logs` persist and retrieve `tool_name`).

---

## 2. Asymmetric Storage & Dual-Write

### 2.1 WhatsApp Contacts Dual-Write
- **Status**: **RESOLVED**
- **Fix Applied**: In [`src/db/contacts.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/contacts.py#L25), `save_whatsapp_contact` performs dual-write: updates MongoDB if online and continues to SQLite `whatsapp_contacts` upsert. Data remains available even if MongoDB goes offline.
- **Verification**: `test_contacts_dual_write` passes.

### 2.2 Knowledge Graph Facts SQLite Fallback
- **Status**: **RESOLVED**
- **Fix Applied**: Added `knowledge_graph` table in [`src/db/connection.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/connection.py) with index on `entity`. Updated `add_knowledge_fact` and `get_knowledge_facts` in [`src/db/rag.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/rag.py#L112) to synchronize facts into SQLite and query SQLite if MongoDB is offline or empty.
- **Verification**: `test_knowledge_graph_sqlite_fallback` passes.

---

## 3. Vector Store & Index Synchronization

### 3.1 Memory Sleep Cycle Zombie Vectors
- **Status**: **RESOLVED**
- **Fix Applied**: In [`src/db/memory.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/memory.py#L83), when episodic conversations are deleted following fact consolidation, `conv_index` in Turbovec is rebuilt from remaining SQLite conversation records under `_turbovec_lock`.

---

## 4. Concurrency & Thread Safety

### 4.1 In-Memory LRU Cache Race Conditions
- **Status**: **RESOLVED**
- **Fix Applied**: `_exact_cache_lock = threading.RLock()` added and used in [`src/db/cache.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/cache.py#L23) around all reads and mutations of `_exact_match_cache`.
- **Verification**: `test_semantic_cache_thread_safety` (5 concurrent worker threads, 50 cache operations) passes cleanly.

### 4.2 Turbovec Vector Read/Write Lock Mismatch
- **Status**: **RESOLVED**
- **Fix Applied**: All vector searches in [`src/db/cache.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/cache.py#L65) and [`src/db/rag.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/rag.py#L76) acquire `with vectors._turbovec_lock:` before executing index search.

---

## 5. Architectural Decoupling & God Object Elimination

### 5.1 Modular `src/db/` Package & Clean Facade
- **Status**: **RESOLVED**
- **Fix Applied**:
  - Modularized database operations into dedicated components in [`meridian_backend/src/db/`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/): `connection.py`, `cache.py`, `profile.py`, `rag.py`, `logs.py`, `contacts.py`, `conversations.py`, `memory.py`, `embeddings.py`, `parsers.py`, `vectors.py`.
  - Replaced 1,736-line monolithic [`meridian_backend/database.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/database.py) with clean, backward-compatible Facade re-exporting all symbols.
- **Verification**: Regression test suites (`test_database.py`, `test_consensus_gate.py`, `test_sprint2_features.py`) 25/25 passed.

---

## 6. Performance Optimizations

### 6.1 Database Indexes
- **Status**: **RESOLVED**
- **Fix Applied**: Added `idx_semantic_cache_expires_at` and `idx_knowledge_graph_entity` in [`src/db/connection.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/connection.py).

### 6.2 Precompiled Regex
- **Status**: **RESOLVED**
- **Fix Applied**: Precompiled `_TRANSIENT_REGEX = re.compile(r"[^\w\s]")` at module scope in [`src/db/conversations.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/conversations.py#L17).
