# 第 0004 题任一个英文的纯文本文件，统计其中的单词出现的个数#
import collections
from ntpath import join
import re

def words_sta(words_file):
    only_words_str = re.sub(r"[^a-zA-Z]+", " ",words_file)   #用空格代替特殊字符
    #print("过滤后的字符串：",only_words_str)
    only_words_str=only_words_str.split()   #以空格化分
    print("str：",only_words_str)
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
    file=open(r'.\test.txt','r')
    total_words_sta = words_sta_by_line(file)
    total_words_sta = sorted(total_words_sta.items(),  key = lambda item:item[1] )
    total_words_sta.reverse()
    print("总的统计结果为：",total_words_sta)
    file.close()