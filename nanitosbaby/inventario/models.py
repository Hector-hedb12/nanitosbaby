# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Merceria(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=150)
    cantidad = models.IntegerField(_('Cantidad'), default=0)
    codigo = models.CharField(_(u'Codigo'), max_length=150, default='')

    def __str__(self):
        return self.nombre

@python_2_unicode_compatible
class Etiqueta(models.Model):
    TALLA = 'T'
    PUBLICIDAD = 'P'
    TIPO_CHOICES = (
        (TALLA, 'Talla'),
        (PUBLICIDAD, 'Publicidad')
    )

    cantidad = models.IntegerField(_('Cantidad'), default=0)
    tipo =  models.CharField(_(u'Tipo'), choices=TIPO_CHOICES, default=TALLA, max_length=1)
    talla = models.ForeignKey('store.Size', models.CASCADE, verbose_name=_('Talla'))

    def __str__(self):
        return '{} - {}'.format(self.tipo, self.talla)

@python_2_unicode_compatible
class Bolsa(models.Model):
    cantidad = models.IntegerField(_('Cantidad'), default=0)
    modelo = models.CharField(_(u'Modelo'), max_length=50)

    def __str__(self):
        return self.modelo
