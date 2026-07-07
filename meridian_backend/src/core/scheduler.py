import os
import time
import asyncio
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

# Initialize directories
from src.core.config import DB_DIR
db_path = os.path.join(DB_DIR, "scheduler.db")

# Define job store
jobstores = {
    'default': SQLAlchemyJobStore(url=f'sqlite:///{db_path}')
}
scheduler = BackgroundScheduler(jobstores=jobstores)

def is_resource_throttled() -> bool:
    """Checks system indicators to determine if resource-heavy tasks should be throttled."""
    try:
        import psutil
        # Get immediate CPU percent check
        cpu_load = psutil.cpu_percent(interval=None)
        if cpu_load > 85.0:
            print(f"[Resource Governor] High CPU load detected: {cpu_load}%")
            return True
            
        from src.core.proactive import get_active_process_and_title
        proc_name, window_title = get_active_process_and_title()
        proc_name = proc_name.lower()
        window_title = window_title.lower()
        heavy_keywords = ["valorant", "cyberpunk", "blender", "unity", "unreal", "steam", "render", "visual studio", "compiler", "csgo", "cs2", "dota2", "leagueoflegends", "minecraft", "javaw"]
        if any(k in window_title or k in proc_name for k in heavy_keywords):
            print(f"[Resource Governor] Throttled by active foreground process: '{window_title or proc_name}'")
            return True
    except Exception as e:
        print(f"[Resource Governor] Check failed: {e}")
    return False

def execute_scheduled_goal(goal: str):
    """Bridge background job to async ReAct agent loop execution."""
    print(f"[Scheduler] Triggered background execution for goal: '{goal}'")
    
    # Check resource limits before execution
    if is_resource_throttled():
        print(f"[Scheduler] Skipping background execution for goal '{goal}' (governor throttling active).")
        try:
            from database import add_background_run
            add_background_run(
                goal, 
                "throttled", 
                "Background execution paused/throttled by Resource Governor to preserve system performance."
            )
        except Exception as ex:
            print(f"[Scheduler] Failed to log throttled run: {ex}")
        return

    status = "success"
    run_log_parts = []
    try:
        from src.core.loop import run_react_agent_loop
        # BUG-39 fix: import from database instead of api to avoid circular import
        # (api.py imports scheduler.py at startup; scheduler importing from api creates a cycle).
        from database import get_ollama_client_host
        import json
        
        brain_model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
        ollama_host = get_ollama_client_host()
        
        # BUG-39 fix: use asyncio.run() instead of new_event_loop+set_event_loop pattern
        # (asyncio.set_event_loop in a background thread is deprecated in Python 3.10+).
        loop = asyncio.new_event_loop()
        
        async def run():
            current_thought = []
            current_output = []
            # Consume SSE generator to trigger tool execution
            async for event in run_react_agent_loop(goal, brain_model, ollama_host):
                lines = event.splitlines()
                event_type = ""
                data_lines = []
                for line in lines:
                    if line.startswith("event: "):
                        event_type = line[7:].strip()
                    elif line.startswith("data: "):
                        data_lines.append(line[6:])
                
                data_payload = "\n".join(data_lines)
                if event_type == "thought":
                    try:
                        payload = json.loads(data_payload)
                        text = payload.get("text", "")
                        status_val = payload.get("status", "")
                        if text:
                            current_thought.append(text)
                        if status_val == "completed":
                            thought_str = "".join(current_thought).strip()
                            if thought_str:
                                run_log_parts.append(f"🤖 Thought:\n{thought_str}\n")
                            current_thought = []
                    except Exception:
                        pass
                elif event_type == "text":
                    current_output.append(data_payload)
                elif event_type == "warning":
                    try:
                        payload = json.loads(data_payload)
                        text = payload.get("text", "")
                        if text:
                            run_log_parts.append(f"⚠️ Warning: {text}\n")
                    except Exception:
                        pass

            # Flush final output and any remaining thought
            thought_str = "".join(current_thought).strip()
            if thought_str:
                run_log_parts.append(f"🤖 Thought:\n{thought_str}\n")
            
            output_str = "".join(current_output).strip()
            if output_str:
                run_log_parts.append(f"📝 Output:\n{output_str}\n")
                
        # BUG-6 fix: use finally to guarantee loop is always closed and cleared,
        # even if run_until_complete() raises (previously leaked the loop on failure).
        try:
            loop.run_until_complete(run())
        finally:
            loop.close()
            asyncio.set_event_loop(None)  # clean up thread-local loop reference
        
        # Log to database
        from database import add_background_run
        log_content = "\n".join(run_log_parts)
        add_background_run(goal, "success", log_content)
        print(f"[Scheduler] Completed goal: '{goal}'")
    except Exception as e:
        status = "failed"
        print(f"[Scheduler] Failed to execute goal '{goal}': {e}")
        try:
            from database import add_background_run
            log_content = "\n".join(run_log_parts) + f"\n[Execution Error] {e}"
            add_background_run(goal, "failed", log_content)
        except Exception:
            pass


