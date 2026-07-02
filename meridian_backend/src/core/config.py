import os

# Base directory for writable user data
MERIDIAN_DATA_DIR = os.environ.get("MERIDIAN_DATA_DIR")

if not MERIDIAN_DATA_DIR:
    # Development mode: fallback to local project root
    # config.py is in meridian_backend/src/core/config.py
    # backend_dir will be meridian_backend
    backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    MERIDIAN_DATA_DIR = os.path.dirname(backend_dir)

# Ensure the base directory exists
os.makedirs(MERIDIAN_DATA_DIR, exist_ok=True)

# Centralized writable paths
DB_DIR = os.path.join(MERIDIAN_DATA_DIR, "meridian_memory")
VAULT_FILE = os.path.join(MERIDIAN_DATA_DIR, "vault.enc")
FINETUNE_FILE = os.path.join(MERIDIAN_DATA_DIR, "finetune_data.jsonl")
ENV_FILE = os.path.join(MERIDIAN_DATA_DIR, ".env")

os.makedirs(DB_DIR, exist_ok=True)
