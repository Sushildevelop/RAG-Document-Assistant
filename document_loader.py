import fitz  # PyMuPDF

def load_document(file_path: str) -> str:
    """
    Loads text from:
    - TXT files
    - PDF files

    WHY:
    - PDFs are binary
    - Need special reader
    """

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif file_path.endswith(".pdf"):
        text = ""
        doc = fitz.open(file_path)

        for page in doc:
            text += page.get_text()

        return text
        
    else:
        raise ValueError("Unsupported file format")


def load_pdf(file_path: str) -> str:
    """
    WHY:
    - PDFs are binary
    - PyMuPDF extracts text safely
    """
    text = ""
    doc = fitz.open(file_path)

    for page_number, page in enumerate(doc, start=1):
        page_text = page.get_text()
        if page_text:
            text += f"\n[Page {page_number}]\n{page_text}"

    return text
