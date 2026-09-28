import scrapy
from json import loads

class PiaoSpider(scrapy.Spider):
    name = "piao"
    allowed_domains = ["piao.qunar.com"]
    start_urls = ["https://touch.piao.qunar.com/touch/toNewCityList.htm"]
    url = 'https://touch.piao.qunar.com/touch/list.json?region={city}&isForeign=false&page={pn}&pageSize=60&keyword=%E6%99%AF%E7%82%B9%E9%97%A8%E7%A5%A8'
    def parse(self, response):
        
        # 提示所有城市信息 第一个xpath是定义热门城市，第二个是定位境内的城市
        all_city = response.xpath('//ul[@class="mp-list mp-tr3"]')[0].xpath('./li/a/text()').extract()
        for city in all_city:
            yield scrapy.Request(self.url.format(city=city,pn=1), callback=self.parse_page,meta={'city':city})
    
    def parse_page(self,response):
        # 将字符串数据转换为字典数据
        resp = loads(response.text)
        # 获取数据列表
        sight_list = resp.get('data').get('sightList')
        # 遍历列表，获取每个景点的信息
        for item in sight_list:
            data = {
                'name':item.get('name'),
                'level':item.get('level'),
                'city':item.get('hybridAddress'),
                'address':item.get('address'),
                'price':item.get('qunarPrice'),
                'comment':item.get('commentCount'),
                'sight_commentScore':item.get('sightCommentScore')
            }
            # 将数据推送到管道
            yield data
        # 获取数据总数
        total = resp.get('data').get('totalCount')
        # 获取要爬取的城市
        city = response.meta.get('city')
        # 获取总页数
        page = (total + 60-1 )//60
        # 判断page是否大于1
        if page > 1:
            count = 1
            for pn in range(2,int(page)+1):
                if count > 3:
                    break
                print(f'正在获取{city},第{pn}页数据')
                yield scrapy.Request(self.url.format(city=city,pn=pn), callback=self.parse_info)
                count += 1

    def parse_info(self,response):
        # 将字符串数据转换为字典数据
        resp = loads(response.text)
        # 获取数据列表
        sight_list = resp.get('data').get('sightList')
        # 遍历列表，获取每个景点的信息
        for item in sight_list:
            data = {
                'name':item.get('name'),
                'level':item.get('level'),
                'city':item.get('hybridAddress'),
                'address':item.get('address'),
                'price':item.get('qunarPrice'),
                'comment':item.get('commentCount'),
                'sight_comment_score':item.get('sightCommentScore')
            }
            yield data