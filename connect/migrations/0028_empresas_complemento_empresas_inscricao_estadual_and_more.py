# Generated by Django 4.2.2 on 2023-06-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0027_alter_pedidos_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='complemento',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empresas',
            name='inscricao_estadual',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='empresas',
            name='numero',
            field=models.IntegerField(default=11),
        ),
    ]
