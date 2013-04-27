Django Feed Me
==============

Django Feed Me is a replacement for Google Reader.  It keeps track of your feeds, fetches the RSS feeds
and parses them in an easy to read interface.  This is currently in development.  The app works as POC using the Django
Admin.  A seperate interface for adding feeds is coming down in the pipeline.


Installation
------------

To install FeedMe simply:

    pip install django-feedme

Add ``feedme`` to your installed apps.

If you want to use Celery for fetching (Recommended) then add:

    FEED_UPDATE_CELERY = True

to your settings file.


Documentation
-------------

Docs are coming soon on RTD.  For now please refer to this file and the Wiki/Issues in this project.


Additional Planned Features
---------------------------

* Import feeds from Google Reader
* Add and manage feeds from the front end (rather than Django Admin)