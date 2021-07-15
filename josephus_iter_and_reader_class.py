
#约瑟夫环作为容器，迭代法实现for循环，reader作为父类，不同类型的文件作为子类，实现策略与机制的分离#

import os
import xlrd
import csv
import zipfile

class Student(object):
    
    def __init__(self,name,gender,school_id):         
        self.name = name
        self.gender = gender
        self.school_id = school_id
    
    def show_student(self):                             
        print("姓名：%s,性别：%s，学号：%s" %(self.name,self.gender,self.school_number))


class Reader(object):
    def __init__(self,path):
        self.path = path
    
    def read(self):
        pass

# txt读取子类 # 
class TxtReader(Reader):
    def read(self):
        student_list = []
        file = open(self.path,'r',encoding='UTF-8')     
        data_in_oneline = file.readline()

        while data_in_oneline:
            divided_data = data_in_oneline.split()            #以空格为分割方式对行内容进行分割
            new_student = Student(divided_data[0],divided_data[1],divided_data[2])
            student_list.append(new_student)
            data_in_oneline = file.readline()
        return student_list

# excel读取子类#
class ExcelReader(Reader):
    def read(self):
        student_list = []
        file = xlrd.open_workbook(self.path)
        sheets = file.sheets()[0]           #通过索引顺序获取,返回一个xlrd.sheet.Sheet()对象
        number_of_rows = sheets.nrows    

        for line in range(number_of_rows):
            data_in_oneline = sheets.row_values(line)   #返回由该行中所有单元格的数据组成的列表
            new_student = Student(data_in_oneline[0],data_in_oneline[1],int(data_in_oneline[2]))
            student_list.append(new_student)
        return student_list

# csv读取子类 # 
class CsvReader(Reader):
    def read(self):
        student_list = []
        file = open(self.path,'r',encoding='UTF-8')
        lines = csv.reader(file)
        for line in lines:
            new_student = Student(line[0],line[1],int(line[2]))
            student_list.append(new_student)
        return student_list

# zip文件读取子类 #
class ZipReader(Reader):
    def read(self):
        student_list = []
        allfile = zipfile.ZipFile(self.path) 
        filename_list = allfile.namelist()            #获得压缩文件内的所有文件命,并返回一个list

        for filename in filename_list:
            file = allfile.open(filename,'r')
            #file_contents = file_contents.decode("UTF-8")
            data_in_oneline = file.readline()

            while data_in_oneline:
                decoded_data = data_in_oneline.decode("UTF-8")        #返回str类型的数据
                divided_data = decoded_data.split()           #以空隔为分割依据，返回list类型
                new_student = Student(divided_data[0],divided_data[1],divided_data[2])
                student_list.append(new_student)
        return student_list


# 将约瑟夫环作为容器，通过迭代法实现for循环 #
class JosephusCircle(object):
    def __init__(self,list,step,start_point):
        assert(len(list) >= 0  and start_point != 0 and step >= 0)
        self._list = list
        self._step = step-1
        self._selected_order = []

        if start_point >0:
            self._start_point = start_point-1
        else:
            self._start_point = start_point


# 以迭代的方式实现for循环 #
#指向对象的指针   双向迭代器
#返回约瑟夫迭代器，在迭代器里进行next
#此处仍需改进
    def __iter__(self):     
        return self           

    def __next__(self):     
        # if len(self._list) == 0:
        #     return []

        # if self._step == -1:
        #     return self._selected_order

        if len(self._list) > 0:
            selected_pos = (self._start_point + self._step) % len(self._list)
            self._selected_order.append(self._list[selected_pos])
            self._list.pop(selected_pos)
            self._start_point = selected_pos
            return self._selected_order[-1]

        else:
	        raise StopIteration                    #异常处理


if __name__ == '__main__':
    path = r'..\test_for_Josephus_Circle\test_for_jc.xls'
    file = ExcelReader(path)
    student_list = file.read()
    step,start_point = 1,-1

    josephus_circle = JosephusCircle(student_list,step,start_point)
    print("被选中的学号顺序依次为：")
    for student in josephus_circle:    #iter(josephus_circle)
        print(student.school_id)