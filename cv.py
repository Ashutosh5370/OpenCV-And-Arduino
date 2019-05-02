
import cv2 , time

face_cascade = cv2.CascadeClassifier('face.xml')

video = cv2.VideoCapture(0)

a = 1

lst = []


while True:
    a = a+1
    check , frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray " , gray)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
	print(x , y)
	lst.append(x)

    cv2.imshow("cap",frame)
    key1 = cv2.waitKey(1)
    if key1  == ord('q') or a== 40:
        break

print(lst)
print(a)
video.release()
cv2.destroyAllWindows()
