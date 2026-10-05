import os
import subprocess
import webbrowser
import tempfile
import base64
from typing import Optional, Dict, Any
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["perception"])

class PolyglotRequest(BaseModel):
    transcript: str
    target_lang: Optional[str] = "en"
    code_target: Optional[str] = "python"

class OpenUrlRequest(BaseModel):
    url: str

@router.post("/api/vision/screenshot")
def api_vision_screenshot():
    try:
        from src.tools.desktop import screenshot, ocr_screen
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "meridian_vision_capture.png")
        screenshot(temp_path)
        
        ocr_text = ""
        try:
            ocr_text = ocr_screen(temp_path)
        except Exception as ocr_err:
            ocr_text = f"OCR failed: {ocr_err}"
            
        with open(temp_path, "rb") as img_file:
            b64_image = base64.b64encode(img_file.read()).decode("utf-8")
            
        try:
            os.remove(temp_path)
        except Exception:
            pass
            
        return {
            "status": "success",
            "image": f"data:image/png;base64,{b64_image}",
            "ocr_text": ocr_text
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/api/perception/screen")
async def api_perception_screen(prompt: Optional[str] = None):
    """PL-06: Multimodal screen capture & analysis endpoint."""
    from src.core.vision import analyze_screen_multimodal
    if prompt:
        return await analyze_screen_multimodal(prompt=prompt)
    return await analyze_screen_multimodal()

@router.get("/api/perception/window")
async def api_perception_window(force_refresh: bool = False):
    """PL-03: Real-time active window metadata & screen sense."""
    from src.core.screen_sense import get_active_window_sense
    return await get_active_window_sense(force_refresh=force_refresh)

@router.get("/api/perception/presence")
def api_perception_presence():
    """PL-01: Facial recognition & workspace user presence state."""
    from src.core.vision_face import get_presence_state
    return get_presence_state()

@router.post("/api/perception/presence/register")
def api_perception_presence_register(req: Dict[str, Any]):
    """PL-01: Register user face embedding."""
    from src.core.vision_face import register_user_face
    user_id = req.get("user_id", "owner")
    return register_user_face(user_id=user_id)

@router.get("/api/perception/ambient")
def api_perception_ambient(limit: Optional[int] = 10):
    """PL-02: Continuous ambient speech transcript history."""
    from src.voice.ambient_listener import get_recent_ambient_transcripts
    return {"transcripts": get_recent_ambient_transcripts(limit=limit or 10)}

@router.post("/api/perception/nudge/synthesize")
async def api_perception_synthesize_nudge():
    """PL-04: Synthesize multi-modal context and trigger proactive nudge."""
    from src.core.proactive import synthesize_ambient_nudge
    return await synthesize_ambient_nudge()

@router.post("/api/perception/predictive/prewarm")
def api_perception_prewarm_context(req: Dict[str, Any]):
    """JARVIS-04: Record application switch and pre-warm developer context."""
    from src.core.predictive_engine import prewarm_dev_context
    proc = req.get("process_name", "code.exe")
    title = req.get("title", "VS Code")
    return prewarm_dev_context(process_name=proc, title=title)

@router.post("/api/telephony/call")
def api_telephony_make_call(req: Dict[str, Any]):
    """CALL-01: Initiate outbound VoIP phone call."""
    from src.tools.phone_agent import make_outbound_call
    to_num = req.get("to_number", "+18005550199")
    obj = req.get("objective", "Assistant call")
    return make_outbound_call(to_number=to_num, objective=obj)

@router.post("/api/telephony/screen")
def api_telephony_screen_call(req: Dict[str, Any]):
    """CALL-02: Screen incoming call with AI receptionist."""
    from src.tools.phone_agent import screen_incoming_call
    caller_id = req.get("caller_id", "Unknown")
    snip = req.get("transcript_snippet", "")
    return screen_incoming_call(caller_id=caller_id, transcript_snippet=snip)

@router.post("/api/telephony/postcall")
def api_telephony_post_call(req: Dict[str, Any]):
    """CALL-03: Process post-call summary, action items, and task sync."""
    from src.tools.phone_agent import process_post_call_intelligence
    cid = req.get("call_id", "call_01")
    lines = req.get("transcript", [])
    return process_post_call_intelligence(call_id=cid, full_transcript=lines)

@router.get("/api/telephony/logs")
def api_telephony_get_logs(limit: Optional[int] = 10):
    """CALL-01..03: Get recent call logs."""
    from src.tools.phone_agent import get_call_logs
    return {"logs": get_call_logs(limit=limit or 10)}

@router.post("/api/sos/trigger")
def api_sos_trigger(req: Dict[str, Any]):
    """CALL-04: Emergency SOS voice protocol trigger."""
    from src.core.sos_protocol import trigger_emergency_sos
    phrase = req.get("trigger_phrase", "emergency help")
    contacts = req.get("contacts")
    return trigger_emergency_sos(phrase=phrase, contacts=contacts)

@router.get("/api/email/triage")
def api_email_triage(limit: Optional[int] = 10):
    """BUTLER-24: Email zero inbox triage."""
    from src.tools.external_connectors import triage_inbox_emails
    return triage_inbox_emails(limit=limit or 10)

@router.post("/api/email/reply")
def api_email_generate_reply(req: Dict[str, Any]):
    """BUTLER-24: Generate draft reply for an email."""
    from src.tools.external_connectors import generate_draft_reply
    eid = req.get("email_id", "msg_01")
    inst = req.get("instructions", "Accept politely")
    return generate_draft_reply(email_id=eid, instructions=inst)

@router.get("/api/crm/occasions")
def api_crm_check_occasions():
    """BUTLER-02: Check upcoming Personal CRM birthdays & silent VIP contacts."""
    from src.core.personal_crm import check_crm_occasions
    return check_crm_occasions()

@router.post("/api/crm/contact")
def api_crm_add_contact(req: Dict[str, Any]):
    """BUTLER-02: Add or update Personal CRM contact."""
    from src.core.personal_crm import add_crm_contact
    name = req.get("name", "New Contact")
    rel = req.get("relationship", "Friend")
    bday = req.get("birthday")
    notes = req.get("notes", "")
    return add_crm_contact(name=name, relationship=rel, birthday=bday, notes=notes)

@router.get("/api/proactive/meetingprep")
def api_proactive_meeting_prep(title: Optional[str] = None):
    """BUTLER-23: Generate T-minus-10-min meeting preparation briefing card."""
    from src.core.proactive import generate_meeting_prep_briefing
    return generate_meeting_prep_briefing(meeting_title=title or "Architecture Sync")

@router.get("/api/network/endpoints")
def api_get_network_endpoints():
    """MOB-01: Get LAN & Tailscale network endpoint URLs for mobile app auto-discovery."""
    from src.core.mobile_bridge import get_network_addresses
    return get_network_addresses()

@router.get("/api/gaze/status")
def get_gaze_status_api():
    """JARVIS-02: Get current gaze tracking status & screen dimming suggestion."""
    try:
        from src.core.gaze_tracker import get_current_gaze
        return get_current_gaze()
    except ImportError:
        return {"status": "inactive", "gaze": None}

@router.post("/api/gaze/start")
def start_gaze_api():
    """JARVIS-02: Start eye-tracking & spatial gaze control."""
    try:
        from src.core.gaze_tracker import start_gaze_tracking
        return start_gaze_tracking()
    except ImportError:
        return {"status": "gaze_tracker_not_installed"}

@router.post("/api/gaze/stop")
def stop_gaze_api():
    """JARVIS-02: Stop eye-tracking."""
    try:
        from src.core.gaze_tracker import stop_gaze_tracking
        return stop_gaze_tracking()
    except ImportError:
        return {"status": "stopped"}

@router.get("/api/camera/feeds")
def get_camera_feeds_api():
    """JARVIS-05: List registered RTSP security camera feeds and recent motion alerts."""
    try:
        from src.core.camera_sentinel import list_camera_feeds, get_recent_alerts
        feeds = list_camera_feeds()
        alerts = get_recent_alerts()
    except ImportError:
        feeds, alerts = [], []
    return {"status": "success", "feeds": feeds, "recent_alerts": alerts}

@router.get("/api/ar/headsets")
def get_ar_headsets_api():
    """JARVIS-08: List connected AR smart glasses & HUD headsets."""
    try:
        from src.core.ar_bridge import list_ar_headsets
        headsets = list_ar_headsets()
    except ImportError:
        headsets = []
    return {"status": "success", "headsets": headsets}

@router.post("/api/polyglot/translate")
def translate_polyglot_api(req: PolyglotRequest):
    """JARVIS-10: Translate multi-lingual speech transcript to executable code."""
    try:
        from src.voice.polyglot import translate_speech_to_code
        return translate_speech_to_code(req.transcript, target_lang=req.target_lang or "en", code_target=req.code_target or "python")
    except ImportError:
        return {"translated_code": req.transcript}

@router.get("/api/predictive/next-action")
def get_predictive_next_action_api():
    """JARVIS-04: Get predictive pre-execution & habit profile."""
    try:
        from src.core.predictive_engine import predict_next_action, get_habit_profile
        prediction = predict_next_action([])
        habits = get_habit_profile()
    except ImportError:
        prediction = {"suggested_action": None}
        habits = {}
    return {"status": "success", "prediction": prediction, "habits": habits}

@router.post("/api/presence/briefing")
def trigger_presence_briefing_api(user_name: Optional[str] = "User"):
    """JARVIS-06: Trigger workspace room arrival executive voice briefing."""
    try:
        from src.core.presence_briefing import generate_presence_briefing
        return generate_presence_briefing(user_name=user_name or "User")
    except ImportError:
        return {"briefing": f"Welcome back, {user_name or 'User'}."}

@router.post("/api/utils/open-url")
async def open_external_url_api(payload: OpenUrlRequest):
    """Opens an external URL in the user's system default web browser."""
    target_url = payload.url.strip()
    try:
        if os.name == "nt":
            subprocess.Popen(["cmd", "/c", "start", "", target_url], shell=False)
        else:
            webbrowser.open(target_url)
        return {"status": "success", "url": target_url}
    except Exception as e:
        return {"status": "error", "message": str(e)}
