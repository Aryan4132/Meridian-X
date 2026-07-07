import subprocess
import csv
import sys
import os
from src.core.history_manager import find_workspace_root

def _get_pythonw_path() -> str:
    py = sys.executable
    if py.endswith("python.exe"):
        pyw = py.replace("python.exe", "pythonw.exe")
        if os.path.exists(pyw):
            return pyw
    return py

def win_schedule_daily(task_name: str, goal: str, start_time: str) -> str:
    """Schedule a daily recurring task in Windows Task Scheduler.
    
    task_name: Unique short identifier (will be prefixed with Meridian_).
    goal: Natural language goal for the agent to achieve.
    start_time: Daily start time in HH:MM format (24-hour, e.g. 08:30).
    """
    if not task_name or not goal or not start_time:
        return "Error: task_name, goal, and start_time must be specified."
        
    full_name = f"Meridian_{task_name}"
    root = find_workspace_root()
    main_py = os.path.join(root, "main.py")
    pyw = _get_pythonw_path()
    
    cmd_str = f'cmd.exe /c cd /d "{root}" && "{pyw}" "{main_py}" --goal "{goal}"'
    
    cmd = [
        "schtasks", "/create",
        "/tn", full_name,
        "/tr", cmd_str,
        "/sc", "DAILY",
        "/st", start_time,
        "/f"
    ]
    
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully scheduled daily OS task '{full_name}' at {start_time}."
    except subprocess.CalledProcessError as e:
        return f"Error creating scheduled task: {e.stderr.strip() or e.stdout.strip()}"

def win_schedule_once(task_name: str, goal: str, start_date: str, start_time: str) -> str:
    """Schedule a one-off task in Windows Task Scheduler.
    
    task_name: Unique short identifier (will be prefixed with Meridian_).
    goal: Natural language goal for the agent to achieve.
    start_date: Start date in YYYY-MM-DD format.
    start_time: Start time in HH:MM format (e.g. 15:45).
    """
    if not task_name or not goal or not start_date or not start_time:
        return "Error: task_name, goal, start_date, and start_time must be specified."
        
    full_name = f"Meridian_{task_name}"
    root = find_workspace_root()
    main_py = os.path.join(root, "main.py")
    pyw = _get_pythonw_path()
    
    clean_date = start_date.replace("-", "/")
    cmd_str = f'cmd.exe /c cd /d "{root}" && "{pyw}" "{main_py}" --goal "{goal}"'
    
    cmd = [
        "schtasks", "/create",
        "/tn", full_name,
        "/tr", cmd_str,
        "/sc", "ONCE",
        "/sd", clean_date,
        "/st", start_time,
        "/f"
    ]
    
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully scheduled one-shot OS task '{full_name}' on {start_date} at {start_time}."
    except subprocess.CalledProcessError as e:
        return f"Error creating scheduled task: {e.stderr.strip() or e.stdout.strip()}"

def win_list_tasks_raw() -> list:
    """List all scheduled Meridian tasks with details."""
    cmd = ["schtasks", "/query", "/fo", "csv", "/v"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Handle potential encoding issues on Windows
        output = res.stdout
        lines = output.splitlines()
        if not lines:
            return []
            
        reader = csv.reader(lines)
        try:
            header = next(reader)
        except StopIteration:
            return []
            
        indices = {
            "name": -1,
            "next_run": -1,
            "status": -1,
            "command": -1
        }
        for idx, col in enumerate(header):
            col_l = col.lower()
            if "taskname" in col_l or "task name" in col_l:
                indices["name"] = idx
            elif "next run" in col_l:
                indices["next_run"] = idx
            elif "status" in col_l and indices["status"] == -1:
                indices["status"] = idx
            elif "task to run" in col_l or "command" in col_l or "run" in col_l:
                if "next" not in col_l:
                    indices["command"] = idx
                    
        tasks = []
        for row in reader:
            # BUG-49 fix: explicitly guard against -1 indices. max(indices.values())==-1
            # when no column is found, making `len(row) <= -1` always False (never skips).
            # Accessing row[-1] returns last column silently with wrong data.
            max_idx = max(indices.values())
            if not row or max_idx < 0 or len(row) <= max_idx:
                continue
            name_val = row[indices["name"]] if indices["name"] >= 0 else ""
            short_name = name_val.lstrip("\\")
            if short_name.startswith("Meridian_"):
                next_run = row[indices["next_run"]] if indices["next_run"] != -1 else "Unknown"
                status = row[indices["status"]] if indices["status"] != -1 else "Unknown"
                cmd_val = row[indices["command"]] if indices["command"] != -1 else ""
                
                goal = ""
                if "--goal" in cmd_val:
                    try:
                        goal = cmd_val.split("--goal", 1)[1].strip().strip('"')
                    except Exception:
                        pass
                if not goal:
                    goal = cmd_val
                    
                tasks.append({
                    "name": short_name.replace("Meridian_", ""),
                    "full_name": short_name,
                    "next_run": next_run,
                    "status": status,
                    "goal": goal
                })
        return tasks
    except Exception as e:
        print("Error listing tasks:", e)
        return []

def win_list_tasks() -> str:
    """Return a formatted string of all scheduled Meridian tasks."""
    tasks = win_list_tasks_raw()
    if not tasks:
        return "No scheduled Meridian OS tasks found."
    
    lines = ["Active Scheduled Windows OS Tasks:"]
    for t in tasks:
        lines.append(f"- Name: {t['name']} | Goal: '{t['goal']}' | Next Run: {t['next_run']} | Status: {t['status']}")
    return "\n".join(lines)

def win_delete_task(task_name: str) -> str:
    """Delete a scheduled task by name."""
    if not task_name:
        return "Error: task_name must be specified."
        
    full_name = task_name if task_name.startswith("Meridian_") else f"Meridian_{task_name}"
    cmd = ["schtasks", "/delete", "/tn", full_name, "/f"]
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"Successfully deleted scheduled OS task '{full_name}'."
    except subprocess.CalledProcessError as e:
        return f"Error deleting scheduled task: {e.stderr.strip() or e.stdout.strip()}"
