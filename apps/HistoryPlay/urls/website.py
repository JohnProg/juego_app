# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.HistoryPlay.views.website import home
from apps.HistoryPlay.views.website import login
from apps.HistoryPlay.views.website import logout
from apps.HistoryPlay.views.website import signup

urlpatterns = patterns('',

    #Home views
    url(r'^$', home.HomeVIe.as_view(),
        name='home'),

    url(r'^sign_up/$', signup.SignUp.as_view(),
        name='sign_up'),

    url(r'^login/$', login.LoginView.as_view(),
        name='login'),

    url(r'^logout/$', logout.LogoutView.as_view(),
        name='logout'),

)
