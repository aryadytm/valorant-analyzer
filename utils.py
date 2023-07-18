import docx2txt
from pypdf import PdfReader
from reportlab.pdfgen import canvas
    

def extract_text_from_pdf(file_path: str):
    pdf = PdfReader(file_path)
    text = "\n\n".join([it.extract_text() for it in pdf.pages])
    return text


def extract_text_from_docx(file_path: str):
    return docx2txt.process(file_path)


def extract_text(file_path: str):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        return "[CV Returned Error]: Unsupported file format. Only PDF and DOCX files are supported."