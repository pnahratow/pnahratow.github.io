AUTHOR = 'Philipp Nahratow'
SITENAME = "flp's website"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ("projects", "../category/projects"),
)

# Social widget
SOCIAL = (
    # ('github', 'https://github.com/pnahratow'),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# my additional settings
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MARKDOWN = {
    "extension_configs": {
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}


PLUGINS = []

THEME = "Flex"
SITETITLE = SITENAME
SITELOGO = "/images/about/baseogre_avatar.png"
SITESUBTITLE = '"I like big pixels and I cannot lie"'
HOME_HIDE_TAGS = True
DISQUS_SITENAME = "flpswebsite"
THEME_COLOR = 'dark'
PYGMENTS_STYLE = 'paraiso-dark'
PYGMENTS_STYLE_DARK = 'paraiso-dark'
