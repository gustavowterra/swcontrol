# Generated by Django 4.1.7 on 2024-11-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0145_produtos_flag_conferir'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos_revenda',
            name='flag_conferir',
            field=models.IntegerField(default=0),
        ),
    ]
