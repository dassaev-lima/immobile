from django.db import models

# Create your models here.
#Modelo de Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    data_entrada = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome

    def get_data_entrada_br(self):
        #return self.data_entrada.strftime('%d/%m/%y %H:%M')
        return self.data_entrada.strftime('%d/%m/%y')

#Modelo de Corretor
class Corretor(models.Model):
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    class Meta:
        db_table = 'corretor'

    def __str__(self):
        return self.nome


# Modelo de Imóvel
class Imovel(models.Model):
    tipo = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    comissao = models.IntegerField(default=5)
    descricao = models.CharField(max_length=255)
    informacoes = models.TextField(blank=True,null=True)

    class Meta:
        db_table = 'imovel'

    def __str__(self):
        return self.descricao

# Modelo de Pagamento
class Pagamento(models.Model):
    opcao = models.CharField(max_length=255)

    class Meta:
        db_table = 'pagamento'

    def __str__(self):
        return self.opcao

# Modelo de Pagamento
class Venda(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    id_imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    id_pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'venda'


