# Generated by Django 2.2.2 on 2019-06-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planos_voo', '0001_initial'),
        ('informacoes_voo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacoesvoo',
            name='planosVoo',
        ),
        migrations.AddField(
            model_name='informacoesvoo',
            name='planosVoo',
            field=models.ManyToManyField(to='planos_voo.PlanoVoo'),
        ),
    ]
