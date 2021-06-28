from django.shortcuts import render,redirect
from core.models import Imovel,Cliente,Corretor,Pagamento,Venda
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

#view que lista os imóveis
@login_required(login_url='/login/')
def lista_imoveis(request):
    lista_de_imoveis = Imovel.objects.all()
    dados = {"imoveis":lista_de_imoveis}
    return render(request,'imoveis.html',dados)

#Views relacionadas aos Clientes
@login_required(login_url='/login/')
def novo_cliente(request):
    return render(request,'novo-cliente.html')

@login_required(login_url='/login/')
def edit_cliente(request,id_cliente):
    dados = Cliente.objects.get(id=id_cliente)
    cliente = {"cliente": dados}
    return render(request,'edit-cliente.html',cliente)

@login_required(login_url='/login/')
def submit_cliente(request):
    if request.POST:
        id_cliente = request.POST.get('id')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        if id_cliente:
            cliente = Cliente.objects.get(id=id_cliente)
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.email = email
            cliente.telefone = telefone
            cliente.save()
        else:
            Cliente.objects.create(nome=nome,
                                   cpf=cpf,
                                   email=email,
                                   telefone=telefone)

    return redirect('/clientes/')

@login_required(login_url='/login/')
def delete_cliente(request,id_cliente):
    if id_cliente:
        cliente = Cliente.objects.get(id=id_cliente)
        cliente.delete()
    return redirect('/clientes/')

@login_required(login_url='/login/')
def lista_clientes(request):
    lista_de_clientes = Cliente.objects.all()
    dados = {"clientes":lista_de_clientes}
    return render(request,'clientes.html',dados)

#Views relacionadas às vendas
@login_required(login_url='/login/')
def lista_vendas(request):
    lista_de_vendas = Venda.objects.all()
    vendas = {
        'vendas':lista_de_vendas
    }
    return render(request, 'vendas.html', vendas)

@login_required(login_url='/login/')
def nova_venda(request,id_imovel):
    clientes = Cliente.objects.all()
    corretores = Corretor.objects.all()
    imovel = Imovel.objects.get(id=id_imovel)
    pagamentos = Pagamento.objects.all()
    dados = {
        'clientes':clientes,
        'corretores':corretores,
        'imovel':imovel,
        'pagamentos':pagamentos
    }
    return render(request,'nova-venda.html',dados)

@login_required(login_url='/login/')
def submit_venda(request):
    if request.POST:
        data = request.POST.get('data')
        id_cliente = Cliente.objects.get(id=int(request.POST.get('id_cliente')))
        id_corretor = Corretor.objects.get(id=int(request.POST.get('id_corretor')))
        id_imovel = Imovel.objects.get(id=int(request.POST.get('id_imovel')))
        id_pagamento = Pagamento.objects.get(id=int(request.POST.get('id_pagamento')))

        Venda.objects.create(id_cliente = id_cliente,
                     id_corretor = id_corretor,
                     id_imovel = id_imovel,
                     id_pagamento = id_pagamento
                     )

    return redirect ('/vendas/')

@login_required(login_url='/login/')
def delete_venda(request,id_venda):
    if id_venda:
        venda = Venda.objects.get(id=id_venda)
        venda.delete()
    return redirect('/vendas/')

@login_required(login_url='/login/')
def extrato_venda(request,id_venda):
    if id_venda:
        venda = {
            'venda': Venda.objects.get(id=id_venda)
        }
    return render(request,'extrato-venda.html',venda)


#Views relacionadas ao login
def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
        else:
            messages.error(request,'Usuário ou senha inválidos')
    return redirect('/imoveis/')

def logout_user(request):
    logout(request)
    return redirect('/')