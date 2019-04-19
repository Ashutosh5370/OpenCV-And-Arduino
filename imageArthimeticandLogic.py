import cv2


import  numpy as np

img1 = cv2.imread('3D.png')

img2 = cv2.imread('mainlogo.png')

img3 = cv2.imread('python.png')

#add = img1 + img2

#cv2.add(img2 , img1)

#weighted = cv2.addWeighted(img1 , 0.6 , img2 , 0.4 ,0)

#cv2.imshow('add', weighted)

rows , cols ,channels = img3.shape

roi = img1[0:rows , 0:cols]

img2gray = cv2.cvtColor(img3 , cv2.COLOR_BGR2GRAY)

ret , mask = cv2.threshold(img2gray , 220 , 255 , cv2.THRESH_BINARY_INV)

#cv2.imshow('mask' , mask)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi , roi , mask = mask_inv)

img3_fg = cv2.bitwise_and(img3 , img3 , mask =mask)

dst = cv2.add(img1_bg , img3_fg)

img1[0:rows , 0 : cols] = dst

cv2.imshow('res' , img1)

cv2.waitKey()

cv2.destroyAllWindows()



