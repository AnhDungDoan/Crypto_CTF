from pwn import *
import base64
import sys
import os
from Crypto.Cipher import AES

flag_key = '\xf0\xc0*\xde\x91\xac\xef\xf2\x93r\xfd\x1c\xde(\xeaL\x98o\xff?U\xf1\x00;\x97\xd4\xe42E;\xd9\x82\x9b\xc5\xd6v\x11\xb0%\xbd\xd9\xfc\x95\x98\xd8ik\x95'

# p = connect("pwn-2021.duc.tf", 31914)

# key = '!_SECRETSOURCE_!'
p.recvuntil(b'AES-128')

for i in range(16):
    for j in range(33,127):
        p.recvuntil(b'Enter plaintext:')
        p.recvuntil(b'\n')
        char = chr(j)
        text = char + key + '0'*16
        p.sendline(text.encode())
        code = p.recvline()
        code = base64.b64decode(code)
        c1,c2,c3 = code[32:48], code[48:64], code[64:80]
        #p.recvline()
        if (c1 == c3):
            key = char+key
            print(key)
            break

# print("key: ", key) 
flag = b'DUCTF{asdasdasd1234567898765432}'
key =   b'!_SECRETSOURCE_!'
def main():
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(flag)
    res = base64.b64encode(ct).decode('utf-8')
    return res


flag = "8MAq3pGs7/KTcv0c3ijqTJhv/z9V8QA7l9TkMkU72YKbxdZ2EbAlvdn8lZjYaWuV"

print(base64.b64decode(flag))

cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.decrypt(base64.b64decode(flag))
print(enc)


