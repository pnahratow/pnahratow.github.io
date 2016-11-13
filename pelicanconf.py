#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Philipp Nahratow'
SITENAME = "flp's website"
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT =('%Y-%m-%d')

# my settings
THEME = "theme/pelican-bold"
MD_EXTENSIONS = ['codehilite(css_class=highlight,linenums=False)','toc']

STATIC_PATHS = [
    'images', 
    'extra/robots.txt', 
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DISQUS_SITENAME = "flpswebsite"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll                                                                                                                                                                                                                                                                     
LINKS = (('Pelican', 'http://getpelican.com/'),                                                                                                                                                                                                                                
         ('Python.org', 'http://python.org/'),                                                                                                                                                                                                                                 
         ('Jinja2', 'http://jinja.pocoo.org/'),                                                                                                                                                                                                                                
        )                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                               
# Social widget                                                                                                                                                                                                                                                                
SOCIAL = (('github', 'https://github.com/pnahratow'),                                                                                                                                                                                                                          
          # ('mail', 'mailto:philippnahratow@gmail.com')
         )      

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['extended_sitemap']
