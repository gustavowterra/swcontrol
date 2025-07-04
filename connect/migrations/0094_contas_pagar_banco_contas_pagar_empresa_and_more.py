# Generated by Django 4.2.2 on 2023-08-18 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0093_pedidos_flag_nfe_antecipada'),
    ]

    operations = [
        migrations.AddField(
            model_name='contas_pagar',
            name='banco',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='connect.bancos'),
        ),
        migrations.AddField(
            model_name='contas_pagar',
            name='empresa',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='connect.empresas'),
        ),
        migrations.AddField(
            model_name='contas_receber',
            name='banco',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='connect.bancos'),
        ),
        migrations.AddField(
            model_name='contas_receber',
            name='pedido_conta',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='connect.pedidos'),
        ),
    ]
