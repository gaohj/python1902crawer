import urllib.request
import random

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}

ip_list = [
    {"http": "http://58.253.156.236:9999"},
    {"http": "http://120.83.108.103:9999"},
    {"http": "http://120.234.138.101:53779"},
    {"http": "http://163.125.115.186:8118"},
]



ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]

proxy = random.choice(ip_list)
print(proxy)
#创建代理句柄
proxy_handler = urllib.request.ProxyHandler(proxies=proxy)

#使用代理句柄创建打开器
opener = urllib.request.build_opener(proxy_handler)

url = "http://httpbin.org/ip"

req = urllib.request.Request(url,headers=headers)

req.add_header('User-Agent',random.choice(ua_list))

resp = opener.open(req)

print(resp.read())

