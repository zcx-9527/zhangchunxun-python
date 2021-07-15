#unittest#

import unittest
from josephus_iter_and_reader_class import JosephusCircle,Student,TxtReader,ExcelReader,ZipReader,CsvReader

def generate_student_list():                 
    student_1=Student("张三","男","2020221")
    student_2=Student("李四","男","2020222")
    student_3=Student("王五","男","2020223")
    student_4=Student("陈六","男","2020224")
    student_5=Student("李华","男","2020225")
    student_6=Student("芳华","女","2020226")
    student_list=[]
    student_list.append(student_1)
    student_list.append(student_2)
    student_list.append(student_3)
    student_list.append(student_4)
    student_list.append(student_5)
    student_list.append(student_6)
    return student_list

class JosephusAndReaderTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [1,2,3,4,5,6]
        print('call setUp')

#测试步进与起始点都为正时#
    def test_step_and_startpoint_is_positive(self):
        step,start_point = 3,1
        josephus_circle = JosephusCircle(self.test_list,step,start_point)
        right_selected_order=[3,6,4,2,5,1]
        selected_order=[]

        for selected_one in josephus_circle:
            selected_order.append(selected_one)
        self.assertEqual(selected_order,right_selected_order)

#测试起始点为负时#
    def test_start_point_is_negtive(self):
        step,start_point = 1,-1
        josephus_circle = JosephusCircle(self.test_list,step,start_point)
        right_selected_order=[6,1,2,3,4,5,]
        selected_order=[]

        for selected_one in josephus_circle:
            selected_order.append(selected_one)
        self.assertEqual(selected_order,right_selected_order)

#测试步进值为0时#
    def test_step_is_zero(self):
        step,start_point = 0,1
        josephus_circle = JosephusCircle(self.test_list,step,start_point)
        right_selected_order=[]
        selected_order=[]

        for selected_one in josephus_circle:
            selected_order.append(selected_one)
        self.assertEqual(selected_order,right_selected_order)

 #测试输入数据为空时#   
    def test_input_list_is_none(self):
        test_list=[]
        step,start_point=3,1
        josephus_circle = JosephusCircle(test_list,step,start_point)
        right_selected_order=[]
        selected_order=[]

        for selected_one in josephus_circle:
            selected_order.append(selected_one)
        self.assertEqual(selected_order,right_selected_order)

#测试txt文件读取情况#
    def test_TxtReader(self):
        test_student_list=generate_student_list()
        path = r'..\test_for_Josephus_Circle\test_for_jc.txt'
        file = TxtReader(path)
        student_list = file.read()
        self.assertEqual(test_student_list,student_list)

#测试excel文件读取情况#
    def test_ExcelReader(self):
        test_student_list=generate_student_list()
        path = r'..\test_for_Josephus_Circle\test_for_jc.xls'
        file = ExcelReader(path)
        student_list = file.read()
        self.assertEqual(test_student_list,student_list)

#测试csv文件读取情况#
    def test_CsvReader(self):
        test_student_list=generate_student_list()
        path = r'..\test_for_Josephus_Circle\test_for_jc.csv'
        file = CsvReader(path)
        student_list = file.read()
        self.assertEqual(test_student_list,student_list)

#测试zip文件读取情况#
    def test_CsvReader(self):
        test_student_list=generate_student_list()
        path = r'..\test_for_Josephus_Circle\test_for_jc.zip'
        file = ZipReader(path)
        student_list = file.read()
        self.assertEqual(test_student_list,student_list)

    def tearDown(self):
        print('call setUp')

if __name__ == '__main__':
    unittest.main()