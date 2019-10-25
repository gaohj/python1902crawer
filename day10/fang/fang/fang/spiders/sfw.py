# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import NewHouseItem,EsfItem
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
            if province == "其它":
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
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={"info":(province,city)})

    def parse_newhouse(self,response):
        province,city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get().strip()
            house_type = li.xpath(".//div[contains(@class,'house_type')]//text()").getall()
            house_type_list = list(map(lambda x:re.sub("\s|\t","",x),house_type))
            rooms = list(filter(lambda x:x.endswith('居'),house_type_list))
            house_type_str = "".join(house_type)
            area = re.sub("\s|－|\t","",house_type_str)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district = re.search(r".*\[(.+)\].*", district).group(1)
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            item = NewHouseItem(name=name, rooms=rooms, price=price, area=area, province=province, city=city,
                                district=district, address=address, origin_url=origin_url)
            yield item
        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={"info":(province,city)})

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath("//div[contains(@class,'shop_list')]/dl")
        for dl in dls:
            item = EsfItem(province=province, city=city)
            item['name'] = dl.xpath(".//p[@class='add_shop']/a/@title").get()

            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x: re.sub(r"\s", "", x), infos))
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                    # print(item['rooms'])
                elif '层' in info:
                    item['floor'] = info
                elif '向' in info:
                    item['toward'] = info
                elif '㎡' in info:
                    item['area'] = info
                elif '年建' in info:
                    item['year'] = info
                else:
                    pass
            item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            item['unit'] = "".join(dl.xpath(".//dd[@class='price_right']/span[2]/text()").getall())
            detail_url = dl.xpath(".//h4[@class='clearfix']/a/@href").get()
            item['origin_url'] = response.urljoin(detail_url)
            yield item
        next_url = response.xpath("//a[@id='PageControl1_hlk_next']/@href").get()
        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf, meta={"info": (province, city)})
