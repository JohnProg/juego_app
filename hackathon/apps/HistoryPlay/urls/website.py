# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.HistoryPlay.views import home as h
from apps.HistoryPlay.views import signup as s
from apps.HistoryPlay.views import logout as o
from apps.HistoryPlay.views import login as l

urlpatterns = patterns('',
    url(r'^sign_up/$', s.SignUp.as_view(),
        name='sign_up'),
    url(r'^login/$',l.LoginView.as_view(),
        name='login'),
    url(r'^logout/$',o.LogoutView.as_view(),
        name='logout'),
    url(r'^$', h.HomeVIe.as_view(),
        name='home'),
    url(r'^map/$', h.MapRoute.as_view(),
        name='map'),
    url(r'^question/(?P<place>\d+)$', h.QuestionView.as_view(),
        name='question'),

    #JSON RESPONSE
    url(r'^json/history-place/(?P<category>\d+)/$',
        h.HistoryPlayJsonView.as_view(),
        name='json-history-play'),

    url(r'^json/question/(?P<place>\d+)/$',
        h.QuestionJsonView.as_view(),
        name='json-question-place'),

    url(r'^json/category/$',
        h.CategoryJsonView.as_view(),
        name='json-category'),
)
