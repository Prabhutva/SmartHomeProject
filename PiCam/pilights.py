#script to control raspicam and capture
#images with different wavelengths of LED
#lights controlled using a Raspberry Pi
#or Jetson Nano with PiCam and decoders.
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
tdelay=0.5
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
camera = PiCamera()
camera.resolution = (2400, 1800)

a0=11
a1=13
a2=15

e1=19
e2=21
e3=23

GPIO.setup(a0, GPIO.OUT)
GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)

GPIO.setup(e1, GPIO.OUT)
GPIO.setup(e2, GPIO.OUT)
GPIO.setup(e3, GPIO.OUT)

def runcamsave(filename):
    sleep(tdelay)
    camera.capture("/home/ubuntu/Desktop/Images/"+filename+".jpg")
    print(filename+" image captured")
    sleep(tdelay)
    
    
def setval(A0, A1, A2):
    if A0:
        GPIO.output(a0, GPIO.HIGH)
    else:
        GPIO.output(a0, GPIO.LOW)
    if A1:
        GPIO.output(a1, GPIO.HIGH)
    else:
        GPIO.output(a1, GPIO.LOW)
    if A2:
        GPIO.output(a2, GPIO.HIGH)
    else:
        GPIO.output(a2, GPIO.LOW)

def setenable(E3, E2, E1):
    if E1:
        GPIO.output(e1, GPIO.HIGH)
    else:
        GPIO.output(e1, GPIO.LOW)
    if E2:
        GPIO.output(e2, GPIO.HIGH)
    else:
        GPIO.output(e2, GPIO.LOW)
    if E3:
        GPIO.output(e3, GPIO.HIGH)
    else:
        GPIO.output(e3, GPIO.LOW) 
try:
    A=1
    while A==1:
        #decoder 1
        camera.start_preview()
        setenable(False, False, False)
        setval(False, False, False)
        runcamsave("led00")
        setval(True, False, False)
        runcamsave("led01")
        setval(False, True, False)
        runcamsave("led02")
        setval(True, True, False)
        runcamsave("led03")
        setval(False, False, True)
        runcamsave("led04")
        setval(True, False, True)
        runcamsave("led05")
        setval(False, True, True)
        runcamsave("led06")
        setval(True, True, True)
        runcamsave("led07")
        #
        #
        #decoder 2
        setenable(True, True, False)
        setval(False, False, False)
        runcamsave("led08")
        setval(True, False, False)
        runcamsave("led09")
        setval(False, True, False)
        runcamsave("led10")
        setval(True, True, False)
        runcamsave("led11")
        setval(False, False, True)
        runcamsave("led12")
        setval(True, False, True)
        runcamsave("led13")
        setval(False, True, True)
        runcamsave("led14")
        setval(True, True, True)
        runcamsave("led15")
        #
        #
        #decoder 3
        setenable(True, False, True)
        setval(False, False, False)
        runcamsave("led16")       
        setval(True, False, False)
        runcamsave("led17")         
        setval(False, True, False)
        runcamsave("led18")         
        setval(True, True, False)
        runcamsave("led19")         
        setval(False, False, True)
        runcamsave("led20")         
        setval(True, False, True)
        runcamsave("led21")         
        setval(False, True, True)
        runcamsave("led22")         
        setval(True, True, True)
        runcamsave("led23")
        camera.stop_preview()
        A=0
except:
    pass
GPIO.cleanup()
