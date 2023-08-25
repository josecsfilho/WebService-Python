from django.db import models
from django.contrib.auth.models import User



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('faturado', 'Faturado'),
        ('entregue', 'Entregue'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')

    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    data_faturado = models.DateTimeField(null=True, blank=True)
    data_entregue = models.DateTimeField(null=True, blank=True)

class ArquivoAnexo(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='anexos/')
    descricao = models.TextField(blank=True, null=True)

