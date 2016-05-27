# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field



class ArtikelItem(Item):

    artikel_link = Field()
    artikel_title = Field()
    artikel_date = Field()

class PicItem(Item):
    image_urls = Field()
    images = Field()
    title = Field()
    url = Field()


class ImageItem(Item):
    image_hash = Field()
    image_link = Field()
    image_caption = Field()
    artikel_hash = Field()
    artikel_link = Field()

