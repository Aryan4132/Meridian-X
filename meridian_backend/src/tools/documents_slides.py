"""PowerPoint presentation tools.

Split from ``src.tools.documents_office`` (Phase 2 god-file refactor). Pure move -
zero behavior changes. ``documents.py`` re-exports every symbol so existing
imports keep working.
"""

import os
from typing import Dict, Any, List, Optional
from src.core.audit_logger import log_sensitive_action

# PowerPoint presentations (all-or-nothing so partial imports cannot NameError later)
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
except ImportError:
    Presentation = None
    Inches = None
    Pt = None

def create_powerpoint_presentation(file_path: str, slides: List[Dict[str, Any]]) -> str:
    """
    Creates a PowerPoint (.pptx) presentation.
    slides is a list of dicts: [{'title': 'Slide 1 Title', 'content': ['Point A', 'Point B']}, ...]
    """
    if not Presentation:
        raise ImportError("The 'python-pptx' package is not installed.")
        
    parent = os.path.dirname(os.path.abspath(file_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
        
    prs = Presentation()
    
    # 0 is usually Title Slide, 1 is Title and Content layout
    title_content_layout = prs.slide_layouts[1]
    
    for slide_data in slides:
        slide = prs.slides.add_slide(title_content_layout)
        
        title_shape = slide.shapes.title
        title_shape.text = slide_data.get("title", "")
        
        body_shape = slide.placeholders[1]
        tf = body_shape.text_frame
        
        content = slide_data.get("content", [])
        if isinstance(content, str):
            tf.text = content
        elif isinstance(content, list):
            # First item in bullet frame
            if content:
                tf.text = content[0]
                for item in content[1:]:
                    p = tf.add_paragraph()
                    p.text = item
                    p.level = 0
                    
    prs.save(file_path)
    log_sensitive_action(
        category="FILE_WRITE",
        action="create_powerpoint_presentation",
        details={"path": file_path, "slides_count": len(slides)},
        status="SUCCESS"
    )
    return f"Successfully created PowerPoint presentation at {file_path}"


def edit_powerpoint_presentation(
    file_path: str, 
    action: str, 
    slide_index: Optional[int] = None, 
    title: Optional[str] = None, 
    content: Optional[List[str]] = None,
    find_text: Optional[str] = None,
    replace_text: Optional[str] = None
) -> str:
    """
    Edits a PowerPoint (.pptx) file.
    Actions supported:
    - 'add_slide': Appends a slide with title and content.
    - 'replace_text': Searches and replaces text inside all shapes.
    """
    if not Presentation:
        raise ImportError("The 'python-pptx' package is not installed.")
        
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PowerPoint file not found: {file_path}")
        
    prs = Presentation(file_path)
    
    if action == "add_slide":
        title = title or ""
        content = content or []
        
        title_content_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(title_content_layout)
        
        title_shape = slide.shapes.title
        title_shape.text = title
        
        body_shape = slide.placeholders[1]
        tf = body_shape.text_frame
        if content:
            tf.text = content[0]
            for item in content[1:]:
                p = tf.add_paragraph()
                p.text = item
                p.level = 0
                
        prs.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_powerpoint_presentation:add_slide",
            details={"path": file_path, "title": title},
            status="SUCCESS"
        )
        return f"Successfully added slide titled '{title}' to {file_path}"
        
    elif action == "replace_text":
        if not find_text:
            raise ValueError("find_text is required for replace_text action")
        replace_text = replace_text or ""
        
        count = 0
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text") and find_text in shape.text:
                    if shape.has_text_frame:
                        for paragraph in shape.text_frame.paragraphs:
                            if find_text in paragraph.text:
                                paragraph.text = paragraph.text.replace(find_text, replace_text)
                                count += 1
                                
        prs.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_powerpoint_presentation:replace_text",
            details={"path": file_path, "find_text": find_text, "replacements": count},
            status="SUCCESS"
        )
        return f"Successfully replaced {count} occurrences of '{find_text}' in PowerPoint presentation {file_path}"
        
    else:
        raise ValueError(f"Unsupported action: {action}")

