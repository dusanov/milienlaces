# Generated by Django 2.2.7 on 2019-12-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enlaces', '0005_auto_20191207_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='netloc',
            field=models.CharField(default='', max_length=50),
        ),
    ]