# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.HistoryPlay.views.player import game
from apps.HistoryPlay.views.player import map

urlpatterns = patterns('',

    url(r'^map/$', map.MapRoute.as_view(),
        name='map'),

    url(r'^question/(?P<place>\d+)$', game.QuestionView.as_view(),
        name='question'),

    url(r'^save-game/$',
        game.SaveGameJsonView.as_view(),
        name='save-game'),

    #JSON RESPONSE
    url(r'^json/history-place/(?P<category>\d+)/$',
        map.HistoryPlayJsonView.as_view(),
        name='json-history-play'),

    url(r'^json/question/(?P<place>\d+)/$',
        game.QuestionJsonView.as_view(),
        name='json-question-place'),

    url(r'^json/category/$',
        map.CategoryJsonView.as_view(),
        name='json-category')

    )