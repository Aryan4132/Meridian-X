import os
import sqlite3
import pymongo
import time
from contextlib import contextmanager
from typing import Optional, Generator

from src.core.config import DB_DIR as _default_db_dir

def get_db_dir() -> str:
    data_dir = os.environ.get("MERIDIAN_DATA_DIR")
    if data_dir:
        target = os.path.join(data_dir, "meridian_memory") if not data_dir.endswith("meridian_memory") else data_dir
        os.makedirs(target, exist_ok=True)
        return target
    return _default_db_dir

db_dir = get_db_dir()
SQLITE_DB_PATH = os.path.join(get_db_dir(), "metadata.db")

# Dummy db for loop.py import compatibility
db = None

def _create_tables(conn: sqlite3.Connection) -> None:
    """Executes table and index creation SQL statements on the given connection."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS semantic_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_text TEXT UNIQUE,
            response_text TEXT,
            expires_at REAL,
            ttl_hours INTEGER DEFAULT 24
        )
    """)
    try:
        cursor.execute("ALTER TABLE semantic_cache ADD COLUMN ttl_hours INTEGER DEFAULT 24")
    except Exception:
        pass

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            role TEXT,
            content TEXT,
            summary TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_base (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            chunk_text TEXT,
            metadata TEXT
        )
    """)

    try:
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS knowledge_base_fts USING fts5(
                source,
                chunk_text,
                content='knowledge_base',
                content_rowid='id'
            )
        """)
        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS kb_ai AFTER INSERT ON knowledge_base BEGIN
                INSERT INTO knowledge_base_fts(rowid, source, chunk_text) VALUES (new.id, new.source, new.chunk_text);
            END;
        """)
        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS kb_ad AFTER DELETE ON knowledge_base BEGIN
                INSERT INTO knowledge_base_fts(knowledge_base_fts, rowid, source, chunk_text) VALUES('delete', old.id, old.source, old.chunk_text);
            END;
        """)
    except Exception as e:
        print("[Database] FTS5 initialization fallback (standard full-text):", e)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_log (
            id TEXT PRIMARY KEY,
            timestamp REAL,
            tool TEXT,
            tier INTEGER,
            outcome TEXT,
            error TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_graph (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity TEXT,
            relation TEXT,
            target TEXT,
            timestamp REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS background_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            goal TEXT,
            status TEXT,
            log TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS thought_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            session_id TEXT,
            step_index INTEGER,
            thought_text TEXT,
            tool_name TEXT,
            metadata TEXT
        )
    """)
    try:
        cursor.execute("ALTER TABLE thought_logs ADD COLUMN tool_name TEXT")
    except Exception:
        pass

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS token_spend_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            provider TEXT,
            model TEXT,
            prompt_tokens INTEGER,
            completion_tokens INTEGER,
            cost_usd REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompt_templates (
            name TEXT PRIMARY KEY,
            prompt_text TEXT,
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS whatsapp_contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            phone_number TEXT,
            alias TEXT,
            notes TEXT,
            updated_at REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clipboard_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            timestamp REAL
        )
    """)

    # Query-path indexes for high-throughput scans
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_semantic_cache_expires_at ON semantic_cache(expires_at)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_knowledge_graph_entity ON knowledge_graph(entity)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_conversations_timestamp ON conversations(timestamp)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_task_log_timestamp ON task_log(timestamp)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_thought_logs_session ON thought_logs(session_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_thought_logs_timestamp ON thought_logs(timestamp)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_background_runs_timestamp ON background_runs(timestamp)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_clipboard_timestamp ON clipboard_history(timestamp)")
    conn.commit()

_schema_initialized = False

def _ensure_schema(conn: sqlite3.Connection):
    """Guarantees SQLite schema exists. Self-heals if database was newly created or wiped."""
    global _schema_initialized
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='user_profile'")
        if not cursor.fetchone():
            _create_tables(conn)
            _schema_initialized = True
    except Exception:
        pass

def get_sqlite_conn() -> sqlite3.Connection:
    """Returns an optimized SQLite connection with WAL journal mode and self-healing schema."""
    target_dir = get_db_dir()
    os.makedirs(target_dir, exist_ok=True)
    db_path = os.path.join(target_dir, "metadata.db")
    conn = sqlite3.connect(db_path, timeout=30.0)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.execute("PRAGMA cache_size=-64000;")
        conn.execute("PRAGMA mmap_size=268435456;")
    except Exception:
        pass
    _ensure_schema(conn)
    return conn

@contextmanager
def get_db_cursor() -> Generator[sqlite3.Cursor, None, None]:
    """Context manager for SQLite operations. Guarantees connection release and auto-commit."""
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        try:
            conn.rollback()
        except Exception:
            pass
        raise
    finally:
        try:
            conn.close()
        except Exception:
            pass

def init_tables() -> None:
    """Initialize all SQLite tables and query-path indexes."""
    target_dir = get_db_dir()
    os.makedirs(target_dir, exist_ok=True)
    db_path = os.path.join(target_dir, "metadata.db")
    conn = sqlite3.connect(db_path, timeout=30.0)
    try:
        _create_tables(conn)
    finally:
        conn.close()

    # Initialize Turbovec vector indexes
    from src.db.vectors import init_turbovec_indexes
    init_turbovec_indexes()

# ----------------- MONGODB HELPERS (Graceful Fallback) -----------------

_mongo_client = None
_mongo_online = None
_last_mongo_check = 0.0

def get_mongo_db() -> Optional[pymongo.database.Database]:
    """Returns MongoDB database handle, or None if offline or in isolated test environment."""
    import sys
    data_dir = os.environ.get("MERIDIAN_DATA_DIR", "")
    if "test" in data_dir.lower() or os.environ.get("TESTING", "").lower() in ("1", "true", "yes") or "PYTEST_CURRENT_TEST" in os.environ or "pytest" in sys.modules:
        return None

    global _mongo_client, _mongo_online, _last_mongo_check
    now = time.time()
    if _mongo_online is not None and (now - _last_mongo_check < 30):
        if not _mongo_online or _mongo_client is None:
            return None
        return _mongo_client["meridian_kg"]

    try:
        if _mongo_client is None:
            mongo_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/meridian_kg")
            _mongo_client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=1000)
        _mongo_client.admin.command('ping')
        _mongo_online = True
    except Exception:
        _mongo_client = None
        _mongo_online = False
    finally:
        _last_mongo_check = now

    if _mongo_online and _mongo_client is not None:
        return _mongo_client["meridian_kg"]
    return None
