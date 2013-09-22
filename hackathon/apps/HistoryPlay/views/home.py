import json
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from apps.HistoryPlay.models.Category import Category


class HomeVIe(TemplateView):
    template_name = 'home.html'


class MapRoute(TemplateView):
    template_name = 'map.html'


class CategoryJsonView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryJsonView, self).dispatch(request, *args, **kwargs)

    def get_categories(self):
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