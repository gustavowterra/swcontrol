# Generated by Django 4.2.2 on 2023-06-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0014_cliente_total_pedidos_cliente_ultimopedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='caminho_layout',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
