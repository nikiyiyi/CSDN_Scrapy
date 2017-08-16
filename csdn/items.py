# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field() #文章连接地址
    name = scrapy.Field() #文章名
    reader = scrapy.Field() #阅读人数
    #store = scrapy.Field() #评论
    time=scrapy.Field() #创建时间
    pass
