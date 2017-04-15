from scrapy.spiders import Spider
from scrapy.selector import Selector

from amazonCrawl.items import AmazonItem


class ItemSpider(Spider):
    name = "item"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/dp/B01EV2094Y",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        items = []
        sel = Selector(response)
        item = AmazonItem()
        item['title'] = sel.xpath('//*[@id="productTitle"]/text()').extract()
        item['discountPrice'] = sel.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
        item['originPrice'] = sel.xpath('//*[@class="a-text-strike"]/text()').extract()
        item['category'] = sel.xpath('//a[@class="a-link-normal a-color-tertiary"]//text()').extract()
        # item['id'] = sel.xpath('text()').re('-\s[^\n]*\\r')
        # item['url'] = sel.xpath('text()').re('-\s[^\n]*\\r')
        # item['rating'] = sel.xpath('text()').re('-\s[^\n]*\\r')
        item['image'] = sel.xpath('//*[@id="landingImage"]/@src')

        items.append(item)

        return items
