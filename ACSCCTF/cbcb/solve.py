import base64
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

data = {"username": "gnud", "is_admin": True}

token = "gZfGlV48HsiORXDnwGe5QMm1YF8cjREX2/hdxvQ9sE/y5vCMBzPKFtVB5kk1R77tH0uQTi1NZM2zfXUudsW1fqDVcSGKK3rx+L1N6CQ9jrU="

token = base64.b64decode(token)
print(token[:16])
print(token[16:16*2])