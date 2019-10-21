
import requests
import os
import urllib.request
import re
from lxml import etree
proxy = {
    'http':"121.226.214.26:9999"
}
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}


def parse_img(url):
    response = requests.get(url,headers=headers,proxies=proxy)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        suffix = os.path.splitext(img_url)[1] #图片后缀
        alt = img.get('alt')
        alt = re.sub(r'[？\?\.。!！]','',alt)
        filename = alt+suffix

        urllib.request.urlretrieve(img_url,"images/"+filename)
def main():
    for page in range(1,51):
        url = "https://www.doutula.com/photo/list/?page=%d" % page
        parse_img(url)

if __name__ == "__main__":
    main()