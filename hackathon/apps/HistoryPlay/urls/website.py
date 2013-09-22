# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.HistoryPlay.views import home as h
from apps.HistoryPlay.views import signup as s
from apps.HistoryPlay.views import login as l

urlpatterns = patterns('',
    url(r'^sign_up/$', s.SignUp.as_view(),
        name='sign_up'),
    url(r'^login/$',l.LoginView.as_view(),
        name='login'),
    url(r'^$', h.HomeVIe.as_view(),
        name='home'),
    url(r'^map/$', h.MapRoute.as_view(),
        name='map'),

    #JSON RESPONSE
    url(r'^json/history-pllay/$',
        h.HistoryPlayJsonView.as_view(),
        name='json-history-play'),
)
