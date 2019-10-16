from urllib import request

url = 'http://httpbin.org/ip'

resp = request.urlopen(url)
# print(resp.read())

#使用代理
url1 = 'http://httpbin.org/ip'
#创建一个代理句柄
handler = request.ProxyHandler({"http":"120.25.212.26:8118"})

#使用代理句柄创建一个打开器
opener = request.build_opener(handler)
#用打开器 发送请求
res = opener.open(url1)
print(res.read())