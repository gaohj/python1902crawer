import requests
import urllib.request
from lxml import etree
import os
import re
import threading
import csv
from queue import Queue

#负责将内容和连接爬取下来 放到队列中
class BSSpider(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    def __init__(self,page_queue,joke_queue,*args,**kwargs):
        super(BSSpider, self).__init__(*args,**kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue
    def run(self):
        while True:
            url = self.page_queue.get()
            response = requests.get(url,headers=self.headers)
            text = response.content.decode('gbk')

            html = etree.HTML(text)
            descs = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in descs:
                jokes = desc.xpath(".//text()")
                joke = "\n".join(jokes).strip()
                link = self.base_domain+desc.xpath(".//a/@href")[0]
                self.joke_queue.put((joke,link))
            print('='*30+"第%s页下载完成" % url.split('/')[-1]+"="*30)


#从队列中取出信息 写到csv文件中
class BSWriter(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    def __init__(self,joke_queue,writer,gLock,*args,**kwargs):
        super(BSWriter, self).__init__(*args,**kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock
    def run(self):
        while True:
            try:
                #从段子队列中取出来然后放到 csv文件中
                joke_info = self.joke_queue.get(timeout=50)
                joke, link = joke_info
                self.lock.acquire()
                self.writer.writerow((joke,link))
                self.lock.release()
                print("保存一条成功")
            except:
                break



def main():
    page_queue = Queue(20)
    joke_queue = Queue(666)
    gLock = threading.Lock()
    fp = open('bsbdj.csv','w',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content','link'))
    for x in range(1,21):
        url = 'http://www.budejie.com/text/%d' % x
        page_queue.put(url) #将每一页的url地址放到队列中

    for x in range(5):
        t = BSSpider(page_queue,joke_queue)
        t.start()

    for x in range(5):
        t = BSWriter(joke_queue,writer,gLock)
        t.start()



if __name__ == '__main__':
    main()