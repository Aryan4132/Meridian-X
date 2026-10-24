import os
import time
import threading
from typing import Optional, Any
from src.db.connection import get_db_dir

try:
    from turbovec import IdMapIndex  # type: ignore # pyright: ignore[reportMissingImports]
except ImportError:
    IdMapIndex = None

def get_kb_index_path() -> str:
    return os.path.join(get_db_dir(), "knowledge_base.tq")

def get_cache_index_path() -> str:
    return os.path.join(get_db_dir(), "semantic_cache.tq")

def get_conv_index_path() -> str:
    return os.path.join(get_db_dir(), "conversations.tq")

KB_INDEX_PATH = get_kb_index_path()
CACHE_INDEX_PATH = get_cache_index_path()
CONV_INDEX_PATH = get_conv_index_path()


kb_index: Optional[Any] = None
cache_index: Optional[Any] = None
conv_index: Optional[Any] = None

# Reentrant lock for vector index operations
_turbovec_lock = threading.RLock()

def run_vector_health_check() -> bool:
    """Verify integrity of all Turbovec vector index files on startup."""
    if IdMapIndex is None:
        return False
    print("[Turbovec Health Check] Starting validation...")
    healthy = True

    def _quarantine(path: str, reason: str):
        quarantine_path = f"{path}.corrupt-{int(time.time())}"
        try:
            os.rename(path, quarantine_path)
            print(f"[Turbovec Health Check] {reason} — quarantined as '{os.path.basename(quarantine_path)}'.")
        except Exception as qe:
            print(f"[Turbovec Health Check] Failed to quarantine '{path}': {qe}")

    for name, path in [("Knowledge Base", KB_INDEX_PATH), ("Semantic Cache", CACHE_INDEX_PATH), ("Conversations", CONV_INDEX_PATH)]:
        if os.path.exists(path):
            if os.path.getsize(path) == 0:
                print(f"[Turbovec Health Check] Warning: {name} index file is empty (0 bytes). Recreating.")
                healthy = False
                _quarantine(path, "empty index file")
            else:
                try:
                    test_idx = IdMapIndex.load(path)
                    if getattr(test_idx, "dim", 0) != 768:
                        raise ValueError(f"Invalid dimension: {getattr(test_idx, 'dim', 0)}")
                except Exception as e:
                    print(f"[Turbovec Health Check] Error: {name} index is CORRUPTED ({e}). Quarantining.")
                    healthy = False
                    _quarantine(path, "corrupted index")
        else:
            print(f"[Turbovec Health Check] {name} index file does not exist yet.")
    return healthy

def init_turbovec_indexes():
    """Initializes Turbovec indexes with health verification."""
    global kb_index, cache_index, conv_index
    if IdMapIndex is None:
        kb_index, cache_index, conv_index = None, None, None
        return

    run_vector_health_check()

    with _turbovec_lock:
        # 1. Knowledge Base Index
        if os.path.exists(KB_INDEX_PATH):
            try:
                kb_index = IdMapIndex.load(KB_INDEX_PATH)
            except Exception as e:
                print("[Turbovec] Failed to load knowledge base index, creating new:", e)
                kb_index = IdMapIndex(dim=768, bit_width=4)
        else:
            kb_index = IdMapIndex(dim=768, bit_width=4)

        # 2. Semantic Cache Index
        if os.path.exists(CACHE_INDEX_PATH):
            try:
                cache_index = IdMapIndex.load(CACHE_INDEX_PATH)
            except Exception as e:
                print("[Turbovec] Failed to load semantic cache index, creating new:", e)
                cache_index = IdMapIndex(dim=768, bit_width=4)
        else:
            cache_index = IdMapIndex(dim=768, bit_width=4)

        # 3. Conversations Index
        if os.path.exists(CONV_INDEX_PATH):
            try:
                conv_index = IdMapIndex.load(CONV_INDEX_PATH)
            except Exception as e:
                print("[Turbovec] Failed to load conversations index, creating new:", e)
                conv_index = IdMapIndex(dim=768, bit_width=4)
        else:
            conv_index = IdMapIndex(dim=768, bit_width=4)
