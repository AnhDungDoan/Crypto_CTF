import math

p = 26513
q = 32321

for v in range(100000):
    if ((1-q*v) % p == 0):
        print("v = ", v, "u = ", (1-q*v)//p)

print(math.gcd(p,q))
print(q*18109-22076*p)