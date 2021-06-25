from django.shortcuts import render
from core.models import Imovel,Cliente

# Create your views here.

#view que lista os imóveis
def lista_imoveis(request):
    lista_de_imoveis = Imovel.objects.all()
    dados = {"imoveis":lista_de_imoveis}
    return render(request,'imoveis.html',dados)

#Views para CRUD de Clientes
def novo_cliente(request):
    return  render(request,'novo-cliente.html')

def lista_clientes(request):
    lista_de_clientes = Cliente.objects.all()
    dados = {"clientes":lista_de_clientes}
    return render(request,'clientes.html',dados)

