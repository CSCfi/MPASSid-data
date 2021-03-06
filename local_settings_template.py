# -*- encoding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2014-2015 Haltu Oy, http://haltu.fi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'authdata',
    'USER': 'authdata',
    'PASSWORD': 'authdata',
  }
}

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
      'level': 'DEBUG',
      'handlers': ['console', 'file'],
    },
    'formatters': {
      'normal': {
        'format': '%(asctime)s %(levelname)s %(name)s %(thread)d %(lineno)s %(message)s %(data)s'
      },
      'verbose': {
        'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s %(data)s'
      },
    },
    'filters': {
      'default': {
        '()': 'project.logging_helpers.Filter',
      },
    },
    'handlers': {
      'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        'formatter': 'verbose',
        'filters': ['default'],
      },
      'file': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': 'authdata.log',
        'formatter': 'verbose'
      },
    },
    'loggers': {
      'django': {
        'level': 'WARNING',
        'handlers': ['console', 'file'],
        'propagate': True,
      },
      'authdata': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
        'propagate': False,
      },
      '': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
        'propagate': False,
      },
    },
}
