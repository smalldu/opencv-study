import numpy as np
import cv2

clicked = False

def onMouse(event ,x ,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

camaraCapture = cv2.VideoCapture(0)
cv2.namedWindow('mywindow')
cv2.setMouseCallback('mywindow',onMouse)
print('点击左键 或者 按任意键结束')

success,frame = camaraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('mywindow',frame)
    success,frame = camaraCapture.read()
cv2.destroyWindow('mywindow')
camaraCapture.release()

