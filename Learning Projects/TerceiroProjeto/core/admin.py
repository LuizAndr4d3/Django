from django.contrib import admin
from .models import Cargo, Funcionario, Servicos, Features
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
    
@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Features)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')

