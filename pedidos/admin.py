from django.contrib import admin
from .models import Cliente, Pedido

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'endereco')


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'status', 'observacoes_display')  # Adicione 'observacoes_display'
    list_filter = ('status',)
    search_fields = ('cliente__nome', 'observacoes')

    def observacoes_display(self, obj):
        return obj.observacoes[:30] if obj.observacoes else ""  # Exibe apenas os primeiros 30 caracteres das observações


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)

