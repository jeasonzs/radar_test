# -*- coding:utf-8 -*-

from serial import Serial
import binascii
import struct
from Tkinter import *
import threading
import time

def main():
    root = Tk()

    canvas = Canvas(root, width=1260, height=260, bg = "white")
    threading.Thread(target=collector, args=(canvas,)).start()



    root.mainloop()


def collector(canvas):
    # while True:
    #     canvas.create_rectangle(10, 10, 110, 110, fill='red')
    #     canvas.pack()
    #
    #     canvas.create_rectangle(120, 120, 210, 210, fill='blue')
    #     canvas.pack_forget()
    #     time.sleep(1)

    serial = Serial('/dev/ttyUSB0', 57600, timeout=4)
    cnt = 0
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
        # print binascii.hexlify(df)
        cnt += 1
        # if cnt % 10 == 0:
        #     continue
        canvas.create_rectangle(0, 0, 1260, 260, fill='white')
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
        canvas.pack()

if __name__ == '__main__':
    main()
