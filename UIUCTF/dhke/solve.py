import random
from Crypto.Cipher import AES

padding = "uiuctf2021uiuctf2021"

cip = bytes.fromhex("b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6")

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
for x in range(28):
    i = 0
    key = ''
    while (16 - len(key) != len(str(x))):
        key = key + padding[i]
        i += 1
    
    key = key + str(x)
    key = bytes(key, encoding='ascii')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    enc = cipher.decrypt(cip)
    print(enc)

