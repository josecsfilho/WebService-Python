# Generated by Django 4.2.4 on 2023-08-25 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data_entregue',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='data_faturado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
