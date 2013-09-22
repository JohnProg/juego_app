# -*- coding: utf-8 -*-
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


class SignUp(View):
    MSG_ERR_EMAIL_EXIST = 'The email you entered already exist.'
    MSG_ERR_REGISTRATION_FAILED = 'Registration is not possible right now.'
    MSG_ERR_MANUFACTURER_NAME_EXIST = 'Manufacturer Name already taken.'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SignUp, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user:
                pass
                #devolver json que usuario ya existe
        except ObjectDoesNotExist:
            pass
        user = User.objects.create_user('john', email, password)

    def login_and_authenticate(self, user, manufacturer):
        user = auth.authenticate(
            username=user.username, password=user.password)
        if user is not None and user.is_active:
            auth.login(self.request, user)
