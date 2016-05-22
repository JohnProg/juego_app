# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.HistoryPlay.views.admin import dashboard

urlpatterns = patterns('',
        url(r'^dashboard/$', dashboard.AdminDashboardTemplateView.as_view(),
        name='admin_dashboard'),
    )