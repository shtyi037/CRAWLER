# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class IthelpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #系列
    series = scrapy.Field()
    #天數
    day = scrapy.Field()
    #名稱
    positionName = scrapy.Field()
    #連結
    positionLink = scrapy.Field()
