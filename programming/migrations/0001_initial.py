# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-04 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import programming.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'framework',
            },
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('creator', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=programming.models.file_upload)),
            ],
            options={
                'db_table': 'programming',
            },
        ),
        migrations.AddField(
            model_name='framework',
            name='programming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.Programming'),
        ),
    ]