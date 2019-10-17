import requests

# response = requests.get('http://httpbin.org/ip')
# # # print(type(response.text))
# # print(response.text)
# # print(response.content.decode('utf-8'))

kw = {'wd':'python'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

response = requests.get(url="http://www.baidu.com/s?",params=kw,headers=headers)
# print(type(response.text)) #Unicode格式数据
# print(response.content.decode('utf-8')) #字节流数据
#
# print(response.url)#http://www.baidu.com/s?wd=python

print(response.encoding) #utf-8

print(response.status_code) #200


