import os
import json
import time
from typing import List, Dict, Any
from src.core.exporter import export_session_runbook
from database import get_conversation_history

# --- Session Export Tools ---

def export_session(format: str, output_path: str) -> str:
    """Export the current conversation session as a formatted report ('md', 'html', or 'runbook')."""
    fmt = format.lower()
    if fmt == "runbook":
        return export_session_runbook(output_path, "md")
    return export_session_runbook(output_path, fmt)

def export_goal(goal_id: str, format: str, output_path: str) -> str:
    """Export a specific past goal and its execution details from the database."""
    # Since LanceDB records are episodic, we can search by goal or runbook export
    # For simplicity, we fallback to exporting the active session as it contains the goal thread
    return export_session(format, output_path)

def list_sessions() -> str:
    """List all previous sessions recorded in the database."""
    try:
        records = get_conversation_history(limit=500)
        if not records:
            return "No previous conversations found in the database."
            
        sessions = {}
        for r in records:
            if r["id"] == "init":
                continue
            # Group by 1-hour windows
            hour_bin = int(r["timestamp"] / 3600)
            if hour_bin not in sessions:
                sessions[hour_bin] = []
            sessions[hour_bin].append(r)
            
        lines = ["Recorded Conversation Sessions:"]
        for hb, items in sorted(sessions.items(), reverse=True):
            timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(items[0]["timestamp"]))
            user_prompts = [i["content"] for i in items if i["role"] == "user"]
            summary = user_prompts[0][:60] + "..." if user_prompts else "Empty context"
            lines.append(f"- Date: {timestamp_str} | Turns: {len(items)} | Query: '{summary}'")
            
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing sessions: {e}"


# --- Fine-Tuning Tools ---

def _get_finetune_file() -> str:
    from src.core.config import FINETUNE_FILE
    return FINETUNE_FILE

def export_finetune_data(output_path: str) -> str:
    """Export the collected fine-tuning JSONL instruction-response dataset to a specified file path."""
    src = _get_finetune_file()
    if not os.path.exists(src):
        return "No fine-tuning dataset has been collected yet."
    try:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        import shutil
        shutil.copy2(src, output_path)
        return f"Successfully exported fine-tuning dataset (JSONL) to '{output_path}'."
    except Exception as e:
        return f"Failed to export fine-tuning data: {e}"

def finetune_stats() -> str:
    """Display statistics and count of logged training correction pairs in the fine-tuning file."""
    src = _get_finetune_file()
    if not os.path.exists(src):
        return "Fine-tuning Stats: 0 correction pairs collected."
    try:
        count = 0
        with open(src, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    count += 1
        return f"Fine-Tuning Dataset Stats:\n- Total correction/training pairs collected: {count}\n- File path: {src}"
    except Exception as e:
        return f"Error reading fine-tuning stats: {e}"

def mark_correction(pair_id: str, quality: str) -> str:
    """Rate a collected correction pair (e.g. 'good', 'bad') for DPO training data selection."""
    src = _get_finetune_file()
    if not os.path.exists(src):
        return "No fine-tuning data available."
    try:
        # Load all pairs, find by timestamp (which acts as pair_id) and update quality attribute
        pairs = []
        updated = False
        with open(src, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                # Check if timestamp matching pair_id
                if str(data.get("timestamp")) == str(pair_id):
                    data["quality"] = quality
                    updated = True
                pairs.append(data)
                
        if updated:
            with open(src, "w", encoding="utf-8") as f:
                for p in pairs:
                    f.write(json.dumps(p, ensure_ascii=False) + "\n")
            return f"Successfully marked pair '{pair_id}' as quality: '{quality}'."
        else:
            return f"Correction pair with ID/timestamp '{pair_id}' not found."
    except Exception as e:
        return f"Error marking correction: {e}"
