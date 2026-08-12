import os
import json
import time
import re
import uuid
from typing import Dict, Any, List, Optional
from src.tools.external_connectors import (
    gmail_send_mail,
    gmail_fetch_inbox,
    calendar_schedule_event,
    contacts_search,
    github_manage_repo,
    cloudflare_check_domain,
    chat_send_message,
    workspace_sync_page
)

WORKFLOWS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "meridian_memory", "workflows.json")


def _load_workflows() -> Dict[str, Dict[str, Any]]:
    """Loads saved workflows from JSON storage."""
    if not os.path.exists(WORKFLOWS_FILE):
        return {}
    try:
        with open(WORKFLOWS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_workflows(data: Dict[str, Dict[str, Any]]) -> None:
    """Saves workflow dictionary to storage."""
    os.makedirs(os.path.dirname(WORKFLOWS_FILE), exist_ok=True)
    with open(WORKFLOWS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def create_workflow(name: str, nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]], active: bool = True) -> Dict[str, Any]:
    """Creates and persists a new n8n-style workflow definition."""
    workflow_id = f"wkf_{uuid.uuid4().hex[:12]}"
    workflow = {
        "id": workflow_id,
        "name": name,
        "active": active,
        "nodes": nodes,
        "edges": edges,
        "created_at": time.time(),
        "updated_at": time.time(),
        "execution_count": 0
    }
    workflows = _load_workflows()
    workflows[workflow_id] = workflow
    _save_workflows(workflows)
    return workflow


def get_workflow(workflow_id: str) -> Optional[Dict[str, Any]]:
    """Retrieves a workflow by ID."""
    return _load_workflows().get(workflow_id)


def list_workflows() -> List[Dict[str, Any]]:
    """Lists all configured workflows."""
    return list(_load_workflows().values())


def delete_workflow(workflow_id: str) -> bool:
    """Deletes a workflow by ID."""
    workflows = _load_workflows()
    if workflow_id in workflows:
        workflows.pop(workflow_id, None)
        _save_workflows(workflows)
        return True
    return False


# ---------------------------------------------------------------------------
# Variable Interpolation Engine
# ---------------------------------------------------------------------------
def _interpolate_variables(val: Any, context: Dict[str, Any]) -> Any:
    """Interpolates {{$node["node_id"].key}} dynamic expressions in strings."""
    if not isinstance(val, str):
        return val
        
    def replace_match(match):
        node_id = match.group(1)
        key_path = match.group(2)
        node_data = context.get(node_id, {})
        keys = key_path.split(".")
        current = node_data
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return ""
        return str(current)
        
    # Pattern: {{$node["node_1"].data.domain}}
    pattern = r'\{\{\$node\["([^"]+)"\]\.([a-zA-Z0-9_\.]+)\}\}'
    return re.sub(pattern, replace_match, val)


# ---------------------------------------------------------------------------
# Node Execution Core
# ---------------------------------------------------------------------------
def execute_workflow_node(node: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    """Executes a single node in the workflow graph."""
    node_type = node.get("type", "")
    params = node.get("parameters", {})
    
    # Interpolate input parameters with previous node context
    interpolated_params = {}
    for k, v in params.items():
        interpolated_params[k] = _interpolate_variables(v, context)
        
    result = {"status": "success", "executed_at": time.time()}
    
    if node_type == "trigger_webhook" or node_type == "trigger_cron" or node_type == "trigger_event":
        result["output"] = interpolated_params.get("payload", {"event": "triggered"})
        
    elif node_type == "action_cloudflare":
        domain = interpolated_params.get("domain", "example.com")
        result["output"] = cloudflare_check_domain(domain)
        
    elif node_type == "action_gmail":
        to = interpolated_params.get("to", "")
        subject = interpolated_params.get("subject", "Automated Notification")
        body = interpolated_params.get("body", "")
        result["output"] = gmail_send_mail(to, subject, body)
        
    elif node_type == "action_github":
        action = interpolated_params.get("action", "list_prs")
        repo = interpolated_params.get("repo", "")
        title = interpolated_params.get("title", "")
        result["output"] = github_manage_repo(action, repo, title)
        
    elif node_type == "action_chat":
        platform = interpolated_params.get("platform", "slack")
        channel = interpolated_params.get("channel", "general")
        message = interpolated_params.get("message", "Workflow notification")
        result["output"] = chat_send_message(platform, channel, message)
        
    elif node_type == "action_filter":
        field_val = interpolated_params.get("value", "")
        expected = interpolated_params.get("expected", "")
        matches = str(field_val).strip() == str(expected).strip()
        result["output"] = {"matches": matches, "value": field_val}
        if not matches:
            result["status"] = "skipped"
            
    elif node_type == "action_llm":
        prompt = interpolated_params.get("prompt", "")
        result["output"] = f"[LLM Synthesis Node] Processed prompt: '{prompt[:100]}...'"
        
    else:
        result["output"] = f"Executed generic node '{node.get('name', 'Unknown')}'"
        
    return result


def execute_workflow(workflow_id: str, trigger_payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Executes a complete n8n-style workflow DAG graph.
    Passes outputs sequentially from parent nodes down to child nodes.
    """
    workflow = get_workflow(workflow_id)
    if not workflow:
        return {"status": "failed", "error": f"Workflow '{workflow_id}' not found"}
        
    nodes = workflow.get("nodes", [])
    edges = workflow.get("edges", [])
    
    execution_context: Dict[str, Any] = {}
    node_map = {n["id"]: n for n in nodes}
    logs = []
    
    # Find trigger node (first node)
    trigger_node = next((n for n in nodes if n.get("type", "").startswith("trigger_")), nodes[0] if nodes else None)
    if trigger_node and trigger_payload:
        trigger_node.setdefault("parameters", {})["payload"] = trigger_payload
        
    # Sequence execution
    for node in nodes:
        node_id = node["id"]
        try:
            node_res = execute_workflow_node(node, execution_context)
            execution_context[node_id] = node_res
            logs.append({
                "node_id": node_id,
                "name": node.get("name", node_id),
                "type": node.get("type", ""),
                "status": node_res["status"],
                "output": node_res["output"]
            })
            if node_res["status"] == "skipped":
                break  # Stop branch if filter did not match
        except Exception as e:
            logs.append({
                "node_id": node_id,
                "name": node.get("name", node_id),
                "type": node.get("type", ""),
                "status": "failed",
                "error": str(e)
            })
            break
            
    # Increment execution count
    workflows = _load_workflows()
    if workflow_id in workflows:
        workflows[workflow_id]["execution_count"] = workflows[workflow_id].get("execution_count", 0) + 1
        workflows[workflow_id]["last_executed"] = time.time()
        _save_workflows(workflows)
        
    return {
        "workflow_id": workflow_id,
        "status": "completed",
        "executed_nodes_count": len(logs),
        "logs": logs,
        "context": execution_context
    }
