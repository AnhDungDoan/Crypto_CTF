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

s.recvuntil('> ')
s.sendline(b'1')

s.recvuntil('Enter your plaintext (in hex): ')
payload2 = int.from_bytes(bytes('gaaaaaaaaaaaaaaa', 'utf-8'), byteorder='big', signed=False)
payload2 ^= (int(a, 16) ^ int(b, 16))
s.sendline(bytes(payload1.encode('utf-8').hex() + hex(payload2)[2:], 'utf-8'))

c = s.recvline().strip().decode('utf-8')[64:96]

s.recvuntil('> ')
s.sendline(b'2')

s.recvuntil('Enter ciphertext (in hex): ')
s.sendline(bytes(a + c, 'utf-8'))

print(s.recvline().strip().decode('utf-8'))