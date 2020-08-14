import serial
import time
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM4',9600)
ser.flushInput()

plot_window = 100
y_var = np.array(np.zeros([plot_window]))# initializing the array to show last x values currently filled with zeroes

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(y_var)

while True:
    try:
        ser_bytes = ser.readline()
        try:
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
        except:
            continue
        y_var = np.append(y_var,decoded_bytes)
        y_var = y_var[1:plot_window+1]
        line.set_ydata(y_var)
        ax.relim()
        ax.autoscale_view()#data is scaled automatically
        fig.canvas.draw()#drawing and showing everything
        fig.canvas.flush_events()#removing the current graph to show the next graph
    except:
        print("Keyboard Interrupt")
        break
    #checked: the x in one approach works better
