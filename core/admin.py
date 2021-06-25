from django.contrib import admin
from core.models import Cliente,Corretor,Imovel,Pagamento,Venda

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Corretor)
admin.site.register(Imovel)
admin.site.register(Pagamento)
admin.site.register(Venda)


