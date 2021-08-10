from math import sqrt
from Crypto.Util.number import inverse, isPrime, long_to_bytes
import gmpy2
from gmpy2 import mpz
import sympy.ntheory as nt

e = 65537
n = 8912842104707541079224121570993638329034035020557185210714114116280331668563654252340343535175707016545559295426444501425380705252374715291953292805647003
x = 5809537483591221825791698676543435344983904307115559017255861785856074978503
c = 5602693857490274561954351758894686207136718233429894558090670376857347135713716375407899329216438442496565889380931501145878893257464980086036950145616474
ne = x

# while (True):
#     ne = gmpy2.next_prime(ne)
#     p = n/ne
#     hint = n % (ne-1)

#     if (n % (ne-1) == x):
#         q = ne
#         p = n // q
    
#         phi = (p-1)*(q-1)
#         d = inverse(e, phi)
#         m = pow(c, d, n)
#         print(long_to_bytes(m))
#         break


#print(n/(x*x)) 

# p = gmpy2.next_prime(x)
# while (n > p*p):
#     print(p)
#     p = gmpy2.next_prime(p)
print((n-x) % x == 0)
# p = n/q
# phi = (p-1)*(q-1)
# d = inverse(e, phi)
# m = pow(c, d, n)
# print(long_to_bytes(m))