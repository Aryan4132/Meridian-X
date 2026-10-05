"""
proactive — Meridian-X Proactive Intelligence Engine (Modular Package).

Pushes unsolicited nudges to frontend via event bus when:
  1. System health anomalies are detected (CPU / RAM / Disk / Battery / Network)
  2. The user has been idle for too long
  3. The clipboard contains something interesting (URL, error, code)
  4. Ergonomic, circadian, or meeting preparation intervals trigger
"""

import sys

from .dispatcher import (
    _main_loop,
    set_main_event_loop,
    get_main_event_loop,
    _now_str,
    publish_nudge_sync,
    push_day8_context_nudge,
    push_proactive_nudge,
    dispatch_notification,
    on_terminal_crash,
    on_user_motion_return,
)

from .guard import (
    game_mode_active,
    auto_game_mode_active,
    CPU_WARN_THRESHOLD,
    RAM_WARN_THRESHOLD,
    DISK_WARN_THRESHOLD,
    DISK_PATH,
    _last_cpu_alert,
    _last_ram_alert,
    _last_disk_alert,
    _health_cooldown,
    check_system_health,
    _auto_detected_game_pid,
    _auto_detected_game_name,
    get_active_process_and_title,
    get_active_window_title,
    is_system_busy_or_fullscreen,
    is_game_process_running,
    get_app_pids,
    check_active_window,
    _last_battery_alert,
    check_battery_status,
    _last_network_alert,
    _is_offline,
    check_network_status,
)

from .commits import (
    _last_activity_time,
    _last_idle_nudge,
    _last_memory_consolidation,
    MEMORY_CONSOLIDATION_COOLDOWN,
    IDLE_THRESHOLD_MINUTES,
    IDLE_NUDGE_COOLDOWN,
    IDLE_SUGGESTIONS,
    _last_arrival_briefing,
    ARRIVAL_BRIEFING_COOLDOWN,
    _last_commit_whisper_time,
    COMMIT_WHISPER_COOLDOWN,
    check_presence_arrival,
    check_proactive_commits,
    trigger_what_broke_auto_fix,
    record_user_activity,
    check_idle_time,
    _last_clipboard_nudge,
    CLIPBOARD_COOLDOWN,
    _URL_RE,
    _TRACEBACK_RE,
    _looks_like_code,
    _clipboard_history_buffer,
    on_clipboard_proactive,
    _pending_followups,
    _followup_lock,
    ENGINEER_FOLLOWUP_DELAY,
    FOLLOWUP_TEMPLATES,
    schedule_followup,
    check_followups,
    _last_git_check,
    check_git_status,
)

from .ergonomics import (
    _continuous_work_start_time,
    _last_ergonomics_nudge_time,
    ERGONOMICS_COOLDOWN,
    check_continuous_work_ergonomics,
    _focus_guard_enabled,
    _suppressed_nudges_buffer,
    toggle_focus_guard,
    generate_focus_digest,
    _last_circadian_alert,
    check_circadian_reminders,
    pomodoro_active,
    pomodoro_work_duration,
    pomodoro_break_duration,
    pomodoro_start_time,
    pomodoro_state,
    check_pomodoro_timer,
    generate_morning_briefing,
    synthesize_ambient_nudge,
    generate_meeting_prep_briefing,
    generate_evening_winddown_digest,
)

from . import dispatcher, guard, commits, ergonomics

_SUB_MODULES = [dispatcher, guard, commits, ergonomics]


class _ProactivePackage(sys.modules[__name__].__class__):
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        for mod in _SUB_MODULES:
            if hasattr(mod, name):
                setattr(mod, name, value)


sys.modules[__name__].__class__ = _ProactivePackage

__all__ = [
    # dispatcher
    "set_main_event_loop",
    "get_main_event_loop",
    "publish_nudge_sync",
    "push_day8_context_nudge",
    "push_proactive_nudge",
    "dispatch_notification",
    "on_terminal_crash",
    "on_user_motion_return",
    # guard
    "game_mode_active",
    "auto_game_mode_active",
    "check_system_health",
    "get_active_process_and_title",
    "get_active_window_title",
    "is_system_busy_or_fullscreen",
    "is_game_process_running",
    "get_app_pids",
    "check_active_window",
    "check_battery_status",
    "check_network_status",
    # commits
    "check_presence_arrival",
    "check_proactive_commits",
    "trigger_what_broke_auto_fix",
    "record_user_activity",
    "check_idle_time",
    "on_clipboard_proactive",
    "schedule_followup",
    "check_followups",
    "check_git_status",
    # ergonomics
    "check_continuous_work_ergonomics",
    "toggle_focus_guard",
    "generate_focus_digest",
    "check_circadian_reminders",
    "check_pomodoro_timer",
    "generate_morning_briefing",
    "synthesize_ambient_nudge",
    "generate_meeting_prep_briefing",
    "generate_evening_winddown_digest",
]
