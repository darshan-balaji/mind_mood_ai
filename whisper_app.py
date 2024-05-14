import whisper
import os

model = whisper.load_model("base")

def transcribe(audio_path):
    audio_file_path = os.path.abspath(audio_path)
    transcription = model.transcribe(audio_file_path)
    return transcription['text']
    
if __name__ == "__main__":
    audio_path = 'sample.wav'
    transcription = transcribe(audio_path)
    print(transcription)