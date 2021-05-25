
from sys import maxsize, path

import tkinter
from tkinter import LabelFrame, filedialog
from tkinter.constants import CENTER, DISABLED, END, YES
from typing import Text

import pickle

file_congi = open('../config/config.dat','rb+')

#line 1 save API key
#line 2 save Reviewer number characters
#line 3 save back grond
a = str(['haha con chó đạt', 'datcho'])
a = bytes(a, encoding='utf-8')
file_congi.write(a)
list = ['haha','hiuhi']
class menu():
    list_API = []
    number_preview = 50
    background_path = 'C:\\Users\\tienm\\Desktop\\text_to_speech\\image\\bg.png'
    def add_API_key(self, key):
        if len(self.list_API) ==  0:
            add_API_key_GUI = tkinter.Tk()
            add_API_key_GUI.geometry('600x300')
            add_API_key_GUI.resizable(width=0,height=0)
            list_API_key_lable =LabelFrame(add_API_key_GUI,text='Your API key',width=580, height=200)
            list_API_key_lable.place(x=10,y=0)
            table = Table(add_API_key_GUI,40,2,2)
            add_API_key_GUI.mainloop()


class Table:
      
    def __init__(self,root,rows, cols,data):
          
        # code for creating table
        self.e = tkinter.Entry(root,width=20)
        self.e.place(x =50,y =30)
        self.e.insert(END,'Email')
        self.e = tkinter.Entry(root,width=65)
        self.e.place(x =150,y =30)
        self.e.insert(END,'API key')
        for i in range(0,cols):
            for j in range(1,rows):
                col_with = 0
                if i%2 ==0:
                    col_with = 20
                else:
                    col_with = 65
                self.e = tkinter.Entry(root, width=col_with)
                  
                self.e.place(x=i*100 +50, y=j*20+ 30)
                self.e.insert(END, 'haha'+str(i)+str(j))




gaga = menu()
gaga.add_API_key('jaja')
