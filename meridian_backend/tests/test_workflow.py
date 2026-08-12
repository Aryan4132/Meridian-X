import os
import sys
import pytest

# Ensure meridian_backend root is in PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.workflow_engine import (
    create_workflow,
    get_workflow,
    list_workflows,
    delete_workflow,
    execute_workflow,
    _interpolate_variables
)


def test_workflow_crud():
    nodes = [
        {"id": "node_1", "type": "trigger_webhook", "name": "Webhook Trigger", "parameters": {}},
        {"id": "node_2", "type": "action_cloudflare", "name": "Check Cloudflare", "parameters": {"domain": "meridian.ai"}}
    ]
    edges = [{"from": "node_1", "to": "node_2"}]
    
    wf = create_workflow("Test Cloudflare Automation", nodes, edges)
    assert wf["id"].startswith("wkf_")
    assert wf["name"] == "Test Cloudflare Automation"
    
    fetched = get_workflow(wf["id"])
    assert fetched is not None
    assert len(fetched["nodes"]) == 2
    
    deleted = delete_workflow(wf["id"])
    assert deleted is True
    assert get_workflow(wf["id"]) is None


def test_variable_interpolation():
    context = {
        "node_1": {"output": {"domain": "myapp.io", "user": "admin"}}
    }
    interpolated = _interpolate_variables("Checking domain {{$node[\"node_1\"].output.domain}}", context)
    assert interpolated == "Checking domain myapp.io"


def test_workflow_execution_pipeline():
    nodes = [
        {"id": "node_1", "type": "trigger_webhook", "name": "Incoming Webhook", "parameters": {}},
        {"id": "node_2", "type": "action_cloudflare", "name": "Cloudflare Check", "parameters": {"domain": "example.org"}},
        {"id": "node_3", "type": "action_gmail", "name": "Send Alert Email", "parameters": {"to": "admin@example.org", "subject": "Domain Alert", "body": "Domain check completed."}}
    ]
    edges = [
        {"from": "node_1", "to": "node_2"},
        {"from": "node_2", "to": "node_3"}
    ]
    
    wf = create_workflow("Domain Monitor Flow", nodes, edges)
    result = execute_workflow(wf["id"], trigger_payload={"domain": "example.org"})
    
    assert result["status"] == "completed"
    assert result["executed_nodes_count"] == 3
    assert len(result["logs"]) == 3
    assert result["logs"][1]["type"] == "action_cloudflare"
    assert result["logs"][2]["type"] == "action_gmail"
    
    delete_workflow(wf["id"])
