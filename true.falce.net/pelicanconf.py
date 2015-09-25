#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matthieu Falce'
SITENAME = u'true.falce.net'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/MatthieuFalce'),
         )

DEFAULT_PAGINATION = 10

#themes :
#  elegant             ++++ (pas de résumé du tout, juste le titre) http://oncrashreboot.com/elegant-best-pelican-theme-features
#  pelican-twitchy     ++++
#  aboutwilson         ++++

#  cid                 +++ (minimaliste)
#  nikhil-theme        +++
#  fresh               +++ (minimaliste)
#  sundown             +++
#  svbhack             +++

THEME=u'cid'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
