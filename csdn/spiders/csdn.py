# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import CsdnItem
class csdnspider(CrawlSpider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/yainyiyi123/article/details/48399511'
                  ]
    rules = (
        #Rule(LinkExtractor(allow=r'/.*/article/details/\d+'), callback='parse_book_list', follow=True),
        Rule(LinkExtractor(allow=r'/.*/article/details/\d+'), callback='parse_csdn_list', follow=True),
    )
    def parse_csdn_list(self,response):
      #print(response)
      url=response.xpath(".//*[@id='article_details']/div[1]/h1/span/a/@href").extract()
      if url==False:
          url=response.url
      name=response.xpath(".//*[@id='article_details']/div[1]/h1/span/a/text()").extract()
      if name==False:
          name=response.xpath("html/body/div[4]/div[2]/div[2]/div[2]/h3/text()").extract()
      reader=response.xpath(".//*[@id='article_details']/div[2]/div/span[2]/text()").extract()
      if reader==False:
          reader=response.xpath("html/body/div[4]/div[2]/div[2]/div[2]/p[1]/i[2]/text()").extract()
      time=response.xpath(".//*[@id='article_details']/div[2]/div/span[1]/text()").extract()
      if name==False:
          time=response.xpath("html/body/div[4]/div[2]/div[2]/div[2]/p[1]/em/text()").extract()
      #print(url,name,reader,time)
      csdnlist=CsdnItem(url=url,name=name,reader=reader,time=time)
      yield csdnlist