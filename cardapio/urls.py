from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:prato_id>', views.cardapio, name='cardapio')
]