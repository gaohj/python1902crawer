import requests
import urllib.request
import random
ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]
ua_list = random.choice(ua_list)

headers = {
    'User-Agent':ua_list
}

url = "http://www.b5200.net/u/login.htm"

data = {
    "autologin":1,
    "autoLogin":1,
    "name":"jiabinxiong",
    "password":"B7DFE9134C7A717A3B6EAF37BDC1EF7B",
}

session = requests.session() #保存会话信息
response = session.post(url=url,headers=headers,data=data)

print(response.content.decode('utf-8'))

print("*" * 30)
url = "http://www.b5200.net/bookcase.php"
#urllib 取消ssl证书验证
# urllib.request.Request(url=url,headers=headers,unverifiable=False)
#requests库忽略方式
response = session.get(url=url,headers=headers,verify=False)
print(response.content.decode('gbk'))
