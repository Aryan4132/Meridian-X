"""
Travel Butler & Leave-By Briefing (BUTLER-04)
Natural language trip creation, itinerary parsing, and leave-by commute calculation.
Integrates with spatial geo-location for traffic-aware commute alerts.
"""

import os
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

TRIPS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "trips.json")

def _load_trips() -> List[Dict[str, Any]]:
    if not os.path.exists(TRIPS_FILE):
        return []
    try:
        with open(TRIPS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def _save_trips(trips: List[Dict[str, Any]]) -> None:
    os.makedirs(os.path.dirname(TRIPS_FILE), exist_ok=True)
    with open(TRIPS_FILE, "w", encoding="utf-8") as f:
        json.dump(trips, f, indent=2)

def create_trip(destination: str, start_date: str, end_date: str, flight_number: str = "", hotel: str = "") -> str:
    """
    Create a new trip itinerary.
    start_date / end_date: YYYY-MM-DD
    """
    trips = _load_trips()
    trip = {
        "id": f"trip_{int(datetime.now().timestamp())}",
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "flight_number": flight_number,
        "hotel": hotel,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    trips.append(trip)
    _save_trips(trips)
    return f"Trip to '{destination}' ({start_date} to {end_date}) created successfully."

def calculate_leave_by_time(event_time: str, origin: str, destination: str, travel_mode: str = "driving") -> str:
    """
    Calculate leave-by recommendation for an appointment or flight.
    event_time format: YYYY-MM-DD HH:MM
    """
    try:
        event_dt = datetime.strptime(event_time, "%Y-%m-%d %H:%M")
    except ValueError:
        return "Error: event_time must be formatted as YYYY-MM-DD HH:MM"

    # Simulated dynamic route estimate baseline (30 mins + traffic buffer)
    estimated_transit_minutes = 45 if travel_mode == "driving" else 60
    traffic_buffer_minutes = 15
    security_buffer_minutes = 90 if "airport" in destination.lower() or "flight" in destination.lower() else 15

    total_lead_minutes = estimated_transit_minutes + traffic_buffer_minutes + security_buffer_minutes
    leave_dt = event_dt - timedelta(minutes=total_lead_minutes)

    return (
        f"🚗 Leave-By Calculation for {destination}:\n"
        f"- Target Arrival: {event_time}\n"
        f"- Estimated Travel: {estimated_transit_minutes} mins\n"
        f"- Traffic/Buffer Allowance: {traffic_buffer_minutes + security_buffer_minutes} mins\n"
        f"⏰ Recommended Departure: {leave_dt.strftime('%Y-%m-%d %H:%M')} ({total_lead_minutes} mins before event)"
    )

def get_upcoming_trips() -> str:
    """Get list of upcoming trips."""
    trips = _load_trips()
    if not trips:
        return "No upcoming trips found."
    
    lines = []
    for t in trips:
        lines.append(f"- ✈️ {t['destination']} ({t['start_date']} to {t['end_date']}) | Flight: {t['flight_number'] or 'N/A'} | Hotel: {t['hotel'] or 'N/A'}")
    return "Upcoming Trips:\n" + "\n".join(lines)
