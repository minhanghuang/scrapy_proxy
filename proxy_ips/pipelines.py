# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy import Item
class ProxyIpsPipeline(object):

    def __init__(self):
        host = "127.0.0.1" # MongoDB地址
        port = 27017 # 端口号
        dbName = "proxy" # 数据库名
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb["proxytable"] # 表名

    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.post.insert(bookInfo)
        return item



    # @classmethod
    # def from_crawler(cls, crawler):
    #     cls.DB_URL = 'mongodb://localhost:27017'
    #     cls.DB_NAME = 'proxy'
    #     return cls()
    #
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.DB_URL)
    #     self.db = self.client[self.DB_NAME]
    #
    # def close_spider(self, spider):
    #     self.client.close()
    #
    # def process_item(self, item, spider):
    #     collection = self.db[spider.name]
    #     post = dict(item) if isinstance(item, Item) else item
    #     collection.insert_one(post)
    #     return item

