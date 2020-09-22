import RPi.GPIO as GPIO
import PCF8591 as pcf
import time
import barometre as b

relay=32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)

pcf.setup(0x48)
sleepTime =1
try:
    while True:
        H, T ,P= pcf.read(1),b.degrees,b.hectopascals
        print("Humidity is: " , H,"%")
        print("temperature is: " , T, "C")
        print("Pressure is: " , P,"hPa")
        time.sleep(sleepTime)
        if(P>1000)and(int(H)>250):#condition d'arrosage
            GPIO.output(relay, GPIO.HIGH)#ouvrir l'électrovanne
            time.sleep(5)#arroser pendant 5 sec
            GPIO.output(relay, GPIO.LOW)#fermer l'électrovanne
        else:
            GPIO.output(relay, GPIO.LOW)
            
except KeyboardInterrupt:
    GPIO.output(relay, GPIO.LOW)
    GPIO.cleanup()
    
