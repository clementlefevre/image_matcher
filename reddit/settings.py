# -*- coding: utf-8 -*-

# Scrapy settings for reddit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'reddit'

SPIDER_MODULES = ['reddit.spiders']

ITEM_PIPELINES = {'reddit.pipelines.MorgenPostImagesPipeline': 300}

#NEWSPIDER_MODULE = 'reddit.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'reddit (+http://www.yourdomain.com)'

FEED_URI = 'logs/%(name)s/%(time)s.csv'
FEED_FORMAT = 'csv'

IMAGES_STORE = 'images/'
IMAGES_EXPIRES = 90  # 90 days of delay for image expiration

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'postgres',  # fill in your username here
	'password': 'postgres',  # fill in your password here
	'database': 'amin1'
}

DEFAULT_REQUEST_HEADERS = {
	'Referer': 'http://www.google.com'

}

