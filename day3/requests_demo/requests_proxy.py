import requests

import random

ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]

ip_list = [
    {"http":"14.29.232.142:8082"},
    {"http": "163.125.115.186:8118"},
]

ua_list = random.choice(ua_list)

headers = {
    'User-Agent':ua_list
}

ip_list = random.choice(ip_list)

url = 'http://httpbin.org/ip'
response = requests.get(url,headers=headers,proxies=ip_list)
print(response.content.decode('utf-8'))

