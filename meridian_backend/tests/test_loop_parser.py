import json
import pytest
from src.core.loop import StreamingXMLParser

def test_parser_well_formed():
    parser = StreamingXMLParser()
    
    # Feeding XML text chunks incrementally
    events = parser.feed("<thought>Analyzing system status...")
    # It yields thought_update event
    assert len(events) == 1
    assert events[0]["type"] == "thought_update"
    
    events = parser.feed(" Done.</thought>")
    # Must yield thought completed event
    assert len(events) > 0
    assert any(e["type"] == "thought" and e["status"] == "completed" for e in events)
    
    # Test self-closing tool call
    parser = StreamingXMLParser()
    events = parser.feed("<call:read_file path=\"test.txt\"/>")
    assert len(events) > 0
    call_events = [e for e in events if e["type"] == "call"]
    assert len(call_events) > 0
    assert call_events[0]["name"] == "read_file"
    args = json.loads(call_events[0]["args"])
    assert args["path"] == "test.txt"

def test_parser_malformed():
    parser = StreamingXMLParser()
    
    # Feeding incomplete tag
    events = parser.feed("<call:read_file path=\"test.txt\"")
    assert len(events) == 0  # No events yet
    
    # Finish the tag
    events = parser.feed("/>")
    call_events = [e for e in events if e["type"] == "call"]
    assert len(call_events) > 0
    assert call_events[0]["name"] == "read_file"
    args = json.loads(call_events[0]["args"])
    assert args["path"] == "test.txt"
