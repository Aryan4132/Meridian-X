from datetime import datetime
from src.core.scheduler import scheduler, execute_scheduled_goal
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

def schedule_task(goal: str, cron_expr: str) -> str:
    """Schedule a recurring natural language goal using standard cron syntax (e.g. '0 8 * * *')."""
    try:
        # cron_expr format: "minute hour day month day_of_week"
        # APScheduler CronTrigger fields: minute, hour, day, month, day_of_week
        fields = cron_expr.split()
        if len(fields) != 5:
            return "Error: Cron expression must contain exactly 5 fields (e.g. '0 8 * * *')."
            
        trigger = CronTrigger(
            minute=fields[0],
            hour=fields[1],
            day=fields[2],
            month=fields[3],
            day_of_week=fields[4]
        )
        
        job = scheduler.add_job(
            execute_scheduled_goal,
            trigger=trigger,
            args=[goal],
            name=goal[:50]
        )
        return f"Successfully scheduled recurring job. Job ID: {job.id}"
    except Exception as e:
        return f"Error scheduling recurring job: {e}"

def schedule_once(goal: str, run_at: str) -> str:
    """Schedule a one-off natural language goal to run at a future timestamp (format: 'YYYY-MM-DD HH:MM:SS')."""
    try:
        dt = datetime.strptime(run_at, "%Y-%m-%d %H:%M:%S")
        if dt < datetime.now():
            return "Error: Target timestamp is in the past."
            
        trigger = DateTrigger(run_date=dt)
        job = scheduler.add_job(
            execute_scheduled_goal,
            trigger=trigger,
            args=[goal],
            name=goal[:50]
        )
        return f"Successfully scheduled one-shot job. Job ID: {job.id} to run at {run_at}"
    except Exception as e:
        return f"Error scheduling one-shot job: {e}"

def list_scheduled() -> str:
    """List all pending and recurring scheduled agent tasks."""
    try:
        jobs = scheduler.get_jobs()
        if not jobs:
            return "No scheduled tasks found."
            
        lines = ["Active Scheduled Tasks:"]
        for j in jobs:
            next_run = j.next_run_time.strftime("%Y-%m-%d %H:%M:%S") if j.next_run_time else "None"
            lines.append(f"- ID: {j.id} | Goal: '{j.name}' | Next Run: {next_run} | Trigger: {j.trigger}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing scheduled tasks: {e}"

def cancel_task(job_id: str) -> str:
    """Cancel and remove a scheduled task by its unique Job ID."""
    try:
        scheduler.remove_job(job_id)
        return f"Successfully cancelled and removed scheduled task '{job_id}'."
    except Exception as e:
        return f"Error cancelling task: {e} (Job ID may not exist)"
