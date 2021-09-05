from apps.cardapio.models import Prato
from django.shortcuts import render


def busca(request):
    lista_pratos = Prato.objects.order_by('-date_prato').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_pratos = lista_pratos.filter(nome_prato__icontains=nome_a_buscar)

    dados = {'pratos': lista_pratos}
    return render(request, 'pratos/buscar.html', dados)