# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request
class BmwPipeline(object):
    def __init__(self):
        #指定存放图片的路径
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        #如果不存在
        if not os.path.exists(self.path):
            #创建
            os.mkdir(self.path)
    def process_item(self, item, spider):
        # print(item['category'])
        category = item['category']
        # print(item['urls'])
        urls = item['urls']
        #指定 轿车目录的文件夹
        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            img_name = url.split('_')[-1]
            urllib.request.urlretrieve(url,os.path.join(category_path,img_name))
        return item
