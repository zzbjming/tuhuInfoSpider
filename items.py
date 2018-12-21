# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TuhuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    carstore_href = scrapy.Field()  # 门店链接
    store_name = scrapy.Field()  # 门店名字
    carstore_level = scrapy.Field()  # 门店等级
    carstore_type = scrapy.Field()  # 门店类型
    trade_num = scrapy.Field()  # 交易数量（包括轮胎，保养，美容）
    estimate = scrapy.Field()  # 评价
    work_time = scrapy.Field()  # 营业时间
    address = scrapy.Field()  # 门店地址
    estimate_num = scrapy.Field()  # 评价数量
    tyre_num = scrapy.Field()  # 轮胎订单数
    maintain_num = scrapy.Field()  # 保养订单数
    fit_num = scrapy.Field()  # 美容订单数
