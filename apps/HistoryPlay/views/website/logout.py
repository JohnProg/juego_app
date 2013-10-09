# -*- coding: utf-8 -*-
import json
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth


class LogoutView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        response = {
            'status': 'OK'
        }
        return HttpResponse(json.dumps(response))