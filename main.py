import time
import os
import subprocess
from record_audio import record_audio
from capture_board import capture_images
from transcribe_audio import transcribe_audio
from summarize_notes import summarize_text
from generate_pdf import create_pdf

FFMPEG_PATH = r"C:\\Users\\manue\\Downloads\\ffmpeg-2025-03-27-git-114fccc4a5-full_build\\ffmpeg-2025-03-27-git-114fccc4a5-full_build\\bin"
if FFMPEG_PATH not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + FFMPEG_PATH

Runtime = int(input("Enter Class Duration in Seconds"))
TOTAL_RUNTIME = Runtime 

OUTPUT_FOLDER = "output"
PDFOUT = "transcriptions"
IMAGE_FOLDER = os.path.join(OUTPUT_FOLDER, "images")
AUDIO_FILE = os.path.join(OUTPUT_FOLDER, "audio.wav")
PDF_FILE = os.path.join(PDFOUT, "lecture_notes.pdf")
CORRECTED_PDF_FILE = os.path.join(PDFOUT, "corrected_lecture_notes.pdf")

os.makedirs(IMAGE_FOLDER, exist_ok=True)

start_time = time.time()

print("Recording started...")
record_audio(AUDIO_FILE, TOTAL_RUNTIME)

while time.time() - start_time < TOTAL_RUNTIME:
    print("Capturing board image...")
    capture_images(IMAGE_FOLDER)  
    remaining_time = TOTAL_RUNTIME - (time.time() - start_time)
    
    if remaining_time > 60:
        time.sleep(60)
    else:
        break  

if not os.path.exists(AUDIO_FILE):
    raise FileNotFoundError(f"Audio file not found: {AUDIO_FILE}")

print("Transcribing audio...")
transcribed_text = transcribe_audio(AUDIO_FILE)

print("Summarizing notes...")
summary = summarize_text(transcribed_text)

print("Generating PDF...")
create_pdf(summary, IMAGE_FOLDER, PDF_FILE)

print(f"Lecture notes saved as {PDF_FILE}")

print("🔄 Running PDF correction script...")
try:
    subprocess.run(["python", "correct_pdf.py"], check=True)
    print(f"✅ Corrected PDF saved as {CORRECTED_PDF_FILE}")
except subprocess.CalledProcessError as e:
    print(f"❌ Error while correcting PDF: {e}")

print("Program finished.")
