# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
   #省份
   province = scrapy.Field()

   #城市
   city = scrapy.Field()
   #楼盘名字
   name = scrapy.Field()

   #价格
   price = scrapy.Field()

   #几居室
   rooms = scrapy.Field()

   #面积
   area = scrapy.Field()

   #地址
   address = scrapy.Field()

   #位于哪个区
   district  = scrapy.Field()

   #是否在售
   sale = scrapy.Field()

   #详情页面的url
   origin_url = scrapy.Field()


class EsfItem(scrapy.Item):
    # 省份
    province = scrapy.Field()

    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()

    # 总价
    price = scrapy.Field()

    #单价
    unit = scrapy.Field()
    # 几室几厅
    rooms = scrapy.Field()

    # 建筑面积
    area = scrapy.Field()

    # 地址
    address = scrapy.Field()

    # 位于哪个区
    district = scrapy.Field()

    #朝向
    toward= scrapy.Field()

    #几层
    floor = scrapy.Field()
    # 详情页面的url
    origin_url = scrapy.Field()

