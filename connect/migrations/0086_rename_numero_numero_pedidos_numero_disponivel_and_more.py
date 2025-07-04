# Generated by Django 4.2.2 on 2023-08-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0085_numero_pedidos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numero_pedidos',
            old_name='numero',
            new_name='numero_disponivel',
        ),
        migrations.RenameField(
            model_name='numero_pedidos',
            old_name='ultimo_numero',
            new_name='ultimo_numero_enviado',
        ),
        migrations.AddField(
            model_name='empresas',
            name='ultimo_pedido_ref',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='numero_pedidos',
            name='ultimo_numero_salvo',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
