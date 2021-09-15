from pwn import *
from Crypto.Util.number import *

N = 0
e = 0
c = 0

def receive():
    f.recvuntil(b"N = ")
    N = int(f.recvline().decode('utf-8').strip("\r\n"))
    f.recvuntil(b"e = ")
    e = int(f.recvline().decode('utf-8').strip("\r\n"))
    f.recvuntil(b"c = ")
    c = int(f.recvline().decode('utf-8').strip("\r\n"))
    return N, e, c
    
    

f = remote("crypto.chal.csaw.io", 5008)
f.recvuntil(b"Part 1 --> This is one of the most common RSA attacks in CTFs!")
#f.interactive()
N, e, c = receive()
f.recvuntil(b"What is the plaintext?") 
f.sendline(b"Wiener wiener chicken dinner")
f.recvuntil(b"Success!")

f.recvuntil(b"Part 2 --> Sexy primes were used to make the modulus!")
N, e, c = receive()
f.recvuntil(b"What is the plaintext?") 
f.sendline(b"Who came up with this math term anyway?")
f.recvuntil(b"Success!")

f.recvuntil(b"Part 3 --> Looks like there is a oracle which is telling the LSB of the plaintext. That will not help you, right?")
N, e, c = receive()
#f.interactive()
e = 65537
upper_limit = N
lower_limit = 0

flag = ""
for i in range(1, 1025):
    chosen_ct = (c*pow(2**i, e, N)) % N
    f.recvuntil(b"What would you like to decrypt? (please respond with an integer)")

    f.sendline(str(chosen_ct).encode('utf-8'))
    f.recvuntil(b"The oracle responds with: ")
    output = int(f.recvline().decode('utf-8').strip("\r\n"))
    
    if output == 0:
        upper_limit = (upper_limit + lower_limit)//2
    elif output == 1:
        lower_limit = (lower_limit + upper_limit)//2
    #i += 1
    f.recvuntil(b"Would you like to continue? (yes/no)")
    #f.interactive()
    f.sendline(b"")
# Wiener wiener chicken dinner
# Who came up with this math term anyway?
# Totally did not mean to put an oracle there

flag = long_to_bytes(lower_limit)
flag2 = long_to_bytes(upper_limit)
f.recvuntil(b"Would you like to continue? (yes/no)")
f.sendline(b"no")
f.recvuntil(b"What is the plaintext?")
f.sendline(flag)
f.interactive()