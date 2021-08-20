from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from cardapio.models import Prato


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('Senha não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('Email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request,user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    else:
        return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        pratos = Prato.objects.order_by('-date_prato').filter(pessoa=id)
        dados = {'pratos': pratos}
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


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
        return render(request, 'usuarios/cria_prato.html')