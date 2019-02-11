import cv2,time

img = cv2.imread("C:\\Users\\Ashutosh\\Desktop\\ch.jpg" ,1)
print(img)
print(img.shape)
print(type(img))

# show image on the screen

#cv2.imshow("chk" , img)

#cv2.waitKey(0)
#cv2.waitKey(1000)

#cv2.destroyAllWindows()

# resize original image
#this will double the size of image
resized = cv2.resize(img ,(int(img.shape[1]*2),int(img.shape[0]*2)))

cv2.imshow("legend",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
face_cascade = cv2.CascadeClassifier('C:\\Users\\Ashutosh\\Downloads\\haarcascade_frontalface_default.xml')
img2 = cv2.imread("C:\\Users\\Ashutosh\\Desktop\\p.jpeg",1)

gray_img = cv2.cvtColor(img2 ,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img ,scaleFactor=1.05,minNeighbors=5)

print(type(faces))

print(faces)

for x,y,w,h in faces:
    img2=cv2.rectangle(img2,(x,y) , (x+w ,y+h),(0,255 , 0),3)

cv2.imshow("gray",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

video = cv2.VideoCapture(0)

cheak ,frame = video.read()

print(cheak)
print(frame)

time.sleep(3)

cv2.imshow("capture",frame)

cv2.waitKey(0)
video.release()

cv2.destroyAllWindows()

video = cv2.VideoCapture(0)

a = 1
import cv2
while True:
    a = a+1
    check , frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("cap",frame)
    key1 = cv2.waitKey(1)
    if key1  == ord('q'):
        break


print(a)
video.release()
cv2.destroyAllWindows()