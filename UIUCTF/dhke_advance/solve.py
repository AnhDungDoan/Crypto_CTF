# from pwn import *

# s = remote('dhke-adventure.chal.uiuc.tf', 1337)
# s.recvuntil("I'm too lazy to find parameters for my DHKE, choose for me.")
# s.recvuntil('Enter prime at least 1024 at most 2048 bits: ')
# prime = b"144935329122152680186138252237473770018578950456553603071441970111313468078396452257034847545422558652928479029350293156347368544808458276474430227346509687411021961839628712413474320257929323014885402808010273619648178969999765065072964519839281514130168855934342211867236627154482536604050291690856680382121"
# s.send(prime)

# s.recvuntil("Dio sends: ")
# dio = s.recv() # dio = pow(g,a,p)
# s.recvuntil("Jotaro sends: ")
# jotaro = s.recv() #jotaro = pow(g,b,p)

# s.recvuntil("Ciphertext: ")
# ciphertext = s.recv()
from random import randint
from Crypto.Util.number import isPrime
from Crypto.Cipher import AES
from hashlib import sha256

key = 10
key = sha256(str(key).encode()).digest()
print(len(str(key)))
print(key)
