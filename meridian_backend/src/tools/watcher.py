import os
import re
from typing import List, Dict, Any, Optional
from src.core.watcher import (
    start_watching_log, stop_watching_log, list_log_watchers,
    start_watching_folder, stop_watching_folder, list_folder_watchers
)

# --- Log Monitor Tools ---

def watch_log(path: str, patterns: List[str], on_match_goal: str) -> str:
    """Start real-time monitoring of a log file for specific error/exception string patterns."""
    return start_watching_log(path, patterns, on_match_goal)

def unwatch_log(path: str) -> str:
    """Stop monitoring a log file."""
    return stop_watching_log(path)

def list_log_watchers() -> str:
    """List all currently active log file observers."""
    watchers = list_log_watchers()
    if not watchers:
        return "No log files are currently being watched."
    return "Active Log Watchers:\n" + "\n".join(f"- {w}" for w in watchers)

def tail_log(path: str, n: int = 30) -> str:
    """Read the last N lines of a log file for quick inspection."""
    if not os.path.exists(path):
        return f"Error: Log file '{path}' does not exist."
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        tail = lines[-n:]
        return "".join(tail)
    except Exception as e:
        return f"Error reading log file: {e}"

def search_log(path: str, pattern: str, limit: int = 50) -> str:
    """Perform a regex/substring search through a log file."""
    if not os.path.exists(path):
        return f"Error: Log file '{path}' does not exist."
    try:
        matches = []
        rx = re.compile(pattern, re.IGNORECASE)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f, 1):
                if rx.search(line):
                    matches.append(f"Line {idx}: {line.strip()}")
                    if len(matches) >= limit:
                        break
        if not matches:
            return f"No matches found for pattern '{pattern}' in '{path}'."
        return f"Found {len(matches)} matches in '{path}':\n" + "\n".join(matches)
    except Exception as e:
        return f"Error searching log file: {e}"

def log_stats(path: str) -> str:
    """Get metrics about a log file, counting log levels and assessing error frequency."""
    if not os.path.exists(path):
        return f"Error: Log file '{path}' does not exist."
    try:
        counts = {"ERROR": 0, "WARNING": 0, "INFO": 0, "DEBUG": 0, "CRITICAL": 0, "EXCEPTION": 0}
        total = 0
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                total += 1
                upper = line.upper()
                for key in counts:
                    if key in upper:
                        counts[key] += 1
                        
        stats = [
            f"Log File Stats for '{path}':",
            f"Total Lines Scanned: {total}",
            "Level Counts:"
        ]
        for k, v in counts.items():
            stats.append(f"  {k}: {v}")
            
        return "\n".join(stats)
    except Exception as e:
        return f"Error calculating log statistics: {e}"


# --- Folder Watcher Tools ---

def watch_folder(path: str, on_create_goal: Optional[str] = None, on_modify_goal: Optional[str] = None) -> str:
    """Monitor a folder. Runs autonomous goals when files are created or modified inside it."""
    return start_watching_folder(path, on_create_goal, on_modify_goal)

def unwatch_folder(path: str) -> str:
    """Stop monitoring a directory/folder."""
    return stop_watching_folder(path)

def list_watchers() -> str:
    """List all currently active folder watchers."""
    watchers = list_folder_watchers()
    if not watchers:
        return "No directory watchers are active."
    return "Active Folder Watchers:\n" + "\n".join(f"- {w}" for w in watchers)
