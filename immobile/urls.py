"""immobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    #rota padrão para acesso do admin django
    path('admin/', admin.site.urls),

    #rotas padrão para acesso ao dashboardo do sistema
    path('',RedirectView.as_view(url='/imoveis/')),
    path('login/',views.login_user),
    path('login/submit',views.submit_login),
    path('logout',views.logout_user),

    #rota padrão para acesso aos imóveis do sistema
    path('imoveis/',views.lista_imoveis),

    #rota padrão para acesso aos clientes do sistema
    path('clientes/',views.lista_clientes),
    path('clientes/delete/<int:id_cliente>/',views.delete_cliente),
    path('clientes/novo/',views.novo_cliente),
    path('clientes/edit/<int:id_cliente>/',views.edit_cliente),
    path('clientes/submit/',views.submit_cliente),

    #rota padrão para acesso às vendas do sistema
    path('vendas/nova/<int:id_imovel>/',views.nova_venda),
    path('vendas/submit/',views.submit_venda),
    path('vendas/',views.lista_vendas),
    path('vendas/delete/<int:id_venda>/',views.delete_venda),
    path('vendas/extrato/<int:id_venda>/',views.extrato_venda)

]
