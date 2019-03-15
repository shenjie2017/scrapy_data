# -*- coding: utf-8 -*-
import scrapy

from scrapy_beike.items import BeikeItem


class BeikeSpider(scrapy.Spider):
    name = 'beike'
    allowed_domains = ['cd.fang.ke.com']
    start_urls = []
    for i in range(1, 100):
        start_urls.append('https://cd.fang.ke.com/loupan/pg{0}'.format(i))

    def parse(self, response):
        node_list = response.xpath(
            "//ul[@class='resblock-list-wrapper']/li")

        for node in node_list:
            item = BeikeItem()
            house_name = node.xpath(
                "./div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/a/text()").extract()
            tmp_type = node.xpath(
                "./div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/span/text()").extract()
            house_address = node.xpath(
                "./div[@class='resblock-desc-wrapper']/a/text()").extract()
            house_price = node.xpath(
                "./div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div/span/text()").extract()

            item['house_name'] = house_name[0]
            item['sale_status'] = tmp_type[0]
            item['house_type'] = tmp_type[1]
            item['house_address']=house_address[1].strip()
            item['house_price'] = house_price[0]

            yield item

        # pass
