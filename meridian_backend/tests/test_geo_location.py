import pytest
from unittest.mock import patch, MagicMock
from src.tools.geo_location import (
    resolve_location,
    get_localized_weather,
    bias_query_spatially,
    DEFAULT_LOCATION,
    _LOCATION_CACHE
)
from src.tools.web import search_web
from src.tools.registry import TOOL_REGISTRY


def setup_function():
    _LOCATION_CACHE.clear()


def test_resolve_location_ipapi_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "city": "New York",
        "region": "New York",
        "country_name": "United States",
        "ip": "1.2.3.4"
    }

    with patch("httpx.get", return_value=mock_response):
        loc = resolve_location()
        assert loc["city"] == "New York"
        assert loc["lat"] == 40.7128
        assert loc["source"] == "ipapi.co"


def test_resolve_location_fallback_to_default():
    with patch("httpx.get", side_effect=Exception("Network error")):
        loc = resolve_location()
        assert loc["city"] == DEFAULT_LOCATION["city"]
        assert loc["source"] == "default_fallback"


def test_get_localized_weather_openmeteo():
    mock_geo = {
        "lat": 51.5074,
        "lon": -0.1278,
        "city": "London",
        "region": "Greater London",
        "country": "United Kingdom",
        "source": "mock"
    }
    mock_weather_res = MagicMock()
    mock_weather_res.status_code = 200
    mock_weather_res.json.return_value = {
        "current_weather": {
            "temperature": 18.5,
            "windspeed": 12.0,
            "weathercode": 0
        }
    }

    with patch("src.tools.geo_location.resolve_location", return_value=mock_geo):
        with patch("httpx.get", return_value=mock_weather_res):
            report = get_localized_weather("London")
            assert "London" in report
            assert "Clear sky" in report
            assert "18.5°C" in report


def test_bias_query_spatially():
    mock_geo = {"city": "Tokyo", "region": "Kanto", "country": "Japan"}
    
    # Query with spatial intent
    query = bias_query_spatially("best ramen restaurant", location=mock_geo)
    assert "in Tokyo" in query

    # Query already containing city
    query_existing = bias_query_spatially("best ramen restaurant in Tokyo", location=mock_geo)
    assert query_existing == "best ramen restaurant in Tokyo"

    # Non-spatial query
    non_spatial = bias_query_spatially("python async tutorial", location=mock_geo)
    assert non_spatial == "python async tutorial"


def test_geo_location_registered_in_registry():
    assert "resolve_location" in TOOL_REGISTRY
    assert "get_localized_weather" in TOOL_REGISTRY
    assert "bias_query_spatially" in TOOL_REGISTRY
    assert TOOL_REGISTRY["resolve_location"]["tier"] == 0
