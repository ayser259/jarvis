
# import high-level pipeline 
import setup
from helpers import save_file
from recordings.audio_file_path import audio_file_path,transcript_name
from transformers import pipeline

# This line will load your desired model
print("Setting up pipeline...")
pipe = pipeline("automatic-speech-recognition",model="openai/whisper-large-v3",max_new_tokens=100, chunk_length_s=30)
print("transcribing...")
text = pipe(audio_file_path,
    max_new_tokens=256,
    generate_kwargs={"task": "transcribe"},
    chunk_length_s=30,
    batch_size=8,
    return_timestamps=True)
print("saving...")
save_file(transcript_name,text)
print("done")

# Helpful for debugging
# https://stackoverflow.com/questions/76846657/how-to-use-model-from-huggingface-to-make-an-app-which-can-transcribe-a-local