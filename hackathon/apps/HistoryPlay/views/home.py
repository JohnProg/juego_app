import json
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from apps.HistoryPlay.models.Category import Category
from apps.HistoryPlay.models.Profile import Profile
from apps.HistoryPlay.models.Question import Question
from apps.HistoryPlay.models.HistoryPlay import HistoryPlay
from apps.HistoryPlay.models.Place import Place
from apps.common.view import LoginRequiredMixin


class HomeVIe(TemplateView):
    template_name = 'home.html'


class MapRoute(TemplateView, LoginRequiredMixin):
    template_name = 'map.html'

    def get_categories(self):
        data = []
        categories = Category.objects.all()
        for category in categories:
            data.append({
                'id': category.id,
                'name': category.name
            })
        return data

    def get_profile(self):
        data = []
        profile = Profile.objects.get(user=self.request.user)
        data.append({
            'name': profile.name,
            'address': profile.address
        })
        return data

    def get_context_data(self, **kwargs):
        context = {}
        context['category'] = self.get_categories()
        context['profile'] = self.get_profile()
        return context


class HistoryPlayJsonView(View, LoginRequiredMixin):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(HistoryPlayJsonView, self).dispatch(request, *args, **kwargs)

    def get_history_place(self, request):
        data = []
        profile = Profile.objects.get(user=self.request.user)
        history_plays = HistoryPlay.objects.filter(
            profile=profile,
            place__status=Place.STATUS_ACTIVE
        )
        for play in history_plays:
            data.append({
                'id':play.id,
                'progress':play.progress,
                'place':play.place.name,
                'latitud':play.place.latitud,
                'longitud':play.place.longitud,
                'step':play.place.step,
                'area':play.place.area,
                'description':play.place.description,
                'address':play.place.address,
                'district':play.place.district,
                'phone':play.place.phone,
                'web_page':play.place.web_page,
                'schedule':play.place.schedule,
                'cost':play.place.cost,
            })
        return data

    def get(self, request, *args, **kwargs):
        response = {}
        response['places'] = self.get_history_place(request)
        return HttpResponse(json.dumps(response))


class QuestionJsonView(View, LoginRequiredMixin):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(QuestionJsonView, self).dispatch(request, *args, **kwargs)

    def get_history_place(self, place_id):
        data = []
        place = Place.objects.get(pk=place_id)
        questions = Question.objects.filter(
            place=place
        )
        for question in questions:
            data.append({
                'name':question.name,
                'image':question.image,
                'type':question.type,
                'answer': []
            })
        return data

    def get(self, request, *args, **kwargs):
        response = {}
        place = kwargs.get('place')
        response['question'] = self.get_history_place(place)
        return HttpResponse(json.dumps(response))