import socket
import subprocess
import re
import os
from typing import List, Dict, Any
from src.core.history_manager import find_workspace_root

def get_all_interfaces_listening_ports() -> set:
    """Run netstat to find which ports are listening on all interfaces (0.0.0.0 or [::])."""
    ports = set()
    try:
        # Run netstat -ano safely on Windows
        res = subprocess.run(["netstat", "-ano"], capture_output=True, text=True, check=True)
        for line in res.stdout.splitlines():
            line = line.strip()
            if "listening" in line.lower() or "list" in line.lower():
                parts = line.split()
                if len(parts) >= 2:
                    local_addr = parts[1]
                    if ":" in local_addr:
                        host, port_str = local_addr.rsplit(":", 1)
                        if host == "0.0.0.0" or host == "[::]":
                            try:
                                ports.add(int(port_str))
                            except ValueError:
                                pass
    except Exception as e:
        print("[Security Auditor] Netstat analysis failed:", e)
    return ports

def run_port_scan() -> List[Dict[str, Any]]:
    """Scan local ports and list active services, flagging external bindings."""
    # Ports to scan: standard network ports + common development local servers
    ports_to_scan = list(range(1, 1025)) + [3000, 4132, 5000, 5173, 8000, 8080, 27017, 11434]
    open_ports = []
    
    # Get all ports bound to 0.0.0.0 (externally accessible)
    public_ports = get_all_interfaces_listening_ports()
    
    for port in ports_to_scan:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.05) # quick timeout
                result = s.connect_ex(("127.0.0.1", port))
                if result == 0:
                    is_public = port in public_ports
                    # Try to infer service name
                    try:
                        service = socket.getservbyport(port)
                    except Exception:
                        if port == 3000: service = "React Dev Server / Node"
                        elif port == 4132: service = "FastAPI Backend / Uvicorn"
                        elif port == 5173: service = "Vite Dev Server"
                        elif port == 8000: service = "FastAPI Backend / Uvicorn (Legacy)"
                        elif port == 11434: service = "Ollama Local LLM API"
                        elif port == 27017: service = "MongoDB Server"
                        else: service = "Unknown Service"
                        
                    open_ports.append({
                        "port": port,
                        "service": service,
                        "binding": "0.0.0.0 (Public)" if is_public else "127.0.0.1 (Local Only)",
                        "severity": "medium" if is_public else "info"
                    })
        except Exception:
            pass
            
    return open_ports

def run_credential_leak_check() -> List[Dict[str, Any]]:
    """Scan the workspace source files for potential hardcoded API keys or credentials."""
    root = find_workspace_root()
    leaks = []
    
    # Credential patterns
    patterns = {
        "Generic Secret/Password": re.compile(r'(?i)(api_key|apikey|secret|password|passwd|token|bearer|signature)\s*[:=]\s*["\']?[A-Za-z0-9_\-\.+=]{16,}["\']?'),
        "AWS Secret Key": re.compile(r'(?i)(aws_secret_access_key|aws_key|aws_token)\s*[:=]\s*["\']?[A-Za-z0-9/+=]{40}["\']?'),
        "Private Key": re.compile(r'-----BEGIN [A-Z ]+ PRIVATE KEY-----'),
        "Database Credentials URL": re.compile(r'(mongodb\+srv|mysql|postgresql)://([^:]+):([^@]+)@'),
    }
    
    skip_dirs = {".git", "node_modules", "venv", "dist", "__pycache__", ".codegraph", ".antigravitycli"}
    
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for filename in filenames:
            if filename.endswith((".png", ".jpg", ".jpeg", ".ico", ".db", ".onnx", ".tflite", ".pdf", ".zip", ".tar.gz", ".exe", ".dll", ".pyd")):
                continue
                
            filepath = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(filepath, root)
            
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        for name, pat in patterns.items():
                            match = pat.search(line)
                            if match:
                                full_match = match.group(0).strip()
                                # Mask the sensitive value for display safety
                                if len(full_match) > 10:
                                    masked = full_match[:len(full_match)//3] + "..." + full_match[-len(full_match)//6:]
                                else:
                                    masked = "...hidden..."
                                leaks.append({
                                    "file": relative_path.replace("\\", "/"),
                                    "line": line_num,
                                    "type": name,
                                    "match": masked
                                })
            except Exception:
                pass
                
    return leaks

def run_security_audit() -> str:
    """Run both port scanning and credentials leak checks, returning a formatted markdown report."""
    ports = run_port_scan()
    leaks = run_credential_leak_check()
    
    lines = ["# Desktop Security Diagnostic Audit Report", ""]
    
    # Ports section
    lines.append("## Active Listening Port Scan")
    if not ports:
        lines.append("No active dev ports or listening ports discovered in range.")
    else:
        lines.append("| Port | Service / Binding | Access Scope | Severity |")
        lines.append("| --- | --- | --- | --- |")
        for p in ports:
            sev_badge = "⚠️ Medium" if p["severity"] == "medium" else "🟢 Low"
            lines.append(f"| {p['port']} | {p['service']} | {p['binding']} | {sev_badge} |")
    lines.append("")
    
    # Credentials leak section
    lines.append("## Source Code Credentials Leak Scan")
    if not leaks:
        lines.append("🟢 Zero hardcoded keys or passwords detected in active workspace files.")
    else:
        lines.append("| File Path | Line | Leak Type | Masked Value | Severity |")
        lines.append("| --- | --- | --- | --- | --- |")
        for l in leaks:
            lines.append(f"| [{l['file']}](file:///{l['file']}) | {l['line']} | {l['type']} | `{l['match']}` | 🔴 High |")
            
    return "\n".join(lines)
