from PIL import Image
import sys
import cv2
cv2.VideoCapture(0)
face="haarcascade_frontalface_alt.xml"
thug="ladka.jpg"
faceCas=cv2.CascadeClassifier(face)
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=faceCas.detectMultiScale(grey,1.5)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("face",image)
    cv2.waitKey(0)

