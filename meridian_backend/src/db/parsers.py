import os

def extract_text_from_file(file_path: str) -> str:
    """Extracts text content from various file formats (.txt, .md, .json, .csv, .pdf, .docx)."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext in [".txt", ".md", ".json", ".csv"]:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    elif ext == ".pdf":
        try:
            import pypdf
            reader = pypdf.PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except ImportError:
            raise ImportError("The 'pypdf' package is required to parse PDF files. Run 'install_package' with arg 'pypdf' first.")
    elif ext == ".docx":
        try:
            import docx
            doc = docx.Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])
        except ImportError:
            raise ImportError("The 'python-docx' package is required to parse DOCX files. Run 'install_package' with arg 'python-docx' first.")
    else:
        raise ValueError(f"Unsupported file extension: '{ext}'. Supported formats: .txt, .md, .json, .csv, .pdf, .docx")
