from django.views.generic import TemplateView


class HomeVIe(TemplateView):
    template_name = 'home.html'