from __future__ import absolute_import, unicode_literals

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wagtailcmsdemodb',
        'USER': 'wagtailcmsdemouser',
        'PASSWORD': 'w4gt41li5a,
        'HOST': 'timcknowles-769.postgres.pythonanywhere-services.com',
        'PORT': 10769,
    }
}
# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
