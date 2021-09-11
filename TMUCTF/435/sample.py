from Crypto.Cipher import AES
from operator import xor
import binascii, sys

KEY_first = "9aF738g9AkI112"
cipher1 = "9e00000000000000000000000000436a" 
cipher2 = "808e200a54806b0e94fb9633db9d67f0"
plain1 = "The message is p"
plain2 = "rotected by AES!"

def decrypt(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, binascii.unhexlify(cipher1))
    return aes.decrypt(cipher)

# iterate through relavent ascii range
for i in range(32, 126):
    for j in range(32, 126):
        key = KEY_first + chr(i) + chr(j)
        dec_plain2 = decrypt(binascii.unhexlify(cipher2),  key)
        if  str(dec_plain2).startswith("r") and str(dec_plain2).endswith('S!'):
            print("decrypted plain2: " + dec_plain2 + " with key: " + key)