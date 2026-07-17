# Spec: Document Processing Tools

## Objective
Enable the Meridian-X agent to read, create, and edit common office document formats including PDF (`.pdf`), Word (`.docx`), Excel (`.xlsx`, `.xls`), and PowerPoint (`.pptx`).

Currently, the agent is restricted to reading and writing plaintext formats. Reading binary formats results in decoding errors or garbled text, and creating/editing them is not supported. Providing dedicated document tools will allow the agent to handle office tasks natively.

## Tech Stack
We will use the following Python packages:
- `pypdf` (already a fallback dependency in `database.py`) for PDF reading and merging.
- `reportlab` for PDF generation from text/markdown.
- `python-docx` for Word document reading, creation, and editing.
- `openpyxl` for Excel (`.xlsx`) reading, creation, and editing.
- `xlrd` (optional, for `.xls` reading).
- `python-pptx` for PowerPoint presentation reading, creation, and editing.

## Commands
### Install Dependencies
To install the new dependencies in the virtual environment:
```powershell
.\venv\Scripts\pip install pypdf reportlab python-docx openpyxl python-pptx xlrd
```

### Run Tests
To verify implementation:
```powershell
.\venv\Scripts\pytest tests/test_document_tools.py
```

## Project Structure
We will add a new tool module under `meridian_backend/src/tools/`:
- `meridian_backend/src/tools/documents.py` -> Core document tools.
- `meridian_backend/tests/test_document_tools.py` -> Automated tests for the new document tools.
- Modify `meridian_backend/src/tools/registry.py` to register the new tools.

## Code Style
We will write standard, clean Python 3.10+ code.
- Functions should handle errors gracefully and return informative strings.
- Add clear typing annotations.
- Log sensitive operations (e.g. file writing or editing) via the existing `log_sensitive_action` utility.

Example structure of a tool:
```python
import os
from typing import Dict, Any, List
from src.core.audit_logger import log_sensitive_action

def read_document_text(file_path: str) -> str:
    """Extracts text or tabular data from a PDF, DOCX, PPTX, or XLSX file."""
    # implementation details...
```

## Testing Strategy
We will create a test suite `meridian_backend/tests/test_document_tools.py` that covers:
1. Reading PDF, DOCX, XLSX, and PPTX files.
2. Creating PDF, DOCX, XLSX, and PPTX files.
3. Modifying DOCX, XLSX, and PPTX files.
4. Error handling for unsupported formats or missing files.

We will run the tests via pytest inside the backend virtual environment.

## Boundaries
- **Always:** Use relative paths or paths validated to be within safe user directories. Check if libraries are imported before running to prevent import failures.
- **Ask first:** Installing packages outside the listed requirements if any network blocks are in place.
- **Never:** Corrupt existing files. If editing a file, create a backup or ensure atomic writes to prevent data loss.

## Success Criteria
1. The agent can extract full text content from PDF, DOCX, PPTX, and XLSX files.
2. The agent can generate clean PDF and DOCX files from markdown-formatted text.
3. The agent can search and replace text or append content to DOCX and PPTX files.
4. The agent can read, create, and edit sheet rows/cells in XLSX files.
5. All new tools are registered in the Meridian-X backend tool registry and exposed to the ReAct reasoning agent loop.
6. The test suite passes completely.
