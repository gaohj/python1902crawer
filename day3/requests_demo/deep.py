import requests
import random
import re
ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]
ua_list = random.choice(ua_list)

headers = {
    'User-Agent':ua_list
}

#获取页面内容
def get_html(url):
    try:
        res = requests.get(url,headers=headers)
        return res.text
    except:
        return ""

def get_son_url(url):
    #获取网页源代码
    html = get_html(url)
    #获取所有的 href
    href_re = '<a .*?href="(.*?)".*?>'
    href_list = re.findall(href_re,html,re.S)
    return href_list

def deep_crawer(url):
    if deep_dict[url] > 3:
        return
    print("*"*100)
    print("\t"*deep_dict[url],"当前层级为:%d" % deep_dict[url])
    print("*"*100)
    son_url_list = get_son_url(url)
    for son_url in son_url_list:
        #过滤有效链接  http开头就是有效链接
        if son_url.startswith('http') or son_url.startswith('https'):
            if son_url not in deep_dict:
                deep_dict[son_url] = deep_dict[url]+1
                deep_crawer(son_url)




if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=岛国" #起始页

    deep_dict = {} #层级控制
    deep_dict[url] = 1
    deep_crawer(url)
