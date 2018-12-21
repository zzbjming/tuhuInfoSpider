# -*- coding: utf-8 -*-
import scrapy
import lxml
from copy import deepcopy
from tuhuinfo.items import TuhuItem


class TuhuSpider(scrapy.Spider):
    name = 'tuhu'
    allowed_domains = ['tuhu.cn']
    start_urls = ['https://www.tuhu.cn/shops/hangzhou3.aspx']

    def parse(self, response):
        item = TuhuItem()
        carstore_list = response.xpath('//div[@class="non-list"]/div')
        for carstore in carstore_list:
            item['carstore_href'] = carstore.xpath('./div[1]/a/@href').extract_first()
            item['store_name'] = carstore.xpath('./div[1]/a/text()').extract_first()
            item['carstore_level'] = carstore.xpath('./div[1]/div/div/span/text()').extract_first()
            item['carstore_type'] = carstore.xpath('./div[1]/div/span[3]/@title').extract_first()
            item['trade_num'] = carstore.xpath('./div[2]/div[2]/span[1]/i/text()').extract_first()
            item['estimate'] = carstore.xpath('./div[2]/div[2]/span[2]/i/text()').extract_first()
            item['address'] = carstore.xpath('.//div[2]/div[2]/p[1]/span[2]/text()').extract_first()

            yield scrapy.Request(
                item['carstore_href'],
                callback=self.get_worktime,
                meta={'item': deepcopy(item)}
            )

    def get_worktime(self, response):
        item = response.meta['item']
        item['work_time'] = response.xpath('//div[@class="shop-info"]/p[1]/span/text()').extract_first()
        item['estimate_num'] = response.xpath('//div[@id="comments"]/div[1]/div[1]/div[2]/span/i/text()').extract_first()
        item['tyre_num'] = response.xpath('//ul[@class="filter clearfix"]/li[2]/label/span/text()').extract_first()
        item['maintain_num'] = response.xpath('//ul[@class="filter clearfix"]/li[3]/label/span/text()').extract_first()
        item['fit_num'] = response.xpath('//ul[@class="filter clearfix"]/li[4]/label/span/text()').extract_first()
        yield item
