import os
import pytest
from src.tools.documents import (
    read_document_text,
    create_word_document,
    edit_word_document,
    create_excel_document,
    edit_excel_document,
    create_powerpoint_presentation,
    edit_powerpoint_presentation,
    create_pdf_document,
    edit_pdf_document
)

def test_word_document_flow(tmp_path):
    doc_path = os.path.join(tmp_path, "test.docx")
    
    # 1. Create document
    content = "# Document Title\n## Section 1\nThis is a **bold** and *italic* paragraph.\n- Bullet point 1\n- Bullet point 2"
    result = create_word_document(doc_path, content)
    assert "Successfully created" in result
    assert os.path.exists(doc_path)
    
    # 2. Read document
    read_content = read_document_text(doc_path)
    assert "Document Title" in read_content
    assert "Section 1" in read_content
    assert "This is a bold and italic paragraph." in read_content
    assert "Bullet point 1" in read_content
    
    # 3. Edit document (replace text)
    edit_result = edit_word_document(
        file_path=doc_path,
        action="replace_text",
        search_text="bold and italic",
        replace_text="modified"
    )
    assert "Successfully replaced" in edit_result
    
    read_content_after_replace = read_document_text(doc_path)
    assert "This is a modified paragraph." in read_content_after_replace
    
    # 4. Edit document (append text)
    append_content = "### Section 2\nThis is appended text."
    append_result = edit_word_document(
        file_path=doc_path,
        action="append_text",
        append_markdown=append_content
    )
    assert "Successfully appended" in append_result
    
    read_content_after_append = read_document_text(doc_path)
    assert "Section 2" in read_content_after_append
    assert "This is appended text." in read_content_after_append


def test_excel_document_flow(tmp_path):
    xls_path = os.path.join(tmp_path, "test.xlsx")
    
    # 1. Create sheet
    sheets_data = {
        "Sheet1": [
            ["Header1", "Header2", "Header3"],
            [1, "Alice", 95.5],
            [2, "Bob", 88.0]
        ],
        "Sheet2": [
            ["ID", "Comment"],
            [101, "First comment"],
            [102, "Second comment"]
        ]
    }
    result = create_excel_document(xls_path, sheets_data)
    assert "Successfully created" in result
    assert os.path.exists(xls_path)
    
    # 2. Read sheet
    read_content = read_document_text(xls_path)
    assert "Sheet: Sheet1" in read_content
    assert "Header1 | Header2 | Header3" in read_content
    assert "Alice" in read_content
    assert "Sheet: Sheet2" in read_content
    assert "First comment" in read_content
    
    # 3. Edit sheet (update cells)
    edit_result = edit_excel_document(
        file_path=xls_path,
        action="update_cells",
        sheet_name="Sheet1",
        range_or_cell="B2",
        data=[["Alex"]]
    )
    assert "Successfully updated" in edit_result
    
    read_content_after_update = read_document_text(xls_path)
    assert "Alex" in read_content_after_update
    assert "Alice" not in read_content_after_update
    
    # 4. Edit sheet (append rows)
    append_result = edit_excel_document(
        file_path=xls_path,
        action="append_rows",
        sheet_name="Sheet1",
        data=[[3, "Charlie", 72.3]]
    )
    assert "Successfully appended" in append_result
    
    read_content_after_append = read_document_text(xls_path)
    assert "Charlie" in read_content_after_append
    
    # 5. Edit sheet (replace text)
    replace_result = edit_excel_document(
        file_path=xls_path,
        action="replace_text",
        sheet_name="Sheet2",
        find_text="First comment",
        replace_text="Updated comment"
    )
    assert "Successfully replaced" in replace_result
    
    read_content_after_replace = read_document_text(xls_path)
    assert "Updated comment" in read_content_after_replace
    assert "First comment" not in read_content_after_replace


def test_powerpoint_presentation_flow(tmp_path):
    ppt_path = os.path.join(tmp_path, "test.pptx")
    
    # 1. Create presentation
    slides_data = [
        {"title": "Introduction", "content": ["Slide content paragraph 1", "Slide content paragraph 2"]},
        {"title": "Methods", "content": ["Step 1: Planning", "Step 2: Execution"]}
    ]
    result = create_powerpoint_presentation(ppt_path, slides_data)
    assert "Successfully created" in result
    assert os.path.exists(ppt_path)
    
    # 2. Read presentation
    read_content = read_document_text(ppt_path)
    assert "Slide 1" in read_content
    assert "Introduction" in read_content
    assert "Slide content paragraph 1" in read_content
    assert "Methods" in read_content
    assert "Step 1: Planning" in read_content
    
    # 3. Edit presentation (add slide)
    edit_result = edit_powerpoint_presentation(
        file_path=ppt_path,
        action="add_slide",
        title="Conclusion",
        content=["Summary of findings", "Future work"]
    )
    assert "Successfully added slide" in edit_result
    
    read_content_after_add = read_document_text(ppt_path)
    assert "Conclusion" in read_content_after_add
    assert "Summary of findings" in read_content_after_add
    
    # 4. Edit presentation (replace text)
    replace_result = edit_powerpoint_presentation(
        file_path=ppt_path,
        action="replace_text",
        find_text="Planning",
        replace_text="Designing"
    )
    assert "Successfully replaced" in replace_result
    
    read_content_after_replace = read_document_text(ppt_path)
    assert "Step 1: Designing" in read_content_after_replace
    assert "Step 1: Planning" not in read_content_after_replace


def test_pdf_document_flow(tmp_path):
    pdf_path = os.path.join(tmp_path, "test.pdf")
    
    # 1. Create PDF
    content = "# PDF Report\n## Introduction\nThis is a standard PDF document compiled from markdown.\n- Point 1\n- Point 2"
    result = create_pdf_document(pdf_path, content)
    assert "Successfully created" in result
    assert os.path.exists(pdf_path)
    
    # 2. Read PDF
    read_content = read_document_text(pdf_path)
    assert "PDF Report" in read_content
    assert "Introduction" in read_content
    assert "This is a standard PDF document compiled from markdown." in read_content
    assert "Point 1" in read_content
    
    # 3. Edit PDF (append pages)
    append_content = "# Appendix\n## Table of Contents\nSome additional text here."
    append_result = edit_pdf_document(
        file_path=pdf_path,
        action="append_pages",
        append_markdown=append_content
    )
    assert "Successfully appended" in append_result
    
    read_content_after_append = read_document_text(pdf_path)
    assert "Appendix" in read_content_after_append
    assert "Table of Contents" in read_content_after_append
    
    # 4. Edit PDF (merge)
    other_pdf_path = os.path.join(tmp_path, "other.pdf")
    create_pdf_document(other_pdf_path, "# Merged Document\nThis comes from another PDF.")
    
    merge_result = edit_pdf_document(
        file_path=pdf_path,
        action="merge",
        merge_with_path=other_pdf_path
    )
    assert "Successfully merged" in merge_result
    
    read_content_after_merge = read_document_text(pdf_path)
    assert "Merged Document" in read_content_after_merge
    assert "This comes from another PDF." in read_content_after_merge
