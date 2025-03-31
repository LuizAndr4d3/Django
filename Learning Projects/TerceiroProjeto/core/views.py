from django.views.generic import TemplateView
from .models import Funcionario, Servicos, Features

class IndexView(TemplateView): 
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all() #ordem aleatória
        context['funcionarios'] = Funcionario.objects.all()
        context['features'] = Features.objects.all()[:3]
        context['features1'] = Features.objects.all()[3:]

        return context





class Error400View(TemplateView):
    template_name = '404.html'

class Error500View(TemplateView):
    template_name = '500.html'