from django.db import models
#from django.contrib.auth.models import User
#from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=500)

    def __str__(self):
        return self.titulo