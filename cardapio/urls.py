from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:prato_id>', views.cardapio, name='cardapio'),
    path('buscar', views.buscar, name='buscar'),
    path('cria/prato', views.cria_prato, name='cria_prato'),
    path('deleta/<int:prato_id>', views.deleta_prato, name='deleta_prato'),
    path('edita/<int:prato_id>', views.edita_prato, name='edita_prato'),
    path('atualiza_prato', views.atualiza_prato, name='atualiza_prato')
]