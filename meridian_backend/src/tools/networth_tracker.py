"""
networth_tracker.py — Net Worth Snapshot & Asset Tracker (FIN-06)
"""

import time
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class NetWorthTracker:
    """Tracks assets vs liabilities and generates weekly net worth briefing cards."""

    def __init__(self):
        self._assets: Dict[str, Dict[str, Any]] = {
            "savings": {"name": "High Yield Savings", "category": "cash", "value": 15000.0},
            "investments": {"name": "Index Funds", "category": "stocks", "value": 45000.0},
        }
        self._liabilities: Dict[str, Dict[str, Any]] = {
            "credit_card": {"name": "Rewards Card", "category": "credit", "value": 1200.0},
        }

    def add_asset(self, asset_id: str, name: str, category: str, value: float) -> Dict[str, Any]:
        asset = {"asset_id": asset_id, "name": name, "category": category, "value": value}
        self._assets[asset_id] = asset
        return asset

    def add_liability(self, liability_id: str, name: str, category: str, value: float) -> Dict[str, Any]:
        liability = {"liability_id": liability_id, "name": name, "category": category, "value": value}
        self._liabilities[liability_id] = liability
        return liability

    def get_networth_summary(self) -> Dict[str, Any]:
        total_assets = sum(a["value"] for a in self._assets.values())
        total_liabilities = sum(l["value"] for l in self._liabilities.values())
        net_worth = total_assets - total_liabilities

        return {
            "net_worth": net_worth,
            "total_assets": total_assets,
            "total_liabilities": total_liabilities,
            "assets_breakdown": list(self._assets.values()),
            "liabilities_breakdown": list(self._liabilities.values()),
            "updated_at": time.time(),
        }

# Global instance
_networth_tracker = NetWorthTracker()

def add_asset(asset_id: str, name: str, category: str, value: float) -> Dict[str, Any]:
    return _networth_tracker.add_asset(asset_id, name, category, value)

def add_liability(liability_id: str, name: str, category: str, value: float) -> Dict[str, Any]:
    return _networth_tracker.add_liability(liability_id, name, category, value)

def get_networth_summary() -> Dict[str, Any]:
    return _networth_tracker.get_networth_summary()
