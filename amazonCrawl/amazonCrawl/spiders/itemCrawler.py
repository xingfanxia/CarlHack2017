from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from amazonCrawl.items import AmazonURLs
from scrapy import signals
from tqdm import tqdm

class ItemSpider(Spider):
    name = "url"
    allowed_domains = ["amazon.com"]
    start_urls = ['https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:1']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(ItemSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_opened(self, spider):
        self.pbar = tqdm()  # initialize progress bar
        self.pbar.clear()
        self.pbar.write('Opening {} spider'.format(spider.name))

    def spider_closed(self, spider):
        self.pbar.clear()
        self.pbar.write('Closing {} spider'.format(spider.name))
        self.pbar.close()  # close progress bar

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        self.pbar.update()
        sel = Selector(response)
        items = []
        item = AmazonURLs()
        item['url'] = sel.xpath('//*[@class="a-link-normal"]/text()').extract()

        items.append(item)

        return items
