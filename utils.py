# -*- coding:utf-8 -*-

import crcmod

def encode_dict(d):
    for k in d:
        if isinstance(d[k], basestring):
            d[k] = d[k].encode('utf-8')

def crc16_modbus(data):
    crc_modbus = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    return crc_modbus(data)

