import requests
import time
import os
from pydub import AudioSegment

def split_path(abs_path):
    flag = 0
    link = abs_path
    for i in range(len(link)):
        if link[i] == '/':
            flag = i
    abs_path = link[:flag+1]
    file_name = link[flag+1:]
    return abs_path, file_name

def saving_audio(url):
    x = requests.get(url)
    time.sleep(7)
    byte_data = x.content
    byte_data_len = len(byte_data)
    audio_data = x.content[44:byte_data_len]
    return audio_data

#AudioSegment.converter  = "C:\\ffmpeg\\bin"
def concat_audio(name, path,step, section_index,url_data_matrix):
    abs_path, file_name = split_path(name)
    full_path = abs_path+path
    parts = len(url_data_matrix)
    if os.path.exists(full_path) == False:
        os.makedirs(full_path)
    audio_data_array = b''
    section_file_start_index = step*section_index+ section_index
    section_file_stop_index = 0
    if section_file_start_index+1+step > parts:
        section_file_stop_index = parts
    else:
        section_file_stop_index = section_file_start_index + 1 + step
    for i in range(section_file_start_index,section_file_stop_index):
        audio_data_array = audio_data_array + saving_audio(url_data_matrix[i])
        print(str(i)+ 'done')
    section_audio = AudioSegment(audio_data_array, sample_width=2 ,frame_rate=16000, channels=1)
    section_audio.export(abs_path+path+'/'+file_name+'_section_'+str(section_index)+'.wav',format='wav')
    # writing mp3 files is a one liner

