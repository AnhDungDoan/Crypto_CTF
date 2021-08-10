from Crypto.Util.number import getPrime, bytes_to_long

flag = bytes_to_long(open("flag.txt", "rb").read())

def genkey():
    e = 0x10001 #65537
    p, q = getPrime(256), getPrime(256)
    if p <= q:
      p, q = q, p
    n = p * q
    pubkey = (e, n)
    privkey = (p, q)
    return pubkey, privkey

def encrypt(m, pubkey):
    e, n = pubkey
    c = pow(m, e, n)
    return c

pubkey, privkey = genkey()
c = encrypt(flag, pubkey)

print(pubkey[0])
print(pubkey[1])

hint = pubkey[1] % (privkey[1] - 1)
print('pubkey:', pubkey)
print('hint:', hint)
print('c:', c)
