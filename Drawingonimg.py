import cv2
import  numpy as np
import  matplotlib.pyplot as plt


#read image and IMREA_GRAYSCALE to convert image in grayscale substitude is 0
img = cv2.imread('D:/d.jpg' ,cv2.IMREAD_COLOR)
#lineDraw
cv2.line(img , (0 ,0) , (150 , 150) , (255 , 0 , 0) ,10)
#line Rectangle
cv2.rectangle(img ,(15 ,25),(200 , 150 ), (0, 255 , 0),5)

cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

pts = np.array([[10,5],[20,30],[70,50],[50,10]] , np.int32)

cv2.polylines(img , [pts] ,True , (0 ,255 ,0),2)
cv2.imshow('image' , img)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img ,'open tuts',(0, 140) ,font ,1,(200 ,255 , 255) ,2 ,cv2.LINE_AA)


cv2.waitKey(0)
cv2.destroyAllWindows()


