from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.views import IndexView

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.nome = 'nome'
        self.email = 'admin@admin.com'
        self.assunto = 'assunto'
        self.mensagem = 'mensagem'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.cliente = Client()
    
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
            'nome': 'invalido',
            'email': 'teste invalido'
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)