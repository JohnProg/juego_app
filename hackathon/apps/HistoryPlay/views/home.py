import json
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from apps.HistoryPlay.models.Category import Category
from apps.HistoryPlay.models.Profile import Profile
from apps.HistoryPlay.models.Question import Question
from apps.HistoryPlay.models.Answer import Answer
from apps.HistoryPlay.models.HistoryPlay import HistoryPlay
from apps.HistoryPlay.models.Place import Place
from apps.common.view import LoginRequiredMixin
from django.views.generic import RedirectView


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


class QuestionView(TemplateView, LoginRequiredMixin):
    template_name = 'question.html'

    def get_context_data(self, **kwargs):
        context = {}
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
            place__status=Place.STATUS_ACTIVE,
        )
        for play in history_plays:
            data.append({
                'id':play.place.id,
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
                'id':question.id,
                'name':question.name,
                'image':question.image,
                'type':question.type,
                'answer': self.get_answer(question)
            })
        return data

    def get_answer(self,question):
        data = []
        answers = Answer.objects.filter(question=question)
        for answer in answers:
            data.append({
                'id':answer.id,
                'name':answer.name,
                'image':answer.image,
                'is_correct':answer.is_correct
            })
        return data

    def get(self, request, *args, **kwargs):
        response = {}
        place = kwargs.get('place')
        response['question'] = self.get_history_place(place)
        return HttpResponse(json.dumps(response))


class CategoryJsonView(View, LoginRequiredMixin):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryJsonView, self).dispatch(request, *args, **kwargs)

    def get_category(self):
        data = []
        categories = Category.objects.all()
        for categori in categories:
            data.append({
                'id':categori.id,
                'name':categori.name
            })
        return data

    def get(self, request, *args, **kwargs):
        response = {}
        response['category'] = self.get_category()
        return HttpResponse(json.dumps(response))


class SaveGameJsonView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SaveGameJsonView, self).dispatch(request, *args, **kwargs)

    def save_game(self, place_id, percentaje):
        try:

            data = []
            profile = Profile.objects.get(user=self.request.user)
            place = Place.objects.get(pk=place_id)
            history_plays = HistoryPlay.objects.get(
                profile=profile,
                place=place
            )
            if percentaje == 100:
                history_plays.status = HistoryPlay.STATUS_COMPLETE
                history_plays.progress = 100
                step = int(history_plays.place.step)
                step = step +1
                place = Place.objects.get(step=step)
                next_play = HistoryPlay()
                next_play.profile = profile
                next_play.place = place
                next_play.progress = 0
                next_play.save()

            if history_plays.progress < percentaje:
                history_plays.progress = percentaje
            history_plays.save()

            data.append({
                'response':'OK',
            })
        except:
            data.append({
                'response':'ERROR',
            })
        return data

    def get_answer(self,question):
        data = []
        answers = Answer.objects.filter(question=question)
        for answer in answers:
            data.append({
                'id':answer.id,
                'name':answer.name,
                'image':answer.image,
                'is_correct':answer.is_correct
            })
        return data

    def get(self, request, *args, **kwargs):
        response = {}
        place = kwargs.get('place')
        percentaje = kwargs.get('percentaje')
        response['question'] = self.save_game(place,percentaje)
        return HttpResponse(json.dumps(response))
