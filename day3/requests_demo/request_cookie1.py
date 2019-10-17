import requests


response = requests.get("http://www.baidu.com")

cookiejar = response.cookies #返回的就是cookiejar对象

print(cookiejar) #<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
#将cookiejar 转成字典
cookie_dict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookie_dict) #{'BDORZ': '27315'}
