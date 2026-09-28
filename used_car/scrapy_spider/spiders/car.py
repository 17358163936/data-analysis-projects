import scrapy
from ershouche.items import ErshoucheItem
#运行 scrapy crawl car
class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.renrenche.com']
    start_urls = ['https://www.renrenche.com/xa/ershouche/']

    def decrypt_price(self,encrypted_price):
        # 创建一个空字符串来存储解密后的价格
        decrypted_price = ""
        decryption_dict = {
            '%': '8', '+': '2', '-': '9', '/': '0', '¥': '5', '万': '1', '元': '3', '折': '4', '时': '6', '起': '7'
        }

        # 遍历加密价格字符串中的每个字符
        for char in encrypted_price:
            # 如果字符在解密字典中，替换为对应的数字
            if char in decryption_dict:
                decrypted_price += str(decryption_dict[char])
            # 如果字符不在字典中，直接添加到解密字符串中
            else:
                decrypted_price += char

        return decrypted_price
    def parse(self, response):
        # 获取当前页面的所有二手车列表项信息
        car_list = response.xpath("//ul[@class='infos infos-card h-clearfix']/li")
        for li in car_list:  # 遍历当前页二手车列表信息
            item = ErshoucheItem()  # 用于接收一个二手车的数据
            # 品牌
            brand = li.xpath("./div/a/div/h2/span/text() ").extract_first()  # 提取品牌数据
            # 如果爬取不到品牌（例如当前li是一个广告），则进行下一次循环
            if brand is None:  
                continue

            brand = brand.split(" ")[0].split("-")[0]  # 品牌
            price = li.xpath("./div/a/div/b/text()").extract_first().strip() # 价格
            price= self.decrypt_price(price)

            # 当前汽车的span标签
            tags = li.xpath("./div/a/div/div/span/text()").extract_first()
            tag_list = []
            # 遍历当前汽车的每个标签，并添加到列表中
            for tag in tags:
                tag_list.append(tag)
            
            # 填充数据到Item
            item["brand"] = brand
            item["price"] = price
            item["tag"] = "_".join(tag_list)
            yield item   # 交给Item Pipeline处理
        
        # 找到“下一页”按钮的URL地址
        next_url = response.xpath("//*[@id='mainCon']/div/a[@class='next']/@href").extract_first()
        # 如果不是最后一页
        if next_url != "javascript:void(0);": 
            next_url =next_url  # 补充完整下一页的URL
            # 向下一页发送请求，并设置回调函数为parse方法，因为下一页的解析方法与当前页相同
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
