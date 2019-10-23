# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['budejie.com']
    start_urls = ['http://www.budejie.com/text/1']
    base_domain = 'http://www.budejie.com'
    #response就是下载器教给我们的数据
    #提取想要的数据
    #生成下个请求的url
    def parse(self, response):

        descs = response.xpath("//div[@class='j-r-list-c-desc']")
        for desc in descs:
            jokes = desc.xpath(".//text()").getall()
            joke = "\n".join(jokes).strip()
            link = desc.xpath(".//a/@href").get()
            links = str(self.base_domain + link)
            # link = self.base_domain+links
            item= QsbkItem(joke=joke,links=links)
            yield item
        next_url = response.xpath("//a[@class='pagenxt']/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+"/text/"+next_url,callback=self.parse)
