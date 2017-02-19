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
