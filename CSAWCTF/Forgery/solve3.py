import owiener
from Crypto.Util.number import *
import gmpy2

f = open("omg.txt", "r")
lines = f.readlines()
i = 0
n = []
c = []
remain_n = []
u = []
e = 17

for line in lines:
    if (i % 2 == 0):
        n.append(int(line))
    else:
        c.append(int(line))
    i+=1

N = 1
for temp_n in n:
    N = N * temp_n

for temp_n in n:
    remain_n.append(N//temp_n)

for i in range(len(remain_n)):
    #tu = gmpy2.invert(remain_n[i], n[i])
    tu = inverse(remain_n[i], n[i])
    u.append(tu)

M = 0
for i in range(len(remain_n)):
    if (u[i] != 0):
        tmp = (c[i]*u[i]*remain_n[i]) %N
        M = (M + tmp) %N 

count = 0
for i in range(len(n)):
    if (u[i] != 0):
        count += 1
        print(M % n[i] == c[i])
    #print(u[i])

m, check = gmpy2.iroot(M, e)
if (check):
    print(long_to_bytes(m))

print(count)


