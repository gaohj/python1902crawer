import urllib
from urllib import request
# python2    python3
#urllib2 = urllib.request

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}

url = "http://www.baidu.com"

#创建请求对象
req = urllib.request.Request(url=url,headers=headers)

#发送请求 获取返回值  urlopen函数
response = urllib.request.urlopen(req)
# print(response.read()) #二进制
print(response.read().decode('utf-8'))#字符串
# print(response.info()) #服务器给的响应信息

