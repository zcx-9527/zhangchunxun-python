#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果#

import cv2 as cv

def write_number_in_img(image,number='2'):
    after_write_img=cv.putText(image, number, (500, 100), cv.FONT_HERSHEY_SIMPLEX,3.0, (0, 0, 255), 5 )    #  cv2.putText(src, text, place, Font, Font_Size, Font_Color, Font_Overstriking)
    return after_write_img


if __name__ == '__main__':
    img=cv.imread('.\head_image.jpg')
    number='6'
    after_write_img=write_number_in_img(img,number)
    cv.imshow("after_write_img",after_write_img)
    cv.waitKey()
    cv.destroyAllWindows()