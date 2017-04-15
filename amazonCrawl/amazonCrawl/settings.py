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


FEED_URI = u'file:///D:\CarlHack2017\item.csv'
FEED_FORMAT = 'CSV'
