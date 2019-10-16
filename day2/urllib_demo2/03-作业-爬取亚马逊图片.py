import re
import urllib
from urllib import request

# 分别爬取下面url的亚马逊图片，保存到本地images文件夹中
#（ 提示：亚马孙有反爬 ）

# url = "https://www.amazon.cn/s/ref=lp_2152154051_pg_2?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051&page=2&ie=UTF8&qid=1516169582"
# url = "https://www.amazon.cn/s/ref=sr_pg_3?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051&page=3&ie=UTF8&qid=1516169970"
# url = "https://www.amazon.cn/s/ref=sr_pg_4?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051&page=4&ie=UTF8&qid=1516171321"
#

# 正则表达式提示:
#	图片1
#   imgReg1 = '<img alt=".*" src="(.*?)" class="s-access-image cfMarker" height="260" width="200">'
#	图片2
#   imgReg2 = 'data-a-image-source="(.*?)"></div></a></div>'


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}

def getData(url):

    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode()

    imgReg1 = '<img alt=".*" src="(.*?)" class="s-access-image cfMarker" height="260" width="200">'
    imgReg2 = 'data-a-image-source="(.*?)"></div></a></div>'

    images1 = re.findall(imgReg1, html, re.S)
    images2 = re.findall(imgReg2, html, re.S)

    images1.extend(images2)
    # print(images1)

    for image in images1:
        # 获取图片名称
        name = image[image.rfind('/')+1:]

        # download image
        request.urlretrieve(image, 'image2/'+name)


if __name__ == "__main__":
    url = "https://www.amazon.cn/s/ref=lp_2152154051_pg_2?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051&page=2&ie=UTF8&qid=1516169582"
    # url = "https://www.amazon.cn/s/ref=sr_pg_3?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051&page=3&ie=UTF8&qid=1516169970"
    # url = "https://www.amazon.cn/s/ref=sr_pg_4?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051&page=4&ie=UTF8&qid=1516171321"

    getData(url)





