#约瑟夫环作为容器实现for循环，将txt\xls\csv\zip写成类，读取不同类型文件#

import os
import xlrd
import csv
import zipfile

class Student(object):
    
    def __init__(self,name,gender,school_number):
        self.name = name
        self.gender = gender
        self.school_number = school_number
    
    def show_student(self):
        print("姓名：%s,性别：%s，学号：%s" %(self.name,self.gender,self.school_number))


class File_Read(object):
    def __init__(self,path):
        self.path = path
        self.format = os.path.splitext(path)[1]             #获得文件类型

    def get_student_list(self):
        student_list = []
# txt文件读取 #
        if self.format == ".txt":
            file_txt = open(self.path,'r',encoding='UTF-8')
            file_by_lines = file_txt.readlines()
            for line in file_by_lines:
                line_list = line.split()                    #以空格为分割方式对行内容进行分割
                new_student = Student(line_list[0],line_list[1],line_list[2])
                student_list.append(new_student)
            return student_list

# excel文件读取 #
        elif self.format == ".xls":
            file_xls = xlrd.open_workbook(self.path)
            #print(type(file_xls))
            file_by_sheet = file_xls.sheets()[0]           #通过索引顺序获取,返回一个xlrd.sheet.Sheet()对象
            print(file_by_sheet)
            nrows = file_by_sheet.nrows                    #nrows=number of rows,获取该sheet中的有效行数
            for line in range(nrows):
                line_list = file_by_sheet.row_values(line)   #返回由该行中所有单元格的数据组成的列表
                #print(line_list)
                new_student = Student(line_list[0],line_list[1],int(line_list[2]))
                student_list.append(new_student)
            return student_list

# csv文件读取 #
        elif self.format == ".csv":
            file_csv = open(self.path,'r',encoding='UTF-8')
            file_by_lines = csv.reader(file_csv)
            for line in file_by_lines:
                new_student = Student(line[0],line[1],int(line[2]))
                student_list.append(new_student)
            return student_list

# zip文件读取 #
        elif self.format == ".zip":
            file_zip = zipfile.ZipFile(self.path) 
            file_list = file_zip.namelist()            #获得压缩文件内的所有文件命,并返回一个list
            for file_name in file_list:
                file_zip = file_zip.open(file_name,'r')
                #file_contents = file_contents.decode("UTF-8")
                file_by_lines = file_zip.readlines()
                for line in file_by_lines:
                    line_utf8 = line.decode("UTF-8")        #返回str类型的数据
                    line_list = line_utf8.split()           #以空隔为分割依据，返回list类型
                    new_student = Student(line_list[0],line_list[1],line_list[2])
                    student_list.append(new_student)
            return student_list
# 异常处理 #            
        else: 
	        raise StopIteration  

# 将约瑟夫环作为容器，通过迭代法实现for循环 #
class Josephus_Circle(list):
    def __init__(self,input_list,step,start_point):
        assert(len(input_list)>0 and step>0)
        self.list = input_list[start_point-1:] + input_list[:start_point-1]       
        self.step = step
        self.step_in_list = self.step-1
        self.start_point = start_point
        self.order_of_select = []

# 以迭代的方式实现for循环 #
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.list)>0:
# 当step<列表长度,直接切片 #
            if self.step < len(self.list):
                self.order_of_select.append(self.list[self.step_in_list])
                self.list = self.list[self.step_in_list+1:] + self.list[:self.step_in_list]
                return self.order_of_select[-1]
#当step=列表长度，去掉列表的最后一位
            if self.step == len(self.list):
                self.order_of_select.append(self.list[-1])
                self.list.pop(-1)
                return self.order_of_select[-1]
#当step>列表长度时
            if self.step > len(self.list):
                if len(self.list) == 1:
                    self.order_of_select.append(self.list[0])
                    self.list.pop(-1)
                    return self.order_of_select[-1]
#取余数，使得m<n
                remainder = self.step % len(self.list)
                self.order_of_select.append(self.list[remainder-1])
                self.list = self.list[remainder:] + self.list[:remainder-1]
                return self.order_of_select[-1]

        else: 
	        raise StopIteration                     #异常处理


if __name__ == '__main__':
    path = r'..\test_for_Josephus_Circle\test_for_jc.zip'
    file = File_Read(path)
    student_list = file.get_student_list()
    step,start_point = 3,1

    josephus_circle = Josephus_Circle(student_list,step,start_point)
    print("被选中的学号顺序依次为：")
    for student in josephus_circle:
        print(student.school_number)