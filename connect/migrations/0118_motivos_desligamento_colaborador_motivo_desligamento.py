# Generated by Django 4.1.7 on 2024-09-20 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0117_status_colaborador_colaborador_data_admissao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivos_Desligamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='motivo_desligamento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='connect.motivos_desligamento'),
        ),
    ]
