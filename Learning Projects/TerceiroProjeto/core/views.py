from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class Error400View(TemplateView):
    template_name = '404.html'

class Error500View(TemplateView):
    template_name = '500.html'