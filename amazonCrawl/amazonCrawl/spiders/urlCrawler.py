from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from amazonCrawl.items import AmazonURLs
from scrapy import signals
from tqdm import tqdm
import amazonCrawl.gen

class URLSpider(Spider):
    name = "url"
    allowed_domains = ["amazon.com"]
    start_urls = ["http://rssfeeds.s3.amazonaws.com/goldbox"]

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(URLSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_opened, signals.spider_opened)
    #     crawler.signals.connect(spider.spider_closed, signals.spider_closed)
    #     return spider
    #
    # def spider_opened(self, spider):
    #     self.pbar = tqdm()  # initialize progress bar
    #     self.pbar.clear()
    #     self.pbar.write('Opening {} spider'.format(spider.name))
    #
    # def spider_closed(self, spider):
    #     self.pbar.clear()
    #     self.pbar.write('Closing {} spider'.format(spider.name))
    #     self.pbar.close()  # close progress bar

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        # regexp = re.compile("<area.*.>")
        # allareascode = re.findall("<area.*.>", response.body)
        more = re.findall("\/dp\/.{10}", response.body)
        res = ["https://www.amazon.com/dp/"+x[4:14] for x in more]
        self.pbar.update()

        items = []
        item = AmazonURLs()
        item['url'] = res
        # items.append(imte)

        return item
