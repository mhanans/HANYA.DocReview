import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> dict:
    """Mengekstrak teks dari PDF per halaman."""
    text_per_page = {}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            text_per_page[i + 1] = text if text else "Tidak ada teks yang dapat diekstrak."
    return text_per_page