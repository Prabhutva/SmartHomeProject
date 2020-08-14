import serial
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

ser0 = serial.Serial('/dev/ttyUSB0',9600)#take note of the baud value
ser1 = serial.Serial('/dev/ttyUSB1',9600)#take note of the baud value
ser2 = serial.Serial('/dev/ttyUSB2',9600)#take note of the baud value
ser0.flushInput()
ser1.flushInput()
ser2.flushInput()

while True:
	while ser0.inWaiting()==0: #Wait here until there is data
		pass #do notvalue3ng
	read_bytes0 = ser0.readline()#get data from the arduino serial port
	decoded_bytes0 = read_bytes0[0:len(read_bytes0)-2].decode("utf-8")#decoding the bytes to readable data
	print(decoded_bytes0)
	#
	#
	while ser1.inWaiting()==0: #Wait here until there is data
		pass #do notvalue3ng
	read_bytes1 = ser1.readline()#get data from the arduino serial port
	decoded_bytes1 = read_bytes1[0:len(read_bytes1)-2].decode("utf-8")#decoding the bytes to readable data
	print(decoded_bytes1)
	#
	#
	while ser2.inWaiting()==0: #Wait here until there is data
		pass #do notvalue3ng
	read_bytes2 = ser2.readline()#get data from the arduino serial port
	decoded_bytes2 = read_bytes2[0:len(read_bytes2)-2].decode("utf-8")#decoding the bytes to readable data
	print(decoded_bytes2)
	#
	#
	print("----------------------------------------")
