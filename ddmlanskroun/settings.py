# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Django settings for ddmlanskroun project.
"""

from django.utils.translation import ugettext_lazy as _
from leprikon.site.settings import *

# Application definition
INSTALLED_APPS = [
    'ddmlanskroun',
] + INSTALLED_APPS + [
    'cms_articles',
    #'cms_articles.import_wordpress',
    'aldryn_search',
]

CMS_TEMPLATES = [
    ('default.html', 'Výchozí'),
    ('home.html', 'Titulní stránka'),
]

# templates used to render plugin article
CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES = [
    ('default', 'Výchozí'),
]

# templates used to render plugin articles
CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES = [
    ('default', 'Výchozí'),
]

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': 'Obsah',
    },
    'footer': {
        'name': 'Patička',
    },
}

THUMBNAIL_ALIASES = {
    '': {
        'preview': {
            'size': (240, 10000),
        },
        'view': {
            'size': (760, 570),
        },
    },
}

# search settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'data', 'search'),
    },
    'cs': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'data', 'search'),
    },
}
