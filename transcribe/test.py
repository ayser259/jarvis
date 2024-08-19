from transformers import pipeline
# import high-level pipeline 
import setup, os, json
from recordings.audio_file_path import audio_file_path,transcript_name

def save_file(file_path,content):
    if type(content) == dict:
        with open(file_path+'.json', 'w') as fp:
            json.dump(content, fp)
            fp.close()
    else:
        with open(file_path, "a+") as f:
            f.write(content)
            f.close()

print("Setting up transcription pipeline...")
transcriber = pipeline("automatic-speech-recognition",model="openai/whisper-large-v3",max_new_tokens=100, chunk_length_s=30)
print("transcribing...")
transcription = transcriber(audio_file_path,max_new_tokens=256,generate_kwargs={"task": "transcribe"},chunk_length_s=30,batch_size=8,return_timestamps=True)
print("saving...")
save_file(transcript_name,transcription)