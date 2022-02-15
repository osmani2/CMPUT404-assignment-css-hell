AUTHOR = 'Natasha Osmani'
SITENAME = 'nahmed2 Assignment 3'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_PATHS = ['homepage']
DELETE_OUTPUT_DIRECTORY = True
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = 'gutenberg/{slug}.html'
ARTICLE_SAVE_AS = 'gutenberg/{slug}.html'
PAGE_URL = 'homepage/{slug}.html'
PAGE_SAVE_AS = 'homepage/{slug}.html'


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'templates/mytheme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True