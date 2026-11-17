"""
car_logbook.py — Car Logbook & Mileage Service Predictor (CAR-01)

Tracks fuel/charge events, maintenance records, and predicts scheduled service
intervals (oil, brakes, tire rotations) based on average weekly mileage.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

class CarLogbookSentinel:
    """Manages vehicle maintenance schedules, fuel efficiency, and service prediction."""

    def __init__(self):
        self._vehicles: Dict[str, Dict[str, Any]] = {
            "primary_auto": {
                "name": "Tesla Model S / Audi A6",
                "odometer_km": 42500,
                "last_service_km": 38000,
                "service_interval_km": 10000,
                "weekly_avg_km": 320,
                "logs": []
            }
        }

    def log_maintenance(
        self,
        vehicle_id: str,
        service_type: str,
        odometer_km: int,
        cost: float = 0.0,
        notes: str = ""
    ) -> Dict[str, Any]:
        """Logs a completed service or inspection."""
        veh = self._vehicles.get(vehicle_id)
        if not veh:
            veh = {
                "name": f"Vehicle-{vehicle_id}",
                "odometer_km": odometer_km,
                "last_service_km": odometer_km,
                "service_interval_km": 10000,
                "weekly_avg_km": 300,
                "logs": []
            }
            self._vehicles[vehicle_id] = veh

        entry = {
            "log_id": f"srv-{int(time.time()*1000)}",
            "service_type": service_type,
            "odometer_km": odometer_km,
            "cost": cost,
            "notes": notes,
            "timestamp": time.time()
        }
        veh["logs"].append(entry)
        veh["odometer_km"] = max(veh["odometer_km"], odometer_km)
        veh["last_service_km"] = odometer_km
        logger.info(f"[CarLogbook] Logged {service_type} for {vehicle_id} at {odometer_km} km")
        return entry

    def predict_next_service(self, vehicle_id: str = "primary_auto") -> Dict[str, Any]:
        """Predicts date and distance until next scheduled service."""
        veh = self._vehicles.get(vehicle_id)
        if not veh:
            return {"status": "error", "message": f"Vehicle '{vehicle_id}' not found"}

        km_since = veh["odometer_km"] - veh["last_service_km"]
        km_remaining = max(0, veh["service_interval_km"] - km_since)
        weeks_remaining = round(km_remaining / max(1, veh["weekly_avg_km"]), 1)
        days_remaining = int(weeks_remaining * 7)

        return {
            "vehicle_id": vehicle_id,
            "name": veh["name"],
            "current_odometer_km": veh["odometer_km"],
            "km_until_service": km_remaining,
            "estimated_days_until_service": days_remaining,
            "urgent": km_remaining < 500,
            "status": "warning" if km_remaining < 500 else "healthy"
        }

car_logbook_sentinel = CarLogbookSentinel()

def log_vehicle_service(vehicle_id: str, service_type: str, odometer_km: int, cost: float = 0.0) -> Dict[str, Any]:
    return car_logbook_sentinel.log_maintenance(vehicle_id=vehicle_id, service_type=service_type, odometer_km=odometer_km, cost=cost)

def get_vehicle_service_prediction(vehicle_id: str = "primary_auto") -> Dict[str, Any]:
    return car_logbook_sentinel.predict_next_service(vehicle_id=vehicle_id)

