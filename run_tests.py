#!/usr/bin/env python

import os
import sys
from django.conf import settings
import django

DIRNAME = os.path.dirname(__file__)

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                           }
                   },
                   ROOT_URLCONF='feedme.urls',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'feedme',),
                   USE_TZ=True,
                   MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',
                                       'django.middleware.csrf.CsrfViewMiddleware'))



django.setup()
from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['feedme', ])

from django.core.management import call_command
call_command('validate')

if failures:
    sys.exit(failures)
