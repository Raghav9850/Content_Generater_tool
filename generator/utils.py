# generator/utils.py

import io
from fpdf import FPDF

def generate_content_pdf(content):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add content to the PDF
    pdf.multi_cell(0, 10, txt=content)
    
    # Save the PDF to a buffer
    buffer = io.BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # Output PDF as bytes
    buffer.write(pdf_bytes)
    
    # Get the content of the buffer
    pdf_content = buffer.getvalue()
    buffer.close()
    
    return pdf_content

def generate_content_txt(content):
    # Your logic to generate TXT from content
    return content
