from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Pedido

def marcar_faturado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.status = 'faturado'
    pedido.save()

# Create your views here.
