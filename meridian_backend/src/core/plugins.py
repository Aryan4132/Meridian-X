import os
import importlib
import importlib.util
import inspect
import sys
import time
from typing import Dict, Any, Callable

_observer = None

def load_plugins(tool_registry: Dict[str, Dict[str, Any]]):
    """Loads all public functions or PLUGIN_MANIFEST defined tools in Python files under root/plugins/."""
    try:
        from src.core.history_manager import find_workspace_root
        plugins_dir = os.path.join(find_workspace_root(), "plugins")
    except Exception:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(backend_dir)
        plugins_dir = os.path.join(root_dir, "plugins")
    
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

    # Add plugins directory to python path
    if plugins_dir not in sys.path:
        sys.path.insert(0, plugins_dir)

    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            filepath = os.path.join(plugins_dir, filename)
            
            try:
                # Support module reloading for dynamic updates
                if module_name in sys.modules:
                    importlib.reload(sys.modules[module_name])
                    module = sys.modules[module_name]
                else:
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                    else:
                        continue
                    
                # Read tier default
                tier = getattr(module, "TIER", 1)
                
                # Check for PLUGIN_MANIFEST dict parsing
                manifest = getattr(module, "PLUGIN_MANIFEST", None)
                if isinstance(manifest, dict) and "tools" in manifest:
                    print(f"[Plugins] Found PLUGIN_MANIFEST in '{filename}'. Loading manifest-defined tools...")
                    for tool_name, tool_cfg in manifest["tools"].items():
                        func = tool_cfg.get("func") or getattr(module, tool_name, None)
                        if func and callable(func):
                            tool_registry[tool_name] = {
                                "tier": tool_cfg.get("tier", tier),
                                "func": func
                            }
                            print(f"[Plugins] Registered manifest tool '{tool_name}' (Tier {tool_cfg.get('tier', tier)}) from '{filename}'")
                else:
                    # Fallback to legacy automatic registration of all public functions
                    for attr_name in dir(module):
                        if attr_name.startswith("_") or attr_name == "PLUGIN_MANIFEST":
                            continue
                        attr = getattr(module, attr_name)
                        if inspect.isfunction(attr):
                            # Ensure it's defined in the module itself
                            if attr.__module__ == module_name:
                                tool_registry[attr_name] = {
                                    "tier": tier,
                                    "func": attr
                                }
                                print(f"[Plugins] Registered dynamic tool '{attr_name}' (Tier {tier}) from '{filename}'")
            except Exception as e:
                print(f"[Plugins] Failed to load plugin '{filename}': {e}")
                
    # Start auto hot-reload observer if not already started
    start_plugin_hot_reload(tool_registry)

def reload_dynamic_plugins(tool_registry: Dict[str, Dict[str, Any]]) -> str:
    """Reload all dynamic plugins in the plugins/ folder and register any new tools."""
    try:
        load_plugins(tool_registry)
        return "Successfully reloaded all plugins. Any new functions or manifest tools in plugins/ have been registered into the TOOL_REGISTRY."
    except Exception as e:
        return f"Failed to reload plugins: {e}"

def start_plugin_hot_reload(tool_registry: Dict[str, Dict[str, Any]]):
    """Start watchdog observer to automatically reload plugins when files are modified."""
    global _observer
    if _observer is not None:
        return
        
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        
        try:
            from src.core.history_manager import find_workspace_root
            plugins_dir = os.path.join(find_workspace_root(), "plugins")
        except Exception:
            backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            root_dir = os.path.dirname(backend_dir)
            plugins_dir = os.path.join(root_dir, "plugins")
            
        if not os.path.exists(plugins_dir):
            os.makedirs(plugins_dir, exist_ok=True)
            
        class PluginChangeHandler(FileSystemEventHandler):
            def on_any_event(self, event):
                if not event.is_directory and event.src_path.endswith(".py"):
                    print(f"[Plugins] Detected file change: {event.src_path}. Triggering auto hot-reload...")
                    try:
                        # Yield a tiny delay to ensure file write is completed on OS
                        time.sleep(0.2)
                        load_plugins(tool_registry)
                    except Exception as e:
                        print(f"[Plugins] Auto hot-reload failed: {e}")
                        
        event_handler = PluginChangeHandler()
        _observer = Observer()
        _observer.schedule(event_handler, plugins_dir, recursive=False)
        _observer.daemon = True
        _observer.start()
        print(f"[Plugins] Auto hot-reload daemon observer started on '{plugins_dir}'.")
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
