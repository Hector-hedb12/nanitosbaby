# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20170219_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(through='store.ProductAmount', to='store.Size', verbose_name='Tallas'),
        ),
    ]
