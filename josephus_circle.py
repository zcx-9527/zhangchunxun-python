
def josephus_circle_by_slice(list,step,start_point):
    assert(len(list)>0 and step>0)
    #list = [x for x in range(1,total_number+1)]
    list = list[start_point-1:] + list[:start_point-1]
    step_in_list= step-1
    order_of_select=[]
#如果n或m等于1.直接返回列表的最后一位
    if len(list) == 1 or step == 1:
        order_of_select=list
        return order_of_select
    
    while len(list):
#当key<列表长度,直接切片
        if step < len(list):
            order_of_select.append(list[step_in_list])
            list = list[step_in_list+1:] + list[:step_in_list]
#当key=列表长度，去掉列表的最后一位
        if step == len(list):
            order_of_select.append(list[-1])
            list.pop(-1)

        if step > len(list):
            if len(list) == 1:
                order_of_select.append(list[0])
                break
#当 key>列表长度时，先取余数，使得m<n
            remainder = step % len(list)
            order_of_select.append(list[remainder-1])
            list = list[remainder:] + list[:remainder-1]
    return order_of_select


class Student(object):
    
    def __init__(self,name,gender,school_number):
        self.name = name
        self.gender = gender
        self.school_number = school_number
    
    def show_student(self):
        print("姓名：%s,性别：%s，学号：%s" %(self.name,self.gender,self.school_number))

def generate_student_list():                  #此处待改进
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

# class josephus_circle(list):
#     def __init__(self,step,start_point):
#         self.step=step
#         self.start_point=start_point
    
if __name__ == '__main__':

    student_list=generate_student_list()

    step,start_point=3,1
    order_of_select=josephus_circle_by_slice(student_list,step,start_point)
    #print("选中的顺序为：",order_of_select)
    print("选中的学号顺序依次为：")
    for student in order_of_select:
        print(student.school_number)