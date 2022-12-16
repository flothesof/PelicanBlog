#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Florian Le Bourdais'
SITENAME = u"Frolian's blog"
SITESUBTITLE = u'standing on the shoulders of PyGiants'
SITEURL = 'http://localhost:8000'

PATH = 'content'

#  localization: dates and formatting
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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# custom theme
THEME = './theme/'

# social
SOCIAL = (('mastodon', 'https://mastouille.fr/@frolian'),
          ('github', 'https://github.com/flothesof'))

# specify markup language as markdown
MARKUP = ['md']

# menu with items: archives, about me
SHOW_ARCHIVES = True
ABOUT_PAGE = 'pages/about.html'

# code highlighting (check README of theme for more info)
COLOR_SCHEME_CSS = 'github.css'

# declaring plugins to be used, some being pip installed (e.g. liquid_tags) and
# others being in the local repo folder (e.g. representative_image)
# `render_math` allows rendering mathjax in markdown posts directly
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['pelican.plugins.liquid_tags', 'representative_image', 'render_math']

# configuring liquid tags (img, and in particular notebook support)
LIQUID_TAGS = ["img", "notebook"]
NOTEBOOK_DIR = '.'
from io import open

if os.path.exists("_nb_header.html"):
    EXTRA_HEADER = open('_nb_header.html', encoding='utf-8').read()
else:
    print(
        "WARNING: the file _nb_header.html needed for Jupyter notebook output seems to be missing. This is a critical error.")

# static paths
STATIC_PATHS = ['images', 'pdfs', 'other']
