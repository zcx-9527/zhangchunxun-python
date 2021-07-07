#第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。#

import os
import collections
from ntpath import join
import re

def words_sta(words_file):
    only_words_str = re.sub(r"[^a-zA-Z]+", " ",words_file)   #用空格代替特殊字符
    #print("过滤后的字符串：",only_words_str)
    only_words_str=only_words_str.split()   #以空格化分
    #print("str：",only_words_str)
    after_sta=collections.Counter(only_words_str)
    #print("部分统计结果为：",after_amount)
    return after_sta

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


def words_sta_by_line(file):
    words_line=file.readline()
    line_sta={}
    total_words_sta={}
    while words_line:
        line_sta=words_sta(words_line)
        total_words_sta=dict_merge(total_words_sta,line_sta)
        words_line=file.readline()
    return total_words_sta

if __name__ == '__main__':
    for dir_path in os.listdir(r"..\test_txt"):
        if os.path.splitext(dir_path)[1] == '.txt':
            file=open(os.path.abspath(os.path.join(r"..\test_txt",dir_path)))
            total_words_sta = words_sta_by_line(file)
            #print(type(total_words_sta))
            the_most_improtant_word=collections.Counter(total_words_sta).most_common(1)
            print("the most important word in day%s："%dir_path,the_most_improtant_word)