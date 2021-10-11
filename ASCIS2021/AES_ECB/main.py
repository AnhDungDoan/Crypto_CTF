import requests

BASE_URL = 'http://125.235.240.166:20104/'

flag = "ASCIS{AES_ECB_is_the_best_crypto"
print(len(flag))

for i in range(32, 64):
    for ichar in range(33,127):
        # get 
        r = requests.get(BASE_URL)

        # post
        char = chr(ichar)
        a = "a"*(64-i - 1) + flag + char + "a"*(64-i - 1)
        enc = a.encode().hex()
        data = {'input': enc}

        r = requests.post(BASE_URL + 'encrypt', data=data)
        getback = r.text
        if (getback[:128] == getback[128:256]):
            flag+=char
            print(flag)
            break
