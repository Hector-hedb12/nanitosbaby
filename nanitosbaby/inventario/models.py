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

