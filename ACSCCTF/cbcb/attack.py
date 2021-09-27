from base64 import b64encode, b64decode
from string import printable
from pwn import *

# tube = process("./cbcbc.py")
with process("./cbcbc.py") as tube:
# with remote("cbcbc.chal.acsc.asia", 52171) as tube:
  print(tube.recvuntil(b"=====================================================").decode())
  print(tube.recvuntil(b"3. Exit").decode())
  tube.recv()
  tube.sendline(b"1")
  tube.recv()
  tube.sendline(b"")
  tube.recvline()
  target_token = b64decode(tube.recvline().strip())

  print("Target token", target_token)

  iv1 = target_token[:16]
  iv2 = target_token[16:32]
  enc = target_token[32:]

  enc = enc[:16]
  fail_msg = b"Failed to login! Check your token again"

  def query(iv1: bytes, iv2: bytes, enc: bytes) -> bool:
    token = iv1 + iv2 + enc
    token = b64encode(token)
    tube.recvuntil(b"3. Exit")
    tube.sendline(b"2")
    tube.recv()
    tube.sendline(b"mugi")
    tube.recv()
    tube.sendline(token)
    res = tube.recvline()
    return fail_msg not in res


  ans = bytearray(b"\0" * 16)
  for i in range(15, -1, -1):
    for c in range(256):
      if chr(c ^ (16 - i)) not in printable:
        continue
      new_iv1 = bytearray(iv1)
      new_iv1[i] ^= c
      for j in range(i + 1, 16):
        new_iv1[j] ^= (16 - i) ^ ans[j]
      if query(new_iv1, iv2, enc):
        ans[i] = (c ^ (16 - i))
        break
    print(ans)