import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar



ALL_DATA = []
def parse_page(url):
    headers = {
        "User-Agent": "User-Agent, Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+"
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')

    soup = BeautifulSoup(text,'html5lib')

    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        # for tr in trs:
        #     tds = tr.find_all('td')
        #     print(tds[0])
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            # print(city_td,index)
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            print(city)
            temp_td = tds[-2]
            max_temp = list(temp_td.stripped_strings)[0]
            print(max_temp)
            ALL_DATA.append({"city":city,"max_temp":int(max_temp)})

def main():
    urls = [
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml",
    ]

    for url in urls:
        parse_page(url)

    ALL_DATA.sort(key=lambda data:data['max_temp'],reverse=True)
    data = ALL_DATA[0:10]
    print(data)
    cities = list(map(lambda x: x['city'], data))
    temp_max = list(map(lambda x: x['max_temp'], data))

    chart=Bar()
    chart.add_xaxis(cities)
    chart.add_yaxis('气温',temp_max)
    chart.render('temperature.html')
if __name__ == "__main__":
   main()
   # ALL_DATA = [
   #     {'city': '武汉', 'max_temp': 29},
   #     {'city': '襄阳', 'max_temp': 33},
   #     {'city': '鄂州', 'max_temp': 31},
   # ]
   #
   # ALL_DATA.sort(key=lambda data:data['max_temp'])
   # print(ALL_DATA)