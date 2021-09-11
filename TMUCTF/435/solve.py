import binascii
import hashlib
import sys
from Crypto.Cipher import AES

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

c = b"9**********b4381646*****01********************8b9***0485******************************0**ab3a*cc5e**********18a********5383e7f**************1b3*******9f43fd66341f3ef3fab2bbfc838b9ef71867c3bcbb"
fc = binascii.unhexlify(c[-42:])
key = '*XhN2*8d%8Slp3*v'
key_len = len(key)

h = hashlib.sha256(bytearray(key.encode())).hexdigest()
hidden = binascii.unhexlify(h)[:10]
message = b'CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption' + hidden

ct2 = fc[-16:]
ct1 = "************1b3*******9f43fd6634"
ct1 = ct1.replace("*","0")

def decrypt(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, binascii.unhexlify(ct1))
    return aes.decrypt(cipher)

def pad(message):
    padding = bytes((key_len - len(message) % key_len) * chr(key_len - len(message) % key_len), encoding='utf-8')
    return message + padding

# find key
# for cp1 in range(32,126):
#     for cp2 in range(32,126):
#         for cp3 in range(32,126):
#             p1 = chr(cp1)
#             p2 = chr(cp2)
#             p3 = chr(cp3)
#             fkey = key.replace('*', p1,1)   
#             fkey = fkey.replace('*', p2,1) 
#             fkey = fkey.replace('*', p3,1) 
#             byte_key = bytearray(fkey.encode())

#             h = hashlib.sha256(byte_key).hexdigest()
#             hidden = binascii.unhexlify(h)[:10]
#             message = b'CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption' + hidden
#             message = pad(message)
#             #print(byte_key)
#             dec_plain2 = decrypt(ct2, byte_key)
#             if (dec_plain2.endswith(message[-3:])):
#                 print(str(dec_plain2))
#                 print(fkey)

KEY = b"0XhN2!8d%8Slp3Ov"
h = hashlib.sha256(KEY).hexdigest()
hidden = binascii.unhexlify(h)[:10]
message = b'CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption' + hidden
message = pad(message)

def decrypt2(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, message[-16:])
    return aes.decrypt(cipher)
    
def decrypt3(cipher, passphrase, i):
    aes = AES.new(passphrase, AES.MODE_CBC, message[-16*i:-16*(i-1)])
    return aes.decrypt(cipher)

cipher1 = decrypt2(ct2, KEY)
ans = binascii.hexlify(cipher1)
for i in range(2, len(message)//16):
    ct2 = cipher1
    cipher1 = decrypt3(ct2, KEY, i)
    ans = binascii.hexlify(cipher1) + ans 

def decrypt_end(cipher, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, message[:16])
    return aes.decrypt(cipher)

cipher1 = b"9f4ac903118b43816462b35101a7b6fe"
print(decrypt_end(binascii.unhexlify(cipher1), KEY))


