import requests
import random


ua_lists = [
    "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "User-Agent,Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
]

ua_list = random.choice(ua_lists)
headers = {
    'User-Agent':ua_list
}
ip_lists = [
    {'http':"125.94.44.129:1080"},
    {'http':"183.234.241.105:8118"},
    {'http':"14.29.232.142:8082"}
]

ip_list = random.choice(ip_lists)

url = 'http://httpbin.org/ip'
response = requests.get(url,headers=headers,proxies=ip_list)

print(response.content.decode('utf-8'))
