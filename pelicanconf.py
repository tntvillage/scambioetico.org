#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DISPLAY_PAGES_ON_MENU = True
LOAD_CONTENT_CACHE = False

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}


AUTHOR = u'scambioetico'
SITENAME = u'Scambioetico.org'
SITEURL = ''
SITESUBTITLE = 'dal 2004<br/>in Italia'

BANNER="Comunità<br/>e Conoscenza"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'wp-content']

# Blogroll
LINKS = (('Chi siamo', "/pages/tntvillage-chi-siamo.html"),
         ('Lo Scambio Etico<br/><span class="text-style1">spiegato bene</span>', 'https://medium.com/@exedre/tntvillage-spiegato-bene-d7ffb62267db?fbclid=IwAR3oEYAlcoB3KG9WHAeE62lqFiZRZItfPjQ2zIi8Swq3IHbQRb6uhh60S-0'),
         ('TNTVillage', 'http://tntvillage.scambioetico.org/'),
         ('Forum', 'http://forum.tntvillage.scambioetico.org/'),
         ('Releaselist', 'http://www.tntvillage.scambioetico.org/?releaselist'),
         ('Archivio', 'http://www.tntvillage.scambioetico.org/archivio'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/tnt_village'),
          ('Twitter', 'https://twitter.com/scambioetico'),
          ('Facebook Group', 'https://www.facebook.com/groups/tntvillage'),
          ('Facebook Page', 'https://www.facebook.com/tntvillage/'),)


# DEFAULT_PAGINATION = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/html5up'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'it': '%d-%m-%Y',
}

LOCALE = ('it_IT',
          )


