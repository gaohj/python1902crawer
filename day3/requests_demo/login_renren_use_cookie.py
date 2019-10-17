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

url = "http://www.renren.com/541197383/profile"


filename = 'renrencookie.txt'

cookies = cookiejar.LWPCookieJar()
#即使cookie失效 也保存  即使过期也保存
cookies.load(filename=filename,ignore_discard=True,ignore_expires=True)
cookie_jar = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(cookie_jar)
urllib.request.install_opener(opener)


req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode())

