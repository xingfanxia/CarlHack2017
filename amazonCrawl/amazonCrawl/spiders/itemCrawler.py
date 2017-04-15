from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from amazonCrawl.items import AmazonItem


class ItemSpider(Spider):
    name = "item"
    allowed_domains = ["amazon.com"]
    start_urls = ['https://www.amazon.com/dp/B00000IGGJ', 'https://www.amazon.com/dp/B00005JNBQ', 'https://www.amazon.com/dp/B00006KGC0', 'https://www.amazon.com/dp/B00006KGC2', 'https://www.amazon.com/dp/B00007EPJ6', 'https://www.amazon.com/dp/B0001LJBTE', 'https://www.amazon.com/dp/B00020HALU', 'https://www.amazon.com/dp/B000001DQI', 'https://www.amazon.com/dp/B000003BGP', 'https://www.amazon.com/dp/B00000JWOJ', 'https://www.amazon.com/dp/B00001NFCY', 'https://www.amazon.com/dp/B00001T3HC', 'https://www.amazon.com/dp/B000020617', 'https://www.amazon.com/dp/B00002EPKT', 'https://www.amazon.com/dp/B00002EQA6', 'https://www.amazon.com/dp/B000035X1M', 'https://www.amazon.com/dp/B000038A2S', 'https://www.amazon.com/dp/B00003L4DJ', 'https://www.amazon.com/dp/B00003NHAR', 'https://www.amazon.com/dp/B00004HYMR', 'https://www.amazon.com/dp/B00004NRPZ', 'https://www.amazon.com/dp/B00004S5YW', 'https://www.amazon.com/dp/B00004SBUI', 'https://www.amazon.com/dp/B00004SCX6', 'https://www.amazon.com/dp/B00004SGS5', 'https://www.amazon.com/dp/B00004U8KD', 'https://www.amazon.com/dp/B00004UAPE', 'https://www.amazon.com/dp/B00004WFIZ', 'https://www.amazon.com/dp/B00004WMZ0', 'https://www.amazon.com/dp/B00004XONN', 'https://www.amazon.com/dp/B00004XQP0', 'https://www.amazon.com/dp/B00004Y6S3', 'https://www.amazon.com/dp/B00004ZB9D', 'https://www.amazon.com/dp/B00005NNVA', 'https://www.amazon.com/dp/B00005U0JZ', 'https://www.amazon.com/dp/B00006879E', 'https://www.amazon.com/dp/B00006F1IJ', 'https://www.amazon.com/dp/B000089RVX', 'https://www.amazon.com/dp/B0000AGWFX', 'https://www.amazon.com/dp/B0000AKCLI', 'https://www.amazon.com/dp/B0000AKGMS', 'https://www.amazon.com/dp/B0001UL7RY', 'https://www.amazon.com/dp/B0002YT776', 'https://www.amazon.com/dp/B0002ZAILY', 'https://www.amazon.com/dp/B00062IZQS', 'https://www.amazon.com/dp/B00067ZNG8', 'https://www.amazon.com/dp/B0006L5IP0', 'https://www.amazon.com/dp/B0007GP660', 'https://www.amazon.com/dp/B0007QS4IC', 'https://www.amazon.com/dp/B0007Y8A1A', 'https://www.amazon.com/dp/B0007Z9R7U', 'https://www.amazon.com/dp/B00004SPE1', 'https://www.amazon.com/dp/B00000012J', 'https://www.amazon.com/dp/B00000018G', 'https://www.amazon.com/dp/B0000001LG', 'https://www.amazon.com/dp/B0000001NZ', 'https://www.amazon.com/dp/B0000001VE', 'https://www.amazon.com/dp/B0000002UE', 'https://www.amazon.com/dp/B0000002UR', 'https://www.amazon.com/dp/B0000002YE', 'https://www.amazon.com/dp/B0000002ZC', 'https://www.amazon.com/dp/B00000030E', 'https://www.amazon.com/dp/B0000003IO', 'https://www.amazon.com/dp/B0000003KJ', 'https://www.amazon.com/dp/B0000003KT', 'https://www.amazon.com/dp/B00000045F', 'https://www.amazon.com/dp/B0000004E0', 'https://www.amazon.com/dp/B0000004QU', 'https://www.amazon.com/dp/B0000004R0', 'https://www.amazon.com/dp/B0000004R1', 'https://www.amazon.com/dp/B0000004TH', 'https://www.amazon.com/dp/B00000050T', 'https://www.amazon.com/dp/B000000518', 'https://www.amazon.com/dp/B00000053E', 'https://www.amazon.com/dp/B00000057M', 'https://www.amazon.com/dp/B000000617', 'https://www.amazon.com/dp/B000000628', 'https://www.amazon.com/dp/B00000064G', 'https://www.amazon.com/dp/B00000064P', 'https://www.amazon.com/dp/B0000006MN', 'https://www.amazon.com/dp/B0000006UO', 'https://www.amazon.com/dp/B0000006X0', 'https://www.amazon.com/dp/B0000007F0', 'https://www.amazon.com/dp/B0000007FV', 'https://www.amazon.com/dp/B00000098O', 'https://www.amazon.com/dp/B0000009OB', 'https://www.amazon.com/dp/B000000A3K', 'https://www.amazon.com/dp/B000000A7M', 'https://www.amazon.com/dp/B000000A7Q', 'https://www.amazon.com/dp/B000000DYU', 'https://www.amazon.com/dp/B000000E5J', 'https://www.amazon.com/dp/B000000E8B', 'https://www.amazon.com/dp/B000000G7S', 'https://www.amazon.com/dp/B000000HHR', 'https://www.amazon.com/dp/B000000I2G', 'https://www.amazon.com/dp/B000000JO3', 'https://www.amazon.com/dp/B000000K5V', 'https://www.amazon.com/dp/B000000M3J', 'https://www.amazon.com/dp/B000000NH8', 'https://www.amazon.com/dp/B000000NN4']

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
