import requests
import re

BASE_URL = 'https://cat-step.disasm.me/'

r = requests.get(BASE_URL)

realflag = "spbctf{"


for i in range(7, 36):
    for ichar in range(33,127):
        char = chr(ichar)
        fake_flag = realflag+char+ "`"*(35-i)
        data = {'flag': fake_flag}
        r = requests.post(url=BASE_URL, data=data)
        num = re.findall('\d+', r.text)[0]
        #print(num)
        if (int(num) == 35-i):
            realflag += char
            print(realflag)
            break

        