def start_scheduler():
    if not scheduler.running:
        scheduler.start()
        print("[Scheduler] Started APScheduler background worker daemon.")
        
        try:
            from src.core.graph_sync import scan_workspaces
            # Check if job already exists to avoid duplication
            if not scheduler.get_job("workspace_scan_job"):
                scheduler.add_job(
                    scan_workspaces,
                    trigger='interval',
                    hours=6,
                    id='workspace_scan_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered recurring workspace scan job (every 6 hours).")
        except Exception as e:
            print(f"[Scheduler] Failed to register recurring scan job: {e}")

        # ── Proactive Intelligence Jobs ──────────────────────────────────────
        try:
            from src.core.proactive import (
                check_system_health, check_idle_time, check_followups,
                check_active_window, check_battery_status, check_git_status,
                check_circadian_reminders, check_network_status
            )
            if not scheduler.get_job("proactive_health_job"):
                scheduler.add_job(
                    check_system_health,
                    trigger='interval',
                    minutes=5,
                    id='proactive_health_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive system health check (every 5 min).")
            if not scheduler.get_job("proactive_idle_job"):
                scheduler.add_job(
                    check_idle_time,
                    trigger='interval',
                    minutes=5,
                    id='proactive_idle_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive idle nudge check (every 5 min).")
            if not scheduler.get_job("proactive_followup_job"):
                scheduler.add_job(
                    check_followups,
                    trigger='interval',
                    minutes=5,
                    id='proactive_followup_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive follow-up check (every 5 min).")
            if not scheduler.get_job("proactive_window_job"):
                scheduler.add_job(
                    check_active_window,
                    trigger='interval',
                    seconds=15,
                    id='proactive_window_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive active window monitor (every 15 sec).")
            if not scheduler.get_job("proactive_battery_job"):
                scheduler.add_job(
                    check_battery_status,
                    trigger='interval',
                    minutes=5,
                    id='proactive_battery_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive battery monitor (every 5 min).")
            if not scheduler.get_job("proactive_git_job"):
                scheduler.add_job(
                    check_git_status,
                    trigger='interval',
                    minutes=5,
                    id='proactive_git_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive git copilot status check (every 5 min).")
            if not scheduler.get_job("proactive_circadian_job"):
                scheduler.add_job(
                    check_circadian_reminders,
                    trigger='interval',
                    minutes=5,
                    id='proactive_circadian_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive circadian reminders check (every 5 min).")
            if not scheduler.get_job("proactive_network_job"):
                scheduler.add_job(
                    check_network_status,
                    trigger='interval',
                    minutes=5,
                    id='proactive_network_job',
                    replace_existing=True
                )
                print("[Scheduler] Registered proactive network connectivity monitor (every 5 min).")
        except Exception as e:
            print(f"[Scheduler] Failed to register proactive jobs: {e}")

def stop_scheduler():
    if scheduler.running:
        scheduler.shutdown()
        print("[Scheduler] Stopped APScheduler background worker daemon.")
