#encoding:utf-8
import urllib2


url = "http://www.qfedu.com"
response = urllib2.urlopen(url)
#print response #socket._fileobject object  文件对象
#print response.read() #返回所有的内容  字符串
#print response.readline() #按行读取 默认返回第一行

# while True:
#     if not response.readline():
#         break
#     print response.readline()

print response.readlines() #返回列表