# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .items import CsdnItem
import re
class CsdnPipeline(object):
     def __init__(self,mongo_uri,mongo_db,replicaset):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.replicaset = replicaset
     @classmethod
     def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'csdn_test'),
            replicaset = crawler.settings.get('REPLICASET')
        )
     def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,replicaset=self.replicaset)
        self.db = self.client[self.mongo_db]
     def close_spider(self, spider):
        self.client.close()
     def process_item(self, item, spider):
        if isinstance(item,CsdnItem):
            self._process_csdn_item(item)
            return item
     def _process_csdn_item(self,item):
        item['url']=item['url'][-1]
        item['time']=item['time'][-1].strip().replace("\r\n","")
        item['name']=item['name'][-1].strip().replace("\r\n","")
        item['reader']=item['reader'][-1]
        #print(item['url'],item['name'],item['reader'],item['time'])
        self.db.csdn_info.insert(dict(item))
