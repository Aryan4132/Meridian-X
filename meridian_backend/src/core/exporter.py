import os
import time
from typing import Dict, Any, List
from database import get_sqlite_conn

def export_session_runbook(output_path: str, format_type: str = "md") -> str:
    # 1. Load conversation items from SQLite
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, role, content, summary FROM conversations ORDER BY timestamp ASC")
        rows = cursor.fetchall()
        conv_items = []
        for r in rows:
            conv_items.append({
                "id": str(r["id"]),
                "timestamp": r["timestamp"],
                "role": r["role"],
                "content": r["content"],
                "summary": r["summary"]
            })
    except Exception as e:
        conv_items = []
        print("[Exporter] Failed to load conversations:", e)
    finally:
        if conn:
            conn.close()  # BUG-61 fix: always close connection
        
    # 2. Load execution task log logs
    conn = None
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, tool, tier, outcome, error FROM task_log ORDER BY timestamp ASC")
        rows = cursor.fetchall()
        log_items = []
        for r in rows:
            log_items.append({
                "id": r["id"],
                "timestamp": r["timestamp"],
                "tool": r["tool"],
                "tier": r["tier"],
                "outcome": r["outcome"],
                "error": r["error"]
            })
    except Exception as e:
        log_items = []
        print("[Exporter] Failed to load task logs:", e)
    finally:
        if conn:
            conn.close()  # BUG-61 fix: always close connection

    if format_type.lower() == "md":
        content = generate_markdown(conv_items, log_items)
    else:
        content = generate_html(conv_items, log_items)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Successfully exported session runbook ({format_type.upper()}) to {output_path}"

def generate_markdown(convs: List[Dict[str, Any]], logs: List[Dict[str, Any]]) -> str:
    lines = [
        "# Meridian-X: Autonomous Session Runbook",
        f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}",
        "\n## 💬 Conversation Summary\n"
    ]
    
    for item in convs:
        if item.get("id") == "init":
            continue
        role_title = "Meridian Assistant" if item.get("role") == "assistant" else "User"
        timestamp = time.strftime('%H:%M:%S', time.localtime(item.get("timestamp", 0.0)))
        lines.append(f"### **{role_title}** [{timestamp}]")
        lines.append(f"{item.get('content')}\n")
        
    lines.append("\n## ⚙️ Core Action Logs")
    lines.append("| Timestamp | Tool Executed | Safety Tier | Outcome | Error Message |")
    lines.append("|---|---|---|---|---|")
    
    for item in logs:
        if item.get("id") == "init":
            continue
        timestamp = time.strftime('%H:%M:%S', time.localtime(item.get("timestamp", 0.0)))
        err = item.get("error", "")
        lines.append(f"| {timestamp} | `{item.get('tool')}` | Tier {item.get('tier')} | **{item.get('outcome').upper()}** | {err if err else '-'} |")
        
    return "\n".join(lines)

def generate_html(convs: List[Dict[str, Any]], logs: List[Dict[str, Any]]) -> str:
    md_content = generate_markdown(convs, logs)
    # Simple markdown-to-html conversion for standard elements
    html_lines = [
        "<html>",
        "<head>",
        "<title>Meridian Session Export</title>",
        "<style>",
        "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; margin: 40px; background: #0c0c0e; color: #e2e8f0; }",
        "h1, h2, h3 { color: #ea580c; }",
        "table { width: 100%; border-collapse: collapse; margin-top: 20px; }",
        "th, td { border: 1px solid #27272a; padding: 12px; text-align: left; }",
        "th { background: #18181b; }",
        "tr:nth-child(even) { background: #121214; }",
        "code { background: #1a1a1e; padding: 3px 6px; border-radius: 4px; font-family: monospace; }",
        "</style>",
        "</head>",
        "<body>"
    ]
    
    for line in md_content.split('\n'):
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("|"):
            # Table conversion
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if not parts or all(p.startswith('-') for p in parts):
                continue
            if "Tool Executed" in line:
                html_lines.append("<table><thead><tr>" + "".join(f"<th>{p}</th>" for p in parts) + "</tr></thead><tbody>")
            else:
                html_lines.append("<tr>" + "".join(f"<td>{p}</td>" for p in parts) + "</tr>")
        elif line.strip():
            html_lines.append(f"<p>{line}</p>")
            
    html_lines.append("</tbody></table>" if "<table>" in "".join(html_lines) else "")
    html_lines.append("</body></html>")
    return "\n".join(html_lines)
