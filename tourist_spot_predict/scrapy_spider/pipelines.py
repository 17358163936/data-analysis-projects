# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class CSVPipeline:
    def __init__(self):
        # 创建csv文件
        self.file = open('data.csv', 'w', encoding='utf-8', newline='')
        # 创建csv写入对象
        self.writer = csv.writer(self.file)
        # 写入表头
        self.writer.writerow([
            'name','level','city',
            'address','price','comment',
            'sight_comment_score'])
    def process_item(self, item, spider):
        # 将数据写入csv文件
        self.writer.writerow([
            item.get('name'),item.get('level'),item.get('city'),
            item.get('address'),item.get('price'),item.get('comment'),
            item.get('sight_comment_score')
            ])
        return item
    def close_spider(self,spider):
        # 关闭文件
        self.file.close()