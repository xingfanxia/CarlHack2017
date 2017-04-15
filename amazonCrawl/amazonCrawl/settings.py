# -*- coding: utf-8 -*-

# Scrapy settings for amazonCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'amazonCrawl'

SPIDER_MODULES = ['amazonCrawl.spiders']
NEWSPIDER_MODULE = 'amazonCrawl.spiders'

FEED_URI = u'output2.json'
FEED_FORMAT = 'Json'
# ITEM_PIPELINES = {
#     'amazonCrawl.pipelines.AmazoncrawlPipeline': 300,
# }
LOG_LEVEL = 'INFO'