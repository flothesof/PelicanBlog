#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Site title and description
AUTHOR = u'Florian Le Bourdais'
SITENAME = u"Frolian's blog"
SITESUBTITLE = u'xkcd, Python, math and beyond'
SITEURL = 'http://flothesof.github.io'

# Timezone
TIMEZONE = "Europe/Paris"
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'

# Language option
DEFAULT_LANG = u'en'
LOCALE = ('usa',  # On Windows
    'en_US'     # On Unix/Linux
    )
	
# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
				('About me', '/pages/about-me.html')]
NEWEST_FIRST_ARCHIVES = True

# Github include settings
GITHUB_USER = 'flothesof'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Twitter
TWITTER_USER = 'frolianlb'
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# Number of articles per page
DEFAULT_PAGINATION = 10

# Static paths that will be copied to the website for content hosting
# 'images' static images linked to in blog articles
STATIC_PATHS = ['images']

# Path for IPython Notebook plugin
NOTEBOOK_DIR = 'posts'

# Theme and plugins
THEME = 'pelican-octopress-theme/'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'feed_summary']

# activate feed summary
FEED_USE_SUMMARY = True		   


DISPLAY_PAGES_ON_MENU = False

# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read()

 
#EXTRA_HEADER = open('_nb_header_minimal.html').read().decode('utf-8')
PYGMENTS_STYLE='default'
	
RELATIVE_URLS = True

# Disqus integration 
DISQUS_SITENAME = "froliansblog"
