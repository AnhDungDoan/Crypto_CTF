from Crypto.Util.number import *

psize = 24
count = 25
primes = [8412883, 8889941, 9251479, 9471269, 9503671, 9723401, 10092149, 10389901, 10551241, 10665527, 11099951]
shadow = [0, 7832917, 8395798, 4599919, 154544, 3430534, 4694683, 123690, 5911445, 7380167, 10597668]

threshold = 11

M = [0 for i in range(11)]
flag = 0
mmax = 1
for i in range(1,threshold):
    mmax = mmax * primes[i]

pmax = 1
for i in range(11):
    pmax = pmax * primes[i]

for i in range(1,threshold):
    M[i] = mmax // primes[i]
    y = inverse(M[i], primes[i])
    flag = flag + (shadow[i] * y * M[i])
    flag = flag % mmax

print(flag)
print(long_to_bytes(flag))
print(mmax)

print('pmax =',pmax)

for i in range(1,threshold):
    print(flag % primes[i])

for i in range(10000000):
    if (b'CTF' in long_to_bytes(flag + i*mmax)):
        print(long_to_bytes(flag + i*mmax))








