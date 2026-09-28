# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 二手车Item
class ErshoucheItem(scrapy.Item):
    brand = scrapy.Field()  # 品牌
    price = scrapy.Field()  # 价格
    tag = scrapy.Field()    # 标签
