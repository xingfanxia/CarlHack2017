from scrapy.spiders import Spider
from scrapy.selector import Selector
import re
from amazonCrawl.items import AmazonURLs
from scrapy import signals
from tqdm import tqdm

class URLSpider(Spider):
    name = "url"
    allowed_domains = ["amazon.com"]
    start_urls = [ 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:1', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:2', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:3', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:4', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:5', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:6', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:7', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:8', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:9', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:10', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:11', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:12', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:13', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:14', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:15', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:16', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:17', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:18', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:19', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:20', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:21', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:22', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:23', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:24', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:25', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:26', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:27', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:28', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:29', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:30', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:31', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:32', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:33', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:34', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:35', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:36', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:37', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:38', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:39', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:40', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:41', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:42', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:43', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:44', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:45', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:46', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:47', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:48', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:49', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:50', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:51', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:52', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:53', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:54', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:55', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:56', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:57', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:58', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:59', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:60', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:61', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:62', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:63', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:64', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:65', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:66', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:67', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:68', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:69', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:70', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:71', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:72', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:73', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:74', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:75', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:76', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:77', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:78', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:79', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:80', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:81', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:82', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:83', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:84', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:85', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:86', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:87', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:88', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:89', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:90', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:91', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:92', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:93', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:94', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:95', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:96', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:97', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:98', 
'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_2?gb_f_GB-SUPPLE=page:99'
]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(URLSpider, cls).from_crawler(crawler, *args, **kwargs)
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