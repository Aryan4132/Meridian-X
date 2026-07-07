import os
import importlib
import importlib.util
import inspect
import sys
from typing import Dict, Any, Callable

def load_plugins(tool_registry: Dict[str, Dict[str, Any]]):
    """Loads all public functions in Python files under root/plugins/ into the tool registry."""
    # BUG-60 fix: use find_workspace_root() for consistent directory resolution.
    try:
        from src.core.history_manager import find_workspace_root
        plugins_dir = os.path.join(find_workspace_root(), "plugins")
    except Exception:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(backend_dir)
        plugins_dir = os.path.join(root_dir, "plugins")
    
    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir, exist_ok=True)
        # Create an example plugin
        example_path = os.path.join(plugins_dir, "example_plugin.py")
        with open(example_path, "w", encoding="utf-8") as f:
            f.write('''# Example Plugin
TIER = 1

async def custom_echo_tool(text: str) -> str:
    """A custom echo tool that returns your text reversed."""
    return f"Echo from plugin: {text[::-1]}"
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
                    
                # Read tier
                tier = getattr(module, "TIER", 1)
                
                # Find functions
                for attr_name in dir(module):
                    if attr_name.startswith("_"):
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

def reload_dynamic_plugins(tool_registry: Dict[str, Dict[str, Any]]) -> str:
    """Reload all dynamic plugins in the plugins/ folder and register any new tools."""
    try:
        load_plugins(tool_registry)
        return "Successfully reloaded all plugins. Any new functions in plugins/ have been registered into the TOOL_REGISTRY."
    except Exception as e:
        return f"Failed to reload plugins: {e}"
