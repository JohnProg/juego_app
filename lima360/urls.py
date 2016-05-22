from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
     url(r'^',  include('apps.HistoryPlay.urls.website')),

     url(r'^player/', include('apps.HistoryPlay.urls.player')),

     url(r'^admin/',  include('apps.HistoryPlay.urls.admin')),
)
urlpatterns += staticfiles_urlpatterns()
