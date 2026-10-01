"""Office document tools (Word / Excel / PowerPoint).

Split from ``src.tools.documents`` (Phase 2 god-file refactor). Pure move -
zero behavior changes. ``documents.py`` re-exports every symbol so existing
imports keep working.
"""

import os
import re
from typing import Dict, Any, List, Optional
from src.core.audit_logger import log_sensitive_action

# Word documents
try:
    import docx
except ImportError:
    docx = None

# Excel spreadsheets
try:
    import openpyxl
except ImportError:
    openpyxl = None

# PowerPoint presentations (all-or-nothing so partial imports cannot NameError later)
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
except ImportError:
    Presentation = None
    Inches = None
    Pt = None

def create_word_document(file_path: str, content_markdown: str) -> str:
    """
    Creates a Word (.docx) document from markdown-formatted text.
    Supports headings (# Heading), bullets (- Bullet), and bold/italic inline markdown.
    """
    if not docx:
        raise ImportError("The 'python-docx' package is not installed.")
        
    parent = os.path.dirname(os.path.abspath(file_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
        
    doc = docx.Document()
    
    def parse_inline_and_add(paragraph, text):
        # Parses **bold** and *italic*
        parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)
        for part in parts:
            if part.startswith("**") and part.endswith("**"):
                r = paragraph.add_run(part[2:-2])
                r.bold = True
            elif part.startswith("*") and part.endswith("*"):
                r = paragraph.add_run(part[1:-1])
                r.italic = True
            else:
                paragraph.add_run(part)

    for line in content_markdown.splitlines():
        stripped = line.strip()
        if not line: # Preserve empty paragraphs
            doc.add_paragraph()
            continue
            
        if stripped.startswith("# "):
            p = doc.add_paragraph()
            p.style = doc.styles['Heading 1']
            parse_inline_and_add(p, stripped[2:])
        elif stripped.startswith("## "):
            p = doc.add_paragraph()
            p.style = doc.styles['Heading 2']
            parse_inline_and_add(p, stripped[3:])
        elif stripped.startswith("### "):
            p = doc.add_paragraph()
            p.style = doc.styles['Heading 3']
            parse_inline_and_add(p, stripped[4:])
        elif stripped.startswith("- ") or stripped.startswith("* "):
            p = doc.add_paragraph(style='List Bullet')
            parse_inline_and_add(p, stripped[2:])
        else:
            p = doc.add_paragraph()
            parse_inline_and_add(p, line)
            
    doc.save(file_path)
    
    log_sensitive_action(
        category="FILE_WRITE",
        action="create_word_document",
        details={"path": file_path, "markdown_length": len(content_markdown)},
        status="SUCCESS"
    )
    return f"Successfully created Word document at {file_path}"


def edit_word_document(
    file_path: str, 
    action: str, 
    search_text: Optional[str] = None, 
    replace_text: Optional[str] = None, 
    append_markdown: Optional[str] = None
) -> str:
    """
    Edits a Word (.docx) file.
    Actions supported:
    - 'replace_text': Searches and replaces all instances of search_text with replace_text.
    - 'append_text': Appends content formatted as markdown to the end of the document.
    """
    if not docx:
        raise ImportError("The 'python-docx' package is not installed.")
        
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Word document not found: {file_path}")
        
    doc = docx.Document(file_path)
    
    if action == "replace_text":
        if not search_text:
            raise ValueError("search_text is required for replace_text action")
        replace_text = replace_text or ""
        
        count = 0
        for paragraph in doc.paragraphs:
            if search_text in paragraph.text:
                # To maintain formatting runs as best as possible, we do run replacement or paragraph-level replace
                # Replacing at run level can be fragmented, so we replace paragraph text if it's simpler
                # However, full text replacement at paragraph level resets formatting. We try run-level first:
                # If search_text matches a single run, replace it. Otherwise, replace paragraph text.
                replaced = False
                for run in paragraph.runs:
                    if search_text in run.text:
                        run.text = run.text.replace(search_text, replace_text)
                        replaced = True
                        count += 1
                if not replaced:
                    paragraph.text = paragraph.text.replace(search_text, replace_text)
                    count += 1
                    
        doc.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_word_document:replace_text",
            details={"path": file_path, "search_text": search_text, "replacements": count},
            status="SUCCESS"
        )
        return f"Successfully replaced {count} instances of '{search_text}' in {file_path}"
        
    elif action == "append_text":
        if not append_markdown:
            raise ValueError("append_markdown is required for append_text action")
            
        def parse_inline_and_add(paragraph, text):
            parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)
            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    r = paragraph.add_run(part[2:-2])
                    r.bold = True
                elif part.startswith("*") and part.endswith("*"):
                    r = paragraph.add_run(part[1:-1])
                    r.italic = True
                else:
                    paragraph.add_run(part)

        for line in append_markdown.splitlines():
            stripped = line.strip()
            if not line:
                doc.add_paragraph()
                continue
                
            if stripped.startswith("# "):
                p = doc.add_paragraph()
                p.style = doc.styles['Heading 1']
                parse_inline_and_add(p, stripped[2:])
            elif stripped.startswith("## "):
                p = doc.add_paragraph()
                p.style = doc.styles['Heading 2']
                parse_inline_and_add(p, stripped[3:])
            elif stripped.startswith("### "):
                p = doc.add_paragraph()
                p.style = doc.styles['Heading 3']
                parse_inline_and_add(p, stripped[4:])
            elif stripped.startswith("- ") or stripped.startswith("* "):
                p = doc.add_paragraph(style='List Bullet')
                parse_inline_and_add(p, stripped[2:])
            else:
                p = doc.add_paragraph()
                parse_inline_and_add(p, line)
                
        doc.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_word_document:append_text",
            details={"path": file_path, "append_length": len(append_markdown)},
            status="SUCCESS"
        )
        return f"Successfully appended markdown content to Word document {file_path}"
        
    else:
        raise ValueError(f"Unsupported action: {action}")


