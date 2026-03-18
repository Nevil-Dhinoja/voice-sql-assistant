import whisper
import sounddevice as sd
import soundfile as sf
from gtts import gTTS
import tempfile, os
import static_ffmpeg
static_ffmpeg.add_paths()  
model = whisper.load_model("base")

def record_audio(duration=5, sample_rate=16000):
    print("Recording... speak now!")
    audio = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate, channels=1,
                   dtype="float32")
    sd.wait()
    print("Done recording.")
    path = tempfile.mktemp(suffix=".wav")
    sf.write(path, audio, sample_rate)
    return path

def transcribe(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"].strip()

def speak(text: str) -> str:
    tts = gTTS(text=text, lang="en")
    path = tempfile.mktemp(suffix=".mp3")
    tts.save(path)
    return path