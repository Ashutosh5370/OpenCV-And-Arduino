import speech_recognition as sr


import serial #Serial imported for Serial communication
import time #Required to use delay functions
 

ArduinoSerial = serial.Serial('/dev/ttyACM1',19200) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print ArduinoSerial.readline() #read the serial data and print it as line



while 1: #Do this forever

    r = sr.Recognizer() 
    with sr.Microphone() as source:
      
   	 print("Speak something")

   	 audio = r.listen(source)
	
   	 var = r.recognize_google(audio)

  	  
    
	
   
    print "you entered", Text
    
    if (var == 'one'): #if the value is 1
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == 'two'): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(1)



