#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QuadrinhosSpider(CrawlSpider):

    '''
    Crawler that searches for Name, description and link to the 
    comic book from the site baixquadrinhos.com
    '''

    # Name of Crawler

    name = 'quadrinhos_crawler'

    # To introduce a 1.5 second delay between requests

    download_delay = 1.5

    # Number of pages to be scanned (solution for pagination)

    NPAGES = 2

    allowed_domains = ['baixarquadrinhos.com']

    # Spider will begin to crawl from, when no particular URLs are specified
    start_urls = ['http://baixarquadrinhos.com/page/{}/'.format(page)
                  for page in range(1, NPAGES)]

    # Rules for Link Extractor and Follow Link
    rules = \
        (Rule(LinkExtractor(restrict_xpaths='//a[contains(@class, "woocommerce-LoopProduct-link")]'
         ), callback='parse_details', follow=True), )

    # Parse result

    def parse_details(self, response):
        yield {'name': response.xpath('//h6/text()').extract_first(),
               'link': response.xpath("//div[@class='links-download']/a[2]/@href"
               ).extract_first(),
               'desc': response.xpath("//div[@id='tab-description']/p[1]/text()"
               ).extract_first()}