# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merceria',
            name='codigo',
            field=models.CharField(default='', max_length=150, verbose_name='Codigo'),
        ),
    ]
