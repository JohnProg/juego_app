from django.views.generic import TemplateView



class HomeVIe(TemplateView):
    template_name = 'home.html'


class MapRoute(TemplateView):
    template_name = 'map.html'