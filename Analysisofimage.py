import cv2
import  numpy as np
import  matplotlib.pyplot as plt


#read image and IMREA_GRAYSCALE to convert image in grayscale substitude is 0
img = cv2.imread('D:/d.jpg' ,cv2.IMREAD_COLOR)

px = img[55,55]
print(px)

img[55,55] = [0,255,255]
print(px)

#ROI region of image
roi = img[100:250 , 100:150]
#print(roi)

img[100:250 , 100:150] = [255,255,255]

cv2.imshow('IMAGE', img)



cv2.waitKey(0)
cv2.destroyAllWindows()


