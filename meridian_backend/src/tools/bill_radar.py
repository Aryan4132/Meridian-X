"""
Bill-Due Radar & Cashflow Calendar (BUTLER-10)
Recurring-bill register, pre-debit reminders, and anomalous subscription fee alerts.
"""

import os
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

from src.core.atomic_storage import atomic_write_json, safe_load_json

BILLS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "bills.json")

def _load_bills() -> List[Dict[str, Any]]:
    return safe_load_json(BILLS_FILE, default=[])

def _save_bills(bills: List[Dict[str, Any]]) -> None:
    atomic_write_json(BILLS_FILE, bills, indent=2)

def register_recurring_bill(payee: str, amount: float, due_day_of_month: int, category: str = "general") -> str:
    """
    Register a recurring bill or subscription.
    due_day_of_month: 1-31
    """
    bills = _load_bills()
    bill = {
        "id": f"bill_{int(datetime.now().timestamp())}",
        "payee": payee,
        "amount": amount,
        "due_day_of_month": due_day_of_month,
        "category": category,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    bills.append(bill)
    _save_bills(bills)
    return f"Registered recurring bill '{payee}' (${amount:.2f}/mo) due on day {due_day_of_month}."

def get_bill_due_radar(days_lookahead: int = 14) -> str:
    """
    Get upcoming bills due within the specified lookahead period.
    """
    bills = _load_bills()
    if not bills:
        return "No recurring bills registered in Bill Radar."

    today = datetime.now()
    upcoming = []
    total_amount = 0.0

    for bill in bills:
        due_day = min(bill["due_day_of_month"], 28)
        # Determine next due date
        target_month = today.month
        target_year = today.year
        if due_day < today.day:
            if target_month == 12:
                target_month = 1
                target_year += 1
            else:
                target_month += 1
        
        due_date = datetime(target_year, target_month, due_day)
        days_left = (due_date - today).days

        if days_left <= days_lookahead:
            upcoming.append(f"- [{days_left} days left] {bill['payee']}: ${bill['amount']:.2f} due on {due_date.strftime('%b %d')}")
            total_amount += bill["amount"]

    if not upcoming:
        return f"No bills due in next {days_lookahead} days."

    return f"💳 Bill-Due Radar (Next {days_lookahead} Days):\n" + "\n".join(upcoming) + f"\n\nTotal Estimated Outflow: ${total_amount:.2f}"
