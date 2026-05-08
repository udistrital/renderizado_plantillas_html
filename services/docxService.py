import tempfile
from io import BytesIO
from pathlib import Path
from pdf2docx import Converter
from .pdfService import renderizar_pdf

def renderizar_docx(plantillaHTML, css=None, context={}):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
        pdf_bytes = renderizar_pdf(plantillaHTML, css, context)
        temp_pdf.write(pdf_bytes)
        temp_pdf_path = temp_pdf.name
    
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as temp_docx:
        temp_docx_path = temp_docx.name
    
    try:
        # Convertir el PDF a DOCX
        cv = Converter(temp_pdf_path)
        cv.convert(temp_docx_path, start=0, end=None)
        cv.close()
        
        # Leer el archivo DOCX generado
        with open(temp_docx_path, "rb") as docx_file:
            docx_bytes = docx_file.read()
        
        return docx_bytes
    finally:
        # Limpiar los archivos temporales
        Path(temp_pdf_path).unlink(missing_ok=True)
        Path(temp_docx_path).unlink(missing_ok=True)