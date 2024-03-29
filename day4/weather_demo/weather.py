import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar

DATA = []
def parse_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')

    #pip install html5lib
    soup = BeautifulSoup(text,'html5lib')

    conMidtab = soup.find('div',class_='conMidtab')
    tables  = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        # print(type(trs))
        # for tr in trs:
        #     tds = tr.find_all('td')
        #     # print(tds[0].stripped_strings)
        #     city_td = tds[0]
        #     city = list(city_td.stripped_strings)[0]
        #     # print(city) #现在的城市容易出现山西 河北 内蒙古 这些名字需要过滤掉
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            # print(tds[0],index)
            #去除 河北 内蒙古 安徽 山东省的名字
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            # print(city)
            temp_td = tds[-5]
            max_temp = int(list(temp_td.stripped_strings)[0])
            DATA.append({'city':city,'max_temp':max_temp})
def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]

    for url in urls:
        parse_page(url)
    DATA.sort(key=lambda data: data['max_temp'],reverse=True)
    data = DATA[0:10]
    print(data)
    cities = list(map(lambda x: x['city'],data))
    max_temp = list(map(lambda x: x['max_temp'],data))
    # max_temp = [10,20,30]
    bar = Bar()
    bar.add_xaxis(cities)
    bar.add_yaxis("全国最高气温排行榜", max_temp)
    bar.render('temperature.html')

if __name__ == "__main__":
    main()
    # DATA = [
    #     {'city':'武汉','max_temp':29},
    #     {'city':'襄阳','max_temp':23},
    #     {'city':'鄂州','max_temp':25}
    # ]
    #
    # DATA.sort(key=lambda data:data['max_temp'])
    # print(DATA[0:2])

