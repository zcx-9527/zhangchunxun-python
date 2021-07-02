#第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小 #

import os
import cv2 as cv

def resize_img(img_path,size_x,size_y):
    for dir_path in os.listdir(img_path):
         if os.path.splitext(dir_path)[1] == '.jpg':
             img=cv.imread(os.path.abspath(os.path.join(img_path,dir_path)))
             after_resize_img=cv.resize(img,(300,300))
             cv.imwrite('new'+dir_path,after_resize_img)
             

resize_img(r"D:\ProgramData\test_img",300,300)