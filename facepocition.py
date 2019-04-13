
import cv2 , time
import serial #Serial imported for Serial communication
import time #Required to use delay functions
 



ArduinoSerial = serial.Serial('/dev/ttyACM0',19200) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established



face_cascade = cv2.CascadeClassifier('face.xml')
video = cv2.VideoCapture(0)
a = 1
lst = []

print ArduinoSerial.readline() #read the serial data and print it as line
print ("Enter 1 to turn ON LED and 0 to turn OFF LED")

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
	
	var = x
    
    if (var > 300 ):
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")
        time.sleep(0.05)
    
    if (var < 300): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(0.05)

    
    cv2.imshow("cap",frame)
    key1 = cv2.waitKey(1)
    if key1  == ord('q') :
        break

print(lst)
print(a)
video.release()
cv2.destroyAllWindows()

 


