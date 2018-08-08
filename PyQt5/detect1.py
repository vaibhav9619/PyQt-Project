import numpy as np
import cv2
def ko():
    img=cv2.VideoCapture(0)
    ret,cap=img.read()
    cv2.imshow("jsdk",cap)
    cv2.imwrite("images/"+"image.jpg",cap)
    cv2.waitKey(0)
s=ko()
