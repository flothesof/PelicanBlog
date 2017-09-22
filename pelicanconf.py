#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Florian Le Bourdais'
SITENAME = u"Frolian's blog"
SITESUBTITLE = u'standing on the shoulders of PyGiants'
SITEURL = 'http://localhost:8000'

PATH = 'content'

# localization: dates and formatting
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'fr': '%d/%m/%Y',
}

DEFAULT_LANG = 'en'
LOCALE = ('usa', 'en_US', 'fr', 'fr_FR')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# activate feed summary (smaller sized feeds)
FEED_USE_SUMMARY = True	

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# custom theme
THEME = './theme/'

# social
SOCIAL = (('twitter', 'https://twitter.com/frolianlb'),
          ('github', 'https://github.com/flothesof'))

# specify markup language as markdown
MARKUP = ['md']

# menu with items: archives, about me
SHOW_ARCHIVES = True
ABOUT_PAGE = 'pages/about.html' 
                
# code highlighting (check README of theme for more info)
COLOR_SCHEME_CSS = 'github.css'

# notebook integration using liquid tags
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['liquid_tags.img', 'pelican-ipynb.liquid']

# rendering mathjax in markdown posts directly
PLUGINS.append('render_math')

ENABLE_MATHJAX = True
