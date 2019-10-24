# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request
from bmw import settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
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

class BmwImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs =super(BmwImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs
    def file_path(self, request, response=None, info=None):
        path = super(BmwImagesPipeline, self).file_path(request,response,info)
        #full/156505d083bcfc3950a61249287292137dc2f46d.jpg
        #需要拿到图片所在的目录名 这个目录名在item中
        #最好的方式是将其绑定到request对象上
        category = request.item.get('category') #拿到图片所在的目录
        image_store = settings.IMAGES_STORE #图片存储的路径
        category_path = os.path.join(image_store, category) #每个图片所在子目录的路径
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        #图片的名字  file_path 返回的就是图片的名字

        image_name = path.replace('full/',"")
        image_path = os.path.join(category_path,image_name)

        return image_path
