# Generated by Django 4.2.2 on 2023-07-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0041_contas_receber_caminho_boleto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contas_receber',
            name='id_cobranca',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
