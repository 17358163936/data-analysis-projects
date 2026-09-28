# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

# Item Pipeline用来处理返回的Item数据
class ErshouchePipeline:
    def __init__(self):
        file = open("data.csv","w",newline="",encoding="utf-8")
        self.writer = csv.writer(file) # 创建csv文件的写入器对象
        self.writer.writerow(["brand","price","tag"])  # 写入标题行

    def process_item(self, item, spider):
        # 将每个Item对象的数据（每个二手车数据）写入csv文件
        self.writer.writerow([item["brand"],item["price"],item["tag"]])
        
