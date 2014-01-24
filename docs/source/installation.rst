Installation
------------

To install FeedMe simply:

    pip install django-feedme

Add ``feedme`` to your installed apps.  Add route a url to ``feedme.urls``

Add the url name 'auth_login' to your login URL so that the template has a login URL to point to.

Make sure to syncdb or migrate the app::

    python manage.py syncdb
    python manage.py migrate


If you want to use Celery for fetching (Recommended) then add::

    FEED_UPDATE_CELERY = True

to your settings file.  Make sure you've installed and configured Celery properly.  The syntax used should be good
for both Celery 2 and 3.

This app bundles static and works out of the box with django static files.  If you aren't collecting static
you'll need to copy the static directory to where ever you serve static from.

You need to provide a login view that Feedme can use to provide a login link when the user isn't logged in.  This is
referenced as ``auth_login`` by name.

    url(r'^something/$', your.login.view, name='auth_login')

You will also need to provide a LOGIN_URL as well.

Dependencies
------------

Django Feedme requires Django 1.5 or above.

Feedme also requires the use of the django-bootstrap-static library for some static files.  It is bundled in setup.py so by installing this package
it should already be downloaded to your machine.  In order to have the bootstrap files picked up by your static files hanlder, you'll need to add
```bootstrap``` to installed apps.  This will alow Django's static files to pick up the boostrap files.


Celery Beat
-----------

To make use of the Celery beat schedule to automatically update feeds at given intervals, open your settings file and
enter something like the following::

    import datetime


    CELERYBEAT_SCHEDULE = {
        "feed-updates": {
            "task": "update_all_feeds",
            "schedule": datetime.timedelta(hours=1),
            },
        }

More documentation for Celery can be found at the CeleryProject.