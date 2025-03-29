from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from textwrap import wrap

def create_pdf(summary_text, image_folder, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, "Lecture Notes")

    text = c.beginText(100, 720)
    text.setFont("Helvetica", 10)

    wrapped_text = []
    for line in summary_text.split('. '):  
        wrapped_text.extend(wrap(line.strip() + '.', width=80))  

    y_position = 720
    for line in wrapped_text:
        if y_position < 100:  
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = 750  

        c.drawString(100, y_position, line)
        y_position -= 15  

    y_position -= 30  
    for img_file in sorted(os.listdir(image_folder)):
        img_path = os.path.join(image_folder, img_file)
        if y_position < 320:  
            c.showPage()
            y_position = 750

        c.drawImage(img_path, 100, y_position - 300, width=400, height=300)
        y_position -= 320  

    c.save()
    print(f"PDF saved as {pdf_filename}")
