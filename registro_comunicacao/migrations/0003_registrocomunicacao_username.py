# Generated by Django 2.2.2 on 2019-06-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_comunicacao', '0002_auto_20190623_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocomunicacao',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
