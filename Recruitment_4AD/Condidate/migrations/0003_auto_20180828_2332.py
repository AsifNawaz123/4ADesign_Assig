# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-08-28 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Condidate', '0002_auto_20180828_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
