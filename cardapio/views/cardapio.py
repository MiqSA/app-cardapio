from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from cardapio.models import Prato
from django.contrib.auth.models import User
from django.contrib import auth, messages


def index(request):
    pratos = Prato.objects.order_by('-date_prato').filter(publicada=True)
    dados = {'pratos': pratos}

    return render(request, 'pratos/index.html', dados)


def cardapio(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)

    prato_a_exibir = {
        'prato': prato
    }
    return render(request, 'pratos/cardapio.html', prato_a_exibir)


def cria_prato(request):
    if request.method == 'POST':
        nome_prato = request.POST['nome_prato']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        preco = request.POST['preco']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_prato = request.FILES['foto_prato']
        user = get_object_or_404(User, pk=request.user.id)
        prato = Prato.objects.create(pessoa=user, nome_prato=nome_prato, ingredientes=ingredientes,
                                     modo_preparo=modo_preparo, preco=preco, rendimento=rendimento,
                                     categoria=categoria, foto_prato=foto_prato)
        prato.save()
        return redirect('dashboard')
    else:
        return render(request, 'pratos/cria_prato.html')


def edita_prato(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)
    prato_a_editar = {'prato': prato}
    return render(request, 'pratos/edita_prato.html', prato_a_editar)


def deleta_prato(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)
    prato.delete()
    return redirect('dashboard')


def atualiza_prato(request):
    if request.method == 'POST':
        prato_id = request.POST['prato_id']
        p = Prato.objects.get(pk=prato_id)
        p.nome_prato = request.POST['nome_prato']
        p.ingredientes = request.POST['ingredientes']
        p.modo_preparo = request.POST['modo_preparo']
        p.preco = request.POST['preco']
        p.rendimento = request.POST['rendimento']
        p.categoria = request.POST['categoria']
        if 'foto_prato' in request.FILES:
            p.foto_prato = request.FILES['foto_prato']

        p.save()
        return redirect('dashboard')
