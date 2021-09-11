from Crypto.Util.number import *
import binascii

pads = [b'\x04', b'\x02', b'\x00', b'\x01', b'\x03']

e = 65537

for i in range(len(pads)):
    for j in range(len(pads)):
        msg = pads[j] * (i + 1) + b'TMUCTF' + pads[len(pads) - j - 1] * (i + 1)
        #enc = pow(bytes_to_long(msg), e, n)

for x in pads:
    print(int.from_bytes(b'TMUCTF' + x*3, 'big'))