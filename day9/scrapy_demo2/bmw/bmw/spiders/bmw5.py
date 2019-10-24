# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['http://autohome.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        scrapy.Request(errback=self.test_error)
        return item
    def test_error(self):
        pass