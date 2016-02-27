#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Philipp Nahratow'
SITENAME = "flp's website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# my settings
THEME = "theme/pelican-bold"
MD_EXTENSIONS = ['toc']

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
         ('You can modify those links in your config file', '#'),)                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                               
# Social widget                                                                                                                                                                                                                                                                
SOCIAL = (('github', 'https://github.com/pnahratow'),                                                                                                                                                                                                                          
        ('mail', 'mailto:philippnahratow@gmail.com'))      

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