def create_excel_document(file_path: str, sheets_data: Dict[str, List[List[Any]]]) -> str:
    """
    Creates an Excel (.xlsx) document.
    sheets_data is a dictionary where keys are sheet names and values are 2D arrays of cells.
    """
    if not openpyxl:
        raise ImportError("The 'openpyxl' package is not installed.")
        
    parent = os.path.dirname(os.path.abspath(file_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
        
    wb = openpyxl.Workbook()
    # Remove default sheet
    default_sheet = wb.active
    if default_sheet is not None:
        wb.remove(default_sheet)
    
    for sheet_name, rows in sheets_data.items():
        ws = wb.create_sheet(title=sheet_name)
        for row in rows:
            ws.append(row)
            
    wb.save(file_path)
    log_sensitive_action(
        category="FILE_WRITE",
        action="create_excel_document",
        details={"path": file_path, "sheets": list(sheets_data.keys())},
        status="SUCCESS"
    )
    return f"Successfully created Excel document at {file_path}"


def edit_excel_document(
    file_path: str, 
    action: str, 
    sheet_name: str, 
    range_or_cell: Optional[str] = None, 
    data: Optional[List[List[Any]]] = None, 
    find_text: Optional[str] = None, 
    replace_text: Optional[str] = None
) -> str:
    """
    Edits an Excel (.xlsx) file.
    Actions supported:
    - 'update_cells': Updates a specific cell or range (e.g. 'A1' or 'A1:B2') in sheet_name using data (2D array).
    - 'append_rows': Appends rows (2D array in data) to the end of sheet_name.
    - 'replace_text': Replaces all cells matching find_text with replace_text in sheet_name.
    """
    if not openpyxl:
        raise ImportError("The 'openpyxl' package is not installed.")
        
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found: {file_path}")
        
    wb = openpyxl.load_workbook(file_path)
    if sheet_name not in wb.sheetnames:
        raise ValueError(f"Sheet '{sheet_name}' not found in Excel workbook.")
        
    ws = wb[sheet_name]
    
    if action == "update_cells":
        if not range_or_cell:
            raise ValueError("range_or_cell is required for update_cells action")
        if not data:
            raise ValueError("data is required for update_cells action")
            
        # Check if single cell or range
        if ":" in range_or_cell:
            cells_range = ws[range_or_cell]
            # data should match the dimensions of the range
            # Flatten or match row-by-row
            for i, row in enumerate(cells_range):
                if i >= len(data):
                    break
                for j, cell in enumerate(row):
                    if j >= len(data[i]):
                        break
                    cell.value = data[i][j]
        else:
            ws[range_or_cell] = data[0][0] if isinstance(data[0], list) else data[0]
            
        wb.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_excel_document:update_cells",
            details={"path": file_path, "sheet": sheet_name, "range": range_or_cell},
            status="SUCCESS"
        )
        return f"Successfully updated cells '{range_or_cell}' in sheet '{sheet_name}' of {file_path}"
        
    elif action == "append_rows":
        if not data:
            raise ValueError("data (list of rows) is required for append_rows action")
            
        for row in data:
            ws.append(row)
            
        wb.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_excel_document:append_rows",
            details={"path": file_path, "sheet": sheet_name, "rows_count": len(data)},
            status="SUCCESS"
        )
        return f"Successfully appended {len(data)} rows to sheet '{sheet_name}' in {file_path}"
        
    elif action == "replace_text":
        if not find_text:
            raise ValueError("find_text is required for replace_text action")
        replace_text = replace_text or ""
        
        count = 0
        for row in ws.iter_rows():
            for cell in row:
                if cell.value is not None and str(cell.value) == find_text:
                    cell.value = replace_text
                    count += 1
                    
        wb.save(file_path)
        log_sensitive_action(
            category="FILE_WRITE",
            action="edit_excel_document:replace_text",
            details={"path": file_path, "sheet": sheet_name, "replacements": count},
            status="SUCCESS"
        )
        return f"Successfully replaced {count} cells in sheet '{sheet_name}' in {file_path}"
        
    else:
        raise ValueError(f"Unsupported action: {action}")




