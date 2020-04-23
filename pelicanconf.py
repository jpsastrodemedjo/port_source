#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Peter Sastrodemedjo'
SITENAME = 'JP'
SITEURL = ''

PATH = 'content'

OUTPUT_PATH = '../output'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['img','extra']
USE_SHORTCUT_ICONS=True

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About me', '/pages/about-me/index.html'),
    ('Trainee Blog', '/category/trainee-blog/index.html'),
    ('Resources','/category/resources/index.html'))

THEME = 'pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

PLUGIN_PATHS = ['plugins/pelican-plugins', ]
PLUGINS = ['i18n_subsites','sitemap','pelican-ipynb.markup','tipue_search','tag_cloud']

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

MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True

BOOTSTRAP_THEME = 'flatly'

PYGMENTS_STYLE = 'github'

ARTICLE_PATHS = ['Articles']
PAGE_PATHS = ['pages']

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# DISPLAY_TAGS_ON_SIDEBAR = True
# DISPLAY_TAGS_INLINE = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/jpsastrodemedjo'),
         ('Anaconda Cloud', 'https://anaconda.org/jpsastrodemedjo/dashboard'),)

# Social widget
# SOCIAL = ('Google Calendar','https://calendar.google.com/calendar/b/1/r')

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True