# Generated by Django 4.1.7 on 2024-10-07 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0119_statusor_tipomedida_pedidos_flag_notificacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento_comentarios',
            name='colaborador',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='connect.colaborador'),
        ),
        migrations.AddField(
            model_name='orcamento_comentarios',
            name='data',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orcamento_comentarios',
            name='orcamento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='connect.orcamentos'),
        ),
    ]
