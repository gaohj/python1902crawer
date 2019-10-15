#encoding:utf-8
import urllib2

#模拟浏览器的访问

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}


url = "http://www.baidu.com"

#创建请求对象

request = urllib2.Request(url,headers=headers)
print request.get_full_url() #http://www.baidu.com
print request.get_method() #GET
print request.get_header('User-Agent') #因为是模拟 这里返回None
print request.get_host() #www.baidu.com
print request.get_type() #http

#增加请求头数据
request.add_header("Connection","Keep-Alive")
print request.get_header("Connection")
#发送请求 得到响应
response = urllib2.urlopen(request)
# print response.read()
print response.code #200