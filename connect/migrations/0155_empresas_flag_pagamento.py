# Generated by Django 4.1.7 on 2025-02-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0154_colaborador_telefone_comercial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='flag_pagamento',
            field=models.IntegerField(default=0),
        ),
    ]
