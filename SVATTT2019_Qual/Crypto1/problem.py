#!/usr/bin/env python3
from Crypto.Util.number import getPrime, inverse
SUFFIX = bytes.fromhex('2019')

def sign(message, private_key):
    m = int.from_bytes(message + SUFFIX, 'big')
    s = pow(m, private_key['d'], private_key['n'])
    return s.to_bytes((private_key['n'].bit_length()+7)//8, 'big')

def verify(signature, message, public_key):
    m = int.from_bytes(message + SUFFIX, 'big')
    s = int.from_bytes(signature, 'big')
    return pow(s, public_key['e'], public_key['n']) == m


if __name__ == '__main__':
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    e = 65537
    d = inverse(e, (p-1)*(q-1))
    private_key = {'n': n, 'e': e, 'd': d}
    public_key = {'n': n, 'e': e}
    print(public_key)
    message = bytes.fromhex(input())
    if b'cat flag' != message:
        signature = sign(message, private_key)
        print(signature.hex())
    else:
        print('Nope!')

    message = bytes.fromhex(input())
    signature = bytes.fromhex(input())

    # is this possible?
    if verify(signature, message, public_key) and message == b'cat flag':
        print(open('flag.txt').read())