# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class ScrapyBeikePipeline(object):
    filename = 'beike_house_info.csv'

    def __init__(self):
        self.file = open(self.filename, 'a+', newline="")
        self.fieldnames = ["house_name", "sale_status", "house_type", "house_address", "house_price"]
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def write_csv_file(self, item):
        self.writer.writerow(item)
        return item

    def process_item(self, item, spider):
        self.write_csv_file(item)
        return item
