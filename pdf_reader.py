import fitz  # PyMuPDF

def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        texto = ""
        for page in doc:
            texto += page.get_text()
        return texto
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return ""

