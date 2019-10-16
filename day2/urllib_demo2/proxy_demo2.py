import urllib.request
import random

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}

ip_list = [
    {"http":"115.213.166.147:4223"},
    {"http":"115.213.167.2:4223"},
    {"http":"115.230.10.16:4223"},
]


ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]

proxy = random.choice(ip_list)
#创建代理句柄
proxy_handler = urllib.request.ProxyHandler(proxies=proxy)

#使用代理句柄创建打开器
opener = urllib.request.build_opener(proxy_handler)

url = "http://www.baidu.com"

req = urllib.request.Request(url,headers=headers)

req.add_header('User-Agent',random.choice(ua_list))

resp = opener.open(req)
print(resp)

