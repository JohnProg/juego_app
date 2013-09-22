# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.HistoryPlay.views import home as h

urlpatterns = patterns('',
    url(r'^$', h.HomeVIe.as_view(),
        name='home'),
    url(r'^map/$', h.MapRoute.as_view(),
        name='map'),
)
