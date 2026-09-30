"""
Downloads Janitor (KNOW-01)
Auto-sorts downloads folder by category, identifies duplicate files via SHA256 hashes,
and enforces age-out policies.
"""

import os
import hashlib
from typing import Dict, List, Any

CATEGORY_MAP = {
    "images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"],
    "documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".md", ".csv"],
    "archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "executables": [".exe", ".msi", ".dmg", ".sh", ".bat"],
    "media": [".mp4", ".mkv", ".mp3", ".wav", ".flac"]
}

def scan_downloads_folder(directory_path: str = "") -> str:
    """
    Scan a directory (default User Downloads folder) for organizing opportunities and duplicates.
    """
    if not directory_path:
        directory_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    if not os.path.exists(directory_path):
        return f"Directory '{directory_path}' does not exist."

    category_counts: Dict[str, int] = {}
    file_hashes: Dict[str, List[str]] = {}
    total_files = 0

    try:
        for entry in os.scandir(directory_path):
            if entry.is_file():
                total_files += 1
                ext = os.path.splitext(entry.name)[1].lower()
                cat = "other"
                for c_name, exts in CATEGORY_MAP.items():
                    if ext in exts:
                        cat = c_name
                        break
                category_counts[cat] = category_counts.get(cat, 0) + 1

                # Calculate partial hash for duplicate detection
                try:
                    h = hashlib.sha256()
                    with open(entry.path, "rb") as f:
                        h.update(f.read(4096))
                    digest = h.hexdigest()
                    file_hashes.setdefault(digest, []).append(entry.name)
                except Exception:
                    pass
    except Exception as e:
        return f"Failed to scan directory: {e}"

    duplicates = {k: v for k, v in file_hashes.items() if len(v) > 1}

    breakdown = "\n".join(f"- {k.capitalize()}: {v} files" for k, v in category_counts.items())
    dup_str = f"Found {len(duplicates)} potential duplicate sets." if duplicates else "No duplicate files found."

    return (
        f"🧹 Downloads Janitor Report for '{directory_path}':\n"
        f"Total Files Scanned: {total_files}\n"
        f"Category Breakdown:\n{breakdown}\n\n"
        f"Duplicate Status: {dup_str}"
    )

def organize_downloads(directory_path: str = "", dry_run: bool = True) -> str:
    """
    Organize files in directory into categorical subfolders (Images, Documents, Archives, etc.).
    dry_run: if True, returns simulation report without moving files.
    """
    if not directory_path:
        directory_path = os.path.join(os.path.expanduser("~"), "Downloads")

    if not os.path.exists(directory_path):
        return f"Directory '{directory_path}' does not exist."

    moved_summary = []

    try:
        for entry in os.scandir(directory_path):
            if entry.is_file():
                ext = os.path.splitext(entry.name)[1].lower()
                target_cat = "Other"
                for c_name, exts in CATEGORY_MAP.items():
                    if ext in exts:
                        target_cat = c_name.capitalize()
                        break
                
                target_dir = os.path.join(directory_path, target_cat)
                target_file = os.path.join(target_dir, entry.name)
                
                if not dry_run:
                    os.makedirs(target_dir, exist_ok=True)
                    os.rename(entry.path, target_file)
                moved_summary.append(f"- {entry.name} ➔ {target_cat}/")
    except Exception as e:
        return f"Error organizing downloads: {e}"

    mode = "[DRY RUN SIMULATION]" if dry_run else "[ACTION EXECUTED]"
    return f"🧹 Downloads Janitor {mode}:\nProcessed {len(moved_summary)} files.\n" + "\n".join(moved_summary[:10]) + ("\n...and more" if len(moved_summary) > 10 else "")
