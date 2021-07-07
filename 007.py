#第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。#
import os

def row_static(code_file):
    with open(code_file,encoding='utf8') as f:
        code_file=f.readlines()
        code_amount=0
        space_amount=0
        expla_amount=0
        for line in code_file:
            if line[0]=="#":        
                expla_amount+=1             #待调试
            elif line=="\n":
                space_amount+=1
            else:
                code_amount+=1
        row_static={'code_amount':code_amount,'expla_amount':expla_amount,'space_amount':space_amount} 
        return row_static

def dict_merge(dict1,dict2):
    dict3={}
    for key in dict1:
        if key in dict2:
            dict3[key]=dict1[key]+dict2[key]
        else:
            dict3[key]=dict1[key]
    for key in dict2:
        if key not in dict1:
            dict3[key]=dict2[key]
    return dict3

def total_code_sta_by_contents(code_path):
    code_amount=0
    space_amount=0
    expla_amount=0
    total_static={'code_amount':code_amount,'expla_amount':expla_amount,'space_amount':space_amount} 
    for dir_path in os.listdir(code_path):
        if os.path.splitext(dir_path)[1] == '.py':
            code_file_path=os.path.abspath(os.path.join(code_path,dir_path))
            one_file_static=row_static(code_file_path)
            total_static=dict_merge(total_static, one_file_static)
    return total_static

if __name__ == '__main__':
    code_path=r'..\python_code'
    total_static=total_code_sta_by_contents(code_path)
    # my_code_path=r'.\word_amount.py'
    # total_static=row_static(my_code_path)
    print(total_static)