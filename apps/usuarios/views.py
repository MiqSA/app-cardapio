from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.cardapio.models import Prato


def cadastro(request):
    """"Cadastra uma nova pessoa no sistema."""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha_nao_sao_iguais(senha, senha2):
            messages.error(request, 'Senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    """"Loga pessoa no sistema."""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
    else:
        return render(request, 'usuarios/login.html')


def logout(request):
    """"Logout de uma pessoa do sistema."""
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    """"Mostra o cardapio."""
    if request.user.is_authenticated:
        id = request.user.id
        pratos = Prato.objects.order_by('-date_prato').filter(pessoa=id)
        dados = {'pratos': pratos}
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def campo_vazio(campo):
    """"Verifica se um campo é vazio."""
    return not campo.strip()


def senha_nao_sao_iguais(senha, senha2):
    """"Verifica se duas senhas são iguais."""
    return senha != senha2



