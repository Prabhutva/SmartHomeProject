######################INFORMATION########################
#This program will show only one value coming from arduino
#and show it in a single plot. The plot has one  y axis
#and data is shown only for a particular number of values
#########################################################

#import statements
import serial
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import time

plt.style.use('dark_background')# welcome to the dark side

#serial port initialization
#TO-DO: auto-detection of port so that it is not required to change it continuously.
#Can use try catch statements for Port checking else find proper methods for it.
ser = serial.Serial('COM4',9600)#take note of the baud value
ser.flushInput()

#all the arrays which will store the values
xval = []#to store the x axis
value1 = []#first and only value to display

#making graph interactive
plt.ion()

#setting the count to 0
cnt = 0

#some function to remove and rerrange the spines of the axes
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

#the function to do all the plotting work 
def showfig():
    # fig, plt1 = plt.subplots()
    plt.subplots_adjust(right=0.75)
    plt.axis('off')
    plt.xlabel("Time")
    plt.title('MQ7 Sensor Data')      #Plot the title
    plt.grid(True) 
    plt1 = plt.twinx()
    
    plt1.yaxis.set_label_position('left')

    p1, = plt1.plot(value1, "b-", label="CO Index (PPM)", linewidth=4)

    plt1.set_xlim(0, 101)

    plt1.set_ylim(np.amin(value1)-2,np.amax(value1)+2)

    plt1.set_xlabel("Time")
    plt1.set_ylabel("CO Index (PPM)")

    plt1.xaxis.label.set_color(p1.get_color())
    plt1.yaxis.label.set_color(p1.get_color())

    tkw = dict(size=4, width=1.5)
    plt1.tick_params(axis='y', colors=p1.get_color(), **tkw)
    plt1.tick_params(axis='x', colors=p1.get_color(), **tkw)

    lines = [p1]

    plt1.legend(lines, [l.get_label() for l in lines])

    # plt.show()

#loop run to update values of the graph
for k in range(1000): #loop for a particular time
    while (ser.inWaiting()==0): #Wait here until there is data
        pass #do notvalue3ng
    read_bytes = ser.readline()#get data from the arduino serial port
    decoded_bytes = read_bytes[0:len(read_bytes)-2].decode("utf-8")#decoding the bytes to readable data

 
    #try ctach block to overcome the errors while getting illegal data from the arduino
    #if number of plots required is one, the only one plot should be shown.
    try:
        dataArray = decoded_bytes.split(',')  #Split it into an array called dataArray

        #getting the data from the serial array to different value arrays
        #TO-DO: automate this process so that arrays are created automatically
        yvalue1 = float(dataArray[0])

        #printing all the values for confirmation
        print(yvalue1)
       
        #appending all the value to the array
        value1.append(yvalue1)           
       
        drawnow(showfig)#Call drawnow to update our live graph

        plt.pause(.0001)#Pause Briefly. Important to keep drawnow from crashing

        cnt=cnt+1#increasing the count
        if(cnt>100):#If you have x or more points, delete the first one from the array
            value1.pop(0)#This allows us to just see the last x data points
    except:
        print("error")# bad data recieved from the arduino serial
        continue 