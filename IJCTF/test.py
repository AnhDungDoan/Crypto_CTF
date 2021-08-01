#!/usr/local/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import *
import binascii
import os

#print(binascii.unhexlify(input("Enter ciphertext (in hex): ")))
# pt1 = "aaaaaaaaaaaagimm".encode("utf-8").hex()
# pt2 = "ieflagaaaaaaaaaa".encode("utf-8").hex()

# pt2 = [chr(ord(a) ^ ord(b)) for a,b in zip(pt1, pt2)]

# print(pt2.hex())
print("aaaaaaaaaagimmie".encode("utf-8").hex())
print("aagimmie aaaaaaaa flagaaaa".encode("utf-8").hex()) 
#print(b"gimmieflag" in b"gimmieflag")

#print(b'gimmieflag' in b"gimmieflag")

# key = b'1234567890123456'
# iv = b'1234567890123456'

# data = b'gimmieflag123456'
# cipher = AES.new(key, AES.MODE_CBC, iv)

# print(binascii.hexlify(cipher.encrypt(pad(data, 16))))#.decode())

# print((b'767a171a831da2ffe0276461b6855cbb6900c0c26a44ede98538cd960c2ad3a8').decode())

# print(cipher.encrypt(data).hex())

