"""
DNS Filter & Web Shield (SEC-39)
DNS resolver health check and hosts-file hijack detection.
NOTE: there is no local domain-signature blocklist or DoH enforcement in this
build — this tool reports live system state only, never fabricated coverage.
"""

import os
import re
import socket
import time
from typing import Dict, Any, List


def _parse_hosts_file(hosts_path: str) -> List[Dict[str, str]]:
    """Returns active (non-comment, non-blank) hosts entries."""
    entries: List[Dict[str, str]] = []
    try:
        with open(hosts_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    entries.append({"ip": parts[0], "hosts": " ".join(parts[1:])})
    except OSError:
        pass
    return entries


def _find_suspicious_redirects(entries: List[Dict[str, str]]) -> List[str]:
    """Flags entries mapping well-known domains to non-local IPs."""
    suspicious: List[str] = []
    local_ips = {"127.0.0.1", "::1", "0.0.0.0"}
    watched = (
        "google", "microsoft", "apple", "facebook", "amazon", "github",
        "bank", "paypal", "login", "account", "windowsupdate",
    )
    for entry in entries:
        names = entry["hosts"].lower()
        if entry["ip"] not in local_ips and any(w in names for w in watched):
            suspicious.append(f"{entry['hosts']} -> {entry['ip']}")
    return suspicious


def audit_dns_health() -> str:
    """
    Check DNS resolver health (live resolution probe) and hosts-file integrity
    (entry inventory + suspicious-redirect scan).
    """
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == "nt" else "/etc/hosts"

    # 1. Live resolver probe
    resolve_status = "Unverified"
    probe_ms: Any = "n/a"
    resolved_ip = ""
    try:
        start = time.time()
        resolved_ip = socket.gethostbyname("example.com")
        probe_ms = round((time.time() - start) * 1000.0, 1)
        resolve_status = f"OK (example.com -> {resolved_ip} in {probe_ms} ms)"
    except Exception as e:
        resolve_status = f"FAILED ({e})"

    # 2. Hosts-file integrity (real parse, not a hardcoded verdict)
    hosts_status = "Default System Config"
    suspicious: List[str] = []
    try:
        entries = _parse_hosts_file(hosts_path)
        mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(hosts_path)))
        suspicious = _find_suspicious_redirects(entries)
        if suspicious:
            hosts_status = (
                f"HIJACK SUSPECT — {len(suspicious)} redirect(s), modified {mtime}"
            )
        else:
            hosts_status = (
                f"Intact — {len(entries)} active entr{'y' if len(entries) == 1 else 'ies'}, "
                f"modified {mtime}"
            )
    except OSError as e:
        hosts_status = f"Unreadable ({e})"

    lines = [
        "DNS Shield Status (live system state):",
        f"- Resolver Probe: {resolve_status}",
        f"- Hosts File Integrity: {hosts_status}",
        "- Local Blocklist: Not deployed in this build",
        "- DNS-over-HTTPS: System default (not enforced by Meridian-X)",
    ]
    if suspicious:
        lines.append("- Suspicious Redirects:")
        lines.extend(f"  ! {s}" for s in suspicious[:20])
    return "\n".join(lines)
