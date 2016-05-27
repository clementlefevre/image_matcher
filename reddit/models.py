#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings
from sqlalchemy.orm import relationship

DeclarativeBase = declarative_base()



def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))


def create_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine,checkfirst=True)





class Artikel(DeclarativeBase):

    __tablename__ = "artikel"

    id = Column(Integer, primary_key=True)
    artikel_hash = Column('artikel_hash', String)
    artikel_title = Column('artikel_title', String, nullable=True)
    artikel_link = Column('artikel_link', String, nullable=True)
    artikel_date = Column('artikel_date', String, nullable=True)
    #images = relationship("Image")


class Image(DeclarativeBase):
    __tablename__ = "image"
    image_hash =  Column('image_hash', String,primary_key=True )
    image_link = Column('image_link', String)
    image_caption = Column('image_caption', String)
    artikel_hash = Column('artikel_hash', String)
    artikel_link = Column('artikel_link', String)

    #artikel_hash =  Column(Integer, ForeignKey('artikel.hash'))



