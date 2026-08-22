import os
import importlib
import importlib.util
import inspect
import sys
import time
import threading
from typing import Dict, Any, Callable

_observer = None
_registry_lock = threading.RLock()
# Files seen by the watchdog that are waiting for an explicit user-triggered reload
_pending_plugin_changes: set = set()
_MODULE_NS_PREFIX = "meridian_plugins_"


def _resolve_plugins_dir() -> str:
    try:
        from src.core.history_manager import find_workspace_root
        return os.path.join(find_workspace_root(), "plugins")
    except Exception:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(backend_dir)
        return os.path.join(root_dir, "plugins")


def _load_module_from_path(module_name: str, filepath: str):
    """Load a plugin file under a NAMESPACED module name (SEC-FIX).

    The plugins directory is no longer prepended to sys.path, so a dropped-in
    file like ``platform.py`` or ``json.py`` can never shadow stdlib modules
    process-wide. Module state lives under ``meridian_plugins_<name>``.
    """
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if not (spec and spec.loader):
        return None
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _register_tool(tool_registry: Dict[str, Dict[str, Any]], tool_name: str, cfg: Dict[str, Any], source: str) -> bool:
    """Register a plugin tool, refusing to overwrite existing/core tools (SEC-FIX)."""
    with _registry_lock:
        existing = tool_registry.get(tool_name)
        if existing is not None:
            # Allow a plugin to update a tool IT previously registered.
            if existing.get("plugin") != source:
                print(f"[Plugins] REFUSED to register '{tool_name}' from '{source}': name collides with an existing/core tool.")
                return False
        cfg = dict(cfg)
        cfg["plugin"] = source
        tool_registry[tool_name] = cfg
    print(f"[Plugins] Registered tool '{tool_name}' from '{source}'")
    return True


def load_plugins(tool_registry: Dict[str, Dict[str, Any]]):
    """Loads PLUGIN_MANIFEST defined tools in Python files under root/plugins/.

    SEC-FIX: manifest-defined tools are the only auto-registered surface.
    Legacy whole-module scanning still works but skips functions whose names
    collide with existing entries, and every registration is guarded by the
    registry lock.
    """
    plugins_dir = _resolve_plugins_dir()

    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir, exist_ok=True)
        # Create an example plugin with a manifest
        example_path = os.path.join(plugins_dir, "example_plugin.py")
        with open(example_path, "w", encoding="utf-8") as f:
            f.write('''# Example Plugin
def custom_echo_tool(text: str) -> str:
    """A custom echo tool that returns your text reversed."""
    return f"Echo from plugin: {text[::-1]}"

PLUGIN_MANIFEST = {
    "name": "Example Plugin",
    "version": "1.0",
    "tools": {
        "custom_echo_tool": {
            "tier": 1,
            "func": custom_echo_tool
        }
    }
}
''')

    for filename in sorted(os.listdir(plugins_dir)):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{_MODULE_NS_PREFIX}{filename[:-3]}"
            filepath = os.path.join(plugins_dir, filename)

            try:
                # Support module reloading for dynamic updates
                if module_name in sys.modules:
                    module = importlib.reload(sys.modules[module_name])
                else:
                    module = _load_module_from_path(module_name, filepath)
                if module is None:
                    continue

                # Read tier default
                tier = getattr(module, "TIER", 1)

                # Check for PLUGIN_MANIFEST dict parsing
                manifest = getattr(module, "PLUGIN_MANIFEST", None)
                if isinstance(manifest, dict) and "tools" in manifest:
                    for tool_name, tool_cfg in manifest["tools"].items():
                        func = tool_cfg.get("func") or getattr(module, tool_name, None)
                        if func and callable(func):
                            _register_tool(
                                tool_registry,
                                tool_name,
                                {"tier": tool_cfg.get("tier", tier), "func": func},
                                filename,
                            )
                else:
                    # Fallback to legacy automatic registration of all public functions
                    for attr_name in dir(module):
                        if attr_name.startswith("_") or attr_name == "PLUGIN_MANIFEST":
                            continue
                        attr = getattr(module, attr_name)
                        if inspect.isfunction(attr) and attr.__module__ == module_name:
                            _register_tool(tool_registry, attr_name, {"tier": tier, "func": attr}, filename)
            except Exception as e:
                print(f"[Plugins] Failed to load plugin '{filename}': {e}")

    # Start auto hot-reload observer if not already started
    start_plugin_hot_reload(tool_registry)

def reload_dynamic_plugins(tool_registry: Dict[str, Dict[str, Any]]) -> str:
    """Reload all dynamic plugins in the plugins/ folder and register any new tools."""
    try:
        load_plugins(tool_registry)
        _pending_plugin_changes.clear()
        return "Successfully reloaded all plugins. Any new functions or manifest tools in plugins/ have been registered into the TOOL_REGISTRY."
    except Exception as e:
        return f"Failed to reload plugins: {e}"

def get_pending_plugin_changes() -> list:
    """Files modified on disk that are waiting for an explicit reload."""
    return sorted(_pending_plugin_changes)

def start_plugin_hot_reload(tool_registry: Dict[str, Dict[str, Any]]):
    """Start watchdog observer to DETECT plugin file changes.

    SEC-FIX: the observer no longer imports/executes changed files by itself —
    module-level code would execute the moment an LLM-written file lands in
    plugins/, before any approval gate runs. Changes are queued and applied
    only when reload_dynamic_plugins() is explicitly invoked by the user/tool.
    """
    global _observer
    if _observer is not None:
        return

    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        plugins_dir = _resolve_plugins_dir()
        if not os.path.exists(plugins_dir):
            os.makedirs(plugins_dir, exist_ok=True)

        class PluginChangeHandler(FileSystemEventHandler):
            def on_any_event(self, event):
                if not event.is_directory and event.src_path.endswith(".py"):
                    filename = os.path.basename(event.src_path)
                    with _registry_lock:
                        _pending_plugin_changes.add(filename)
                    print(f"[Plugins] Detected file change: {event.src_path}. Queued for explicit reload (call /api/plugins/reload or the reload_dynamic_plugins tool).")

        event_handler = PluginChangeHandler()
        _observer = Observer()
        _observer.schedule(event_handler, plugins_dir, recursive=False)
        _observer.daemon = True
        _observer.start()
        print(f"[Plugins] Hot-reload watcher started on '{plugins_dir}' (changes require explicit reload).")
    except ImportError:
        print("[Plugins] 'watchdog' library not installed. Auto hot-reload is disabled.")
    except Exception as e:
        print(f"[Plugins] Failed to start auto hot-reload observer: {e}")

def stop_plugin_hot_reload():
    global _observer
    if _observer:
        try:
            _observer.stop()
            _observer.join(timeout=2.0)
        except Exception:
            pass
        _observer = None
        print("[Plugins] Auto hot-reload daemon observer stopped.")
