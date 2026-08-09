import httpx
import os
import time
from typing import Dict, Any, Optional

_LOCATION_CACHE: Dict[str, Any] = {}
_CACHE_EXPIRY = 3600  # 1 hour cache TTL

DEFAULT_LOCATION = {
    "lat": 37.7749,
    "lon": -122.4194,
    "city": "San Francisco",
    "region": "California",
    "country": "United States",
    "ip": "127.0.0.1",
    "source": "default_fallback",
}

WEATHER_CODE_MAP = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}


def resolve_location() -> Dict[str, Any]:
    """
    Resolves the current location using IP geo-location APIs with caching and fallback.
    """
    now = time.time()
    if _LOCATION_CACHE and (now - _LOCATION_CACHE.get("_timestamp", 0)) < _CACHE_EXPIRY:
        return _LOCATION_CACHE["data"]

    # 1. Primary IP API: ipapi.co
    try:
        res = httpx.get("https://ipapi.co/json/", timeout=4.0)
        if res.status_code == 200:
            data = res.json()
            if "city" in data:
                loc = {
                    "lat": float(data.get("latitude", DEFAULT_LOCATION["lat"])),
                    "lon": float(data.get("longitude", DEFAULT_LOCATION["lon"])),
                    "city": data.get("city", "Unknown City"),
                    "region": data.get("region", "Unknown Region"),
                    "country": data.get("country_name", "Unknown Country"),
                    "ip": data.get("ip", "127.0.0.1"),
                    "source": "ipapi.co",
                }
                _LOCATION_CACHE["data"] = loc
                _LOCATION_CACHE["_timestamp"] = now
                return loc
    except Exception as e:
        print("[GeoLocation] ipapi.co failed:", e)

    # 2. Secondary IP API: ip-api.com
    try:
        res = httpx.get("http://ip-api.com/json/", timeout=4.0)
        if res.status_code == 200:
            data = res.json()
            if data.get("status") == "success":
                loc = {
                    "lat": float(data.get("lat", DEFAULT_LOCATION["lat"])),
                    "lon": float(data.get("lon", DEFAULT_LOCATION["lon"])),
                    "city": data.get("city", "Unknown City"),
                    "region": data.get("regionName", "Unknown Region"),
                    "country": data.get("country", "Unknown Country"),
                    "ip": data.get("query", "127.0.0.1"),
                    "source": "ip-api.com",
                }
                _LOCATION_CACHE["data"] = loc
                _LOCATION_CACHE["_timestamp"] = now
                return loc
    except Exception as e:
        print("[GeoLocation] ip-api.com failed:", e)

    # 3. Environment or default fallback
    env_city = os.environ.get("USER_LOCATION_CITY")
    if env_city:
        loc = dict(DEFAULT_LOCATION)
        loc["city"] = env_city
        loc["source"] = "environment"
        return loc

    return DEFAULT_LOCATION


def get_localized_weather(city: Optional[str] = None) -> str:
    """
    Fetches real-time weather information for the resolved or specified city.
    """
    loc = resolve_location()
    target_city = city or loc.get("city", "San Francisco")
    lat = loc.get("lat", DEFAULT_LOCATION["lat"])
    lon = loc.get("lon", DEFAULT_LOCATION["lon"])

    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        res = httpx.get(url, timeout=5.0)
        if res.status_code == 200:
            weather = res.json().get("current_weather", {})
            temp_c = weather.get("temperature", 0)
            temp_f = round((temp_c * 9 / 5) + 32, 1)
            windspeed = weather.get("windspeed", 0)
            code = weather.get("weathercode", 0)
            condition = WEATHER_CODE_MAP.get(code, "Clear")
            return (
                f"Weather for {target_city} ({loc.get('region', '')}, {loc.get('country', '')}):\n"
                f"• Condition: {condition}\n"
                f"• Temperature: {temp_c}°C ({temp_f}°F)\n"
                f"• Wind Speed: {windspeed} km/h\n"
                f"• Resolved Location Source: {loc.get('source', 'ip')}"
            )
    except Exception as e:
        print("[GeoLocation] Weather API error:", e)

    # Fallback to wttr.in text service
    try:
        res = httpx.get(f"https://wttr.in/{target_city}?format=3", timeout=5.0)
        if res.status_code == 200 and res.text.strip():
            return f"Weather briefing for {target_city}: {res.text.strip()}"
    except Exception:
        pass

    return f"Weather information currently unavailable for {target_city}."


def bias_query_spatially(query: str, location: Optional[Dict[str, Any]] = None) -> str:
    """
    Biases search or query with spatial context (city/region) if local intent is detected.
    """
    loc = location or resolve_location()
    city = loc.get("city", "")
    if not city or city == "Unknown City":
        return query

    spatial_keywords = ["weather", "restaurant", "events", "traffic", "news", "stores", "hospitals", "local", "near me"]
    query_lower = query.lower()

    if any(kw in query_lower for kw in spatial_keywords):
        if city.lower() not in query_lower:
            return f"{query} in {city}"

    return query
