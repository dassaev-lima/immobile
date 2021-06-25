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

def add_cliente(request):
    if request.POST:
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        Cliente.objects.create(nome=nome,
                               cpf=cpf,
                               email=email,
                               telefone=telefone)
    return redirect('/')
def lista_clientes(request):
    lista_de_clientes = Cliente.objects.all()
    dados = {"clientes":lista_de_clientes}
    return render(request,'clientes.html',dados)

