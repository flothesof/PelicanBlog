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

# activate RSS feed (but not Atom)
FEED_DOMAIN = SITEURL
FEED_RSS = 'rss.xml'

# activate feed summary (smaller sized feeds)
RSS_FEED_SUMMARY_ONLY = True	

# show feed icon in theme
SHOW_FEED = True


# Start from fresh folder
DELETE_OUTPUT_DIRECTORY = True

# Google Analytics
GOOGLE_ANALYTICS = 'UA-68753870-1'

