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

# Disqus integration 
DISQUS_SITENAME = "froliansblog"

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'
FEED_MAX_ITEMS = 10

DELETE_OUTPUT_DIRECTORY = True

# Google Analytics
GOOGLE_ANALYTICS = 'UA-68753870-1'
