from sys import prefix
import tkinter
from tkinter import Canvas, Label, Menu, PhotoImage, Radiobutton, Variable, filedialog
from tkinter import font
from tkinter.constants import ANCHOR
from PIL import Image, ImageTk
from typing import Text

from typing_extensions import IntVar
import function.config
import time
from threading import Thread

import function.openfile as openfile
import function.content_process as content_process

import main as main

class Main_window(tkinter.Tk):
    filename = ''
    file_path = 'file'
    section_number = 1
    number_thread = 1 # Cái này = running speed
    tone_value = 1
    def __init__(self):
        super(Main_window, self).__init__()
        #chỗ này để cấu hình cửa sổ tkinter
        self.title('Read your book')
        self.geometry('1280x720')
        self.photo = PhotoImage(file='./image/bg.png')
        self.radio_icon = PhotoImage(file='./image/kurama.gif',format="gif -index 0")
        self.resizable(width=0, height=0)
        self.gif_coordinate = [180,420]
        self.tone = tkinter.IntVar()
        self.menu = tkinter.Menu(self)
        self.config(menu=self.menu)
        #chỗ này lưu biến cần dùng cho việc chạy mã nguồn main
        
        #chỗ này để lưu biến tự tạo cho việc khởi tạo giao diện
        self.is_close = False
        self.canvas()
        self.text()
        self.radiobutton()
        self.entry()
        self.button()
        self.gif_icon()
        self.menu_bar()
    
    def canvas(self):
        gif_path ='image/kurama.gif'
        self.canvas_bg = Canvas(self,width=1280,height=720)
        self.canvas_bg.place(x=0,y=0)
        self.canvas_bg.create_image(640,360, image=self.photo)
        self.canvas_bg.create_text(640,50, text='T2S', font=('Ninja Naruto',50),fill='#fff')
        self.canvas_bg.create_text(120,120,text='Choise your file', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(120,180,text='Section number', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(120,240,text='Running speed', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(120,300,text='Reading speed', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(120,360,text='Tone', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(270,420,text='South women', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(520,420,text='Northern women', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(270,480,text='Northern men', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(520,480,text='South men', font=('Ninja Naruto',13), fill='#fff')
        self.canvas_bg.create_text(680,120,text='Preview',font=('Ninja Naruto',13), fill='#fff')
    def menu_bar(self):
        #chỗ này cho việc cài đặt
        setting_menu = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Setting', menu=setting_menu)
        # chỗ này để cho việc cài đặt API
        API_menu = tkinter.Menu(setting_menu, tearoff=0)
        setting_menu.add_cascade(label='API setting',menu=API_menu)
        API_menu.add_command(label='Add key',command=print('haha'))
        API_menu.add_command(label='Change key', command=print('dat cho'))
        API_menu.add_command(label='Delete key', command=print('haha dat cho'))
        # chỗ này để thay đổi số kí tự xem trước
        setting_menu.add_command(label='Reviewer number characters',command=print('cjp'))
        # chỗ này cho phép thay đổi hình nền
        setting_menu.add_command(label='Change background',command=print('chó'))
        #chỗ này cách ra nhìn cho nó đẹp
        setting_menu.add_separator()
        # chỗ này dùng để đóng chương trình
        setting_menu.add_command(label='Exit', command=print('chó'))

        #chỗ này cho việc cài đặt server
        server_menu = tkinter.Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='Server', menu=server_menu)
        server_menu.add_command(label='Server info',command=print('kaka'))
        server_menu.add_command(label='Change server',command='hhaha')


        #chỗ này cho việc giúp đỡ người dùng
        help_menu = tkinter.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='Version info', command=print('haha chpos'))
        help_menu.add_command(label='Tutorial', command='haha chó')
        help_menu.add_command(label='Contact',command=print('haha chó'))
    def text(self):
        self.textbox = tkinter.Text(self,width=60,height = 17,font=(13))
        self.textbox.place(x=642,y=150)
    def entry(self):
        self.file_path_entry = tkinter.Entry(self ,font=('Ninja Naruto',13),justify='left', width=17, textvariable = self.filename)
        self.file_path_entry.place(x=250,y=105,height=30)
        self.section_number_entry = tkinter.Entry(self ,font=('Ninja Naruto',13),justify='left', width=5)
        self.section_number_entry.place(x=250,y=165,height=30)
        self.running_speed_entry = tkinter.Entry(self ,font=('Ninja Naruto',13),justify='left', width=5)
        self.running_speed_entry.place(x=250,y=225,height=30)
        self.reading_speed_entry = tkinter.Entry(self ,font=('Ninja Naruto',13),justify='left', width=5)
        self.reading_speed_entry.place(x=250,y=285,height=30)
        
    def button(self):
        self.file_path_button = tkinter.Button(self,font=('Ninja Naruto',13), text='Browse', command=self.file_dialog).place(x=500,y=105)
        self.conver_button = tkinter.Button(self, text='Convert',font=('Ninja Naruto',13), command=self.main).place(x=1100,y=500)
    def radiobutton(self):
        self.south_woman = tkinter.Radiobutton(self,variable=self.tone,value=1,tristatevalue=0,command=self.forget_radio_selected)
        self.northern_women = tkinter.Radiobutton(self,variable=self.tone,value=2,tristatevalue=0,command=self.forget_radio_selected)
        self.northern_women.place(x=400, y = 410)
        self.south_men = tkinter.Radiobutton(self,variable=self.tone,value=3,tristatevalue=0,command=self.forget_radio_selected)
        self.south_men.place(x=160,y=470)
        self.northern_men = tkinter.Radiobutton(self,variable=self.tone,value=4,tristatevalue=0,command=self.forget_radio_selected)
        self.northern_men.place(x= 400, y =470)
    def file_dialog(self):
        self.filename =filedialog.askopenfilename(initialdir =  "C:\\Users\\tienm\\Desktop", title = "Select A File", filetype =(("document","*.*"),("all files","*.*")))
        self.file_path_entry.insert(0,self.filename)
        self.review_content()
        #print(self.text_content)
        self.textbox.delete("1.0","end")
        self.textbox.insert('insert',self.review_content())
    def on_closing(self):
        self.is_close = True
        print(self.is_close)
        self.destroy()


    def gif_icon(self):
        self.radio_icon_canvas = self.canvas_bg.create_image(self.gif_coordinate[0],self.gif_coordinate[1],image=self.radio_icon)
        def gif_radio_icon(self):
            gif_path ='image/kurama.gif'
            gif_info = Image.open(gif_path)
            gif_frames = gif_info.n_frames
            frames_list = []
            frames_index = 0
            for i in range(gif_frames):
                frames_list.append(PhotoImage(file = gif_path,format=f"gif -index {i}"))
            def load_gif(frame_index,self):
                load_frame = frames_list[frame_index]
                self.canvas_bg.itemconfig(self.radio_icon_canvas,image=load_frame)
                frame_index +=1
                if frame_index == gif_frames:
                    frame_index = 0
                self.after(200,lambda:load_gif(frame_index,self))

            load_gif(frames_index,self)
        gif_radio_icon(self)
    def forget_radio_selected(self):
        self.radido_button_selected_value = self.tone.get()
        if self.radido_button_selected_value == 1:
            self.canvas_bg.delete(self.radio_icon_canvas)
            self.south_woman.place_forget()
            self.northern_women.place(x=400, y = 410)
            self.south_men.place(x=160,y=470)
            self.northern_men.place(x= 400, y =470)
            self.gif_coordinate[0] = 180
            self.gif_coordinate[1] = 420
            self.gif_icon()
            self.tone_value = 1
        if self.radido_button_selected_value == 2:
            self.canvas_bg.delete(self.radio_icon_canvas)
            self.south_woman.place(x = 160, y = 410)
            self.northern_women.place_forget()
            self.south_men.place(x=160,y=470)
            self.northern_men.place(x= 400, y =470)
            self.gif_coordinate[0] = 420
            self.gif_coordinate[1] = 420
            self.gif_icon()
            self.tone_value = 2
        if self.radido_button_selected_value == 3:
            self.canvas_bg.delete(self.radio_icon_canvas)
            self.south_woman.place(x = 160, y = 410)
            self.northern_women.place(x=400, y = 410)
            self.south_men.place_forget()
            self.northern_men.place(x= 400, y =470)
            self.gif_coordinate[0] = 180
            self.gif_coordinate[1] = 480
            self.gif_icon()
            self.tone_value = 3       
        if self.radido_button_selected_value == 4:
            self.canvas_bg.delete(self.radio_icon_canvas)
            self.south_woman.place(x = 160, y = 410)
            self.northern_women.place(x=400, y = 410)
            self.south_men.place(x = 160, y = 470)
            self.northern_men.place_forget()
            self.gif_coordinate[0] = 420
            self.gif_coordinate[1] = 480
            self.gif_icon()
            self.tone_value = 4
    
    
    #chỗ này để viết các hàm và gọi nó
    def review_content(self):
        raw_content = openfile.open_file(self.filename)
        self.text_content = content_process.remove_extra_space(raw_content)
        del raw_content
        #text_content = content_process.prepair_content(text_content)
        return self.text_content[0:50]
    def main(self):
        self.section_number = int(self.section_number_entry.get())
        self.number_thread = int(self.running_speed_entry.get())
        main.reading_file(self.filename,self.file_path,self.section_number,self.number_thread)


main_window = Main_window()
main_window.mainloop()