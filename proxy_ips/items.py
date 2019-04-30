# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyIpsItem(scrapy.Item):

    http = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    is_active = scrapy.Field()
    check_time = scrapy.Field()