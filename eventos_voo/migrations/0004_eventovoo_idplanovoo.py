# Generated by Django 2.2.2 on 2019-06-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_voo', '0003_remove_eventovoo_informacoesvoo'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventovoo',
            name='idPlanoVoo',
            field=models.CharField(max_length=10, null=True),
        ),
    ]