# Generated by Django 4.2.4 on 2023-08-25 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]