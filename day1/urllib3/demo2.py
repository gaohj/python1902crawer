import urllib.request
import urllib.parse

params = {'name':'张三','age':18,'greet':'helloworld'}

result = urllib.parse.urlencode(params)
#name=%E5%BC%A0%E4%B8%89&age=18&greet=helloworld
print(result)