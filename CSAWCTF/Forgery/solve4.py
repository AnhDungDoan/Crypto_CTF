import binascii
import string
import gmpy2
import sys

from Crypto.Util.number import long_to_bytes
file1 = open('pokemon.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
a = []
for line in Lines:
    a.append(line.strip('\n'))

print(a)