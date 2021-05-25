from http.client import FAILED_DEPENDENCY
from typing import Text
import PyPDF2
import pikepdf
from tika import parser
from tika.tika import EncodeUtf8
'''nơi đây chỉ dành cho việc đọc file'''

# Cái chốn này để đọc file text
def read_text_file(file_name):
    file = open(file_name,"r",encoding="utf-8")
    contain = file.read()
    file.close()
    return contain


'''Cái chốn này đọc file pdf'''
def parse_name(file_name):
    name = ""
    name_extendsion = ""
    dot_index = 0;
    for i in range(len(file_name)):
        if(file_name[i]=="."):
            dot_index = i;
    for i in range(dot_index):
        name = name + file_name[i]
    for i in range(dot_index+1,len(file_name)):
        name_extendsion = name_extendsion + file_name[i]
    return name, name_extendsion

#Đọc file pdf
def decrypt_pdf_file(file_name):
    pdf = pikepdf.open(file_name)
    parsed_name = parse_name(file_name)
    decrypted_file_name = "decrypted "+parsed_name[0]+"."+parsed_name[1]
    pdf.save(decrypted_file_name)
    pdf.close()

def reading_pdf_file(file_name):
    file = open(file_name,"rb")
    contain = PyPDF2.PdfFileReader(file)
    is_encrypted = contain.isEncrypted
    if(is_encrypted == True):
        file.close()
        parsed_name = parse_name(file_name)
        decrypt_pdf_file(file_name)
        decrypted_file_name = "decrypted "+parsed_name[0]+"."+parsed_name[1]
        return process_pdf_file(decrypted_file_name)
    else:
        return process_pdf_file(file_name)


def process_pdf_file(file_name):
    f = parser.from_file(file_name)
    contain_data = f['content']
    return contain_data

def open_file(file_name):
    name = parse_name(file_name)[0]
    name_extendsion = parse_name(file_name)[1]
    if(name_extendsion == "txt"):
        return read_text_file(file_name)
    if(name_extendsion == "pdf"):
        return reading_pdf_file(file_name)
        

