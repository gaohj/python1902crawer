# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
class FangPipeline(object):
    def __init__(self):
        self.new_fp = open("newhouse.json", 'wb')
        self.esf_fp = open("esfhouse.json", 'wb')
        self.newhouse_exporters = JsonLinesItemExporter(self.new_fp, ensure_ascii=False)
        self.esf_exporters = JsonLinesItemExporter(self.esf_fp, ensure_ascii=False)

    def process_item(self, item, spider):
        self.newhouse_exporters.export_item(item)
        self.esf_exporters.export_item(item)
        return item

    def close_item(self):
        self.new_fp.close()
        self.esf_fp.close()
