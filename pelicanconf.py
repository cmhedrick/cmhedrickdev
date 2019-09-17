#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Christopher Hedrick'
SITENAME = 'cmhedrick.dev'
SITEURL = ''
SITESUBTITLE = 'A developer of infinite developments.'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

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
# SOCIAL = ((('Github', 'https://github.com/cmhedrick'))

SOCIAL = (('Github', 'https://github.com/cmhedrick'),
          ('Twitter', 'http://twitter.com/cmhedrick')
          )

DEFAULT_PAGINATION = 6
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = '/home/drake/proj/cmhedrickdev/env/lib/python3.6/site-packages/pelican/themes/attila'

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

# Plugins

PLUGIN_PATHS = [
    '/home/drake/proj/pelican-plugins'
]

PLUGINS = [
    'sitemap',
    'neighbors',
    'assets'
]

# Sitemap
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

# Theme specific settings

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COVER and use cover in individual articles.
# HEADER_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COLOR and use color in individual articles.
# HEADER_COLOR = 'black'

# To set background image for the home page.
# HOME_COVER = 'static/images/servers.jpg'
# HOME_COLOR = '#343434'

# Custom Header

# HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png',
#                         'general': 'https://casper.ghost.org/v1.0.0/images/writing.jpg'}
HEADER_COVERS_BY_TAG = {}


AUTHORS_BIO = {
    "cmhedrick": {
        "name": "Chris Hedrick",
        "cover": "",
        "image": "https://avatars3.githubusercontent.com/u/4511891?s=460&v=4",
        "website": "https://cmhedrick.dev",
        "linkedin": "https://www.linkedin.com/in/christopher-hedrick/",
        "github": "https://github.com/cmhedrick",
        "location": "DC",
        "bio": "The Hannibal Lecter of Programming."
    }
}

CSS_OVERRIDE = ['static/css/global.css']

COLOR_SCHEME_CSS = 'monokai.css'
# HEADER_COLOR = 'black'
# HEADER_COVER = 'theme/images/home-bg.jpg'

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.loopcontrols',
        'jinja2.ext.i18n',
        'jinja2.ext.with_',
        'jinja2.ext.do'
    ]
}

PARTICLE = True
SITE_LOGO = '/static/images/logo-white.png'
