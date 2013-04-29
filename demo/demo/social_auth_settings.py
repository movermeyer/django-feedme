from settings import INSTALLED_APPS, TEMPLATE_CONTEXT_PROCESSORS

SOCIAL_AUTH_CREATE_USERS = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = True
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'twitter')
SOCIAL_AUTH_DEFAULT_USERNAME = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'

SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

LOGIN_ERROR_URL = '/login/error/'
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_ERROR_KEY = 'socialauth_error'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.stripe.StripeBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.contrib.instagram.InstagramBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.yandex.YandexBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.douban.DoubanBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.yandex.YandexOAuth2Backend',
    'social_auth.backends.contrib.yandex.YaruBackend',
    'social_auth.backends.contrib.mailru.MailruBackend',
    'social_auth.backends.contrib.dailymotion.DailymotionBackend',
    'social_auth.backends.contrib.shopify.ShopifyBackend',
    'social_auth.backends.contrib.stocktwits.StocktwitsBackend',
    'social_auth.backends.contrib.behance.BehanceBackend',
    'social_auth.backends.contrib.readability.ReadabilityBackend',
    'social_auth.backends.steam.SteamBackend',
    'social_auth.backends.reddit.RedditBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
)

INSTALLED_APPS += (
    'social_auth',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'social_auth.context_processors.social_auth_by_type_backends',
)
