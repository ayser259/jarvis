import os
from helpers import save_file

current_directory = os.getcwd()

if not os.path.exists('recordings/audio_file_path.py'):

    print("required files are not available...")
    print("setting up now...")

    audio_file_path = input("What is the name of the file you want to transcribe?   ")

    audio_file_path = current_directory + '/recordings/' + audio_file_path 
    file_name = 'recordings/audio_file_path.py'

    save_file(file_name,"audio_file_path = '" + audio_file_path + "'")
    print('created audio_file_path')

    print("Copy over any recordings you want to transcribe into the 'Recordings' folder and then update the name of the file you want to transcribe in the audio file path folder.")
    print("Example:")
    print(audio_file_path)
else:
    from recordings.audio_file_path import audio_file_path
    print("transcribing file: ")
    print(audio_file_path)
