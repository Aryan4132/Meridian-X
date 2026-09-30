"""
Unit tests for Day 13 Network & Boundary Security features.
"""

import pytest
from src.tools.phishing_guard import check_url_reputation
from src.tools.totp_generator import generate_totp_code
from src.tools.password_auditor import audit_password_strength
from src.tools.network_guardian import audit_network_boundary
from src.tools.usb_watchdog import audit_usb_peripherals
from src.tools.dns_shield import audit_dns_health
from src.tools.cam_guard import audit_camera_mic_access
from src.tools.detonation_sandbox import detonate_attachment_sample

def test_phishing_guard():
    safe_res = check_url_reputation("https://google.com")
    assert "Safe" in safe_res

    phish_res = check_url_reputation("http://secure-bank-login-verify.xyz")
    assert "PHISHING ALERT" in phish_res

def test_totp_generator():
    totp = generate_totp_code("JBSWY3DPEHPK3PXP")
    assert "TOTP 2FA Code" in totp

def test_password_auditor():
    res = audit_password_strength("Short1!")
    assert "Password Health Audit" in res

def test_network_guardian():
    res = audit_network_boundary()
    assert "Network Guardian Status Report" in res

def test_usb_watchdog():
    res = audit_usb_peripherals()
    assert "USB Watchdog Sentinel Status" in res

def test_dns_shield():
    res = audit_dns_health()
    assert "DNS Shield Status" in res

def test_cam_guard():
    res = audit_camera_mic_access()
    assert "Cam & Mic Access Guard Status" in res

def test_detonation_sandbox():
    res = detonate_attachment_sample("invoice.pdf.exe")
    assert "HIGH RISK" in res
