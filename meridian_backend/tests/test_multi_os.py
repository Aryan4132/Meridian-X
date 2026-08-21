import sys
import os
import pytest
import platform

# Ensure backend root is in sys.path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from src.tools.system import (
    get_system_info,
    get_hardware_info,
    get_disk_info,
    list_startup_items,
    list_installed_apps,
    list_services,
    ping_host,
    open_url_in_browser
)
from src.tools.task_scheduler import (
    schedule_daily,
    schedule_once,
    list_tasks,
    delete_task
)
from src.tools.developer import _get_venv_executable
from src.tools.shell import validate_shell_ast_denylist
from src.core.hardware_detector import detect_hardware_specs
from src.core.system_defense import get_system_health_status, purge_system_caches, isolate_rogue_processes
from src.core.proactive import get_active_process_and_title, is_system_busy_or_fullscreen

def test_system_tools_cross_platform():
    """Verify system.py functions execute without platform import crashes."""
    sys_info = get_system_info()
    assert "CPU Load:" in sys_info
    assert "RAM Usage:" in sys_info

    hw_info = get_hardware_info()
    assert isinstance(hw_info, str) and len(hw_info) > 0

    disk_info = get_disk_info()
    assert isinstance(disk_info, str)

    startup = list_startup_items()
    assert isinstance(startup, str)

    apps = list_installed_apps()
    assert isinstance(apps, str)

    services = list_services()
    assert isinstance(services, str)

def test_task_scheduler_cross_platform():
    """Verify task_scheduler.py dispatches cleanly on any OS."""
    tasks = list_tasks()
    assert isinstance(tasks, str)

    # Test daily scheduling format validation
    res = schedule_daily("test_job", "echo hello", "12:00")
    assert isinstance(res, str)

    # Test deletion
    del_res = delete_task("test_job")
    assert isinstance(del_res, str)

def test_developer_venv_resolver():
    """Verify _get_venv_executable returns valid executable string."""
    python_path = _get_venv_executable("python")
    assert isinstance(python_path, str) and len(python_path) > 0

    pip_path = _get_venv_executable("pip")
    assert isinstance(pip_path, str) and len(pip_path) > 0

def test_shell_ast_denylist():
    """Verify shell safety validation works."""
    blocked, reason = validate_shell_ast_denylist("rmdir /s /q C:\\")
    assert blocked is True
    assert "Safety Gate blocked" in reason

    blocked_safe, _ = validate_shell_ast_denylist("echo 'Hello World'")
    assert blocked_safe is False

def test_hardware_detector_multi_os():
    """Verify hardware_detector returns structured dict without pynvml failure."""
    specs = detect_hardware_specs()
    assert "cpu_cores" in specs
    assert "ram_gb" in specs
    assert "gpu" in specs
    assert "hardware_tier" in specs
    assert specs["gpu"]["has_gpu"] in (True, False)

def test_system_defense_multi_os():
    """Verify system_defense metrics and cache purging."""
    status = get_system_health_status()
    assert "cpu_percent" in status
    assert "ram_percent" in status
    assert "is_healthy" in status

    purge_res = purge_system_caches()
    assert "gc_objects_purged" in purge_res

    rogues = isolate_rogue_processes(max_cpu_pct=99.9)
    assert isinstance(rogues, list)

def test_proactive_window_tracking():
    """Verify active window tracking on current OS."""
    proc_name, title, pid = get_active_process_and_title()
    assert isinstance(proc_name, str)
    assert isinstance(title, str)

    busy = is_system_busy_or_fullscreen(None)
    assert isinstance(busy, bool)
