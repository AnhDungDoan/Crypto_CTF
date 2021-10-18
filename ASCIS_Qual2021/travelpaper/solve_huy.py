from pwn import *
import qrtools
import os
import pyscreenshot as ps

r = remote('125.235.240.166', 20123)

def qr_recive():
    qr = b''
    while not b'ID Number:' in qr:
        qr += r.recv()
    print(qr.decode('utf8'))

def qr_decode():
    # invert color
    os.system('convert qr.png -channel RGB -negate qr.png')

    qr = qrtools.QR()
    qr.decode('qr.png')
    return qr.data.split('|')

def screenshot():
    im = ps.grab()
    im.save('qr.png')

for i in range(100):

    qr_recive()
    screenshot()

    data = qr_decode()

    r.sendline(data[0])
    print(r.recv())

    r.sendline(data[1])
    print(r.recv())

    r.sendline(data[2])
    print(r.recvline())