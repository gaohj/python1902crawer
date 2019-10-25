# -*- coding: utf-8 -*-
import scrapy
import re

class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    #获取所有的城市 构建 新房二手房 url链接
    def parse(self, response):
        province = None
        trs = response.xpath("//div[@class='outCont']//tr")
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            provience_td = tds[0]
            provience_text = provience_td.xpath(".//text()").get()
            provience_text = re.sub(r"\s","",provience_text)
            if provience_text:
                province = provience_text
            if provience_text == "其它":
                continue
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                #https://tj.fang.com/
                #构建新房url链接
                url_module = city_url.split(".")
                if 'bj' in url_module[0]:
                    newhouse_url = 'https://newhouse.fang.com/house/s/'
                    esf_url = 'https://esf.fang.com/'
                else:
                    newhouse_url = url_module[0]+'.newhouse.fang.com/house/s/'
                    esf_url = url_module[0]+'.esf.fang.com/'
                # print("新房链接:",newhouse_url)
                # print("二手房链接:",esf_url)
                # print(province,city)
                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={"info":(province,city)})
                # yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={"info",(province,city)})

    def parse_newhouse(self,response):
        provice,city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            name = "".join(name).strip()
            house_type = li.xpath(".//div[contains(@class,'house_type')]//text()").getall()
            house_type_list = list(map(lambda x:re.sub("\s|\t","",x),house_type))
            rooms = list(filter(lambda x:x.endswith('居'),house_type_list))
            house_type_str = "".join(house_type)
            area = re.sub("\s|－|\t","",house_type_str)
            print(area)





    def parse_esf(self):
        pass
