import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import binascii

def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

def encrypt(plainbytes, key):
    
    iv = Random.new().read(AES.block_size)
    
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    cipherbytes = cipher.encrypt(plainbytes)

    ciphertext = base64.b64encode(iv + cipherbytes)

    return ciphertext

# input: base64 text, output: bytes
def decrypt(ciphertext, key):

    cipherbytes = base64.b64decode(ciphertext)

    iv = cipherbytes[:AES.block_size]

    cipher = AES.new(key, AES.MODE_CFB, iv)

    plainbytes = cipher.decrypt(cipherbytes[AES.block_size:])

    return plainbytes

user = [422, "dr00py1234567", "dr00py", "dr00py1@gmail.com", b'ZG9hbmFuaGR1bmcxMjM0NQ==', 1]

userid = user[0]
username = user[1]
role = user[5]

key = base64.b64decode(user[4])

usernamebytes = username.encode('utf-8')
usernamelen = len(usernamebytes)
plainbytes = len(usernamebytes).to_bytes(2, "little") + usernamebytes + role.to_bytes(1, "little")

#plainbytes1 = len(usernamebytes).to_bytes(2, "little") + usernamebytes + role.to_bytes(0, "little")
plainbytes1 = b'\r\x00dr00py1234567\x00'

# print("plaintext = ", plainbytes)
# print("len = ", len(plainbytes))

# ciphertext = encrypt(plainbytes, key)

# print(ciphertext)

authtoken = "hBlIJVgM/brypR2GoA0xs3MEyRUuyesjltZ58mkVaNI="
tokenarray = base64.b64decode(authtoken)
iv = tokenarray[:16]
cipherbytes = tokenarray[16:]

print("iv =", iv)
print("cipher =", cipherbytes)

new_cipher = xor(xor(plainbytes, cipherbytes), plainbytes1)
print("cipher =", new_cipher)
print(base64.b64encode(iv+new_cipher))

# thay cookie => solve

