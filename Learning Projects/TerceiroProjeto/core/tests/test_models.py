import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path, Servicos, Cargo, Features, Funcionario

class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServicosTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servicos')

    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class FeaturesTestCase(TestCase):
    def setUp(self):
        self.features = mommy.make('Features')

    def test_str(self):
        self.assertEqual(str(self.features), self.features.nome)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)