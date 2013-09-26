from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
     url(r'^',  include('apps.HistoryPlay.urls.website')),
)
urlpatterns += staticfiles_urlpatterns()
