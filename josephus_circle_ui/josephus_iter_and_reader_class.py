
#约瑟夫环作为容器，迭代法实现for循环，reader作为父类，不同类型的文件作为子类，实现策略与机制的分离#
#一组界面，图形界面(前台)，控制台界面(后台)。后台约瑟夫一套，控制台界面的多种，同一套代码#
#1从选择的文件中选择人员信息，组成人员信息，2在界面中显示弹出顺序，3编辑读取的信息，4可以存取信息# 使用QT或者tpk

import os
import xlrd
import csv
import zipfile
ZIP_FILE_SAVE_PATH = '..\decoded_file'
#from Ui_josephus_circle_ui import Ui_MainWindow

class Student(object):
    
    def __init__(self,name,gender,school_id):         
        self.name = name
        self.gender = gender
        self.school_id = school_id
    
    def __str__(self):
        student_msg = "姓名：" + self.name +"  "+ "性别：" + self.gender +"  "+ "学号：" + self.school_id                       
        return student_msg
    
    def get_msg(self):
        msg =  self.name +"  "+ self.gender +"  " + str(self.school_id)
        return msg


#父类#
class Reader(object):
    def __init__(self,path):
        self._path = path
    
    def read(self):
        pass

# txt读取子类 #               ##文件关闭(报错的时候file.close()并没有真正关掉)
class TxtReader(Reader):      #使用 with...open() 创建到消亡为生存周期
    def read(self):
        student_list = []
        with open(self._path,'r',encoding='UTF-8') as file: 
 
            for line in file:
                divided_data = line.split()                 #以空格为分割方式对行内容进行分割
                new_student = Student(divided_data[0],divided_data[1],divided_data[2])
                student_list.append(new_student)
            return student_list


# excel读取子类#
class ExcelReader(Reader):
    def read(self):
        student_list = []
        file = xlrd.open_workbook(self._path)
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
        with open (self._path,'r',encoding='UTF-8') as file:
            lines = csv.reader(file)
            for line in lines:
                new_student = Student(line[0],line[1],int(line[2]))
                student_list.append(new_student)
            return student_list

# zip文件读取子类 #            #读取多个文件 返回有问题#
class ZipReader(Reader):
    def read(self):
        #student_list = []
        with zipfile.ZipFile(self._path,'r') as allfile: 
            filename_list = allfile.namelist()            #获得压缩文件内的所有文件命,并返回一个list

            for filename in filename_list:
                file_suffix = filename.split('.', 2)[1]
                allfile.extract(filename, ZIP_FILE_SAVE_PATH )
                file_path_in_save_path = os.path.join(ZIP_FILE_SAVE_PATH, filename) 
                file_maps = {'txt' : TxtReader, 'xls' : ExcelReader, 'csv': CsvReader}
                class_instance = file_maps[file_suffix]
                obj = class_instance(file_path_in_save_path )
                student_list=obj.read()
            return student_list

# 将约瑟夫环作为容器，通过迭代法实现for循环 #
class JosephusCircle(object):
    def __init__(self,list,step,start_point):
        assert(len(list) >= 0  and start_point != 0 and step >= 0)
        self._list = list
        self._step=step-1
        self._count = len(list)
        self._selected_order = []
    
        if start_point >0:
            self._start_point = start_point-1
        else:
            self._start_point = start_point
# 以迭代的方式实现for循环 #
#指向对象的指针   双向迭代器
#返回约瑟夫迭代器，在迭代器里进行next
    def __iter__(self):     
        return self           

    def __next__(self):     
        if self._count > 0 :         #以循环次数作为判断依据#
            if len(self._list) == 0:            #处理list为空时特殊情况
                self._count-=0
                return []
        
            elif self._step == -1:      #处理step为0时特殊情况
                self._count =0
                return []
            
            else:                      #step and start_point >0:
                selected_pos = (self._start_point + self._step) % len(self._list)
                self._selected_order.append(self._list[selected_pos])
                self._list.pop(selected_pos)
                self._start_point = selected_pos
                self._count-=1
                return self._selected_order[-1]    

        else:
	        raise StopIteration                    #异常处理


if __name__ == '__main__':
    path = r'..\test_for_Josephus_Circle\test_for_jc.zip'
    file = ZipReader(path)
    student_list = file.read()
    step,start_point = 3,1

    josephus_circle = JosephusCircle(student_list,step,start_point)
    print("被选中的学号顺序依次为：")
    for student in josephus_circle:    #iter(josephus_circle)
        print(student.name)