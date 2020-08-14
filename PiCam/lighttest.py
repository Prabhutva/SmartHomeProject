from time import sleep
import RPi.GPIO as GPIO
#from picamera import PiCamera
tdelay=2
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#camera = PiCamera()
#camera.resolution = (3280, 2464)

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

# def runcamsave(filename):
#     sleep(1)
#     camera.capture("/home/pi/Desktop/Images/"+filename+".jpg")
    
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
        #camera.start_preview()
        setenable(False, False, False)
        setval(False, False, False)
        print("led00")
        sleep(tdelay)
        setval(True, False, False)
        print("led01")
        sleep(tdelay)
        setval(False, True, False)
        print("led02")
        sleep(tdelay)
        setval(True, True, False)
        print("led03")
        sleep(tdelay)
        setval(False, False, True)
        print("led04")
        sleep(tdelay)
        setval(True, False, True)
        print("led05")
        sleep(tdelay)
        setval(False, True, True)
        print("led06")
        sleep(tdelay)
        setval(True, True, True)
        print("led07")
        sleep(tdelay)
        #
        #
        #decoder 2
        setenable(True, True, False)
        setval(False, False, False)
        print("led08")
        sleep(tdelay)
        setval(True, False, False)
        print("led09")
        sleep(tdelay)
        setval(False, True, False)
        print("led10")
        sleep(tdelay)
        setval(True, True, False)
        print("led11")
        sleep(tdelay)
        setval(False, False, True)
        print("led12")
        sleep(tdelay)
        setval(True, False, True)
        print("led13")
        sleep(tdelay)
        setval(False, True, True)
        print("led14")
        sleep(tdelay)
        setval(True, True, True)
        print("led15")
        sleep(tdelay)
        #
        #
        #decoder 3
        setenable(True, False, True)
        setval(False, False, False)
        print("led16")
        sleep(tdelay)
        setval(True, False, False)
        print("led17")
        sleep(tdelay)
        setval(False, True, False)
        print("led18")
        sleep(tdelay)
        setval(True, True, False)
        print("led19")
        sleep(tdelay)
        setval(False, False, True)
        print("led20")
        sleep(tdelay)
        setval(True, False, True)
        print("led21")
        sleep(tdelay)
        setval(False, True, True)
        print("led22")
        sleep(tdelay)
        setval(True, True, True)
        print("led23")
        sleep(tdelay)
        #camera.stop_preview()
        A=1
except:
    pass
GPIO.cleanup()
