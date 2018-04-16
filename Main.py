# -*- coding:utf-8 -*-

from serial import Serial
import binascii
import struct

def main():
    serial = Serial('/dev/ttyUSB0', 57600, timeout=4)
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
        data = data.replace('\x01', '\x11')
        print binascii.hexlify(data)
        dis, df = struct.unpack('>H126s', data[0:128])
        # print df

if __name__ == '__main__':
    main()
