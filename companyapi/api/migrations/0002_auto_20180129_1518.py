# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-01-29 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='e_id',
            field=models.IntegerField(),
        ),
    ]
