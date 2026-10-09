import os
import shutil
import subprocess
import webbrowser
import logging
import platform
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)

DEFAULT_PRESETS: Dict[str, Dict[str, Any]] = {
    "coding": {
        "apps": ["code"],
        "docker": True,
        "docs": ["https://fastapi.tiangolo.com", "https://react.dev"],
        "media": "https://open.spotify.com/genre/focus"
    },
    "research": {
        "apps": [],
        "docker": False,
        "docs": ["https://arxiv.org", "https://github.com/trending"],
        "media": "https://open.spotify.com/genre/focus"
    },
    "debugging": {
        "apps": ["code"],
        "docker": True,
        "docs": ["http://localhost:8000/docs", "https://developer.mozilla.org"],
        "media": None
    },
    "focus": {
        "apps": ["code"],
        "docker": False,
        "docs": [],
        "media": "https://open.spotify.com/genre/focus"
    }
}

class WorkspaceOrchestrator:
    """
    Seamless Multi-App Orchestration (⚙️)
    Launches developer tools, databases, documentation URLs, and media apps simultaneously.
    """
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root
        self._presets: Dict[str, Dict[str, Any]] = dict(DEFAULT_PRESETS)
        self._active_processes: List[subprocess.Popen] = []

    def register_preset(self, name: str, config: Dict[str, Any]) -> None:
        """Registers or overrides a named workspace preset."""
        self._presets[name.lower()] = config

    def get_presets(self) -> List[str]:
        """Lists all registered preset names."""
        return list(self._presets.keys())

    def launch_preset(self, preset_name: str = "coding") -> Dict[str, Any]:
        """Launches a full developer workspace environment."""
        p_name = (preset_name or "coding").lower()
        preset_cfg = self._presets.get(p_name, self._presets["coding"])

        results = {
            "preset": p_name,
            "actions": [],
            "status": "success"
        }

        # 1. Launch Applications (e.g. VS Code)
        for app in preset_cfg.get("apps", []):
            if app == "code":
                code_bin = shutil.which("code") or shutil.which("code.cmd")
                if not code_bin:
                    results["actions"].append({
                        "app": "VS Code",
                        "status": "skipped",
                        "reason": "VS Code CLI ('code') not found in PATH"
                    })
                else:
                    try:
                        if platform.system() == "Windows":
                            proc = subprocess.Popen(["cmd.exe", "/c", code_bin, self.workspace_root], shell=False)
                        else:
                            proc = subprocess.Popen([code_bin, self.workspace_root])
                        self._active_processes.append(proc)
                        results["actions"].append({"app": "VS Code", "status": "launched", "path": self.workspace_root})
                    except Exception as e:
                        results["actions"].append({"app": "VS Code", "status": "failed", "error": str(e)})

        # 2. Launch Local Database / Docker Container
        if preset_cfg.get("docker", False):
            docker_compose_path = os.path.join(self.workspace_root, "docker-compose.yml")
            docker_bin = shutil.which("docker")
            if not docker_bin:
                results["actions"].append({"app": "Docker Compose", "status": "skipped", "reason": "Docker CLI not found in PATH"})
            elif os.path.exists(docker_compose_path):
                try:
                    proc = subprocess.Popen([docker_bin, "compose", "up", "-d"], cwd=self.workspace_root, shell=False)
                    self._active_processes.append(proc)
                    results["actions"].append({"app": "Docker Compose", "status": "launched"})
                except Exception as e:
                    results["actions"].append({"app": "Docker Compose", "status": "failed", "error": str(e)})
            else:
                results["actions"].append({"app": "Local DB", "status": "skipped", "reason": "No docker-compose file"})

        # 3. Open Documentation in Browser
        doc_urls = preset_cfg.get("docs", [])
        if doc_urls:
            try:
                for url in doc_urls:
                    webbrowser.open(url)
                results["actions"].append({"app": "Browser Docs", "status": "opened", "urls": doc_urls})
            except Exception as e:
                results["actions"].append({"app": "Browser Docs", "status": "failed", "error": str(e)})

        # 4. Open Spotify / Media
        media_url = preset_cfg.get("media")
        if media_url:
            try:
                webbrowser.open(media_url)
                results["actions"].append({"app": "Media Focus", "status": "opened", "url": media_url})
            except Exception as e:
                results["actions"].append({"app": "Media Focus", "status": "failed", "error": str(e)})

        return results

    def stop_preset(self, preset_name: Optional[str] = None) -> Dict[str, Any]:
        """Stops active spawned processes and tears down services."""
        stopped = 0
        errors = []

        # Terminate tracked child processes
        for proc in list(self._active_processes):
            try:
                if proc.poll() is None:
                    proc.terminate()
                    stopped += 1
            except Exception as e:
                errors.append(str(e))
        self._active_processes.clear()

        # If docker compose exists, stop containers
        docker_compose_path = os.path.join(self.workspace_root, "docker-compose.yml")
        if shutil.which("docker") and os.path.exists(docker_compose_path):
            try:
                subprocess.run(["docker", "compose", "down"], cwd=self.workspace_root, shell=True, timeout=10)
            except Exception as e:
                logger.warning(f"Error stopping docker-compose: {e}")

        return {
            "status": "stopped",
            "processes_terminated": stopped,
            "errors": errors
        }

