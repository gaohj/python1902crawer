# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bmw.items import BmwItem

class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['http://autohome.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'), callback='parse_item', follow=True),
    )

    #https://car.autohome.com.cn/pic/series/65-1.html
    #https://car.autohome.com.cn/pic/series/65-10.html
    #https://car.autohome.com.cn/pic/series/65-3.html
    #https://car.autohome.com.cn/pic/series/65-12.html

    def parse_item(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        # print(srcs)
        # for src in srcs:
        #     src = response.urljoin(src)
        #     print(src)
        srcs = list(map(lambda x:response.urljoin(x.replace("240x180_0_q95_c42_","")),srcs))
        yield BmwItem(category=category,image_urls=srcs)