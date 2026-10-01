import os
import re
from typing import Dict, Any, List, Optional
from src.core.audit_logger import log_sensitive_action

# PDF reading & merging
try:
    import pypdf
except ImportError:
    pypdf = None

# PDF generation (all-or-nothing so partial imports can't NameError later)
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
except ImportError:
    letter = None
    SimpleDocTemplate = None
    Paragraph = None
    Spacer = None
    getSampleStyleSheet = None
    ParagraphStyle = None



def parse_receipt_subscription(file_path_or_text: str) -> Dict[str, Any]:
    """Parses local receipts/invoices privately to track subscriptions and price hikes (FIN-01)."""
    text = file_path_or_text
    if os.path.exists(file_path_or_text):
        text = read_document_text(file_path_or_text)
        
    result = {
        "service_name": "Subscription/Vendor",
        "amount": 0.0,
        "is_recurring": False,
        "parsed_raw": text[:200]
    }
    
    # Amount extraction heuristic
    match = re.search(r"\$(\d+(?:\.\d{2})?)", text)
    if match:
        result["amount"] = float(match.group(1))
    if any(k in text.lower() for k in ["monthly", "annual", "subscription", "recurring", "auto-renew"]):
        result["is_recurring"] = True
        
    log_sensitive_action("EXPENSE_PARSED", "parse_receipt_subscription", result, "SUCCESS")
    return result


def _extract_pdf_layout_and_tables(file_path: str) -> str:
    """Pure-Python XY-Cut layout sorting and table parser using pypdf visitor_text."""
    if not pypdf:
        raise ImportError("The 'pypdf' package is not installed.")

    reader = pypdf.PdfReader(file_path)
    text_parts = []

    for i, page in enumerate(reader.pages):
        text_parts.append(f"--- Page {i + 1} ---")
        page_fragments = []

        def visitor_body(text, cm, tm, font_dict, font_size):
            if text and text.strip():
                # Extract (x, y) coordinates from transformation matrix
                x = tm[4] if len(tm) > 4 else 0
                y = tm[5] if len(tm) > 5 else 0
                page_fragments.append({"x": float(x), "y": float(y), "text": text.strip()})

        try:
            page.extract_text(visitor_text=visitor_body)
        except Exception:
            pass

        if not page_fragments:
            text_parts.append(page.extract_text() or "")
            continue

        # Sort top-to-bottom (PDF y is bottom-up, so higher y is top of page)
        # Group fragments into horizontal lines (y threshold 4.0)
        lines: List[List[Dict[str, Any]]] = []
        page_fragments.sort(key=lambda f: f["y"], reverse=True)

        current_line: List[Dict[str, Any]] = []
        current_y = None

        for frag in page_fragments:
            if current_y is None or abs(frag["y"] - current_y) <= 4.0:
                current_line.append(frag)
                if current_y is None:
                    current_y = frag["y"]
            else:
                current_line.sort(key=lambda f: f["x"])
                lines.append(current_line)
                current_line = [frag]
                current_y = frag["y"]

        if current_line:
            current_line.sort(key=lambda f: f["x"])
            lines.append(current_line)

        # Format lines into text / markdown tables
        page_str_lines = []
        for line_frags in lines:
            if len(line_frags) >= 2:
                # Table row detection based on x gaps
                row_cells = [line_frags[0]["text"]]
                for idx in range(1, len(line_frags)):
                    gap = line_frags[idx]["x"] - (line_frags[idx-1]["x"] + len(line_frags[idx-1]["text"]) * 5)
                    if gap > 15:
                        row_cells.append(line_frags[idx]["text"])
                    else:
                        row_cells[-1] += " " + line_frags[idx]["text"]
                if len(row_cells) > 1:
                    page_str_lines.append("| " + " | ".join(row_cells) + " |")
                else:
                    page_str_lines.append(" ".join(f["text"] for f in line_frags))
            else:
                page_str_lines.append(" ".join(f["text"] for f in line_frags))

        text_parts.append("\n".join(page_str_lines))

    return "\n".join(text_parts)


