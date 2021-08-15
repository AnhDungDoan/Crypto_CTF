import string 

flag = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = bytes.fromhex(flag)

ALPHABET = string.ascii_lowercase

print(type(flag[1]))

for _ in range(256):
    new = ''.join(chr(ord(c) ^ _) for c in flag)
    print(new)

