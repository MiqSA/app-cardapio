from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Prato


def index(request):
    pratos = Prato.objects.order_by('-date_prato').filter(publicada=True)
    dados = {'pratos': pratos}

    return render(request, 'index.html', dados)


def cardapio(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)

    prato_a_exibir = {
        'prato': prato
    }
    return render(request, 'cardapio.html', prato_a_exibir)


def buscar(request):
    lista_pratos = Prato.objects.order_by('-date_prato').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_pratos = lista_pratos.filter(nome_prato__icontains=nome_a_buscar)

    dados = {'pratos': lista_pratos}
    return render(request, 'buscar.html', dados )
