#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ilya Bezrukov'
SITENAME = u'Personal Public Blog'
SITEURL = 'http://dgihangesht.github.io'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PDF_GENERATOR = False

OUTPUT_PATH = 'articles/'
PATH = 'content'
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
NEWEST_FIRST_ARCHIVES = True
METADATA = u'Personal Public Blog'
THEME = "pelican-octopress-theme"
STATIC_PATHS = ['images',]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = 'http://dgihangesht.github.io'
FEED_RSS = 'feeds/rss.xml'
FEED_ATOM = 'feeds/atom.xml'
FEED_MAX_ITEMS = 3

#Pages
DISPLAY_PAGES_ON_MENU  = False

# Social Links
SOCIAL = (('github', 'http://github.com/dgihangesht'),
            ('twitter', 'http://twitter.com/dgihan'),)


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)





