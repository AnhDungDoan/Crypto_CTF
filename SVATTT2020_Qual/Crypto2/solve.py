from bitarray import bitarray

flag = "ahihi"

a = bitarray()

a.frombytes(flag.encode())
print(a)