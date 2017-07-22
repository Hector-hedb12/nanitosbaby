# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Descripcion(models.Model):
    titulo = models.CharField(_('titulo'), max_length=150)
    contenido = models.TextField(_('Contenido'), default='')
    orden = models.IntegerField(_('Orden'), default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Descripciones'
