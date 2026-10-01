---
name: hardening
version: 1.0.0
description: Phishing, password, network, USB, DNS, camera, and Wi-Fi auditing.
keywords: [phishing, phish, password, totp, 2fa, wifi, wi-fi, dns, usb, sandbox, audit, malware, camera access, mic access, virus, scam, breach]
---

# Hardening Skill

Security auditing and phishing defense. Loaded lazily on security,
audit, or safety prompts.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `check_url_reputation` | 0 | Check a URL for phishing risk. |
| `generate_totp_code` | 0 | Generate a TOTP 2FA code. |
| `audit_password_strength` | 0 | Audit password strength. |
| `assess_wifi_security` | 1 | Assess Wi-Fi security posture. |
| `audit_network_boundary` | 0 | Audit network boundary. |
| `audit_usb_peripherals` | 0 | Audit connected USB devices. |
| `audit_dns_health` | 0 | Audit DNS health. |
| `audit_camera_mic_access` | 0 | Audit camera/mic access. |
| `detonate_attachment_sample` | 2 | Sandbox-detonate a suspicious file. |
