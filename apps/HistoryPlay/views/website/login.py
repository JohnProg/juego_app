# -*- coding: utf-8 -*-
import json
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth


class LoginView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(
            username=email,
            password=password
        )
        if user is not None:
            auth.login(self.request, user)
            response['status'] = 'OK'
            response['message'] = 'Login successfully'
            response['access'] = False
        else:
            response['status'] = 'ERROR'
            response['message'] = 'Incorrect Email or Password'

        return HttpResponse(json.dumps(response))