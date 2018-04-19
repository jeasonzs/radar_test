# -*- coding:utf-8 -*-

from serial import Serial
import binascii
import struct
from Tkinter import *
import threading
import array
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy.fftpack import fft,ifft

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1,xlim=(0, 125), ylim=(-50, 50))
ax2 = fig.add_subplot(2,1,2,xlim=(0, 125), ylim=(-1, 1))
line, = ax1.plot([], lw=2)
line2, = ax2.plot([], lw=2)


def init():
    return line,line2

# animation function.  this is called sequentially
def animate(i):

    # x = np.linspace(0, 2, 100)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    # line.set_data(x, y)
    #
    #
    # x2 = np.linspace(0, 2, 100)
    # y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))
    # line2.set_data(x2, y2)
    return line,line2


def main():
    root = Tk()



    threading.Thread(target=collector, args=(root,)).start()

    anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=50, interval=10)
    plt.show()
    # root.mainloop()

def collector(root):
    canvas = Canvas(root, width=1260, height=260, bg = "white")
    serial = Serial('com6', 57600, timeout=4)
    count = 0
    zs = 0
    while True:
        count = 0
        while True:
            data = serial.read(1)
            if ord(data[0]) == 255:
                count += 1
            else:
                count = 0
            if count >= 3:
                break
        data = serial.read(131)
        dis, df = struct.unpack('>H126s', data[0:128])


        sh = array.array('B', df)
        x=np.linspace(0,125,126)
        y=np.array(sh)
        line.set_data(x, y)
        ret = ifft(y)
        line2.set_data(x, ret)

        # canvas.delete("all")
        # left = 0
        # for i in range(0, 126):
        #     value = ord(df[i])
        #     if value == 0x01:
        #         continue
        #     value *= 3
        #     x1 = left + i * 10
        #     y1 = 255 - value
        #     x2 = x1 + 8
        #     y2 = 255
        #     canvas.create_rectangle(x1, y1, x2, y2, fill='red')
        #     canvas.create_text(x1 + 5, y1 - 5, text=str(i) + ':' + str(value / 3))
        # canvas.create_text(50, 50, text='dis=' + str(dis))
        # canvas.pack()



if __name__ == '__main__':
    main()





# first set up the figure, the axis, and the plot element we want to animate




