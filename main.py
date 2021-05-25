from io import RawIOBase
from tempfile import tempdir
from threading import Thread
import queue
from os import name, path
import time
import function.openfile as openfile
import function.content_process as content_process
import function.request_api as request_api
import function.audio_process as audio_process


class reading_file:
    def __init__(self, file_name, file_path, section_number,number_thread):
        #Các biến số truyền vào
        self.file_name = file_name
        self.file_path = file_path
        self.section_number = section_number
        self.number_thread = number_thread
        self.threads = list()
        self.que = queue.Queue()
        self.step = 0
        #Các biến số luôn được tạo ra cùng với quá trình khởi tạo
        self.name , self.extention = openfile.parse_name(self.file_name)
        self.raw_content = openfile.open_file(self.file_name)
        self.text_content = content_process.remove_extra_space(self.raw_content)
        del self.raw_content
        self.text_content = content_process.prepair_content(self.text_content)
        self.sentence_matrix = content_process.split_by_sentence(self.text_content)
        self.matrix_content_2k = content_process.make_2k_content_matrix(self.sentence_matrix)
        del self.text_content
        #Chia mảng lưu các đoạn gồm 2k kí tự thành 1 matran 
        self.thread_data_get_url = self.thread_data_process()
        self.url_audio = self.create_url_data()
        self.saving_audio()
    def get_text_context(self):
        return self.text_content
    def thread_data_process(self):
        temp = []
        data = []
        for i in range(self.number_thread):
            step = int((len(self.matrix_content_2k)-1)/self.number_thread)
            self.step = step
            start = i*step + i
            stop = 0
            if start+ step < len(self.matrix_content_2k):
                stop = start+ step
            else:
                stop = len(self.matrix_content_2k)
            temp_content =self.matrix_content_2k[int(start):int(stop+1)]
            data.append(temp_content)
        for i in data:
            if len(i) != 0:
                temp.append(i)
        return temp
    def get_url_threads(self,data, index):
        content = data
        index = index
        url_data_matrix = []
        for i in content:
            url = request_api.request_api(str(i))['data']['url']
            url_data_matrix.append(url)
        return url_data_matrix , index
    def create_url_data(self):
        temp = [None]*len(self.matrix_content_2k)
        for index in range(self.number_thread):
            self.threads.append(Thread(target=lambda q: q.put(self.get_url_threads(data = self.thread_data_get_url[index], index=index)), args=(self.que,)))
            self.threads[index].start()
        for i in self.threads:
            i.join()
        while not self.que.empty():
            result, t_index = self.que.get()
            for j in range(len(result)):
                temp[t_index*(self.step+1)+j]= result[j]
        return temp
    def saving_audio(self):
        thread_saving_audio_list = []
        for section_index in range(self.section_number):
            thread_saving_audio_list.append(Thread(target=audio_process.concat_audio,args=(self.name,self.file_path, self.step, section_index,self.url_audio)))
            thread_saving_audio_list[section_index].start()
        for i in thread_saving_audio_list:
            thread_saving_audio_list[i].join()




#boook = reading_file('C:/Users/tienm/Desktop/text_to_speech/text.txt','file',2,2)





