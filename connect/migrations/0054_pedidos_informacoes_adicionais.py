# Generated by Django 4.2.2 on 2023-07-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0053_remove_pedidos_informacoes_adicionais_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='informacoes_adicionais',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
