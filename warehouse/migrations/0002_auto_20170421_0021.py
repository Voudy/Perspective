# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipe',
            name='size',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Диаметр'),
        ),
    ]
