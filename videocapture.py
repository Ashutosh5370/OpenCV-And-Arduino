import cv2
import  numpy as np
import  matplotlib.pyplot as plt


#read image and IMREA_GRAYSCALE to convert image in grayscale substitude is 0
#img = cv2.imread('D:/d.jpg' ,cv2.IMREAD_GRAYSCALE)

#cv2.imshow('Image' , img)
#wait for any key to be close

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


