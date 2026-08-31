import os
import sys
import pytest

# Ensure backend root is on Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from src.core.emergency_lockdown import trigger_emergency_lockdown, verify_and_unlock, get_lockdown_status, set_lockdown_pin
from src.core.vault import freeze_vault, unfreeze_vault, is_vault_frozen, get_secret, save_secret
from src.core.fim_sentinel import deploy_canaries, check_canaries, get_canary_registry
from src.core.behavior_monitor import scan_process_behavior
from src.core.system_defense import trigger_defense_lockdown, run_edr_process_scan
from src.core.malware_scanner import scan_file, quarantine_file, scan_file_and_quarantine, restore_quarantined_file, calculate_entropy
from src.tools.filesystem import write_file
from src.core.breach_sentinel import check_password_breach, audit_account_breaches, monitor_darkweb_keywords
from src.core.persistence_sentinel import build_persistence_baseline, audit_persistence, rollback_persistence_entry


def test_emergency_lockdown():
    """Verify SEC-34 Emergency Lockdown mode state transitions and vault freezing."""
    set_lockdown_pin("9999")
    
    # 1. Trigger Lockdown
    res = trigger_emergency_lockdown(pin="9999")
    assert res["status"] == "LOCKED"
    assert res["network_isolated"] is True
    assert res["vault_frozen"] is True
    assert is_vault_frozen() is True

    # 2. Assert Vault access is blocked while frozen
    os.environ["MERIDIAN_VAULT_PASSPHRASE"] = "TestPassphrase123!"
    with pytest.raises(PermissionError, match="Vault is frozen"):
        get_secret("test_key")

    # 3. Unlock with invalid PIN -> fails
    failed_unlock = verify_and_unlock("1111")
    assert failed_unlock["status"] == "FAILED"
    assert is_vault_frozen() is True

    # 4. Unlock with correct PIN -> succeeds
    success_unlock = verify_and_unlock("9999")
    assert success_unlock["status"] == "SUCCESS"
    assert is_vault_frozen() is False
    assert get_lockdown_status()["is_locked"] is False


def test_system_defense_lockdown_helper():
    """Verify system_defense helper for Emergency Lockdown."""
    res = trigger_defense_lockdown(pin="4321")
    assert res["status"] == "LOCKED"
    verify_and_unlock("4321")


def test_ransomware_canary_tripwire(tmp_path):
    """Verify SEC-31 Ransomware Canary deployment and tampering tripwire."""
    test_dir = str(tmp_path / "canary_test")
    os.makedirs(test_dir, exist_ok=True)

    # 1. Deploy canaries
    deployed = deploy_canaries(target_directories=[test_dir])
    assert len(deployed) >= 3
    
    # 2. Check intact canaries
    scan_clean = check_canaries()
    assert scan_clean["tripwire_triggered"] is False
    assert len(scan_clean["tampered_files"]) == 0

    # 3. Tamper with a canary file
    tampered_target = deployed[0]
    with open(tampered_target, "wb") as f:
        f.write(b"RANSOMWARE_ENCRYPTED_DATA_LOCK_123")

    # 4. Scan again -> tripwire fires
    scan_tripped = check_canaries()
    assert scan_tripped["tripwire_triggered"] is True
    assert tampered_target in scan_tripped["tampered_files"]


def test_edr_behavior_monitor():
    """Verify SEC-37 Process Behavior Monitoring and scanning."""
    scan_res = scan_process_behavior(auto_quarantine=False)
    assert "flagged_threats_count" in scan_res
    assert "threats" in scan_res
    assert isinstance(scan_res["threats"], list)

    edr_res = run_edr_process_scan(auto_quarantine=False)
    assert "flagged_threats_count" in edr_res


def test_malware_scanner_and_quarantine(tmp_path):
    """Verify SEC-36 Signature scanner, entropy calculation, and AES-quarantine."""
    # 1. Entropy calculation check
    random_bytes = os.urandom(1000)
    high_entropy = calculate_entropy(random_bytes)
    assert high_entropy > 7.0

    # 2. Create malicious payload file
    malware_file = str(tmp_path / "suspicious_payload.ps1")
    with open(malware_file, "wb") as f:
        f.write(b"powershell -nop -w hidden -e aW52b2tlLWV4cHJlc3Npb24=")

    # 3. Scan file
    scan_res = scan_file(malware_file)
    assert scan_res["is_threat"] is True
    assert any("malware signature" in r for r in scan_res["threat_reasons"])

    # 4. Quarantine file
    quarantine_res = scan_file_and_quarantine(malware_file)
    assert quarantine_res["status"] == "QUARANTINED"
    assert not os.path.exists(malware_file)
    assert os.path.exists(quarantine_res["quarantine_path"])

    # 5. Restore file
    restored = restore_quarantined_file(quarantine_res["quarantine_path"], malware_file)
    assert restored is True
    assert os.path.exists(malware_file)


def test_filesystem_write_malware_hook(tmp_path):
    """Verify SEC-36 integration in filesystem write_file."""
    bad_file = str(tmp_path / "bad_script.vbs")
    bad_content = "WScript.Shell powershell -nop -w hidden"
    result = write_file(bad_file, bad_content)
    assert "WARNING" in result or "quarantine" in result.lower()


def test_breach_sentinel():
    """Verify SEC-28 Breach & Leak Sentinel HIBP k-anonymity and email auditing."""
    # 1. Known breached password check (password123)
    pwned_res = check_password_breach("password123")
    assert pwned_res["is_breached"] is True
    assert pwned_res["breach_count"] > 0
    assert pwned_res["sha1_prefix"] == "CBFDA"

    # 2. Email breach audit
    email_res = audit_account_breaches("test_leaked@domain.com")
    assert email_res["is_compromised"] if "is_compromised" in email_res else email_res["is_breached"] is True

    # 3. Darkweb keyword monitor
    darkweb_res = monitor_darkweb_keywords(["company_secret_leak"])
    assert len(darkweb_res) > 0
    assert darkweb_res[0]["keyword"] == "company_secret_leak"


def test_persistence_autoruns_sentinel():
    """Verify SEC-38 Persistence Sentinel baseline and audit routines."""
    baseline = build_persistence_baseline()
    assert isinstance(baseline, dict)

    audit_res = audit_persistence()
    assert "threats_found" in audit_res
    assert "baseline_count" in audit_res

    # Test rollback
    dummy_entry_id = "startup:dummy_threat.exe"
    rollback_res = rollback_persistence_entry(dummy_entry_id)
    assert rollback_res["status"] == "FAILED"
