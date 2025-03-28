from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=11)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__ (self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.IntegerField('Telefone')

    def __str__ (self):
        return self.nome