from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:prato_id>', cardapio, name='cardapio'),
    path('buscar', busca, name='buscar'),
    path('cria/prato', cria_prato, name='cria_prato'),
    path('deleta/<int:prato_id>', deleta_prato, name='deleta_prato'),
    path('edita/<int:prato_id>', edita_prato, name='edita_prato'),
    path('atualiza_prato', atualiza_prato, name='atualiza_prato')
]