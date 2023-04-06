from django.contrib import admin
from supermercadosistema.models import clientes, fornecedores, produtos, setores

class clientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email', 'endereco')

admin.site.register(clientes, clientesAdmin)

class fornecedoresAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area', 'endereco')

admin.site.register(fornecedores, fornecedoresAdmin)

class produtosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade')

admin.site.register(produtos, produtosAdmin)

class setoresAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')

admin.site.register(setores, setoresAdmin)