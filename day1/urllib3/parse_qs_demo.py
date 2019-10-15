#wd=%E7%BE%8E%E5%A5%B3&oq=%25E7%25BE%258E%25E5%25A5%25B3

import urllib.parse

# qs = "wd=%E7%BE%8E%E5%A5%B3&oq=%25E7%25BE%258E%25E5%25A5%25B3"
# print(urllib.parse.parse_qs(qs))

params = {'name':'扛把子','age':'18','greet':'我喜欢你，你要是不喜欢我，把这四个字还给我'}
qs = urllib.parse.urlencode(params)
print(qs)
result = urllib.parse.parse_qs(qs)
print(result)