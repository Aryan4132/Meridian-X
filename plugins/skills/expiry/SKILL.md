---
name: expiry
version: 1.0.0
description: Expiry sentinel for passports, visas, licenses, and insurance.
keywords: [expiry, expire, expiring, passport, visa, license expiry, insurance expiry, renewal, renew]
---

# Expiry Skill

Watches time-sensitive documents and warns before they lapse. Loaded
lazily on expiry, renewal, or document-deadline prompts.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `add_expiry_document` | 1 | Register a document with its expiry date. |
| `check_document_expiries` | 0 | Check which documents expire soon. |
| `list_expiry_documents` | 0 | List all tracked documents. |
