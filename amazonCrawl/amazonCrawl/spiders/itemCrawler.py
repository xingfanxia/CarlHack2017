from scrapy.spiders import Spider
from scrapy.selector import Selector
import re, amazonCrawl.gen2
from amazonCrawl.items import AmazonItem
from scrapy import signals
from tqdm import tqdm

class ItemSpider(Spider):
    name = "item"
    allowed_domains = ["amazon.com"]
    start_urls = amazonCrawl.gen2.retriveLS()

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(ItemSpider, cls).from_crawler(crawler, *args, **kwargs)
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
        regexp = re.compile("dp\/(.*)$")
        items = []
        sel = Selector(response)
        item = AmazonItem()
        item['title'] = sel.xpath('//*[@id="productTitle"]/text()').extract()
        item['discountPrice'] = sel.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice") or contains(@id,"priceblock_dealprice")]/text()').extract()
        item['originPrice'] = sel.xpath('//*[@class="a-text-strike"]/text()').extract()
        item['category'] = sel.xpath('//a[@class="a-link-normal a-color-tertiary"]//text()').extract()
        item['url'] = response.url 
        item['id'] = regexp.search(response.url).group(1)
        item['rating'] = sel.xpath('//*[@class="arp-rating-out-of-text"]//text()').extract()
        item['image'] = sel.xpath('//*[@id="landingImage"]/@src').extract()

        items.append(item)

        return items
