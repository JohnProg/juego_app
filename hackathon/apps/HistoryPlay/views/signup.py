# -*- coding: utf-8 -*-
import json
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import Http404, HttpResponse
from apps.HistoryPlay.models.Profile import Profile
from apps.HistoryPlay.models.Place import Place
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from apps.HistoryPlay.models.HistoryPlay import HistoryPlay


class SignUp(View):
    MSG_ERR_EMAIL_EXIST = 'The email you entered already exist.'
    MSG_ERR_REGISTRATION_FAILED = 'Registration is not possible right now.'
    MSG_ERR_MANUFACTURER_NAME_EXIST = 'Manufacturer Name already taken.'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SignUp, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = {}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email )
            if user:
                response['status'] = 'ERROR'
                response['message'] = 'correo ya existe'
                return HttpResponse(json.dumps(response))
        except ObjectDoesNotExist:
            pass

        try:
            user = User.objects.get(username=username)
            if user:
                response['status'] = 'ERROR'
                response['message'] = 'username ya existe'
                return HttpResponse(json.dumps(response))
        except:
            pass
        user = User.objects.create_user(username, email, password)

        profile = self.create_profile(user)
        self.create_default_data(profile)
        user = auth.authenticate(username=user.username, password=password)
        auth.login(self.request, user)

        response['status'] = 'OK'
        response['message'] = 'Bienvenido'
        return HttpResponse(json.dumps(response))

    def create_profile(self, user):
        profile = Profile()
        profile.user = user
        profile.save()
        return profile

    def create_default_data(self, profile):
        try:
            place = Place.objects.get(step=1)
            history_play = HistoryPlay()
            history_play.place = place
            history_play.profile = profile
            history_play.progress = 0
            history_play.save()
        except:
            print('no default data')

    def login_and_authenticate(self, user):
        user = auth.authenticate(
            username=user.username, password=user.password)
        import pdb;pdb.set_trace()
        if user is not None and user.is_active:
            auth.login(self.request, user)
