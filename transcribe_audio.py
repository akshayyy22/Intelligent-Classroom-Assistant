import os
import whisper
import warnings
import subprocess

warnings.filterwarnings("ignore")

os.environ["PATH"] += os.pathsep + "C:\\Users\\manue\\Downloads\\ffmpeg-2025-03-27-git-114fccc4a5-full_build\\ffmpeg-2025-03-27-git-114fccc4a5-full_build\\bin"

def transcribe_audio(audio_file=None):
    if audio_file is None:
        audio_file = os.path.abspath("output/audio.wav")  

    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Error: The audio file '{audio_file}' was not found!")

    model = whisper.load_model("base")

    result = model.transcribe(audio_file)
    return result["text"]

if __name__ == "__main__":
    try:
        text = transcribe_audio()
        print("Transcribed Text:\n", text)
    except Exception as e:
        print(f"An error occurred: {e}")
