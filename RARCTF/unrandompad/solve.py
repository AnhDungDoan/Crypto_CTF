from pwn import *
from gmpy2 import *

p = remote('193.57.159.27', 65532)
#p.interactive()

p.recvuntil('e: ')
e = p.recv()

p.recvuntil('n: ')
n = p.recv()

p.sendline(b'2')
p.recvuntil('c: ')
c = p.recv()

for i in range(1000):
    tmp = c+n*i
    flag = gmpy2.iroot(tmp, e)
    print(flag)
