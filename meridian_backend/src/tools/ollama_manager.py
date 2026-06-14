import threading
from database import get_ollama_client

# Dictionary to keep track of active pulling tasks: model_name -> status string
pull_status = {}

def ollama_list_models() -> str:
    """List all locally installed Ollama models."""
    try:
        client = get_ollama_client()
        res = client.list()
        models = res.get("models", [])
        if not models:
            return "No models installed in local Ollama."
        
        lines = ["Installed Ollama Models:"]
        for m in models:
            name = m.get("name", "Unknown")
            size_gb = m.get("size", 0) / (1024 ** 3)
            details = m.get("details", {})
            family = details.get("family", "Unknown")
            lines.append(f"- {name} (Size: {size_gb:.2f} GB | Family: {family})")
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing Ollama models: {e}"

def _pull_thread(model_name: str):
    try:
        pull_status[model_name] = "downloading"
        client = get_ollama_client()
        client.pull(model_name)
        pull_status[model_name] = "completed"
    except Exception as e:
        pull_status[model_name] = f"failed: {str(e)}"

def ollama_pull_model(model_name: str) -> str:
    """Download (pull) a new model from the Ollama library in the background."""
    if not model_name:
        return "Error: model_name must be specified."
    
    current = pull_status.get(model_name)
    if current == "downloading":
        return f"Model '{model_name}' is already downloading."
    
    t = threading.Thread(target=_pull_thread, args=(model_name,))
    t.daemon = True
    t.start()
    
    return f"Started background download for model '{model_name}'. You can check status via chat or status endpoints."

def ollama_delete_model(model_name: str) -> str:
    """Uninstall (delete) a local Ollama model."""
    if not model_name:
        return "Error: model_name must be specified."
    
    try:
        client = get_ollama_client()
        client.delete(model=model_name)
        return f"Successfully deleted model '{model_name}' from local Ollama."
    except Exception as e:
        return f"Error deleting model '{model_name}': {e}"
