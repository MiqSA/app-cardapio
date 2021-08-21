from django.urls import path
from . import views

urlpatterns = [
        path('cadastro', views.cadastro, name='cadastro'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('logout', views.logout, name='logout'),
        path('cria/prato', views.cria_prato, name='cria_prato'),
        path('deleta/<int:prato_id>', views.deleta_prato, name='deleta_prato')
]
