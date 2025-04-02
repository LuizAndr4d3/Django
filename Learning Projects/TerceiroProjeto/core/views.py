from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Funcionario, Servicos, Features
from .forms import ContatoForm

class IndexView(FormView): 
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all() #ordem aleatória
        context['funcionarios'] = Funcionario.objects.all()
        context['features'] = Features.objects.all()[:3]
        context['features1'] = Features.objects.all()[3:]

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
