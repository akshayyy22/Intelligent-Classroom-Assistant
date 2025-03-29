import os
import pyaudio
import wave

def record_audio(output_filename, duration):
    CHUNK = 1024  
    FORMAT = pyaudio.paInt16  
    CHANNELS = 1  
    RATE = 44100  

    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    except OSError as e:
        print("Error: Could not access the microphone. Check your input device.")
        p.terminate()
        return

    print(f"Recording audio for {duration} seconds...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    print("Recording complete.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved to {output_filename}")
