# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/[cp]/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        pub_time = response.xpath("////*[@id='__next']/div[1]/div/div/section[1]/div[1]/div/time/text()").get()
        word_count = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/span[2]/text()').get()
        # word_count = word_count.replace("字数 ","")
        # word_count = word_count.split(" ")[-1]
        read_count = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/span[3]/text()').get()
        # read_count = read_count.split(" ")[-1]
        content = response.xpath('//article[@class="_2rhmJa"]//p/text()').getall()
        content = "".join(content).strip()

        item = JianshuItem(
            title=title,
            pub_time=pub_time,
            word_count=word_count,
            origin_url = response.url,
            read_count=read_count,
            content=content
        )

        yield item

