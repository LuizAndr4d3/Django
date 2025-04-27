from model_mommy import mommy
from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCasse(TestCase):
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

        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)