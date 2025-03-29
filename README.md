# Intelligent-Classroom-Assistant

## Overview
The **Intelligent Classroom Assistant** is an AI-powered tool designed to enhance lecture recordings by transcribing, summarizing, and generating organized lecture notes. It records audio, captures blackboard images, and creates a well-structured PDF for easy reference.

## Features
- **Audio Recording:** Records lecture audio for transcription.
- **Blackboard Capture:** Captures images of the blackboard for visual notes.
- **Speech-to-Text Transcription:** Converts audio into text.
- **Text Summarization:** Generates concise lecture summaries.
- **PDF Generation:** Combines text summaries and images into a PDF file.
- **Post-Processing:** Corrects errors in transcribed text for better accuracy.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- FFmpeg (for audio processing)
- Required Python libraries (see below)

### Clone the Repository
```sh
git clone https://github.com/retr0alfred/Intelligent-Classroom-Assistant.git
cd Intelligent-Classroom-Assistant
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up FFmpeg (Windows Users)
Download FFmpeg and add its `bin` directory to your system's PATH.

## Usage
### 1. Start the Assistant
Run the main script to start recording and processing a lecture:
```sh
python main.py
```

### 2. Output Files
- **Audio File:** `output/audio.wav`
- **Captured Images:** `output/images/`
- **Generated PDF Notes:** `transcriptions/lecture_notes.pdf`

### 3. Correct the PDF (Post-processing)
To run the correction script after generating the PDF:
```sh
python correct_pdf.py
```

## Project Structure
```
Intelligent-Classroom-Assistant/
├── main.py              # Main script to run the assistant
├── record_audio.py      # Handles audio recording
├── capture_board.py     # Captures blackboard images
├── transcribe_audio.py  # Converts audio to text
├── summarize_notes.py   # Summarizes transcribed text
├── generate_pdf.py      # Creates PDF with notes and images
├── correct_pdf.py       # Improves the generated PDF
├── utils/               # Utility scripts
│   ├── pdf_utils.py     # PDF processing utilities
│   ├── ai_model.py      # AI-powered text correction
├── output/              # Stores recordings & images (ignored by Git)
├── transcriptions/      # Stores generated PDFs (ignored by Git)
└── README.md            # Project documentation
```

## Contributions
Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
Developed by **retr0alfred**.

