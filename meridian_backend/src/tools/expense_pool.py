"""
expense_pool.py — Group Expense Settlement & Split Calculator (FIN-05)

Manages shared trip and household expense pools, calculates net participant
balances, and computes minimal-transaction settlement paths.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from collections import defaultdict

logger = logging.getLogger(__name__)

class ExpensePoolSentinel:
    """Computes group expense splits and optimal debt settlement transactions."""

    def __init__(self):
        self._pools: Dict[str, Dict[str, Any]] = {}

    def create_pool(self, pool_id: str, title: str, members: List[str]) -> Dict[str, Any]:
        pool = {
            "pool_id": pool_id,
            "title": title,
            "members": members,
            "expenses": [],
            "created_at": time.time()
        }
        self._pools[pool_id] = pool
        return pool

    def add_expense(
        self,
        pool_id: str,
        payer: str,
        amount: float,
        description: str,
        beneficiaries: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        pool = self._pools.get(pool_id)
        if not pool:
            pool = self.create_pool(pool_id, f"Pool-{pool_id}", [payer])

        b_list = beneficiaries or pool["members"]
        expense = {
            "expense_id": f"exp-{int(time.time()*1000)}",
            "payer": payer,
            "amount": amount,
            "description": description,
            "beneficiaries": b_list,
            "timestamp": time.time()
        }
        pool["expenses"].append(expense)
        for b in b_list + [payer]:
            if b not in pool["members"]:
                pool["members"].append(b)

        logger.info(f"[ExpensePool] Added ${amount:.2f} by {payer} in {pool_id}")
        return expense

    def calculate_settlement(self, pool_id: str) -> Dict[str, Any]:
        """Calculates minimal transactions needed to balance all debts."""
        pool = self._pools.get(pool_id)
        if not pool:
            return {"status": "error", "message": "Pool not found"}

        net_balances: Dict[str, float] = defaultdict(float)

        for exp in pool["expenses"]:
            amount = exp["amount"]
            payer = exp["payer"]
            b_list = exp["beneficiaries"]
            split = amount / len(b_list)

            net_balances[payer] += amount
            for b in b_list:
                net_balances[b] -= split

        # Greedily match debtors with creditors to minimize transactions
        debtors = []
        creditors = []
        for person, bal in net_balances.items():
            r_bal = round(bal, 2)
            if r_bal < -0.01:
                debtors.append([person, -r_bal])
            elif r_bal > 0.01:
                creditors.append([person, r_bal])

        settlements = []
        d_idx, c_idx = 0, 0
        while d_idx < len(debtors) and c_idx < len(creditors):
            debtor, d_amt = debtors[d_idx]
            creditor, c_amt = creditors[c_idx]

            transfer = min(d_amt, c_amt)
            settlements.append({
                "from": debtor,
                "to": creditor,
                "amount": round(transfer, 2)
            })

            debtors[d_idx][1] -= transfer
            creditors[c_idx][1] -= transfer

            if debtors[d_idx][1] < 0.01:
                d_idx += 1
            if creditors[c_idx][1] < 0.01:
                c_idx += 1

        return {
            "pool_id": pool_id,
            "total_expenses": sum(e["amount"] for e in pool["expenses"]),
            "net_balances": dict(net_balances),
            "settlement_transactions": settlements
        }

expense_pool_sentinel = ExpensePoolSentinel()

def add_pool_expense(pool_id: str, payer: str, amount: float, description: str) -> Dict[str, Any]:
    return expense_pool_sentinel.add_expense(pool_id=pool_id, payer=payer, amount=amount, description=description)

def get_pool_settlement(pool_id: str) -> Dict[str, Any]:
    return expense_pool_sentinel.calculate_settlement(pool_id=pool_id)

