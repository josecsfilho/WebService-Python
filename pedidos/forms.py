from django import forms
from .models import Cliente, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # ou uma lista de campos que desejar

class PedidoFormPendente(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'status', 'observacoes')