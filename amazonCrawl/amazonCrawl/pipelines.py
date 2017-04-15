# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AmazoncrawlPipeline(object):
    def process_item(self, item, spider):
        item['title'] = ' '.join(''.join(item['title']).split()) if item['title'] else None
        item['discountPrice'] = ' '.join(''.join(item['discountPrice']).split()).strip()[1:] if item['discountPrice'] else None
        item['rating'] = item['rating'][0][:4]
        item['originPrice'] = ' '.join(''.join(item['originPrice']).split()).strip()[1:] if item['originPrice'] else None
        item['category'] = ' > '.join([i.strip() for i in item['category']]) if item['category'] else None
        return item
