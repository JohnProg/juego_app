# -*- coding: utf-8 -*-
import json
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


class LoginBuyerView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LoginBuyerView, self).dispatch(request, *args, **kwargs)

    def check_role_buyer(self, roles):
        for role in roles:
            if role == User.ROLE_BUYER:
                return True

    def post(self, request, *args, **kwargs):
        response = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(
            username=email,
            password=password
        )
        if user is not None and user.is_active and (len(user.get_roles()) > 0):
            user_roles = user.get_roles()
            result = self.check_role_buyer(user_roles)
            if result:
                response['status'] = 'OK'
                response['message'] = 'Login successfully'
            else:
                response['status'] = 'OK'
                response['message'] = 'Incorrect Email or Password'
        else:
            response['status'] = 'ERROR'
            response['message'] = 'Incorrect Email or Password'

        return HttpResponse(json.dumps(response))