# Generated by Django 4.1.7 on 2024-03-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0112_produtos_revenda_preco_base_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='comprador_email',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='comprador_nome',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='comprador_telefone',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
