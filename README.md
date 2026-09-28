# 数据分析实战项目
>2027届计算机科学与技术本科，完整数据分析链路实战：爬虫采集、数据清洗、特征工程、可视化、机器学习回归建模。

## 仓库目录
- used_car：二手车价格预测项目
  - scrapy_spider：Scrapy分布式爬虫代码
  - data：清洗后数据集csv
  - analysis.ipynb：数据清洗、EDA、GBDT建模
  - mysql_script.sql：MySQL建表+业务统计、窗口函数示例
  - powerbi_img：PowerBI交互式看板截图
- tourist_spot_predict：旅游景点票价预测
  - scrapy_spider爬虫、数据、随机森林回归建模notebook

## 技术栈
Python、Scrapy、Pandas、NumPy、Matplotlib、Seaborn、Scikit‑learn、MySQL、PowerBI、Git

## 项目1｜二手车价格预测
- 使用Scrapy搭建爬虫，配置UA、代理IP池，抓取17000+二手车数据
- Pandas完成数据清洗、去重、缺失值处理，数据导入MySQL数据库
- SQL完成品牌均价、价格区间统计，窗口函数组内排序
- 特征工程One‑Hot编码，GBDT梯度提升回归树完成价格预测
- PowerBI制作交互式看板，支持切片器联动多维度分析

## 项目2｜旅游景点票价预测
- Scrapy定向爬虫抓取去哪儿网景点数据
- 数据清洗，多维度探索性数据分析
- 类别特征独热编码，RandomForestRegressor随机森林回归完成票价预测

## 个人信息
- 求职意向：初级数据分析师 / 数据分析助理
- 简历：见个人简历PDF