from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(101):

    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    encoding = received["type"]
    challenge_words = received["encoded"]

    if encoding == "base64":
        decoded = base64.b64decode(challenge_words.encode()).decode() # wow so encode
    elif encoding == "hex":
        decoded = bytearray.fromhex(challenge_words).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(challenge_words, 'rot_13')
    elif encoding == "bigint":
        decoded = long_to_bytes(int(challenge_words.encode(), 0)).decode('utf-8')
    
    elif encoding == "utf-8":
        decoded = ''.join(chr(b) for b in challenge_words)

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)

    #json_recv()
