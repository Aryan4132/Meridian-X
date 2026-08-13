"""
test_day3_features.py — Unit Tests for Day 3 Roadmap Features (WAP-01, WAP-02, WAP-03, PL-12, SEC-27, JARVIS-07, PL-18)
"""

import pytest
from database import save_whatsapp_contact, get_whatsapp_contacts, resolve_whatsapp_contact
from src.tools.whatsapp_manager import manage_whatsapp_contacts, read_whatsapp_messages, list_whatsapp_chats
from src.tools.communication import send_whatsapp_message, send_native_toast_notification
from src.core.loop import check_approval_gate, active_confirmations
from src.core.sandbox_runner import run_sandboxed_command
from src.core.system_defense import get_system_health_status, purge_system_caches, isolate_rogue_processes

def test_whatsapp_contact_directory():
    # 1. Save contact
    saved = save_whatsapp_contact(name="Mom", phone_number="+1234567890", alias="Mother")
    assert saved["name"] == "Mom"
    assert saved["phone_number"] == "+1234567890"

    # 2. List contacts
    contacts = get_whatsapp_contacts()
    assert any(c["name"] == "Mom" for c in contacts)

    # 3. Resolve contact by alias
    res_alias = resolve_whatsapp_contact("Mother")
    assert res_alias is not None
    assert res_alias["name"] == "Mom"

    # 4. Resolve contact by exact name (case-insensitive)
    res_name = resolve_whatsapp_contact("mom")
    assert res_name is not None
    assert res_name["phone_number"] == "+1234567890"

def test_whatsapp_manager_tool_wrapper():
    res_add = manage_whatsapp_contacts(action="add", name="Boss", phone_number="+9876543210", alias="Manager")
    assert "Saved WhatsApp contact" in res_add

    res_list = manage_whatsapp_contacts(action="list")
    assert "Boss" in res_list

    res_resolve = manage_whatsapp_contacts(action="resolve", name="Manager")
    assert "Resolved contact" in res_resolve

from src.tools.whatsapp_manager import manage_whatsapp_contacts, read_whatsapp_messages, list_whatsapp_chats, login_whatsapp_session

def test_whatsapp_read_and_list_tools():
    read_res = read_whatsapp_messages(contact="Mom", limit=3)
    assert "WhatsApp Message Puller" in read_res or "Recent WhatsApp messages" in read_res

    list_res = list_whatsapp_chats()
    assert "Mom" in list_res or "Active WhatsApp Contact Directory" in list_res

def test_login_whatsapp_session_import():
    assert callable(login_whatsapp_session)

def test_send_whatsapp_message_resolution():
    msg_res = send_whatsapp_message(contact="Mom", message="Hello Mom!")
    assert "Mom" in msg_res

def test_native_toast_notification():
    res = send_native_toast_notification(title="Test Alert", message="Unit test notification")
    assert "notification" in res.lower()

def test_approval_gate_evaluator():
    requires_approval, reason = check_approval_gate("delete_file", {"filepath": "important.txt"})
    assert requires_approval is True
    assert "delete_file" in reason

    requires_cmd, reason_cmd = check_approval_gate("nl_run", {"natural_language": "rm -rf /tmp"})
    assert requires_cmd is True
    assert "dangerous command" in reason_cmd.lower()

    safe_req, _ = check_approval_gate("read_file", {"filepath": "readme.txt"})
    assert safe_req is False

def test_sandbox_runner():
    code, stdout, stderr = run_sandboxed_command("echo 'Sandbox Test'")
    assert code == 0
    assert "Sandbox Test" in stdout or "Sandbox" in stdout

def test_system_defense_governor():
    health = get_system_health_status()
    assert "cpu_percent" in health
    assert "ram_percent" in health
    assert "is_healthy" in health

    purge_res = purge_system_caches()
    assert "gc_objects_purged" in purge_res
    assert "new_ram_percent" in purge_res

    rogue = isolate_rogue_processes()
    assert isinstance(rogue, list)
