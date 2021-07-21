# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ProgramData\python_code\josephus_circle_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import  QFileDialog 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from josephus_iter_and_reader_class import TxtReader,ExcelReader,ZipReader,CsvReader,JosephusCircle,Student
import time
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.data_textedit = QtWidgets.QTextEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_textedit.sizePolicy().hasHeightForWidth())

        #设置文件内容显示编辑区#
        self.data_textedit.setSizePolicy(sizePolicy)
        self.data_textedit.setMinimumSize(QtCore.QSize(250, 170))
        self.data_textedit.setMaximumSize(QtCore.QSize(250, 170))
        self.data_textedit.setObjectName("datas_textEdit")
        self.gridLayout.addWidget(self.data_textedit, 0, 3, 2, 1)

        #设置打开文件按钮#
        self.openfile_pushbutton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openfile_pushbutton.sizePolicy().hasHeightForWidth())
        self.openfile_pushbutton.setSizePolicy(sizePolicy)
        self.openfile_pushbutton.setMinimumSize(QtCore.QSize(104, 40))
        self.openfile_pushbutton.setMaximumSize(QtCore.QSize(104, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.openfile_pushbutton.setFont(font)
        self.openfile_pushbutton.setObjectName("openfile_pushbutton")
        self.openfile_pushbutton.clicked.connect(self.show_data_in_textedit)            #打开文件按钮信号与槽#

        self.gridLayout.addWidget(self.openfile_pushbutton, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)

        #设置清空文本数据按钮#
        self.cleardata_pushbutton = QtWidgets.QPushButton(self.widget)
        self.cleardata_pushbutton.setMinimumSize(QtCore.QSize(104, 40))
        self.cleardata_pushbutton.setMaximumSize(QtCore.QSize(104, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.cleardata_pushbutton.setFont(font)
        self.cleardata_pushbutton.setObjectName("cleardata_pushbutton")
        self.cleardata_pushbutton.clicked.connect(self.clear_filedata)       #清空文本数据按钮信号与槽#

        self.gridLayout.addWidget(self.cleardata_pushbutton, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        #起始位置设置区#
        self.start_point = QtWidgets.QLineEdit(self.widget_3)
        self.start_point.setMinimumSize(QtCore.QSize(80, 20))
        self.start_point.setMaximumSize(QtCore.QSize(80, 20))
        self.start_point.setText("")
        self.start_point.setObjectName("start_point")
        self.horizontalLayout_2.addWidget(self.start_point)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        #步进位置设置区#
        self.step = QtWidgets.QLineEdit(self.widget_3)
        self.step.setMinimumSize(QtCore.QSize(80, 20))
        self.step.setMaximumSize(QtCore.QSize(80, 20))
        self.step.setObjectName("step")
        self.horizontalLayout_2.addWidget(self.step)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")

        #约瑟夫弹出顺序结果显示区#
        self.results_textedit = QtWidgets.QTextEdit(self.widget_4)
        self.results_textedit.setMinimumSize(QtCore.QSize(250, 170))
        self.results_textedit.setMaximumSize(QtCore.QSize(250, 170))
        self.results_textedit.setObjectName("results_textedit")
        self.gridLayout_2.addWidget(self.results_textedit, 0, 3, 2, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 1, 0, 1, 1)

        #存储约瑟夫运行结果按钮#
        self.save_results_pushbutton = QtWidgets.QPushButton(self.widget_4)
        self.save_results_pushbutton.setMinimumSize(QtCore.QSize(104, 40))
        self.save_results_pushbutton.setMaximumSize(QtCore.QSize(104, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.save_results_pushbutton.setFont(font)
        self.save_results_pushbutton.setObjectName("save_results_pushbutton")
        self.gridLayout_2.addWidget(self.save_results_pushbutton, 1, 1, 1, 1)
        self.save_results_pushbutton.clicked.connect(self.save_results_into_file)

        #获取约瑟夫运行结果按钮#
        self.get_out_order_pushbutton = QtWidgets.QPushButton(self.widget_4)
        self.get_out_order_pushbutton.setMinimumSize(QtCore.QSize(104, 40))
        self.get_out_order_pushbutton.setMaximumSize(QtCore.QSize(104, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)    
        self.get_out_order_pushbutton.setFont(font)
        self.get_out_order_pushbutton.setObjectName("get_out_order_pushbutton")
        self.gridLayout_2.addWidget(self.get_out_order_pushbutton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_4)
        self.get_out_order_pushbutton.clicked.connect(self.get_out_order_of_josephus)       #获取约瑟夫运行结果信号与槽#

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "约瑟夫环"))
        self.openfile_pushbutton.setText(_translate("MainWindow", "打开文件"))
        self.cleardata_pushbutton.setText(_translate("MainWindow", "清空数据"))
        self.label_2.setText(_translate("MainWindow", "起始位置："))
        self.label_3.setText(_translate("MainWindow", "步进值："))
        self.save_results_pushbutton.setText(_translate("MainWindow", "保存结果"))
        self.get_out_order_pushbutton.setText(_translate("MainWindow", "获取弹出顺序"))

#错误输入提示界面#
    def show_error_input_reminder_dialog(self):
        vbox=QVBoxLayout()#纵向布局
        hbox=QHBoxLayout()#横向布局
        panel=QLabel()
        panel.setText("输入错误，请重新输入整形start_point>0及整形step>=0")
        self.dialog=QDialog()
        self.dialog.resize(100,100)
        self.ok_pushbutton=QPushButton("确定")
        self.dialog.setWindowTitle("提示信息！")
        self.ok_pushbutton.clicked.connect(self.close_error_reminder_dialog)
        hbox.addWidget(self.ok_pushbutton)
        vbox.addWidget(panel)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    def close_error_reminder_dialog(self):
        self.dialog.close()


#打开文件按钮槽函数#
    def show_data_in_textedit (self):
        file = QFileDialog.getOpenFileName(self.centralwidget, '打开文件', '.')   #返回元组，file[0]为地址
        if file[0]:            #用户在选择程序文件时若点击取消，file[0]长度为0，由此作为判断依据#
            file_path = file[0]
            file_suffix = file_path.split('.', 2)[1]   #后缀名
            file_suffix_dict = {'txt' : TxtReader, 'xls' : ExcelReader, 'csv': CsvReader,'zip':ZipReader}
            class_instance = file_suffix_dict[file_suffix]
            obj = class_instance(file_path)
            student_list=obj.read()
        #向文本框写入数据#
            for student in student_list:
                student_msg = student.get_msg()
                self.data_textedit.append(student_msg)

#清空数据按钮槽函数#
    def clear_filedata(self):
        self.data_textedit.clear()
        self.results_textedit.clear()
        self.step.clear()
        self.start_point.clear()

#获取弹出顺序按钮槽函数#
    def get_out_order_of_josephus(self):     
        data = self.data_textedit.toPlainText()
        student_list = []
        if len(data):     #判断文本框内容是否不为空#
            #获取学生列表#
            lines = data.split('\n')
            for line in lines:
                divided_data = line.split()
                new_student = Student(divided_data[0],divided_data[1],divided_data[2])
                student_list.append(new_student)

        #获取步进与起始点信息#
        step = self.step.text()
        start_point = self.start_point.text()

        #判断输入step以及start_point是否符合要求#
        if step.isdigit() and start_point.isdigit():  #判断是否为整形#    ###若不要求起始点为负，可用
            step = int(step)
            start_point = int(start_point)
            if step >= 0 and start_point != 0: 
                josephus_circle = JosephusCircle(student_list,step,start_point)
                #将弹出顺序显示到文本框里#
                for student in josephus_circle:    #iter(josephus_circle)
                    student_msg = student.get_msg()
                    self.results_textedit.append(student_msg)

            else:              #输入异常处理#
                self.step.clear()
                self.start_point.clear()
                self.show_error_input_reminder_dialog()
        else:       #输入异常处理#
                self.step.clear()
                self.start_point.clear()
                self.show_error_input_reminder_dialog()
#将结果写入文件#
    def save_results_into_file(self):
        with open(r'./results_of_joseohus_circle.txt','w',encoding='UTF-8') as f:
            results = self.results_textedit.toPlainText()
            f.write(results)

        