import requests
import os
import urllib.request
import re
from lxml import etree
import threading
from queue import Queue
proxy = {
    'http':"119.27.181.141:8080"
}
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

#获取每个表情的url 并把它存储到队列中
class ProducerThread(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(ProducerThread, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self): #用来解析 init
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.page_img(url) #爬取图片url的方法

    def page_img(self,url):
        response = requests.get(url, headers=headers, proxies=proxy)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original') #获取图片的url地址
            suffix = os.path.splitext(img_url)[1]  # 图片后缀
            alt = img.get('alt') #获取图片的alt
            alt = re.sub(r'[？\?\.。!！]', '', alt)#windows 文件名不允许特殊字符 需要将特殊字符转成 空白
            filename = alt + suffix #拼接文件名
            if not self.img_queue.full():
                self.img_queue.put((img_url,filename))


#消费者只是用来将图片下载下来
class CustomerThread(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(CustomerThread, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            urllib.request.urlretrieve(img_url, "imgs/" + filename)
            print(filename+"下载完成")



def main():
    page_queue = Queue(50)  #存储50页
    img_queue = Queue(1000) #存储1000个表情

    for x in range(1,51):
        url = "https://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = ProducerThread(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = CustomerThread(page_queue,img_queue)
        t.start()

if __name__ == "__main__":
    print('开始下载')
    main()