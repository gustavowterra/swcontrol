# Generated by Django 4.2.2 on 2023-07-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0051_itens_pedido_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='informacoes_adicionais',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
