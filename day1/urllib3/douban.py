#encoding:utf-8
import urllib.request
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}

for i in range(10):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d" % (i)

    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)

    html = response.read().decode('utf8')
    # print(html)

    data = json.loads(html)
    datalists = data.get('data')

    for lists in datalists:
        title = lists['title']
        casts = lists['casts']
        print(title,casts)