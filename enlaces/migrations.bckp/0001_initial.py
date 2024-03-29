# Generated by Django 2.2.7 on 2019-12-01 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('domain', models.URLField()),
                ('status', models.CharField(choices=[('a', 'Active'), ('h', 'On Hold')], default='a', max_length=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateField(auto_now_add=True, verbose_name='date modified')),
                ('status', models.CharField(choices=[('o', 'opportunity'), ('d', 'declined'), ('r', 'requested'), ('p', 'pending'), ('c', 'confirmed')], default='o', max_length=1)),
                ('niche', models.CharField(choices=[('biz', 'business'), ('lfs', 'lifestyle'), ('hmi', 'home improvement'), ('eco', 'green'), ('tra', 'travel'), ('fml', 'family'), ('dsg', 'design'), ('mrk', 'marketing'), ('tch', 'tech'), ('edu', 'education'), ('car', 'auto'), ('hlt', 'health & beauty'), ('oth', 'other')], max_length=3)),
                ('link_type', models.CharField(choices=[('g', 'guest post'), ('p', 'paid post'), ('b', 'blog comment'), ('c', 'citation'), ('f', 'forum'), ('o', 'other')], max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enlaces.Client')),
            ],
        ),
    ]
