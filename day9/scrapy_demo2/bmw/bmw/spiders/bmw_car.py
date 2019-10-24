# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem

class BmwCarSpider(scrapy.Spider):
    name = 'bmw_car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            img_urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for img_url in img_urls:
            #     img_url = response.urljoin(img_url)
            #     print(img_url)
            urls = list(map(lambda img_url:response.urljoin(img_url),img_urls))
            yield BmwItem(category=category,urls=urls)