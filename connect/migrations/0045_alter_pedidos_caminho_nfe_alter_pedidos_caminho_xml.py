# Generated by Django 4.2.2 on 2023-07-26 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0044_alter_pedidos_numero_nfe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='caminho_nfe',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='caminho_xml',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
