#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果#
import cv2 as cv

def write_number(image):
    after_write_img=cv.putText(image, '6', (500, 100), cv.FONT_HERSHEY_SIMPLEX,3.0, (0, 0, 255), 5 )
    return after_write_img

img=cv.imread('D:\ProgramData\python_code\head_image.jpg')
after_write_img=write_number(img)
cv.imshow("after_write_img",after_write_img)
cv.waitKey()
cv.destroyAllWindows()