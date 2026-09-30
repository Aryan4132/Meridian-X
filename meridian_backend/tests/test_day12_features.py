"""
Unit tests for Day 12 Butler Operations, Knowledge & File Intelligence features.
"""

import pytest
from src.tools.expiry_sentinel import add_expiry_document, check_document_expiries, list_expiry_documents
from src.tools.travel_butler import create_trip, calculate_leave_by_time, get_upcoming_trips
from src.tools.bill_radar import register_recurring_bill, get_bill_due_radar
from src.tools.finance_sentinel import analyze_stock_sentiment, get_market_watchlist
from src.tools.file_janitor import scan_downloads_folder, organize_downloads
from src.tools.search_hub import universal_search
from src.tools.screenshot_memory import capture_screenshot_memory, query_screenshot_memory
from src.tools.household import add_grocery_item, add_household_chore, get_household_summary

def test_expiry_sentinel():
    res_add = add_expiry_document("Passport", "passport", "2026-12-31", "International passport")
    assert "Successfully registered" in res_add
    
    res_check = check_document_expiries(365)
    assert "Passport" in res_check or "Expiry Sentinel" in res_check

    res_list = list_expiry_documents()
    assert "Passport" in res_list

def test_travel_butler():
    res_trip = create_trip("Tokyo", "2026-10-01", "2026-10-10", "JL001", "Grand Hyatt")
    assert "Tokyo" in res_trip
    
    res_leave = calculate_leave_by_time("2026-10-01 10:00", "Home", "Haneda Airport")
    assert "Recommended Departure" in res_leave

    res_upcoming = get_upcoming_trips()
    assert "Tokyo" in res_upcoming

def test_bill_radar():
    res_bill = register_recurring_bill("Netflix", 19.99, 15, "entertainment")
    assert "Netflix" in res_bill
    
    res_radar = get_bill_due_radar(30)
    assert "Netflix" in res_radar or "Bill-Due Radar" in res_radar

def test_finance_sentinel():
    res = analyze_stock_sentiment("AAPL", "Apple surges to record high quarterly earnings")
    assert "BULLISH" in res

    watchlist = get_market_watchlist("AAPL,MSFT")
    assert "AAPL" in watchlist

def test_file_janitor(tmp_path):
    # Create test file
    test_file = tmp_path / "sample.pdf"
    test_file.write_text("dummy PDF content")
    
    report = scan_downloads_folder(str(tmp_path))
    assert "Total Files Scanned: 1" in report

    org = organize_downloads(str(tmp_path), dry_run=True)
    assert "[DRY RUN SIMULATION]" in org

def test_universal_search():
    res = universal_search("meridian", domain_filter="all")
    assert "Universal Search Hub Results" in res

def test_screenshot_memory():
    res_cap = capture_screenshot_memory("VS Code")
    assert "captured & indexed snapshot" in res_cap

    res_query = query_screenshot_memory("VS Code")
    assert "VS Code" in res_query

def test_household_ops():
    res_grocery = add_grocery_item("Oat Milk", "2 cartons")
    assert "Oat Milk" in res_grocery

    res_chore = add_household_chore("Water plants")
    assert "Water plants" in res_chore

    summary = get_household_summary()
    assert "Oat Milk" in summary
