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

plt.ion()
cnt = 0

fig, axs = plt.subplots(3, sharex=True, sharey=False)
axs[0].plot(x, y1, 'tab:blue')
axs[0].set_title('Axis 1')
axs[1].plot(x, y2, 'tab:orange')
axs[1].set_title('Axis 2')
axs[2].plot(x, y3, 'tab:green')
axs[2].set_title('Axis 3')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()
plt.pause(1000)