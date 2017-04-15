from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from amazonCrawl.items import AmazonItem


class ItemSpider(Spider):
    name = "item"
    allowed_domains = ["amazon.com"]
    start_urls = ['https://www.amazon.com/dp/B01EV2094Y']

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
        item['discountPrice'] = sel.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
        item['originPrice'] = sel.xpath('//*[@class="a-text-strike"]/text()').extract()
        item['category'] = sel.xpath('//a[@class="a-link-normal a-color-tertiary"]//text()').extract()
        item['url'] = response.url 
        item['id'] = regexp.search(response.url).group(1)
        item['rating'] = sel.xpath('//*[@class="arp-rating-out-of-text"]//text()').extract()
        item['image'] = sel.xpath('//*[@id="landingImage"]/@src').extract()

        items.append(item)

        return items
