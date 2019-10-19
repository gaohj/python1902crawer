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
    # requests库模式采用 猜测的编码将抓取下来的内容进行解码 然后存储到text属性上面
    # 如果猜错产生乱码
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
    # print(detail_urls)
    return detail_urls


#获取电影url后  进入获取电影详情信息
#参数为 https://www.dytt8.net/html/gndy/dyzz/20190628/58771.html
def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=headers)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title
    Zoom = html.xpath("//div[@id='Zoom']")[0]
    imgs = Zoom.xpath(".//img/@src")
    cover = imgs[0]
    screenshoot = imgs[1]
    movie['cover'] = cover
    movie['screenshoot'] = screenshoot
    infos = Zoom.xpath(".//text()")

    def parse_info(info,rule):
        return info.replace(rule,"").strip()
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print("="*50)
        if info.startswith("◎年　　代"):
            # info = info.replace("◎年　　代","").strip()
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演") #只能拿到第一个主演
            #用一个列表存储所有的演员
            actors = [info] #将第一个演员先放进去
            # print(len(infos))
            #从第一个演员索引的下一个开始截取直到最后的infos
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"): #遇到下一个◎结束
                    break
                actors.append(actor)
                # print(actors)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介") #只能拿到第一行简介
            for x in range(index+1,len(infos)): #从第一行截取到最后
                profile = infos[x].strip()
                if profile.startswith("【下载地址】") or profile.startswith("◎获奖情况"):
                    break
                # print(profile)
                movie['profile'] = profile

    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie
#起始页 入口方法
def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,8):
        url = base_url.format(x)
        detail_urls = get_detail_url(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
    print(movies)

if __name__ == "__main__":
    spider()