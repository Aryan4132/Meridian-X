import os
import subprocess

_cached_workspace_root = None

def find_workspace_root() -> str:
    """Finds the workspace root by walking up from this file's directory until finding .git."""
    global _cached_workspace_root
    if _cached_workspace_root is not None:
        return _cached_workspace_root
        
    curr = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(curr, ".git")):
            _cached_workspace_root = curr
            return curr
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    # Default fallback: 4 levels up from meridian_backend/src/core/
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    _cached_workspace_root = root
    return root

def ensure_git_initialized(workspace_dir: str = None):
    """Ensures git is initialized and has at least one commit so we can create checkpoints."""
    if workspace_dir is None:
        workspace_dir = find_workspace_root()
    try:
        if not os.path.exists(os.path.join(workspace_dir, ".git")):
            print(f"[History Manager] Initializing git in {workspace_dir}...")
            subprocess.run(["git", "init"], cwd=workspace_dir, check=True, capture_output=True)
            
        # Check if there is at least one commit
        res = subprocess.run(["git", "rev-parse", "HEAD"], cwd=workspace_dir, capture_output=True)
        if res.returncode != 0:
            print("[History Manager] Creating baseline commit...")
            subprocess.run(["git", "add", "-A"], cwd=workspace_dir, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "meridian_baseline_commit", "--allow-empty"], cwd=workspace_dir, check=True, capture_output=True)
    except Exception as e:
        print(f"[History Manager] Failed to initialize git repository: {e}")

def create_checkpoint(checkpoint_id: str, workspace_dir: str = None) -> bool:
    """Creates a local shadow commit checkpoint of the workspace."""
    if workspace_dir is None:
        workspace_dir = find_workspace_root()
    try:
        ensure_git_initialized(workspace_dir)
        # 1. Add all changes (untracked, modified, deleted)
        subprocess.run(["git", "add", "-A"], cwd=workspace_dir, check=True, capture_output=True)
        # 2. Commit with checkpoint_id prefix
        msg = f"meridian_checkpoint:{checkpoint_id}"
        subprocess.run(
            ["git", "commit", "-m", msg, "--allow-empty"],
            cwd=workspace_dir,
            check=True,
            capture_output=True
        )
        print(f"[History Manager] Created workspace checkpoint: {checkpoint_id}")
        return True
    except Exception as e:
        print(f"[History Manager] Failed to create checkpoint '{checkpoint_id}': {e}")
        return False

def rollback_to_checkpoint(checkpoint_id: str, workspace_dir: str = None) -> bool:
    """Rolls back the workspace files to a specific checkpoint_id."""
    if workspace_dir is None:
        workspace_dir = find_workspace_root()
    try:
        # Find the commit hash for the matching checkpoint
        log_res = subprocess.run(
            ["git", "log", "--all", "--grep", f"meridian_checkpoint:{checkpoint_id}", "--format=%H"],
            cwd=workspace_dir,
            check=True,
            capture_output=True,
            text=True
        )
        hashes = [h.strip() for h in log_res.stdout.strip().split("\n") if h.strip()]
        commit_hash = hashes[0] if hashes else None
        
        if not commit_hash:
            print(f"[History Manager] Checkpoint '{checkpoint_id}' not found in git log.")
            return False
            
        # BUG-46 fix: stash uncommitted changes before hard reset to prevent silent data loss.
        stash_result = subprocess.run(
            ["git", "stash", "--include-untracked"],
            cwd=workspace_dir, capture_output=True
        )
        if stash_result.returncode == 0 and b"No local changes" not in stash_result.stdout:
            print(f"[History Manager] Uncommitted changes stashed before rollback.")
        
        # Reset hard to that commit
        subprocess.run(["git", "reset", "--hard", commit_hash], cwd=workspace_dir, check=True, capture_output=True)
        print(f"[History Manager] Successfully rolled back to checkpoint '{checkpoint_id}' (commit {commit_hash})")
        return True
    except Exception as e:
        print(f"[History Manager] Failed to roll back to checkpoint '{checkpoint_id}': {e}")
        return False
