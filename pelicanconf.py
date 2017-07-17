#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Florian Le Bourdais'
SITENAME = u"Frolian's blog"
SITESUBTITLE = u'xkcd, Python, math and beyond'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'

DEFAULT_LANG = 'en'
LOCALE = 'en'

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
THEME = 'pelican-clean-blog/'

# social
SOCIAL = (('twitter', 'https://twitter.com/frolianlb'),
          ('github', 'https://github.com/flothesof'))

# menu with items: archives, about me
MENUITEMS = [('Archives', '/archives.html')]
                
# code highlighting (check README of theme for more info)
COLOR_SCHEME_CSS = 'github.css'

# notebook integration using liquid tags
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['liquid_tags.img', 'pelican-ipynb.liquid']
NOTEBOOK_DIR = 'posts'
# we're not injecting the notebook header, because it pollutes the blog style
#EXTRA_HEADER = open('_nb_header.html').read()
# however, to get mathjax properly working in the notebook posts, we need this basic header
#header_name = 'custom_header.html'
header_name = '_custom_nb_header.html'
if not os.path.exists(header_name):
    import warnings
    warnings.warn("Custom header not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open(header_name).read()

# rendering mathjax in markdown posts directly
PLUGINS.append('render_math')

# since upgrade to Pelican 3.7, to prevent KeyError
# MD_EXTENSIONS = []
