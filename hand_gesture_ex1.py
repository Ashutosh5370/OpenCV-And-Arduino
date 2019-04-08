import  cv2
import  numpy as np

hand = cv2.imread('D:/b.jpg', 0)


ret ,the = cv2.threshold(hand , 100 ,255, cv2.THRESH_BINARY)

contours,hierachy = cv2.findContours(the.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(c) for c in contours]
print(hull)

final = cv2.drawContours(hand , hull , -1 ,(0 , 255 , 0 ))
cv2.imshow('original Image', hand)
cv2.imshow('thresh' ,the)
cv2.imshow('convex hull' ,final)
cv2.waitKey(0)
cv2.destroyAllWindows()