# -*- coding:utf-8 -*-

from serial import Serial
import binascii
import struct
from Tkinter import *
import threading
import time

def main():
    root = Tk()
    threading.Thread(target=collector, args=(root,)).start()
    root.mainloop()


def collector(root):
    canvas = Canvas(root, width=1260, height=260, bg = "white")
    serial = Serial('com6', 57600, timeout=4)
    count = 0
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
        canvas.delete("all")
        left = 0
        for i in range(0, 126):
            value = ord(df[i])
            if value == 0x01:
                continue
            value *= 3
            x1 = left + i * 10
            y1 = 255 - value
            x2 = x1 + 8
            y2 = 255
            canvas.create_rectangle(x1, y1, x2, y2, fill='red')
            canvas.create_text(x1 + 5, y1 - 5, text=str(i) + ':' + str(value / 3))
        canvas.create_text(50, 50, text='dis=' + str(dis))
        canvas.pack()



if __name__ == '__main__':
    main()
