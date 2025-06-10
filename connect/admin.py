from django.contrib import admin
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register (Colaborador)
admin.site.register (Cliente)
admin.site.register (Pedidos)
admin.site.register (TipoPgto)
admin.site.register (Fornecedor)
admin.site.register (Tipo_Fornecedor)
admin.site.register (Contas_Pagar)
admin.site.register (Empresas)
admin.site.register (Status_Colaborador)
admin.site.register (Motivos_Desligamento)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(TipoMedida)
admin.site.register(StatusOr)
admin.site.register(Tipo_Indicacao)
admin.site.register(Status_Reparo)
admin.site.register(Condicoes_Pagamentos)




# Register your models here.