def read_office_document_text(file_path: str, ext: str) -> str:
    """Reads Word / PowerPoint / Excel formats. Split from documents.read_document_text."""
    if ext == ".docx":
        if not docx:
            raise ImportError("The 'python-docx' package is not installed.")
        doc = docx.Document(file_path)
        text_parts = []
        for p in doc.paragraphs:
            text_parts.append(p.text)
        for table in doc.tables:
            text_parts.append("\n--- Table ---")
            for row in table.rows:
                row_text = [cell.text for cell in row.cells]
                text_parts.append(" | ".join(row_text))
        return "\n".join(text_parts)
        
    elif ext == ".pptx":
        if not Presentation:
            raise ImportError("The 'python-pptx' package is not installed.")
        prs = Presentation(file_path)
        text_parts = []
        for i, slide in enumerate(prs.slides):
            text_parts.append(f"--- Slide {i + 1} ---")
            for shape in slide.shapes:
                if hasattr(shape, "text") and shape.text.strip():
                    text_parts.append(shape.text)
        return "\n".join(text_parts)
        
    elif ext in [".xlsx", ".xls"]:
        if ext == ".xlsx":
            if not openpyxl:
                raise ImportError("The 'openpyxl' package is not installed.")
            wb = openpyxl.load_workbook(file_path, data_only=True)
            text_parts = []
            for sheet_name in wb.sheetnames:
                sheet = wb[sheet_name]
                text_parts.append(f"--- Sheet: {sheet_name} ---")
                
                # Convert sheet to a Markdown table
                rows = list(sheet.iter_rows(values_only=True))
                if not rows:
                    text_parts.append("(Empty Sheet)")
                    continue
                
                # Filter trailing empty rows/cols to keep the representation clean
                clean_rows = []
                for row in rows:
                    if any(cell is not None for cell in row):
                        clean_rows.append(row)
                
                if not clean_rows:
                    text_parts.append("(Empty Sheet)")
                    continue
                
                # Determine max columns
                max_cols = max(len(r) for r in clean_rows)
                for r in clean_rows:
                    cells = [str(c) if c is not None else "" for c in r]
                    # Pad cells to max_cols
                    cells += [""] * (max_cols - len(cells))
                    text_parts.append(" | " + " | ".join(cells) + " |")
                    
            return "\n".join(text_parts)
        else:
            try:
                import importlib
                xlrd = importlib.import_module("xlrd")
            except ImportError:
                raise ImportError("The 'xlrd' package is required to read old Excel .xls files.")
            wb = xlrd.open_workbook(file_path)
            text_parts = []
            for sheet_index in range(wb.nsheets):
                sheet = wb.sheet_by_index(sheet_index)
                text_parts.append(f"--- Sheet: {sheet.name} ---")
                for r in range(sheet.nrows):
                    row_vals = [f"{sheet.cell_value(r, c)}" for c in range(sheet.ncols)]
                    text_parts.append(" | " + " | ".join(row_vals) + " |")
            return "\n".join(text_parts)
    else:
        raise ValueError(f"Unsupported office document format: {ext}")
