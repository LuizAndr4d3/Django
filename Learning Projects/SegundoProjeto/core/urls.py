from django.urls import path
from .views import index, contato, cadastrarproduto, exibirprodutos

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto', cadastrarproduto, name='cadastrarproduto'),
    path('produtos', exibirprodutos, name='exibirprodutos')
]