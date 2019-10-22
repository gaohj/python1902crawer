#encoding:utf-8
import requests   #网络请求
from lxml import etree  #数据解析
import threading  #多线程
from queue import Queue  #线程安全队列
import csv  #保存

class BSSpider(threading.Thread):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    def  __init__(self,page_queue,joke_queue,*args,**kwargs):
        super(BSSpider, self).__init__(*args,**kwargs)
        self.base_domain = "http://www.budejie.com"
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            try:
               if self.page_queue.empty():
                   break
               url = self.page_queue.get()
               print(url.split("/")[-1])
               response = requests.get(url,headers=self.headers)
               text = response.text
               html = etree.HTML(text)
               descs = html.xpath("//div[@class='j-r-list-c-desc']")
               for desc in descs:
                   jokes = desc.xpath(".//text()")
                   joke = "\n".join(jokes).strip()
                   link = self.base_domain+desc.xpath(".//a/@href")[0]
                   self.joke_queue.put((joke,link))
               print("="*30 +'第%s页下载完成!'% url.split("/")[-1] + "="*30)
            except:
                pass

class BSWriterSpider(threading.Thread):
    def  __init__(self,writer,joke_queue,gLock,*args,**kwargs):
        super(BSWriterSpider, self).__init__(*args,**kwargs)
        self.joke_queue = joke_queue
        self.lock = gLock
        self.writer = writer
    def run(self):
        while True:
            try:
                joke_info = self.joke_queue.get(timeout=30)
                joke,link = joke_info
                self.lock.acquire()
                self.writer.writerow((joke,link))
                self.lock.release()
                print("保存一条")
            except:
                pass


def main():
    page_queue = Queue(10)
    joke_queue = Queue(500)

    gLock = threading.Lock()
    fp = open("bsbdj.csv",'a',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content','link'))
    for x in range(1,11):
        url = "http://www.budejie.com/text/%d" % x
        page_queue.put(url)
    #消费者存的时候 一行行的存
    for x in range(5):
        t = BSSpider(page_queue,joke_queue)
        t.start()

    for x in range(5):
        t = BSWriterSpider(writer,joke_queue,gLock)
        t.start()


if __name__ == "__main__":
    main()