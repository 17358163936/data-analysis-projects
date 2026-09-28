
USE used_car_db;

SET GLOBAL local_infile = 1;


LOAD DATA LOCAL INFILE 'D:/桌面/文档/源码/Project/二手车/ershou/data.csv'
INTO TABLE used_car_db
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS; --跳过第一行表头brand,price,tag

-- 1.各品牌平均价格、车辆数量，按均价降序
SELECT 
    brand,
    ROUND(AVG(price),2) AS avg_price,
    COUNT(*) AS car_count
FROM used_car
GROUP BY brand
ORDER BY avg_price DESC;

-- 2.价格TOP5车辆
SELECT brand,price,tag
FROM used_car
ORDER BY price DESC
LIMIT 5;

--3.按标签统计车辆数量
SELECT tag,COUNT(*) car_num
FROM used_car
GROUP BY tag;

--4.价格区间统计
SELECT
CASE
    WHEN price < 8 THEN '0-8万'
    WHEN price BETWEEN 8 AND 15 THEN '8-15万'
    WHEN price BETWEEN 15 AND 25 THEN '15-25万'
    ELSE '25万以上'
END AS price_range,
COUNT(*) total
FROM used_car
GROUP BY price_range;

--5.窗口函数：每个品牌内部车辆价格排名（面试重点）
SELECT brand,price,tag,
ROW_NUMBER() OVER(PARTITION BY brand ORDER BY price DESC) AS price_rank
FROM used_car;