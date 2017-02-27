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
class Size(models.Model):
    name = models.CharField(_('Nombre'), max_length=5)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProductAmount(models.Model):
    product = models.ForeignKey('Product', models.CASCADE, verbose_name=_('Producto'))
    size = models.ForeignKey('Size', models.CASCADE, verbose_name=_('Talla'))
    amount = models.IntegerField(_('Cantidad'), default=0)

    def __str__(self):
        return '{} - {}'.format(self.product, self.size)


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(_('Nombre'), max_length=150)
    description = models.TextField(_(u'Descripción'), default='')
    price = models.DecimalField(_('Precio'), max_digits=12, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    category = models.ForeignKey('Category', models.SET_NULL, verbose_name=_(u'Categoría'), null=True)
    sizes = models.ManyToManyField('Size', through='ProductAmount', verbose_name=_('Tallas'))

    def __str__(self):
        return self.name
