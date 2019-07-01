# Generated by Django 2.2.2 on 2019-06-30 21:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planos_voo', '0003_auto_20190623_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planovoo',
            name='autonomiaHora',
        ),
        migrations.RemoveField(
            model_name='planovoo',
            name='autonomiaMinutos',
        ),
        migrations.AddField(
            model_name='planovoo',
            name='autonomiaHoras',
            field=models.CharField(max_length=2, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Duracao em horas')]),
        ),
        migrations.AlterField(
            model_name='planovoo',
            name='outrosDados',
            field=models.TextField(blank=True, null=True),
        ),
    ]
