# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from reddit.models import db_connect,  Artikel, create_table, Image
from sqlalchemy.orm import sessionmaker


class RedditPipeline(object):
    def process_item(self, item, spider):
        item['title'] = ''.join(item['title']).upper()

        return item


class MorgenPostPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates deals table.

        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        artikel = Artikel(**item)

        try:
            session.add(artikel)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

class MorgenPostImagesPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates deals table.

        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        image = Image(**item)

        try:
            session.merge(image)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item