import fitz  

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def save_corrected_pdf(original_pdf, corrected_text, output_pdf):
    doc = fitz.open(original_pdf)
    
    for page_num, page in enumerate(doc):
        page.clean_contents()  
        text_rect = fitz.Rect(50, 50, 500, 750)  
        page.insert_textbox(text_rect, corrected_text, fontsize=10)

    doc.save(output_pdf)
    doc.close()
