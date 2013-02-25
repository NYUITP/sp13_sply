from urlparse import urljoin 
import simplejson

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from myproject.items import ProductItem


class BookSpider(CrawlSpider):
    name = 'manufactum'
    allowed_domains = ['manufactum.com']
    start_url=["http://www.manufactum.com/ladies-elysian-duffle-coat-p1465087/"]
    rules = (           
             Rule(SgmlLinkExtractor(allow=(r'http://www.manufactum.com/ladies-elysian-duffle-coat-p1465087/')),callback = "parse_item"),
            )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = ProductItem()
        item['product_name'] = hxs.select('//div[@class = "nameAndImages"]/h1/text()').extract()[0]
        item['status'] = hxs.select('//dl[@class = "verfuegbarkeit vorraetig"]/dt/text()').extract()
  
        return item
                            
 


