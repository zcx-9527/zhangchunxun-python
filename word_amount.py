#004任一个英文的纯文本文件，统计其中的单词出现的个数#
import collections
import re

file=open(r'D:\ProgramData\python_code\test.txt','r')
words_file=file.read()
print("文本内容为：", words_file)
only_words_str = re.sub(r"[^a-zA-Z]+", " ",words_file)
print("过滤后的字符串：",only_words_str)
only_words_str=only_words_str.split()   #以空格为化分
print(collections.Counter(only_words_str))

file.close()




