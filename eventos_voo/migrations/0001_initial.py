# Generated by Django 2.2.2 on 2019-06-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacoes_voo', '0005_remove_informacoesvoo_registrocomunicacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoVoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data', models.DateField(auto_now_add=True)),
                ('informacoesVoo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='informacoes_voo.InformacoesVoo')),
            ],
        ),
    ]
