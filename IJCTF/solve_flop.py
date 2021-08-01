from pwn import *

s = remote('chal.imaginaryctf.org', 42011)

s.recvuntil('> ')
s.sendline(b'1')

s.recvuntil('Enter your plaintext (in hex): ')
payload1 = 'aaaaaaaagimmefla' + 'aaaaaaaaaaaaaaaa'
s.sendline(bytes(payload1.encode('utf-8').hex(), 'utf-8'))

d = s.recvline().strip().decode('utf-8')[:64]

a = d[:32]
b = d[32:]

payload2 = int('gaaaaaaaaaaaaaaa'.encode('utf-8').hex(), 16)
payload2 ^= (int(a, 16) ^ int(b, 16))

payload2 = hex(payload2)

s.recvuntil('> ')
s.sendline(b'1')
s.recvuntil('Enter your plaintext (in hex): ')

s.sendline(bytes(payload1.encode('utf-8').hex() + payload2[2:], 'utf-8'))

e = s.recvline().strip().decode('utf-8')
e = e[64:96]

s.recvuntil('> ')
s.sendline(b'2')
s.recvuntil('Enter ciphertext (in hex): ')

s.sendline(bytes(a + e, 'utf-8'))

flag = s.recvline()
print(flag)


