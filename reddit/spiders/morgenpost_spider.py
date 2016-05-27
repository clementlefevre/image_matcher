# -*- coding: utf-8 -*-
import hashlib
import random
from datetime import datetime
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from reddit.items import  ArtikelItem
import pandas as pd
import pdb
from scrapy.linkextractors.sgml import SgmlLinkExtractor


def all_days_archives():
    base_url = "http://www.morgenpost.de/printarchiv/nachrichten-vom-"
    datelist = pd.date_range(datetime(2014, 1, 1), datetime(2016, 5, 25)).tolist()
    dates_as_string = [base_url + str(date.day) + "-" + str(date.month) + "-" + str(date.year) for date in datelist]
    return dates_as_string


class MorgenPostSpider(CrawlSpider):
    name = "artikel"
    allowed_domains = ["www.morgenpost.de"]
    start_urls = all_days_archives()


    rules = [
    	Rule(LinkExtractor(
            allow=(['printarchiv/nachrichten']),
            restrict_xpaths=('//div[@class="content"]')),
    		callback='parse_item',
    		follow=True)
    ]



    def parse_item(self, response):

        
        article_list = response.xpath('//div[@class="content"]/div/div/div/article')
        items=[]


        for selector in article_list:
            item = ArtikelItem()
            #pdb.set_trace()

            item['artikel_link'] = selector.xpath('a/@href').extract()
            hash = hashlib.sha1(str(item['artikel_link'])).hexdigest()
            print hash
            item['artikel_hash'] = hash
            item['artikel_title'] = selector.xpath('a/@title').extract()
            item['artikel_date'] = response.url
            items.append(item)

        return items
