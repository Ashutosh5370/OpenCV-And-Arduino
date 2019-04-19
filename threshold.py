import  cv2

import  numpy as np

img = cv2.imread('book.jpg')

ret , threshold  = cv2.threshold(img , 200 , 255 ,cv2.THRESH_BINARY )


grayscale = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY )


ret2, threshold2  = cv2.threshold(grayscale , 200 , 255 ,cv2.THRESH_BINARY )


gaus = cv2.adaptiveThreshold(grayscale , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY  , 155 ,1)

cv2.imshow('oroginal' , img)
cv2.imshow('threshold'  ,threshold)
cv2.imshow('threshold2'  ,threshold2)
cv2.imshow('threshold3'  ,gaus )




cv2.waitKey()

cv2.destroyAllWindows()
