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

def width_crawer(start_url):
   url_quene = [] #模拟队列
   url_quene.append(start_url) #让起始页先进队列
   while len(url_quene)>0:
        #先处理起始页
        url = url_quene.pop(0)
        print("\t"*deep_dict[url],"当前层级为:%d" % deep_dict[url])
        if deep_dict[url] <=3: #只捕获到第三级
            #获取起始页的子url列表
            son_url_list = get_son_url(url)
            for son_url in son_url_list:
                #过滤出有效链接
                if son_url.startswith('http') or son_url.startswith('https'):
                    if son_url not in deep_dict:
                        #层架控制 子url作为key  层级=父url的层级+1
                        deep_dict[son_url] = deep_dict[url]+1
                        #将子url进入队列
                        url_quene.append(son_url)




if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=岛国" #起始页

    deep_dict = {} #层级控制
    deep_dict[url] = 1
    width_crawer(url)
