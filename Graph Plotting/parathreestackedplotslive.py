import serial
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import time
import matplotlib.animation as animation

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
plt.tight_layout()
plt.title('DHT Sensor Data')      #Plot the title
plt.xlabel('Time')
plt.grid(True) 
fig = plt.figure()
fig, axs = plt.subplots(3, sharex=True, sharey=False)

#set labels here
label = ['Humidity','Temperature','Heat Index']
#shows all the labels once
print(label)

#making graph interactive
# plt.ion()

#setting the count to 0
cnt = 0

#this time we will need lesser modifications
#spine modification not required

def animate(i, xval, value1, value2, value3):
    global cnt
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
        # print(yvalue1)
        # print(yvalue2)
        # print(yvalue3)
        print(decoded_bytes)
        
        #appending all the value to the array
        value1.append(yvalue1)           
        value2.append(yvalue2)
        value3.append(yvalue3)
        xval.append(cnt)
        

        
        if(cnt>50):#If you have x or more points, delete the first one from the array
            value1.pop(0)#This allows us to just see the last x data points
            value2.pop(0)
            value3.pop(0)
            xval.pop(0)
        axs[0].clear()
        axs[1].clear()
        axs[2].clear()
        cnt=cnt+1#increasing the count
        

        p1, = axs[0].plot(value1, "b-", label=label[0],linewidth=2)
        p2, = axs[1].plot(value2, "r-", label=label[1], linewidth=2)
        p3, = axs[2].plot(value3, "g-", label=label[2],linewidth=2)

        axs[0].set_ylim(np.amin(value1)-5,np.amax(value1)+6)
        axs[1].set_ylim(np.amin(value2)-1.5, np.amax(value2)+1.0)
        axs[2].set_ylim(np.amin(value3)-1, np.amax(value3)+0.5)

        axs[0].set_title(label[0])
        axs[1].set_title(label[1])
        axs[2].set_title(label[2])

        axs[0].set_ylabel(label[0])
        axs[1].set_ylabel(label[1])
        axs[2].set_ylabel(label[2])

        axs[0].yaxis.label.set_color(p1.get_color())
        axs[1].yaxis.label.set_color(p2.get_color())
        axs[2].yaxis.label.set_color(p3.get_color())

        for ax in axs.flat:
            ax.label_outer()

        lines = [p1, p2, p3]

        plt.legend(lines, [l.get_label() for l in lines])


    except:
        print("error")# bad data recieved from the arduino serial


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xval, value1, value2, value3), interval=1000)
plt.show()




############################## Older Code ###################################

# Some example data to display
# x = np.arange(0,100)
# y1 = x*1
# y2 = x*2
# y3 = x*3

# plt.ion()
# cnt = 0

# label = ['Humidity','Temperature','Heat Index']
# print(label)
# fig, axs = plt.subplots(3, sharex=True, sharey=False)
# axs[0].plot(x, y1, 'tab:blue')
# axs[0].set_title(label[0])
# axs[1].plot(x, y2, 'tab:orange')
# axs[1].set_title(label[1])
# axs[2].plot(x, y3, 'tab:green')
# axs[2].set_title(label[2])

# for ax in axs.flat:
#     ax.set(xlabel='x-label', ylabel='y-label')

# # Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()

# plt.show()
# plt.pause(1000)