#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matthieu Falce'
SITENAME = u'true.falce.net'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'fr': ('fr_FR.utf8','%d %b %Y'),
}

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                'toc(permalink=true)']
PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = [
    'sitemap',
    # 'extract_toc',
    'tipue_search',
    'liquid_tags.img',
    'neighbors',
    'latex',
    'related_posts',
    'assets',
    'share_post',
    ]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/MatthieuFalce'),
          ('Github', 'http://github.com/ice3'),
           ('Email', 'mailto:falce.matthieu+contact@gmail.com')
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

THEME=u'elegant'
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_URL = "true.falce.net"
CONTACT_URL = "matthieu.falce.net"
GALLERY_URL = "photos.falce.net"

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Blog', INDEX_URL),
                    ("Contact / A propos", CONTACT_URL),
                    ("Gallerie Photo", GALLERY_URL),
                    )
