from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    data_pedido = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    data_faturado = models.DateTimeField(null=True, blank=True)
    data_entregue = models.DateTimeField(null=True, blank=True)

    observacoes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.data_pedido:
            self.data_pedido = timezone.now()
        super(Pedido, self).save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.pk} - {self.cliente.nome}"
