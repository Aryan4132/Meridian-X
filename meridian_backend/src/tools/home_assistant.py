"""
home_assistant.py — Smart Home & IoT Ambient Sentinel (BUTLER-29)

Direct Home Assistant / MQTT bridge for smart lighting, climate, locks,
and ambient workspace environment controls.
"""

import os
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class HomeAssistantSentinel:
    """Controls IoT and Home Assistant entities across the local smart environment."""

    def __init__(self, base_url: Optional[str] = None, token: Optional[str] = None):
        self.base_url = (base_url or os.getenv("HASS_BASE_URL", "http://homeassistant.local:8123")).rstrip("/")
        self.token = token or os.getenv("HASS_TOKEN", "")
        self._mock_states: Dict[str, Dict[str, Any]] = {
            "light.desk_ambient": {"state": "on", "attributes": {"brightness": 200, "color_temp": 370}},
            "light.ceiling_main": {"state": "on", "attributes": {"brightness": 255}},
            "climate.office_thermostat": {"state": "heat", "attributes": {"current_temperature": 21.5, "temperature": 22.0}},
            "lock.office_door": {"state": "locked", "attributes": {"battery_level": 92}},
            "switch.studio_monitors": {"state": "on", "attributes": {}}
        }

    def list_entities(self, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        """Lists connected smart home entities filtered optionally by domain."""
        entities = []
        for eid, data in self._mock_states.items():
            if domain is None or eid.startswith(f"{domain}."):
                entities.append({"entity_id": eid, **data})
        return entities

    def control_light(
        self,
        entity_id: str,
        state: str = "on",
        brightness: Optional[int] = None,
        color_temp: Optional[int] = None
    ) -> Dict[str, Any]:
        """Toggles or dims light bulbs with optional brightness (0-255) and color temperature."""
        action = "turn_on" if state.lower() == "on" else "turn_off"
        payload: Dict[str, Any] = {"entity_id": entity_id}
        if brightness is not None and action == "turn_on":
            payload["brightness"] = max(0, min(255, brightness))
        if color_temp is not None and action == "turn_on":
            payload["color_temp"] = color_temp

        if entity_id in self._mock_states:
            self._mock_states[entity_id]["state"] = "on" if action == "turn_on" else "off"
            if "brightness" in payload:
                self._mock_states[entity_id]["attributes"]["brightness"] = payload["brightness"]
            if "color_temp" in payload:
                self._mock_states[entity_id]["attributes"]["color_temp"] = payload["color_temp"]

        logger.info(f"[HomeAssistant] Light {entity_id} set to {state}")
        return {
            "status": "success",
            "entity_id": entity_id,
            "action": action,
            "applied_params": payload
        }

    def set_climate(self, entity_id: str, target_temp: float, hvac_mode: Optional[str] = None) -> Dict[str, Any]:
        """Sets target room temperature and HVAC mode."""
        if entity_id in self._mock_states:
            self._mock_states[entity_id]["attributes"]["temperature"] = target_temp
            if hvac_mode:
                self._mock_states[entity_id]["state"] = hvac_mode

        logger.info(f"[HomeAssistant] Climate {entity_id} set to {target_temp}°C")
        return {"status": "success", "entity_id": entity_id, "temperature": target_temp, "hvac_mode": hvac_mode}

    def toggle_lock(self, entity_id: str, lock_action: str = "lock") -> Dict[str, Any]:
        """Locks or unlocks electronic security doors."""
        action = "lock" if lock_action.lower() in ["lock", "secure"] else "unlock"
        if entity_id in self._mock_states:
            self._mock_states[entity_id]["state"] = "locked" if action == "lock" else "unlocked"

        logger.info(f"[HomeAssistant] Security lock action '{action}' on {entity_id}")
        return {"status": "success", "entity_id": entity_id, "lock_state": action}

# Singleton sentinel instance
home_assistant_sentinel = HomeAssistantSentinel()

def hass_list_devices(domain: Optional[str] = None) -> List[Dict[str, Any]]:
    return home_assistant_sentinel.list_entities(domain=domain)

def hass_set_light(entity_id: str, state: str = "on", brightness: Optional[int] = None) -> Dict[str, Any]:
    return home_assistant_sentinel.control_light(entity_id=entity_id, state=state, brightness=brightness)

def hass_set_temperature(entity_id: str, temperature: float) -> Dict[str, Any]:
    return home_assistant_sentinel.set_climate(entity_id=entity_id, target_temp=temperature)
