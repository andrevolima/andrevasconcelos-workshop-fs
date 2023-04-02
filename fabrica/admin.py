from django.contrib import admin
from fabrica.models import clientes, colaboradores

class clientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area')

admin.site.register(clientes, clientesAdmin)

class colaboradoresAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'curso')

admin.site.register(colaboradores, colaboradoresAdmin)


