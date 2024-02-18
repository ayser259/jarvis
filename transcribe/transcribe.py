# # import high-level pipeline 
# from transformers import pipeline

# # This line will load your desired model
# pipe = pipeline("automatic-speech-recognition", model="thennal/whisper-medium-ml")

# # to get an output, the file can be mp4, wav, or others
# # print(pipe("recordings/stecker.m4a")) # will get a transcribed output as a text

# steckler =  pipe("/Users/ayserchoudhury/playground/speech-to-text/recordings/steckler.m4a")

# # anne = pipe("/Users/ayserchoudhury/playground/speech-to-text/recordings/anne.m4a")
# # bella = pipe("/Users/ayserchoudhury/playground/speech-to-text/recordings/bella.m4a")

# print(steckler)
# print("")
# print(type(steckler))
# print(len(steckler))


# import high-level pipeline 
import setup
from transformers import pipeline
from recordings.audio_file_path import audio_file_path

# This line will load your desired model
# pipe = pipeline("automatic-speech-recognition", model="thennal/whisper-medium-ml")
# print(pipe(audio_file_path,max_new_tokens=100, chunk_length_s=10)) # will get a transcribed output as a text
