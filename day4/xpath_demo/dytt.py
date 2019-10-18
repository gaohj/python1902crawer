import requests
from lxml import etree
BASE_URL = 'https://www.dytt8.net'
headers = {
    "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Referer":"https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
}
#获取每一页中的 电影 url
#参数为 https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
def get_detail_url(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # print(detail_urls)
    # def a(url):
    #     return BASE_URL+url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = a(detail_url)
    #     detail_urls[index] = detail_url
    #     index+=1
    detail_urls = list(map(lambda url:BASE_URL+url,detail_urls))
    print(detail_urls)


#获取电影url后  进入获取电影详情信息
#参数为 https://www.dytt8.net/html/gndy/dyzz/20190628/58771.html
def parse_detail_page(url):
    pass

#起始页 入口方法
def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,8):
        url = base_url.format(x)
        detail_urls = get_detail_url(url)
        # for detail_url in detail_urls:
        #     movie = parse_detail_page(detail_url)
        #     movies.append(movie)
    # print(movies)

if __name__ == "__main__":
    spider()