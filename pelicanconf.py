#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ro Avery'
SITENAME = 'ro-bot blog'
SITEURL = ''

THEME = 'themes/medius'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
         #('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Custom home page
# DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
# PAGINATED_DIRECT_TEMPLATES = (('blog',))
# TEMPLATE_PAGES = {'home.html','index.html',}

# Medius-specific
MEDIUS_AUTHORS = {
    "Ro Avery": {
        "description": """
            Ro is a lazy software developer and hobbyist game designer
        """,
        "links": (('twitter-square', 'http://twitter.com/r0botblues'),),
    }
}

MEDIUS_CATEGORIES = {
    "30 Day Project": {
        "description": "Posts relating to a project undertaken over a period of thirty days - an attempt to Get Stuff Done",
		"logo": 'images/30-day.jpg',
		"thumbnail": 'images/30-day.jpg'
    }
}
