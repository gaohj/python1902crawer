import random
import urllib.request
import urllib.parse
from http import cookiejar

ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]
ua_list = random.choice(ua_list)

headers = {
    'User-Agent':ua_list
}

url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20199410460"

data = {
    "f":"",
    "icode":"",
    "rkey":"00de0309607d2424dc154f5b5f5a9f6d",
    "key_id":"1",
    "password":"833df4914709457db7c002d1351b6ac18d3a22485c4247ff8d11ff3985af615b",
    "email":"gaohj5@163.com",
    "origURL":"http://www.renren.com/home",
    "domain":"renren.com",
    "autoLogin":"true",
    "captcha_type":"web_login"
}

filename = 'renrencookie.txt'

cookies = cookiejar.LWPCookieJar(filename=filename)
cookie_jar = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(cookie_jar)
urllib.request.install_opener(opener)

data = urllib.parse.urlencode(data).encode()
req = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode())

cookies.save()
