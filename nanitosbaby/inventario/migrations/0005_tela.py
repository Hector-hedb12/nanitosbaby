# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-22 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_bolsa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, help_text='(Kg)', max_digits=3, verbose_name='Peso')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
            ],
        ),
    ]