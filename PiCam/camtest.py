from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.resolution = (2400, 1800)
camera.start_preview()
sleep(240)
camera.stop_preview()
