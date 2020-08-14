from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
tdelay=0.05
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
camera = PiCamera()
camera.resolution = (3280, 2464)


<launch>
  <arg name="enable_raw" default="false"/>
  <arg name="camera_id" default="0"/>
  <arg name="camera_frame_id" default="raspicam"/>
  <arg name="camera_name" default="camerav2_410x308"/>

  <node type="raspicam_node" pkg="raspicam_node" name="raspicam_node" output="screen">
    <param name="camera_frame_id" value="$(arg camera_frame_id)"/> 
    <param name="enable_raw" value="$(arg enable_raw)"/>
    <param name="camera_id" value="$(arg camera_id)"/> 

    <param name="camera_info_url" value="package://raspicam_node/camera_info/camerav2_410x308.yaml"/>
    <param name="camera_name" value="$(arg camera_name)"/>
    <param name="width" value="410"/>
    <param name="height" value="308"/>

    <param name="framerate" value="30"/>
    <param name="exposure_mode" value="antishake"/>
    <param name="shutter_speed" value="0"/>
  </node>
</launch>

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
    sleep(1)
    camera.capture("/home/ubuntu/Desktop/Images/"+filename+".jpg")
    
    
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
        runcamsave("led00")
        sleep(tdelay)
        setval(True, False, False)
        runcamsave("led01")
        sleep(tdelay)
        setval(False, True, False)
        runcamsave("led02")
        sleep(tdelay)
        setval(True, True, False)
        runcamsave("led03")
        sleep(tdelay)
        setval(False, False, True)
        runcamsave("led04")
        sleep(tdelay)
        setval(True, False, True)
        runcamsave("led05")
        sleep(tdelay)
        setval(False, True, True)
        runcamsave("led06")
        sleep(tdelay)
        setval(True, True, True)
        runcamsave("led07")
        sleep(tdelay)
        #
        #
        #decoder 2
        setenable(True, True, False)
        setval(False, False, False)
        runcamsave("led08")
        sleep(tdelay)
        setval(True, False, False)
        runcamsave("led09")
        sleep(tdelay)
        setval(False, True, False)
        runcamsave("led10")
        sleep(tdelay)
        setval(True, True, False)
        runcamsave("led11")
        sleep(tdelay)
        setval(False, False, True)
        runcamsave("led12")
        sleep(tdelay)
        setval(True, False, True)
        runcamsave("led13")
        sleep(tdelay)
        setval(False, True, True)
        runcamsave("led14")
        sleep(tdelay)
        setval(True, True, True)
        runcamsave("led15")
        sleep(tdelay)
        #
        #
        #decoder 3
        setenable(True, False, True)
        setval(False, False, False)
        runcamsave("led16")
        sleep(tdelay)
        setval(True, False, False)
        runcamsave("led17")
        sleep(tdelay)
        setval(False, True, False)
        runcamsave("led18")
        sleep(tdelay)
        setval(True, True, False)
        runcamsave("led19")
        sleep(tdelay)
        setval(False, False, True)
        runcamsave("led20")
        sleep(tdelay)
        setval(True, False, True)
        runcamsave("led21")
        sleep(tdelay)
        setval(False, True, True)
        runcamsave("led22")
        sleep(tdelay)
        setval(True, True, True)
        runcamsave("led23")
        sleep(tdelay)
        #camera.stop_preview()
        A=0
except:
    pass
GPIO.cleanup()
