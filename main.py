from Weather import Weather
import datetime
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

current_Date_Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

location = "60 Cranbury Neck Road"

while (True):
    
    
    
    print(Weather(location, current_Date_Time).makeRequest())
    if (Weather(location, current_Date_Time).makeRequest()) < 32:
        print("its cold")
        #turn on LED
        GPIO.output(4, True)
        time.sleep(4)
        GPIO.output(4, False)
        time.sleep(2)
        
    
    time.sleep(3)
GPIO.cleanup()