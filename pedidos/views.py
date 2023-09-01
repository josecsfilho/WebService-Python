from django.template import context
from django.views.decorators.cache import cache_page
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Pedido



@cache_page(60 * 1000000)  # Cache por 15 minutos
def minha_visualizacao(request):
    # Código da visualização aqui
    return render(request, 'template.html', context)
def marcar_faturado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.status = 'faturado'
    pedido.save()

# Create your views here.
