import random, sys
from Crypto.Util.number import long_to_bytes

def bxor(ba1,ba2):
	return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


#ran = random.seed(51244664924293845115576096916550700677)
flag = bytearray.fromhex("f00128738e0088f30852ac90af5c97f659ca54413e7009a95412b48762c8f6")

for i in range(100):
    random.seed(51244664924293845115576096916550700677)
    print(bxor(flag, long_to_bytes(random.getrandbits(i*8))))    

#print(bxor(flag, long_to_bytes(random.getrandbits(len(flag)*8))).hex())