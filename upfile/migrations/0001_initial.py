# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-21 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import upfile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ana', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('pFile', models.FileField(upload_to=upfile.models.ana_version_path)),
            ],
        ),
    ]
