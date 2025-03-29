from utils.ai_model import correct_text
from utils.pdf_utils import extract_text_from_pdf
from fpdf import FPDF
import os

def save_to_pdf(text, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    lines = text.split("\n")
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True, align="L")

    pdf.output(output_path)
    print(f"Corrected PDF saved as: {output_path}")

def main():
    pdf_path = "transcriptions/lecture_notes.pdf"  
    output_pdf = "output/finalpdf/corrected_output.pdf"

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("Correcting text using AI...")
    corrected_text = correct_text(text)  

    print("Saving corrected text to PDF...")
    save_to_pdf(corrected_text, output_pdf)

if __name__ == "__main__":
    main()
