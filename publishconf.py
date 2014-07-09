#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://flothesof.github.io'
RELATIVE_URLS = False

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

DELETE_OUTPUT_DIRECTORY = True


