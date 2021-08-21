from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from cardapio.models import Prato


def cadastro(request):
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


def deleta_prato(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)
    prato.delete()
    return redirect('dashboard')


def campo_vazio(campo):
    return not campo.strip()


def senha_nao_sao_iguais(senha, senha2):
    return senha != senha2
