# Generated by Django 4.2.4 on 2023-08-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_pedido_observacoes_delete_arquivoanexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
