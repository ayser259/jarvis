
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

def transcribe(audio_file_path):
    from transformers import pipeline
    print("Setting up transcription pipeline...")
    transcribe = pipeline("automatic-speech-recognition",model="openai/whisper-large-v3",max_new_tokens=100, chunk_length_s=30)
    print("transcribing...")
    transcription = pipe(audio_file_path,max_new_tokens=256,generate_kwargs={"task": "transcribe"},chunk_length_s=30,batch_size=8,return_timestamps=True)
    return transcription

def extract(sr, data):
    processed_data = np.array(data).astype(np.float32) / 32767.0
    transcription_res = pipe({"sampling_rate": sr, "raw": processed_data})["text"]
    return transcription_res

def diarization(audio_file_path):
    from pyannote.audio import Pipeline
    from keys import pyannote_key
    
    print("initializing diarization pipeline...")
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=pyannote_key)
    print("diarizing audio..")
    diarization = pipeline(audio_file_path)

    starts = []
    ends = []
    speakers = []

    for segment, _, speaker in diarization.itertracks(yield_label=True):
        starts.append(segment.start)
        ends.append(segment.end)
        speakers.append(speaker)

    return starts, ends, speakers

starts, ends, speakers = diarization(audio_file_path)

print("building diarized transcript...")

diarized_transcription = ""

for start_time, end_time, speaker_id in zip(starts, ends, speakers):
        segment = data[int(start_time * sr) : int(end_time * sr)]
        diarized_transcription += f"{speaker_id} {round(start_time, 2)}:{round(end_time, 2)} \t {extract(sr, segment)}\n"

print("saving...")
save_file(transcript_name,diarized_transcription)
print("done")

'''
First get diarize the audio
Then transcribe the audio
Then generate the diarized transcript
Then return the diarized transcript
'''












# Helpful for debugging
# https://stackoverflow.com/questions/76846657/how-to-use-model-from-huggingface-to-make-an-app-which-can-transcribe-a-local