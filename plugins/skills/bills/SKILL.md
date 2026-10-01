---
name: bills
version: 1.0.0
description: Recurring-bill radar and due-date tracking.
keywords: [bill, bills, invoice, due, recurring, payment due, subscription bill]
---

# Bills Skill

Tracks recurring bills and surfaces what is due. Loaded lazily when the
user mentions bills, invoices, or due payments.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `register_recurring_bill` | 1 | Register a recurring bill (name, amount, cadence). |
| `get_bill_due_radar` | 0 | List upcoming due bills. |
