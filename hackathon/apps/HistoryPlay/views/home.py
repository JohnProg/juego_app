import json
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from apps.HistoryPlay.models.Category import Category
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

    def get_context_data(self, **kwargs):
        context = {}
        context['category'] = self.get_categories()
        return context


class HistoryPlayJsonView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(HistoryPlayJsonView, self).dispatch(request, *args, **kwargs)

    def get_history_play(self):
        data = []
        categories = Category.objects.all()
        for category in categories:
            data.append({
                'id': category.id,
                'name': category.name
            })
        return data

    def get(self, request, *args, **kwargs):
        response = {}
        response['category'] = self.get_categories()
        return HttpResponse(json.dumps(response))