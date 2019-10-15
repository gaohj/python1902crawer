#encoding:utf-8

import urllib.parse

url = "http://www.qfedu.com/s?wd=美女&usrname=扛把子#666"

result1 = urllib.parse.urlparse(url)
result2 = urllib.parse.urlsplit(url)

print(result1)
print(result2)

#ParseResult(scheme='http', netloc='www.qfedu.com', path='/s', params='', query='wd=美女&usrname=扛把子', fragment='666')
#SplitResult(scheme='http', netloc='www.qfedu.com', path='/s', query='wd=美女&usrname=扛把子', fragment='666')
print('scheme:',result1.scheme)
print('netloc:',result1.netloc)
print('path:',result1.path)
print('params:',result1.params)
print('query:',result1.query)
print('fragment:',result1.fragment)