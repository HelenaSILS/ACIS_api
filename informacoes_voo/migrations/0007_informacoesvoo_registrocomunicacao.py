# Generated by Django 2.2.2 on 2019-06-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_comunicacao', '0004_remove_registrocomunicacao_username'),
        ('informacoes_voo', '0006_informacoesvoo_eventovoo'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacoesvoo',
            name='registroComunicacao',
            field=models.ManyToManyField(to='registro_comunicacao.RegistroComunicacao'),
        ),
    ]