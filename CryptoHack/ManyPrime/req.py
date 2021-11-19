import requests

url = "https://shcd.ueh.edu.vn/login/index.php"

obj = {"username": "aaaa", "password": "aaaa"}

x = requests.get(url=url, data=obj)
print(x.text)