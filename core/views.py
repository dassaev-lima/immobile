from django.shortcuts import render,redirect
from core.models import Imovel,Cliente

# Create your views here.

#view que lista os imóveis
def lista_imoveis(request):
    lista_de_imoveis = Imovel.objects.all()
    dados = {"imoveis":lista_de_imoveis}
    return render(request,'imoveis.html',dados)

#Views para CRUD de Clientes
def novo_cliente(request):
    return render(request,'novo-cliente.html')

def edit_cliente(request,id_cliente):
    dados = Cliente.objects.get(id=id_cliente)
    cliente = {"cliente": dados}
    return render(request,'edit-cliente.html',cliente)

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

def delete_cliente(request,id_cliente):
    if id_cliente:
        cliente = Cliente.objects.get(id=id_cliente)
        cliente.delete()
    return redirect('/clientes/')

def lista_clientes(request):
    lista_de_clientes = Cliente.objects.all()
    dados = {"clientes":lista_de_clientes}
    return render(request,'clientes.html',dados)

