import serial
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import time

plt.style.use('dark_background')

# Some example data to display
x = np.arange(0,100)
y1 = x*1
y2 = x*2
y3 = x*3
y4 = x*4
plt.ion()
cnt = 0

fig, axs = plt.subplots(2, 2, sharex='col', sharey='row')
axs[0, 0].plot(x, y1, 'tab:blue')
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y2, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, y3, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, y4, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()
plt.pause(1000)