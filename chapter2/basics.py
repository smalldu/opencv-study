import numpy as np
import cv2
import os



# img = np.zeros((3,3),dtype="uint8")
# img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# print(img)
# print(img.shape)


# img = cv2.imread('MyPic.png')
# cv2.imwrite('my-pic.jpg',img)


def generalRandomPNG():
    randomByteArray = bytearray(os.urandom(120000))
    flatNumpyArray = np.array(randomByteArray)

    # 转换成灰度图
    grayImage = flatNumpyArray.reshape(300, 400)
    cv2.imwrite('randomGray.png', grayImage)

    # 转换成色彩图

    bgrImage = flatNumpyArray.reshape(100, 400, 3)
    cv2.imwrite('randomColor.png', bgrImage)


img = cv2.imread('MyPic.png')
# 输出 150，120坐标b的值  （BGR的顺序)
# print(img.item(150,120,0))
# img.itemset((150,120,0),255)
# print(img.item(150,120,0))

# 将图片中所有绿色设置为0
# img[:,:, 1] = 0

# 复制感兴趣区域
# my_roi = img[0:100 , 0:100]
# img[100:200 , 100:200] = my_roi

print(img.shape) # 宽度 高度 通道数（如果是单色或者灰度图 则没有通道数）
print(img.size) # 像素大小
print(img.dtype) # 数据类型通常是uint8

# cv2.imshow('pic',img)
# cv2.waitKey()
# cv2.destroyAllWindows()






















