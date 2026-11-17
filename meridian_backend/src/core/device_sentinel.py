"""
device_sentinel.py — Remote Device Telemetry & Battery Sentinel (AUTO-04)

Continuously aggregates battery vitals, storage headroom, and ping latency
across all connected Meridian-X desktop and mobile nodes.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class DeviceTelemetry:
    device_id: str
    device_name: str
    platform: str  # android, ios, windows, macos, linux
    battery_level: float  # 0.0 - 100.0
    is_charging: bool
    free_storage_gb: float
    last_ping_ms: float
    last_seen: float = field(default_factory=time.time)

class DeviceSentinelEngine:
    """Monitors telemetry and health across peer nodes in the personal device mesh."""

    def __init__(self):
        self._nodes: Dict[str, DeviceTelemetry] = {}
        # Pre-seed local device node
        self.update_telemetry(
            device_id="local_desktop",
            name="Primary Workstation",
            platform="windows",
            battery=100.0,
            is_charging=True,
            free_storage_gb=128.5,
            latency_ms=0.5
        )

    def update_telemetry(
        self,
        device_id: str,
        name: str,
        platform: str,
        battery: float,
        is_charging: bool,
        free_storage_gb: float,
        latency_ms: float
    ) -> DeviceTelemetry:
        """Records or refreshes vitals from a remote node."""
        telemetry = DeviceTelemetry(
            device_id=device_id,
            device_name=name,
            platform=platform,
            battery_level=max(0.0, min(100.0, battery)),
            is_charging=is_charging,
            free_storage_gb=free_storage_gb,
            last_ping_ms=latency_ms,
            last_seen=time.time()
        )
        self._nodes[device_id] = telemetry
        logger.debug(f"[DeviceSentinel] Updated vitals for {name}: {battery}% battery")
        return telemetry

    def list_connected_devices(self) -> List[Dict[str, Any]]:
        """Returns all registered devices and flags low-battery or storage warnings."""
        now = time.time()
        devices = []
        for d in self._nodes.values():
            is_stale = (now - d.last_seen) > 120
            low_battery = d.battery_level < 20.0 and not d.is_charging
            low_storage = d.free_storage_gb < 5.0

            devices.append({
                "device_id": d.device_id,
                "name": d.device_name,
                "platform": d.platform,
                "battery_level": d.battery_level,
                "is_charging": d.is_charging,
                "free_storage_gb": d.free_storage_gb,
                "latency_ms": d.last_ping_ms,
                "is_online": not is_stale,
                "alerts": {
                    "low_battery_warning": low_battery,
                    "low_storage_warning": low_storage
                }
            })
        return devices

    def ping_device(self, device_id: str) -> Dict[str, Any]:
        """Simulates latency ping measurement against a peer node."""
        node = self._nodes.get(device_id)
        if not node:
            return {"status": "error", "message": f"Device {device_id} not registered."}
        return {"device_id": device_id, "status": "pong", "latency_ms": node.last_ping_ms}

device_sentinel_engine = DeviceSentinelEngine()

def list_mesh_devices() -> List[Dict[str, Any]]:
    return device_sentinel_engine.list_connected_devices()

def record_device_vitals(device_id: str, battery: float, charging: bool) -> Dict[str, Any]:
    node = device_sentinel_engine.update_telemetry(
        device_id=device_id,
        name=f"Device-{device_id}",
        platform="mobile",
        battery=battery,
        is_charging=charging,
        free_storage_gb=32.0,
        latency_ms=12.0
    )
    return {"status": "recorded", "device_id": node.device_id}

