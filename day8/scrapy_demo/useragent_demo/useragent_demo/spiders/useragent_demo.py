# -*- coding: utf-8 -*-
import scrapy
import json

class UseragentSpider(scrapy.Spider):
    name = 'useragent_demo'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print(response)
        user_agent = json.loads(response.text)['user-agent']
        print("="*50)
        print(user_agent)
        print("="*50)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)