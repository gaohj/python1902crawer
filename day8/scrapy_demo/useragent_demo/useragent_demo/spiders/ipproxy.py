# -*- coding: utf-8 -*-
import scrapy
import json

class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        user_agent = json.loads(response.text)['origin']
        print("=" * 50)
        print(user_agent)
        print("=" * 50)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
