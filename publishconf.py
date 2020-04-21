#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import sys
sys.path.append('.')
from pelicanconf import *

# use absolute URLs to publish (unlike pelicanconf)
RELATIVE_URLS = False

# put real site URL instead of localhost
SITEURL = 'http://flothesof.github.io'

# Disqus integration 
DISQUS_SITENAME = "froliansblog"

# activate RSS and ATOM feed
FEED_DOMAIN = SITEURL
FEED_RSS = 'rss.xml'
FEED_ATOM = 'atom.xml'

# the RSS and ATOM feeds both contain the full notebooks, which makes them big
# by limiting the number of items to the last ones, we try to limit this problem
FEED_MAX_ITEMS = 10

# by default, the RSS feed only holds the summary, but we want it to hold full articles
# (see http://docs.getpelican.com/en/latest/settings.html#feed-settings for details)
RSS_FEED_SUMMARY_ONLY = False	

# show feed icon in theme (this triggers a Jinja if)
SHOW_FEED = True


# Start from fresh folder
DELETE_OUTPUT_DIRECTORY = True

# Google Analytics
GOOGLE_ANALYTICS = 'UA-68753870-1'

