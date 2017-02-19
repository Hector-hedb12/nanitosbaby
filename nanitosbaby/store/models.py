# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(_(u'Categoría'), max_length=150)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(_('Nombre'), max_length=150)
    description = models.TextField(_(u'Descripción'), default='')
    price = models.DecimalField(_('Precio'), max_digits=12, decimal_places=2, default=0)
    amount = models.IntegerField(_('Cantidad'), default=0)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    category = models.ForeignKey('Category', models.SET_NULL, verbose_name=_(u'Categoría'), null=True)

    def __str__(self):
        return self.name
