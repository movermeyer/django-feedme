from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^', include('feedme.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, name='auth_login'),
]
