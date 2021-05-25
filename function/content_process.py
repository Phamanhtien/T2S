import re
from tempfile import tempdir

# Cái thứ này để bỏ khoảng trắng thừa
def remove_extra_space(content):
    sentence = " ".join(re.split("\s+", content, flags=re.UNICODE))
    return (sentence)



# Cái thứ này để xóa mất cái thừa mà không phải khoảng trắng
def prepair_content(content):
    content = content +"\n\n"
    lines = []
    temp = ""
    index = 0
    content = list(content)
    while index < len(content)-1:
        if content[index] == "\n" and content[index+1] !="\n":
            content.pop(index)
        index = index + 1
    for i in content:
        temp = temp + i
    content = temp;
    temp = ""
    for i in range(len(content)-1):
        if (content[i]=="\n" and content[i+1]=="\n"):
            lines.append(temp)
            temp = ""
        else:
            temp = temp+content[i]
    temp = ''
    for i in lines:
        if(i == " " or i == "  " or i =="   " or i=="    "):
            temp = temp
        else:
            if(len(i)!=0 and i[len(i)-1]!="."):
                temp = temp + i
            else:
                temp = temp + i
    return temp



# Cái thứ này để tách text thành các câu
def split_by_sentence(content):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
    return sentences



def make_2k_content_matrix(content):
    temp_matric = []
    temp_string = ''
    for i in content:
        if len(temp_string)+ len(i)< 2000:
            temp_string = temp_string +' '+ i
        else:
            temp_matric.append(temp_string)
            temp_string = ''
    if temp_string != '' or temp_string != '  ' or temp_string != '   ' or temp_string != '    ':
        temp_matric.append(temp_string)
    return temp_matric

