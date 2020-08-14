######################INFORMATION#######################
#This program will show three values coming from arduino
#and show them in a single plot. The plot has three axes 
#and data is shown only for a particular number of values
########################################################

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
ser = serial.Serial('COM4',9600)#take note of the baud value
ser.flushInput()

#all the arrays which will store the values
xval = []#to store the x axis
value1 = []#first value to display
value2 = []#second value to display
value3 = []#third value to display

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
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True) 
    plt1 = plt.twinx()
    plt2 = plt.twinx()
    plt3 = plt.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    plt3.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(plt3)
    # Second, show the right spine.
    plt3.spines["right"].set_visible(True)

    plt2.spines["left"].set_position(("axes", 1.2 ))
    plt1.yaxis.set_label_position('left')


    p1, = plt1.plot(value1, "b-", label="Humidity",linewidth=4)
    p2, = plt2.plot(value2, "r-", label="Temperature", linewidth=4)
    p3, = plt3.plot(value3, "g-", label="Heat Index",linewidth=4)

    plt1.set_xlim(0, 101)
    plt1.set_ylim(np.amin(value1)-5,np.amax(value1)+6)
    plt2.set_ylim(np.amin(value2)-1.5, np.amax(value2)+1.0)
    plt3.set_ylim(np.amin(value3)-1, np.amax(value3)+0.5)

    plt1.set_xlabel("Time")
    plt1.set_ylabel("Humidity")
    plt2.set_ylabel("Temperature")
    plt3.set_ylabel("Heat Index")

    plt1.xaxis.label.set_color(p1.get_color())
    plt1.yaxis.label.set_color(p1.get_color())
    plt2.yaxis.label.set_color(p2.get_color())
    plt3.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    plt1.tick_params(axis='y', colors=p1.get_color(), **tkw)
    plt2.tick_params(axis='y', colors=p2.get_color(), **tkw)
    plt3.tick_params(axis='y', colors=p3.get_color(), **tkw)
    plt1.tick_params(axis='x', colors=p1.get_color(), **tkw)

    lines = [p1, p2, p3]

    plt1.legend(lines, [l.get_label() for l in lines])

    # plt.show()

#loop run to update values of the graph
for k in range(1000): #loop for a particular time
    while (ser.inWaiting()==0): #Wait here until there is data
        pass #do notvalue3ng
    read_bytes = ser.readline()#get data from the arduino serial port
    decoded_bytes = read_bytes[0:len(read_bytes)-2].decode("utf-8")#decoding the bytes to readable data

    #try ctach block to overcome the errors while getting illegal data from the arduino
    #TO-DO: plot data according to number of plots present.
    #if number of plots required is one, the only one plot should be shown.
    try:
        dataArray = decoded_bytes.split(',')  #Split it into an array called dataArray

        #getting the data from the serial array to different value arrays
        #TO-DO: automate this process so that arrays are created automatically
        yvalue1 = float(dataArray[0])
        yvalue2 = float(dataArray[1])
        yvalue3 = float(dataArray[2])

        #printing all the values for confirmation
        print(yvalue1)
        print(yvalue2)
        print(yvalue3)
       
        #appending all the value to the array
        value1.append(yvalue1)           
        value2.append(yvalue2)
        value3.append(yvalue3)
       
        drawnow(showfig)#Call drawnow to update our live graph

        plt.pause(.0001)#Pause Briefly. Important to keep drawnow from crashing

        cnt=cnt+1#increasing the count
        if(cnt>100):#If you have x or more points, delete the first one from the array
            value1.pop(0)#This allows us to just see the last x data points
            value2.pop(0)
            value3.pop(0)
    except:
        print("error")# bad data recieved from the arduino serial
        continue 