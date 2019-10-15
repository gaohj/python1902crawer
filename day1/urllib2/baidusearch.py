#encoding:utf-8
import urllib
import urllib2
#https://www.baidu.com/s?wd=关键词
def baidu_search(params):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    url = "https://www.baidu.com/s?"+params
    #创建请求对象
    request = urllib2.Request(url=url,headers=headers)

    #发送请求
    response = urllib2.urlopen(request)

    print response.read()


if __name__ == "__main__":
    kw = raw_input("请输入要搜索的内容:")

    params = {"wd":kw}

    #将字典转成字符串
    #urllib 和  urllib2的区别:
    #urllib只能接收url  不能接收设置了header的Request实例
    #urllib库中 提供了 urlencode get查询字符串   urllib2没有
    params = urllib.urlencode(params)
    baidu_search(params)
