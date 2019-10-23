# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('bsbdj.json','w',encoding='utf-8')
#     def open_spider(self,spider):
#         print('爬虫开始了')
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+"\n")
#         return item
#     def close_spider(self,spider):
#         print('爬虫结束')

#保存json数据的时候有两个类操作起来更简单
#先把数据存到内存中最后统一存入磁盘中
#好处是  满足json
#坏处是 数据量耗内存
# from scrapy.exporters import JsonItemExporter
#
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json','wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print('爬虫开始了')
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#     def close_spider(self,spider):
#         print('爬虫结束')

from scrapy.exporters import JsonLinesItemExporter

#每次调用export_item 方法 就把数据存到磁盘中
#好处是 节约内存   数据安全性高
#坏处是 这个可能不是满足json数据格式
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi1.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了')
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        print('爬虫结束')
