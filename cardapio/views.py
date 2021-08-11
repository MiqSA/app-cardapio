from django.shortcuts import render


def index(request):
    pratos = {
        1: 'Macarrão à Carbonara',
        2: 'Hamburguer',
        3: 'Pudim'
    }
    dados = {'nome_dos_pratos': pratos}

    return render(request, 'index.html', dados)


def cardapio(request):
    return render(request, 'cardapio.html')
