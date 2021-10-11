import random

def keygen(ln):
    # Generate a linearly independent key
    arr = [ 1 << i for i in range(ln) ]

    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[j] ^= arr[i]
    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[ln - 1 - j] ^= arr[ln - 1 - i]

    return arr

def gen_keystream(key):
    ln = len(key)
    
    # Generate some fake values based on the given key...
    fake = [0] * ln
    for i in range(ln):
        for j in range(ln // 3):
            if i + j + 1 >= ln:
                break
            fake[i] ^= key[i + j + 1]

    # Generate the keystream
    res = []
    for i in range(ln):
        t = 1
        if t:
            res.append((t, [fake[i], key[i]]))
        else:
            res.append((t, [key[i], fake[i]]))

    # Shuffle!
    random.shuffle(res)

    keystream = [v[0] for v in res]
    public = [v[1] for v in res]
    return keystream, public

def bytes_to_bits(inp):
    res = []
    for v in inp:
        res.extend(list(map(int, format(v, '08b'))))
    return res

def bits_to_bytes(inp):
    res = []
    for i in range(0, len(inp), 8):
        res.append(int(''.join(map(str, inp[i:i+8])), 2))
    return bytes(res)

flag = b"123456789"

flag = bytes_to_bits(flag)

key = keygen(len(flag))

keystream, public = gen_keystream(key)

real = [x[0] for x in public]
fake = [x[1] for x in public]
# print("len =", len(real))

# for x in public:
#     v1, v2 = x[0], x[1]
#     p = v1^v2
#     print(v1, v2, p, p>v1, p<v2)

# for i, r in enumerate(real):
#     for j, f in enumerate(fake):
#         if (r==f):
#             print("found", i, j)

