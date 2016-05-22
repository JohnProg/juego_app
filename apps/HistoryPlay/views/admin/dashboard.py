# -*- coding: utf-8 -*-
from apps.common.view import LoginRequiredMixin
from django.views.generic import TemplateView


class AdminDashboardTemplateView(TemplateView, LoginRequiredMixin):
    template_name = 'admin/dashboard.html'
    superAdmin = True
