# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Merceria


@admin.register(Merceria)
class MerceriaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'codigo', 'cantidad']
    list_display = ['nombre', 'codigo', 'cantidad']
