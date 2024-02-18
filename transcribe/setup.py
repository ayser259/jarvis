import os

current_directory = os.getcwd()

if not os.path.exists('recordings/audio_file_path.py'):
    audio_file_path = input("What is the name of the file you want to transcribe?   ")

    audio_file_path = current_directory + '/recordings/' + audio_file_path 
    file_name = 'recordings/audio_file_path.py'

    f = open(file_name, 'a+')  # open file in append mode
    f.write("audio_file_path = ' " + audio_file_path+ "'")
    f.close()
    print('created audio_file_path')
else:
    print('setup is already complete')