def read_document_text(file_path: str) -> str:
    """
    Extracts text content or data from office document formats (.pdf, .docx, .pptx, .xlsx, .xls).
    Returns formatted string content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return _extract_pdf_layout_and_tables(file_path)
        
    elif ext in [".docx", ".pptx", ".xlsx", ".xls"]:
        from src.tools.documents_office import read_office_document_text
        return read_office_document_text(file_path, ext)
        
            
    else:
        raise ValueError(f"Unsupported document format: {ext}")





# --- Office/slides tools live in documents_office.py + documents_slides.py (re-exported here) ---
from src.tools.documents_office import (
    create_word_document,
    edit_word_document,
    create_excel_document,
    edit_excel_document,
)  # noqa: F401
from src.tools.documents_slides import (
    create_powerpoint_presentation,
    edit_powerpoint_presentation,
)  # noqa: F401

def create_pdf_document(file_path: str, content_markdown: str) -> str:
    """
    Generates a PDF document from Markdown text using reportlab.
    Supports headings (# Heading), bullets (- Bullet), and bold/italic markup.
    """
    if SimpleDocTemplate is None:
        raise ImportError("The 'reportlab' package is not installed.")
        
    parent = os.path.dirname(os.path.abspath(file_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
        
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Helper to convert basic md to html-like tags for reportlab Paragraph
    def md_to_html(text: str) -> str:
        text = re.sub(r'\*\*(.*?)\*\*|__(.*?)__', r'<b>\1\2</b>', text)
        text = re.sub(r'\*(.*?)\*|_(.*?)_', r'<i>\1\2</i>', text)
        return text

    story = []
    
    for line in content_markdown.splitlines():
        stripped = line.strip()
        if not line:
            story.append(Spacer(1, 10))
            continue
            
        if stripped.startswith("# "):
            title = md_to_html(stripped[2:])
            story.append(Paragraph(title, styles['Title']))
            story.append(Spacer(1, 12))
        elif stripped.startswith("## "):
            h1 = md_to_html(stripped[3:])
            story.append(Paragraph(h1, styles['Heading1']))
            story.append(Spacer(1, 10))
        elif stripped.startswith("### "):
            h2 = md_to_html(stripped[4:])
            story.append(Paragraph(h2, styles['Heading2']))
            story.append(Spacer(1, 8))
        elif stripped.startswith("- ") or stripped.startswith("* "):
            item = md_to_html(stripped[2:])
            story.append(Paragraph(f"&bull; {item}", styles['Normal']))
            story.append(Spacer(1, 4))
        else:
            body = md_to_html(line)
            story.append(Paragraph(body, styles['Normal']))
            story.append(Spacer(1, 6))
            
    doc.build(story)
    
    log_sensitive_action(
        category="FILE_WRITE",
        action="create_pdf_document",
        details={"path": file_path, "markdown_length": len(content_markdown)},
        status="SUCCESS"
    )
    return f"Successfully created PDF document at {file_path}"


def edit_pdf_document(
    file_path: str, 
    action: str, 
    merge_with_path: Optional[str] = None, 
    append_markdown: Optional[str] = None
) -> str:
    """
    Edits a PDF document. Since PDFs are not easily modified in-place, the actions supported are:
    - 'merge': Merges the current PDF file with another PDF file (specified in merge_with_path), saving the output at file_path.
    - 'append_pages': Generates a temporary PDF from append_markdown and appends it to the end of the PDF at file_path.
    """
    if not pypdf:
        raise ImportError("The 'pypdf' package is not installed.")
        
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF document not found: {file_path}")
        
    if action == "merge":
        if not merge_with_path:
            raise ValueError("merge_with_path is required for merge action")
        if not os.path.exists(merge_with_path):
            raise FileNotFoundError(f"PDF file to merge not found: {merge_with_path}")
            
        writer = pypdf.PdfWriter()
        writer.append(file_path)
        writer.append(merge_with_path)
        
        # Temp save then move to keep atomic
        temp_path = file_path + ".tmp"
        writer.write(temp_path)
        writer.close()
        
        if os.path.exists(file_path):
            os.remove(file_path)
        os.rename(temp_path, file_path)
        
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_pdf_document:merge",
            details={"path": file_path, "merged_with": merge_with_path},
            status="SUCCESS"
        )
        return f"Successfully merged {merge_with_path} into {file_path}"
        
    elif action == "append_pages":
        if not append_markdown:
            raise ValueError("append_markdown is required for append_pages action")
            
        temp_pdf = file_path + ".append.tmp.pdf"
        try:
            create_pdf_document(temp_pdf, append_markdown)
            
            writer = pypdf.PdfWriter()
            writer.append(file_path)
            writer.append(temp_pdf)
            
            temp_path = file_path + ".tmp"
            writer.write(temp_path)
            writer.close()
            
            if os.path.exists(file_path):
                os.remove(file_path)
            os.rename(temp_path, file_path)
        finally:
            if os.path.exists(temp_pdf):
                os.remove(temp_pdf)
                
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_pdf_document:append_pages",
            details={"path": file_path, "append_length": len(append_markdown)},
            status="SUCCESS"
        )
        return f"Successfully appended pages generated from markdown to {file_path}"
        
    else:
        raise ValueError(f"Unsupported action: {action}")
