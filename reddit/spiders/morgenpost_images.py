# -*- coding: utf-8 -*-
import hashlib
import pdb

from reddit.models import db_connect, Artikel
from scrapy.contrib.spiders import CrawlSpider

from reddit.items import   ImageItem



from sqlalchemy.orm import sessionmaker
import re



def all_artikels_url():
    engine = db_connect()

    Session = sessionmaker(bind=engine)
    session = Session()
    all_artikel = session.query(Artikel).all()
    only_url = [re.sub('[{}]','',url.artikel_link) for url in all_artikel]

    return only_url


class MorgenPostSpider(CrawlSpider):
    name = "images"
    allowed_domains = ["img.morgenpost.de", "www.morgenpost.de"]
    start_urls = all_artikels_url()
    #start_urls = ['http://www.morgenpost.de/wirtschaft/article123706116/Polen-sollen-sich-mit-Boykott-an-Briten-raechen.html']


    def parse(self, response):


        image_list = response.xpath('//div[@class="article__header"]/figure')
        items=[]
        if len(image_list)>0:

            for selector in image_list:

                item = ImageItem()



                item['image_link'] = selector.xpath('picture/source/@srcset').extract()[0]
                hash = hashlib.sha1(str(item['image_link'])).hexdigest()
                caption = selector.xpath('figcaption/p/text()').extract()
                item['image_caption']=re.sub('\s+','',caption[0])
                #item['image_caption']= 'fuck Simone'
                item['image_hash'] = hash
                item['artikel_link'] = response.url
                item['artikel_hash'] = hashlib.sha1(response.url).hexdigest()
                #pdb.set_trace()
                items.append(item)

            return items
