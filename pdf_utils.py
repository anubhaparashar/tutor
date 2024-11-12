# pdf_utils.py
import PyPDF2

def extract_text_from_pdf(file) -> str:
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(min(10, pdf_reader.numPages)):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text.strip()
