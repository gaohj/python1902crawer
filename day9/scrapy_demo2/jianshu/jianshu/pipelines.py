# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi
class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'123456',
            'database':'jianshu2',
            'charset':'utf8'
        }
        self.conn = pymysql.connect(**dbparams) #连接数据库
        self.cursor = self.conn.cursor() #创建一个句柄
        self._sql = None #存sql语句

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,word_count,read_count,pub_time,origin_url) values(null,%s,%s,%s,%s,%s,%s)  
            """
            return self._sql
        return self._sql
    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content'],item['word_count'],item['read_count'],item['pub_time'],item['origin_url']))
        self.conn.commit() #提交数据库
        return item


#异步mysql io操作    twisted

class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'123456',
            'database':'jianshu2',
            'charset':'utf8',
            'cursorclass':cursors.DictCursor,
        }

        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None #存sql语句

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article1(title,content,word_count,read_count,pub_time,origin_url) values(%s,%s,%s,%s,%s,%s)  
            """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item,item) #异步操作
        defer.addErrback(self.handle_error,item,spider)

    #真正执行 需要 下面两个方法  一个插入数据 另外一个抛异常
    def insert_item(self,cursor,item):
        print(item['title'], item['content'], item['word_count'], item['read_count'], item['pub_time'], item['origin_url'])
        cursor.execute(self.sql,(item['title'], item['content'], item['word_count'], item['read_count'], item['pub_time'], item['origin_url']))

    #error用来接收 异常信息
    def handle_error(self,error,item,spider):
        print("="*20+error+"="*20)