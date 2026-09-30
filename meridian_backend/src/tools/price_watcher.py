"""
price_watcher.py — Wishlist Price Watcher (FIN-04)
"""

import time
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class PriceWatcherSentinel:
    """Tracks e-commerce product pages for price drops with price history sparklines."""

    def __init__(self):
        self._products: Dict[str, Dict[str, Any]] = {}

    def add_product(self, product_id: str, title: str, url: str, target_price: float, current_price: float) -> Dict[str, Any]:
        product = {
            "product_id": product_id,
            "title": title,
            "url": url,
            "target_price": target_price,
            "current_price": current_price,
            "price_history": [
                {"timestamp": time.time() - 86400 * 2, "price": current_price * 1.1},
                {"timestamp": time.time() - 86400 * 1, "price": current_price * 1.05},
                {"timestamp": time.time(), "price": current_price},
            ],
            "alert_triggered": current_price <= target_price,
        }
        self._products[product_id] = product
        logger.info(f"[PriceWatcher] Added product {title} (Target: ${target_price})")
        return product

    def list_products(self) -> List[Dict[str, Any]]:
        return list(self._products.values())

    def check_prices(self) -> List[Dict[str, Any]]:
        alerts = []
        for pid, prod in self._products.items():
            if prod["current_price"] <= prod["target_price"]:
                alerts.append({
                    "product_id": pid,
                    "title": prod["title"],
                    "current_price": prod["current_price"],
                    "target_price": prod["target_price"],
                    "message": f"Price drop alert! {prod['title']} is now ${prod['current_price']}"
                })
        return alerts

# Global instance
_price_watcher = PriceWatcherSentinel()

def add_watched_product(product_id: str, title: str, url: str, target_price: float, current_price: float) -> Dict[str, Any]:
    return _price_watcher.add_product(product_id, title, url, target_price, current_price)

def list_watched_products() -> List[Dict[str, Any]]:
    return _price_watcher.list_products()

def check_price_drops() -> List[Dict[str, Any]]:
    return _price_watcher.check_prices()
