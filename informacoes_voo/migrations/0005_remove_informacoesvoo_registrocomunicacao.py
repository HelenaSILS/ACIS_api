# Generated by Django 2.2.2 on 2019-06-21 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes_voo', '0004_informacoesvoo_idinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacoesvoo',
            name='registroComunicacao',
        ),
    ]
